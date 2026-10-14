"""Tách tài liệu đầu vào thành các file gọn cho agent đọc.

Dùng:
  python tach_srs.py srs  <SRS.docx>  <thư mục ra>   SRS theo mẫu Trí Nam → muc-luc.md, chuc-nang/<mã>.md, anh/, cau-truc-srs.json
  python tach_srs.py csdl <CSDL.docx> <file .md ra>  Tài liệu thiết kế CSDL → Markdown (giữ bảng trường)
  python tach_srs.py van-ban <file .docx|.pdf|.md|.txt> <file .md ra>   Tài liệu bất kỳ → chữ thuần (khi SRS không theo mẫu)
In ra một dòng JSON tóm tắt để agent đọc kết quả.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import tach_tai_lieu  # noqa: E402  (mã tách đã kiểm chứng trên SRS BTXH: 5 phân hệ, 233 chức năng)


def _md_chuc_nang(cn, ten_ph):
    tt = cn["thong_tin"]
    d = [f"# {cn['ma']} – {cn['ten']}", "", f"Phân hệ: {ten_ph}", ""]
    if tt["mo_ta"]:
        d += [f"**Mô tả:** {tt['mo_ta']}", ""]
    d += [f"**Tác nhân:** {', '.join(tt['tac_nhan']) or '(không ghi)'}",
          f"**Điều kiện trước:** {tt['dieu_kien_truoc'] or '(không ghi)'}",
          f"**Điều kiện sau:** {tt['dieu_kien_sau'] or '(không ghi)'}", ""]
    if tt["luong_chinh"]:
        d += ["## Luồng sự kiện chính", "", "| Bước | Hệ thống | Luồng thay thế |", "|---|---|---|"]
        d += [f"| {b['buoc']} | {b['he_thong']} | {b['thay_the']} |".replace("\n", " ") for b in tt["luong_chinh"]]
        d.append("")
    if tt["luong_ngoai_le"]:
        d += ["## Luồng ngoại lệ", ""] + [f"- {x}".replace("\n", " ") for x in tt["luong_ngoai_le"]] + [""]
    if tt["quy_tac"]:
        d += ["## Quy tắc nghiệp vụ", ""] + [f"- **{q['ma'] or 'BR?'}**: {q['noi_dung'] or '(để trống)'}".replace("\n", " ")
                                            for q in tt["quy_tac"]] + [""]
    for m in tt["man_hinh"]:
        d += [f"## Màn hình: {m['ten'] or '(không tên)'}", "", "| Nhóm | Tên | Loại | Mặc định | Bắt buộc | Đầu vào | Mô tả |",
              "|---|---|---|---|---|---|---|"]
        d += [f"| {p['nhom']} | {p['ten']} | {p['loai']} | {p['mac_dinh']} | {p['bat_buoc']} | {'Có' if p['la_dau_vao'] else ''} | {p['mo_ta']} |"
              .replace("\n", " ") for p in m["phan_tu"]]
        d.append("")
    if cn["anh"]:
        d += ["## Ảnh giao diện", ""] + [f"- anh/{a}" for a in cn["anh"]] + [""]
    if cn["thieu"]:
        d += ["## Tài liệu còn thiếu (gợi ý điểm cần xác nhận)", ""] + [f"- {x}" for x in cn["thieu"]] + [""]
    d += ["## Nguyên văn trong SRS", "", "```", cn["van_ban"], "```", ""]
    return "\n".join(d)


def tach_srs(docx, ra):
    ra = Path(ra)
    (ra / "chuc-nang").mkdir(parents=True, exist_ok=True)
    kq = tach_tai_lieu.tach_srs(docx, ra)
    (ra / "chung.md").write_text(kq["chung"], encoding="utf-8")
    (ra / "phi-chuc-nang.md").write_text(kq["phi_chuc_nang"], encoding="utf-8")
    muc_luc = [f"# Mục lục SRS – {Path(docx).name}", "", f"Tổng: {len(kq['phan_he'])} phân hệ, {kq['tong_chuc_nang']} chức năng", "",
               "| Mã | Chức năng | Tác nhân | Màn hình | Trường nhập | Ảnh | Thiếu |", "|---|---|---|---|---|---|---|"]
    for ph in kq["phan_he"]:
        muc_luc.append(f"| **{ph['ma']}** | **{ph['ten']}** | | | | | |")
        for cn in ph["chuc_nang"]:
            tt = cn["thong_tin"]
            so_nhap = sum(1 for m in tt["man_hinh"] for p in m["phan_tu"] if p["la_dau_vao"])
            muc_luc.append(f"| {cn['ma']} | {cn['ten']} | {', '.join(tt['tac_nhan'])} | {len(tt['man_hinh'])} | {so_nhap} | "
                           f"{len(cn['anh'])} | {len(cn['thieu'])} |")
            (ra / "chuc-nang" / f"{cn['ma']}.md").write_text(_md_chuc_nang(cn, f"{ph['ma']} {ph['ten']}"), encoding="utf-8")
    (ra / "muc-luc.md").write_text("\n".join(muc_luc) + "\n", encoding="utf-8")
    (ra / "cau-truc-srs.json").write_text(json.dumps(kq, ensure_ascii=False, indent=1), encoding="utf-8")
    return {"loai": "srs", "phan_he": len(kq["phan_he"]), "chuc_nang": kq["tong_chuc_nang"],
            "anh": sum(len(c["anh"]) for p in kq["phan_he"] for c in p["chuc_nang"]), "thu_muc": str(ra)}


def van_ban(tep, ra):
    tep = Path(tep)
    duoi = tep.suffix.lower()
    if duoi == ".docx":
        chu = tach_tai_lieu.tach_csdl(tep)  # đọc đúng thứ tự đoạn + bảng
    elif duoi == ".pdf":
        from pypdf import PdfReader
        chu = "\n\n".join((p.extract_text() or "") for p in PdfReader(str(tep)).pages)
    else:
        chu = tep.read_text(encoding="utf-8", errors="replace")
    Path(ra).parent.mkdir(parents=True, exist_ok=True)
    Path(ra).write_text(f"# {tep.name}\n\n{chu}\n", encoding="utf-8")
    return {"loai": "van-ban", "so_ky_tu": len(chu), "file": str(ra)}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) != 4 or sys.argv[1] not in ("srs", "csdl", "van-ban"):
        print(__doc__)
        sys.exit(2)
    lenh, vao, ra = sys.argv[1:]
    try:
        if lenh == "srs":
            if not tach_tai_lieu.la_srs_chuan(vao):
                print(json.dumps({"loi": "SRS không theo mẫu Trí Nam (không có mục 'YÊU CẦU CHI TIẾT VỀ CHỨC NĂNG') – dùng lệnh van-ban"},
                                 ensure_ascii=False))
                sys.exit(1)
            kq = tach_srs(vao, ra)
        else:
            kq = van_ban(vao, ra)
    except Exception as e:  # noqa: BLE001 – báo lỗi gọn cho agent
        print(json.dumps({"loi": f"{type(e).__name__}: {e}"}, ensure_ascii=False))
        sys.exit(1)
    print(json.dumps(kq, ensure_ascii=False))


if __name__ == "__main__":
    main()
