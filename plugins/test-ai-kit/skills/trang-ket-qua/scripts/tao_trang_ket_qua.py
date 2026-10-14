"""Tạo trang kết quả kiểm thử (một file HTML tự chứa) từ thư mục dự án – để đăng thành Artifact trong Claude.

Dùng: python tao_trang_ket_qua.py <thư mục dự án> [<file .html ra>]
  Mặc định ghi <dự án>/bao-cao/trang-ket-qua.html. In JSON: {"file", "tieu_de", "can_tester", "tong_tc", "tong_loi"}.
Số liệu lấy từ hàm thong_ke của skill xuat-bao-cao (cùng số với Biểu mẫu Excel).
"""
import json
import sys
from datetime import datetime
from pathlib import Path

GOC = Path(__file__).resolve().parent
sys.path.insert(0, str(GOC.parents[1] / "xuat-bao-cao" / "scripts"))
from xuat_bao_cao import thong_ke  # noqa: E402

BUOC = [("ho_so", "Đọc hiểu hệ thống"), ("giao_dien", "Khám phá giao diện"), ("kich_ban", "Thiết kế kịch bản"),
        ("du_lieu", "Sinh dữ liệu"), ("thiet_lap", "Kiểm tra thiết lập"), ("dieu_kien", "Kiểm tra điều kiện"),
        ("thuc_thi", "Thực thi"), ("bao_cao", "Báo lỗi và báo cáo"), ("lark", "Đẩy lên Lark")]
TEP = [("ho-so/ho-so-he-thong.md", "Bản đọc hiểu hệ thống"), ("giao-dien/ban-do-giao-dien.md", "Bản đồ giao diện"),
       ("kich-ban/kich-ban-kiem-thu.xlsx", "Kịch bản kiểm thử (Excel)"), ("du-lieu/du-lieu-kiem-thu.xlsx", "Dữ liệu kiểm thử (Excel)"),
       ("du-lieu/van-ban", "Văn bản mẫu đính kèm"), ("thiet-lap/ket-qua-kiem-tra.md", "Kết quả kiểm tra thiết lập"),
       ("thuc-thi/bang-chung", "Ảnh bằng chứng"), ("bao-cao/bieu-mau-ket-qua.xlsx", "Biểu mẫu kết quả kiểm thử (Mẫu 3)")]


def _doc(p, mac_dinh):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else mac_dinh


def viec_cua_tester(st, tk, tcs):
    """Các việc chỉ tester làm được, theo thứ tự quy trình."""
    b = st.get("buoc", {})
    tt = lambda k: b.get(k, {}).get("trang_thai", "Chưa làm")  # noqa: E731
    viec = []
    for k, ten in BUOC:
        if tt(k) in ("Lỗi", "Bị chặn"):
            viec.append(f"{ten} đang {tt(k).lower()}: {b[k].get('loi') or b[k].get('ly_do') or 'xem nhật ký'}")
    kb = b.get("kich_ban", {})
    if tt("kich_ban") == "Xong" and not kb.get("da_duyet"):
        viec.append(f"Duyệt kịch bản ({len(tcs)} test case) – trả lời các điểm cần xác nhận nếu có")
    dk = b.get("dieu_kien", {})
    if tt("dieu_kien") == "Xong" and str(dk.get("ket_luan", "")).startswith("Chưa") and not dk.get("bo_qua"):
        viec.append("Cổng điều kiện chưa đạt – xử lý các mục còn thiếu, hoặc quyết định bỏ qua kèm lý do")
    if tk["ket_qua_ai_chua_xac_nhan"]:
        viec.append(f"Xác nhận {tk['ket_qua_ai_chua_xac_nhan']} kết quả test do AI chạy")
    if tk["loi_chua_xac_nhan"]:
        viec.append(f"Xác nhận {tk['loi_chua_xac_nhan']} lỗi AI đã báo (mức độ, nội dung)")
    if tt("bao_cao") == "Xong" and tt("lark") != "Xong":
        viec.append("Đồng ý đẩy kết quả lên Lark Base")
    if not viec:
        tiep = next((ten for k, ten in BUOC if tt(k) not in ("Xong",) and k != "giao_dien"), None)
        if tiep:
            viec.append(f"Gõ “làm tiếp” để Agent tổng chạy bước {tiep}")
    return viec


def tao(da, ra=None):
    da = Path(da)
    st = _doc(da / "trang-thai.json", {})
    tcs = _doc(da / "kich-ban" / "test-case.json", {}).get("test_cases", [])
    loi = _doc(da / "bao-cao" / "loi.json", [])
    dg = _doc(da / "bao-cao" / "danh-gia.json", {})
    tk = thong_ke(da)
    b = st.get("buoc", {})
    du_lieu = {
        "ma": st.get("ma", da.name), "ten": st.get("ten", ""), "url": st.get("url", ""),
        "nguoi_phu_trach": st.get("nguoi_phu_trach", ""), "cap_nhat": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "ket_luan": dg.get("ket_luan", ""),
        "buoc": [{"ten": ten, "trang_thai": b.get(k, {}).get("trang_thai", "Chưa làm"),
                  "tom_tat": b.get(k, {}).get("tom_tat") or b.get(k, {}).get("ly_do") or b.get(k, {}).get("loi") or ""} for k, ten in BUOC],
        "can_tester": viec_cua_tester(st, tk, tcs),
        "dau_vao": st.get("dau_vao", {}),
        "thong_ke": tk,
        "test_cases": [{"ma_tc": t.get("ma_tc", ""), "tieu_de": t.get("tieu_de", ""), "chuc_nang": t.get("chuc_nang", ""),
                        "nhom": t.get("nhom", ""), "uu_tien": t.get("uu_tien", ""), "trang_thai": t.get("trang_thai") or "Chưa chạy",
                        "ai": str(t.get("nguon_ket_qua", "")).startswith("AI"), "ma_loi": t.get("ma_loi", "")} for t in tcs],
        "loi": [{k: l.get(k) for k in ("ma_loi", "tieu_de", "muc_do", "trang_thai", "ma_tc", "buoc_tai_hien",
                                       "ket_qua_mong_doi", "ket_qua_thuc_te", "bang_chung", "da_xac_nhan")} for l in loi],
        "nhat_ky": list(reversed(st.get("nhat_ky", [])[-12:])),
        "tep": [{"duong_dan": p, "mo_ta": m} for p, m in TEP if (da / p).exists()],
    }
    mau = (GOC.parent / "assets" / "mau-trang.html").read_text(encoding="utf-8")
    json_an_toan = json.dumps(du_lieu, ensure_ascii=False).replace("</", "<\\/")
    tieu_de = du_lieu["ma"].replace("<", "").replace(">", "")
    html = mau.replace("__TIEU_DE__", tieu_de).replace("__DU_LIEU__", json_an_toan)
    ra = Path(ra) if ra else da / "bao-cao" / "trang-ket-qua.html"
    ra.parent.mkdir(parents=True, exist_ok=True)
    ra.write_text(html, encoding="utf-8")
    return {"file": str(ra.resolve()), "tieu_de": f"Kiểm thử {tieu_de}", "can_tester": du_lieu["can_tester"],
            "tong_tc": tk["tong_tc"], "tong_loi": tk["tong_loi"]}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) not in (2, 3):
        print(__doc__)
        sys.exit(2)
    print(json.dumps(tao(*sys.argv[1:]), ensure_ascii=False))


if __name__ == "__main__":
    main()
