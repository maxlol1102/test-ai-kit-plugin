# Cấu trúc thư mục dự án và file trạng thái

Mỗi hệ thống kiểm thử là một thư mục trong `test-ai-kit/du-an/<MÃ>/` (thư mục làm việc của tester). Mã dự án: chữ không dấu, số, gạch nối (vd `BTXH`, `TTHC-TN`).

```
test-ai-kit/du-an/<MÃ>/
├── trang-thai.json            ← Agent tổng đọc/ghi – nguồn sự thật về tiến độ
├── he-thong.md                ← thông tin tester cung cấp: URL, vai trò, Figma, chuyên đề, phạm vi
├── dau-vao/                   ← tài liệu tester gửi (SRS, CSDL, dữ liệu mẫu, ảnh UI, checklist dev) + danh-muc.json (phân loại) + yeu-cau.md
├── ho-so/                     ← agent doc-hieu-he-thong
│   ├── ho-so-he-thong.md      ← bản đọc hiểu tổng hợp (đọc file này trước tiên)
│   ├── srs/                   ← muc-luc.md, chuc-nang/<mã>.md, anh/, cau-truc-srs.json, chung.md, phi-chuc-nang.md
│   ├── csdl.md
│   └── ui.md                  ← từ Figma hoặc quy ước UI
├── giao-dien/                 ← agent kham-pha-giao-dien: ban-do-giao-dien.md, anh/
├── kich-ban/                  ← agent thiet-ke-kich-ban: test-case.json, kich-ban-kiem-thu.xlsx
├── du-lieu/                   ← agent sinh-du-lieu: du-lieu.json, du-lieu-kiem-thu.xlsx, van-ban/ (hồ sơ mẫu .docx)
├── thiet-lap/                 ← agent kiem-tra-thiet-lap: checklist.json, ket-qua-kiem-tra.md
├── dieu-kien/                 ← agent kiem-tra-dieu-kien: kiem-tra.json
├── thuc-thi/                  ← agent thuc-thi: lan-<n>.json (mỗi lần chạy), bang-chung/<mã TC>/*.png
└── bao-cao/                   ← agent bao-loi-bao-cao: loi.json, danh-gia.json, bieu-mau-ket-qua.xlsx
                                 + trang-ket-qua.html (skill trang-ket-qua – đăng thành Artifact)
```

Không lưu mật khẩu, cookie, token ở bất kỳ file nào.

## trang-thai.json

```json
{
  "ma": "BTXH",
  "ten": "Hệ thống Bảo trợ xã hội",
  "url": "https://...",
  "nguoi_phu_trach": "Họ tên tester (từ test-ai-kit/cau-hinh.json)",
  "tao_luc": "14/10/2026 09:00",
  "dau_vao": {"website": "https://...", "figma": ["https://www.figma.com/design/..."], "tai_lieu": [{"file": "dau-vao/SRS.docx", "loai": "SRS"}], "yeu_cau": "Test phân hệ IV.4, vai trò cán bộ xã", "tiep_nhan_luc": "..."},
  "buoc": {
    "ho_so":      {"trang_thai": "Xong", "luc": "...", "tom_tat": "5 phân hệ, 233 chức năng; chuyên đề: Bảo trợ xã hội"},
    "giao_dien":  {"trang_thai": "Chưa làm"},
    "kich_ban":   {"trang_thai": "Xong", "pham_vi": ["IV.4.1"], "che_do": "Gọn", "da_duyet": false, "nguoi_duyet": "", "ngay_duyet": ""},
    "du_lieu":    {"trang_thai": "Chưa làm"},
    "thiet_lap":  {"trang_thai": "Chưa làm"},
    "dieu_kien":  {"trang_thai": "Chưa làm", "ket_luan": "", "bo_qua": null},
    "thuc_thi":   {"trang_thai": "Chưa làm", "so_lan": 0},
    "bao_cao":    {"trang_thai": "Chưa làm"},
    "lark":       {"trang_thai": "Chưa làm", "lan_day_cuoi": ""}
  },
  "trang_ket_qua": {"url": "https://claude.ai/...", "cap_nhat": "..."},
  "nhat_ky": [{"luc": "...", "ai": "Agent tổng | <agent> | Tester", "noi_dung": "..."}]
}
```

- `trang_thai` mỗi bước: `Chưa làm` | `Đang làm` | `Xong` | `Lỗi` (kèm `loi`) | `Bị chặn` (kèm `ly_do`).
- `bo_qua` (bước điều kiện): `{"nguoi": "...", "luc": "...", "ly_do": "..."}` – chỉ ghi khi **tester** quyết định bỏ qua.
- `da_duyet` (kịch bản): chỉ đặt `true` khi **tester** nói duyệt. Kịch bản sinh lại / cập nhật → đặt lại `false`.
- `nhat_ky`: thêm 1 dòng cho mỗi việc đã làm (giữ tối đa 200 dòng gần nhất).
- Thời gian dạng `dd/mm/yyyy HH:MM`.
