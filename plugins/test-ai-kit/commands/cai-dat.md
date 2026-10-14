---
description: Cài đặt và kiểm tra Test AI Kit trên máy tester – Node.js, trình duyệt Playwright, kết nối Lark, Lark Base "Quản lý kiểm thử", thư mục làm việc
---

Bạn đang cài đặt Test AI Kit cho tester. Làm lần lượt, mỗi mục báo ✅ / ⚠️ / ❌ ngắn gọn bằng tiếng Việt. Không hỏi API key (công cụ chạy bằng gói Claude Max, không dùng Claude API).

## 1. Môi trường

- Chạy `node --version`. Thiếu hoặc < 18 → ❌, hướng dẫn: cài bộ **TRINAM-Claude-Lark** của công ty (tự cài Node.js) hoặc tải Node LTS tại nodejs.org; cài xong mở lại Claude.
- Kiểm tra đang chạy trên Windows/macOS bản thường, **không phải WSL** (plugin và trình duyệt không chạy trong WSL).

## 2. Python cho các script (đọc SRS, xuất Excel, tạo văn bản mẫu)

- Tìm Python ≥ 3.10: Windows thử `py -3 --version` rồi `python --version`; macOS/Linux `python3 --version`.
  - Không có → hỏi tester đồng ý rồi cài: Windows `winget install --id Python.Python.3.12 -e` (cài xong mở lại Claude); macOS hướng dẫn tải tại python.org.
- Tạo môi trường riêng trong thư mục làm việc (nếu chưa có): `<python> -m venv test-ai-kit/.venv`.
- Cài thư viện: nạp skill `doc-tai-lieu` để biết thư mục gốc của nó, rồi chạy
  `test-ai-kit/.venv/Scripts/python -m pip install -q -r <thư mục skill doc-tai-lieu>/scripts/requirements.txt`
  (macOS/Linux: `test-ai-kit/.venv/bin/python`).
- Kiểm tra: `test-ai-kit/.venv/Scripts/python -c "import docx, openpyxl, PIL, pypdf; print('ok')"` → ✅.

## 3. Trình duyệt kiểm thử (Playwright)

- Gọi `browser_navigate` tới `about:blank` rồi `browser_close`.
  - Được → ✅ (cửa sổ Microsoft Edge vừa mở và đóng là bình thường).
  - Lỗi thiếu trình duyệt → chạy `npx -y @playwright/mcp@0.0.83 --help` để tải gói; vẫn lỗi thì báo tester cần Microsoft Edge.
  - Không thấy công cụ `browser_*` → plugin chưa nạp xong: nhắc tester khởi động lại Claude Code.

## 4. Kết nối Lark

- Tìm công cụ `lark-base` (vd liệt kê base: `bitable_v1_app_get` không cần, chỉ cần thấy công cụ có sẵn).
  - Có → thử một lệnh đọc nhẹ với `useUAT: true` để chắc đã đăng nhập. Lỗi xác thực → nhắc bấm `DANG-NHAP-LAI.cmd` trong thư mục bộ cài TRINAM-Claude-Lark.
  - Không có → ⚠️, hướng dẫn cài bộ **TRINAM-Claude-Lark** (bấm `CAI-DAT.cmd`, đăng nhập Lark, Authorize), thoát hẳn Claude rồi mở lại, sau đó chạy lại lệnh này. Các bước còn lại vẫn làm được, riêng Lark để sau.

## 5. Thư mục làm việc

Trong thư mục hiện tại tạo (nếu chưa có):
```
test-ai-kit/
├── cau-hinh.json      ← {"phien_ban": "<version trong plugin.json>", "nguoi_dung": {...}, "lark": {...}}
├── .venv/             ← Python + thư viện cho script (bước 2)
├── du-an/             ← mỗi hệ thống kiểm thử một thư mục con
└── bang-chung/        ← ảnh chụp do Playwright lưu
```
Hỏi họ tên + chức danh của tester (Tester / Trưởng nhóm kiểm thử / BA / Quản lý dự án) để ghi vào `nguoi_dung` – tên này ghi vào kết quả, người duyệt, người xác nhận lỗi. Đã có thì giữ, chỉ hỏi có muốn đổi không.

## 6. Lark Base

Kết nối Lark ✅ → làm theo skill `cai-dat-lark-base` (trình cấu trúc, chờ tester đồng ý rồi mới tạo).

## 7. Tổng kết

Bảng 6 dòng (Môi trường, Python, Trình duyệt, Lark, Thư mục làm việc, Lark Base) với trạng thái và việc tester cần làm nếu có. Lark chưa xong không chặn việc dùng thử.

Kết thúc bằng 2 lựa chọn:
- **Dùng thử ngay** (khuyên dùng lần đầu): `/test-ai-kit:thu-demo` – chạy cả quy trình trên hệ thống DEMO giả lập đi kèm, có trang kết quả để xem.
- **Kiểm thử hệ thống thật**: `/test-ai-kit:kiem-thu` – Agent tổng hỏi mã dự án, URL, tài liệu rồi dẫn từng bước.

Hỏi tester muốn bắt đầu cái nào; tester chọn thì làm luôn (nạp skill `thu-demo` hoặc `dieu-phoi-kiem-thu`), không bắt gõ lại lệnh.
