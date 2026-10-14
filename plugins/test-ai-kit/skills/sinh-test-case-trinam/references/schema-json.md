# Schema JSON đầu vào cho `xuat_excel.py`

```json
{
  "thong_tin": {
    "ma_du_an": "GL-TTHC",
    "ten_module": "Tiếp nhận hồ sơ",
    "tai_lieu_nguon": "SRS-gia-lap-tiep-nhan-ho-so.md",
    "phien_ban_tai_lieu": "0.9",
    "nguoi_lap": "AI – thiet-ke-kich-ban",
    "ngay_lap": "12/10/2026"
  },
  "yeu_cau": [
    {"ma": "IV.1-CN19", "mo_ta": "Quản lý danh mục loại bảo hiểm y tế", "nhom": "Use case"},
    {"ma": "IV.1-CN19-BR1", "mo_ta": "Quy tắc BR1 (SRS để trống)", "nhom": "Quy tắc nghiệp vụ"}
  ],
  "diem_can_xac_nhan": [
    {
      "ma": "DX-IV.1-CN19-01",
      "vi_tri": "BR-01",
      "loai": "Mâu thuẫn",
      "noi_dung": "…",
      "anh_huong": "…",
      "cau_hoi": "…",
      "muc_anh_huong": "Cao"
    }
  ],
  "test_cases": [
    {
      "ma_tc": "TC-IV.1-CN19-001",
      "ma_yeu_cau": ["IV.1-CN19", "IV.1-CN19-BR1"],
      "nhom": "Happy case",
      "chuc_nang": "Tiếp nhận hồ sơ mới",
      "tieu_de": "…",
      "loai": "Chức năng",
      "ky_thuat": "LUC",
      "uu_tien": "Cao",
      "dieu_kien_truoc": "…",
      "buoc_thuc_hien": ["Bước 1", "Bước 2"],
      "du_lieu_test": "…",
      "ket_qua_mong_doi": "…",
      "ma_dx": ["DX-IV.1-CN19-01"]
    }
  ]
}
```

## Giá trị hợp lệ

| Trường | Giá trị |
|---|---|
| `yeu_cau[].nhom` | `Use case`, `Quy tắc nghiệp vụ`, `Phi chức năng`, `Khác` |
| `diem_can_xac_nhan[].loai` | `Mơ hồ`, `Thiếu`, `Mâu thuẫn`, `Không kiểm chứng được` |
| `diem_can_xac_nhan[].muc_anh_huong` | `Cao`, `Trung bình`, `Thấp` |
| `test_cases[].nhom` | `Happy case`, `Chức năng`, `UI/UX`, `Hiệu năng` (bắt buộc) |
| `test_cases[].loai` | `Chức năng`, `Giao diện`, `Phân quyền`, `Biên`, `Ngoại lệ`, `API`, `Hiệu năng`, `ATTT` |
| `test_cases[].ky_thuat` | `PVTĐ`, `GTB`, `BQĐ`, `CTT`, `PQ`, `LUC`, `ĐL` |
| `test_cases[].uu_tien` | `Cao`, `Trung bình`, `Thấp` |
| `test_cases[].ma_dx` | Danh sách mã DX liên quan (rỗng nếu không có). Có DX thì kết quả mong đợi phải chứa `[CẦN XÁC NHẬN`, và ngược lại |
| `thong_tin.che_do` | `Đầy đủ` (mặc định), `Gọn`. Chế độ Gọn không được có TC ưu tiên `Thấp` |
| `thong_tin.lan_cap_nhat` | Không bắt buộc. Ghi lần cập nhật gần nhất, vd `"13/10/2026 – theo trả lời BA (8 DX)"` |

## Trường dùng khi cập nhật (không bắt buộc lúc sinh mới)

| Trường | Ý nghĩa |
|---|---|
| `diem_can_xac_nhan[].tra_loi` | Trả lời của BA/KH (do `doc_tra_loi.py` đọc từ Excel) |
| `diem_can_xac_nhan[].trang_thai` | `Chờ trả lời` (mặc định), `Đã trả lời` (có trả lời, chưa xử lý), `Đã cập nhật TC`. TC không được gắn DX có trạng thái khác `Chờ trả lời` |
| `test_cases[].cap_nhat` | Ghi chú thay đổi, vd `"13/10/2026 – Sửa theo DX-04: …"` |
| `test_cases[].ket_qua_thuc_te`, `trang_thai`, `ma_loi`, `nguoi_thuc_hien` | Do tester điền khi chạy. Agent **không được sửa** |
