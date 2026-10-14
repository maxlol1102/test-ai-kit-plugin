# Bộ mẫu để thử Test AI Kit

Toàn bộ là **dữ liệu giả lập** – dùng để làm quen và thử cả quy trình mà không cần hệ thống thật.

| File | Dùng để |
|---|---|
| `SRS-gia-lap-tiep-nhan-ho-so.md` | Đặc tả giả lập chức năng "Tiếp nhận hồ sơ" – làm đầu vào cho dự án thử |
| `he-thong-demo/` | Website giả lập dựng đúng theo SRS trên, **có 4 lỗi cài sẵn** để xem AI có phát hiện không |
| `he-thong-demo/tai-khoan-demo.js` | Tài khoản giả của hệ thống DEMO (chỉ dùng cho DEMO) |

## Thử nhanh
1. Bấm đúp `he-thong-demo/CHAY-DEMO.cmd` (cần Node.js) → mở http://127.0.0.1:8766.
2. Trong Claude Code: `/test-ai-kit:kiem-thu` → tạo dự án mã `DEMO`, URL `http://127.0.0.1:8766`, vai trò "Cán bộ tiếp nhận", chép file SRS giả lập vào `test-ai-kit/du-an/DEMO/dau-vao/`.
3. Agent tổng dẫn từng bước; khi trình duyệt mở trang đăng nhập DEMO, tự đăng nhập bằng tài khoản trong `tai-khoan-demo.js`.

4 lỗi cài sẵn: không giới hạn độ dài họ tên; nhận số điện thoại 9 chữ số; tra cứu thấy hồ sơ của đơn vị khác; tìm họ tên phân biệt dấu.
