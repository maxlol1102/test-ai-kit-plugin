---
name: thu-demo
description: Chạy thử Test AI Kit ngay sau khi cài, trên hệ thống DEMO giả lập đi kèm plugin (Tiếp nhận hồ sơ TTHC, có 4 lỗi cài sẵn) – bật DEMO ở cổng 8766, tạo dự án DEMO với SRS giả lập, rồi để Agent tổng dẫn cả quy trình. Dùng khi chạy /test-ai-kit:thu-demo, hoặc tester nói "chạy thử", "làm quen", "thử demo", "cho xem tool làm được gì".
---

# Chạy thử trên hệ thống DEMO

Mọi thứ cần dùng nằm cạnh file này – tester không phải tải gì thêm:

| File | Dùng để |
|---|---|
| `SRS-gia-lap-tiep-nhan-ho-so.md` | Đặc tả giả lập chức năng "Tiếp nhận hồ sơ" – đầu vào của dự án DEMO |
| `he-thong-demo/` | Website giả lập dựng theo SRS trên, **có 4 lỗi cài sẵn** |
| `he-thong-demo/CHAY-DEMO.cmd` | Cách bật tay (bấm đúp) nếu cần |

Toàn bộ là dữ liệu giả. Trang đăng nhập DEMO tự hiện tài khoản thử – tester tự đăng nhập như hệ thống thật (vẫn theo skill `dang-nhap-an-toan`, AI không gõ mật khẩu).

## Các bước

1. **Đã cài đặt chưa**: chưa có `test-ai-kit/cau-hinh.json` → chạy phần cài đặt trước (lệnh `/test-ai-kit:cai-dat`), xong quay lại đây.
2. **Bật DEMO** (gọi `<thư mục skill>` là thư mục chứa file này):
   - Thử `curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8766` – ra `200` là đang chạy, sang bước 3.
   - Chưa chạy → bật bằng lệnh nền (công cụ Bash, `run_in_background: true`):
     `npx -y http-server@14.1.1 "<thư mục skill>/he-thong-demo" -p 8766 -a 127.0.0.1 -c-1 --silent`
     rồi thử lại `curl` vài lần (lần đầu npx tải gói mất khoảng 10–30 giây).
3. **Tạo dự án `DEMO`** (đã có thì hỏi tester: làm tiếp hay làm lại từ đầu – làm lại thì đổi tên thư mục cũ thành `DEMO-cu-<ngày>`, không xoá):
   - Thư mục theo `dieu-phoi-kiem-thu/references/cau-truc-du-an.md`.
   - Chép `SRS-gia-lap-tiep-nhan-ho-so.md` vào `test-ai-kit/du-an/DEMO/dau-vao/`.
   - `he-thong.md`: URL `http://127.0.0.1:8766`, vai trò "Cán bộ tiếp nhận", chuyên đề Thủ tục hành chính, phạm vi "Tiếp nhận hồ sơ, Tra cứu hồ sơ", ghi chú "Hệ thống giả lập – được phép tạo dữ liệu tuỳ ý".
   - `trang-thai.json` với `ten` = "DEMO – Tiếp nhận hồ sơ TTHC (giả lập)".
4. **Báo tester** 3–4 dòng: DEMO đang chạy ở http://127.0.0.1:8766; tool sẽ tự đọc SRS, sinh kịch bản, sinh dữ liệu, mở trình duyệt để anh/chị đăng nhập rồi tự chạy test; thử xem AI có tìm ra **4 lỗi cài sẵn** không (chưa nói lỗi là gì).
5. Chuyển sang vai trò **Agent tổng** (skill `dieu-phoi-kiem-thu`) và làm dự án `DEMO` từ bước Đọc hiểu hệ thống. Với DEMO: dùng chế độ **Gọn**, tester có thể trả lời "duyệt" nhanh; bước Kiểm tra thiết lập bỏ qua được (DEMO không có checklist dev) – vẫn ghi `bo_qua` với lý do "Hệ thống giả lập".

## Đáp án (chỉ nói khi đã chạy xong bước Thực thi, hoặc tester hỏi)

1. Họ tên không giới hạn độ dài.
2. Số điện thoại nhận 9 chữ số.
3. Tra cứu thấy hồ sơ của đơn vị khác.
4. Tìm theo họ tên phân biệt dấu (gõ không dấu không ra).

So với lỗi AI đã báo trong `bao-cao/loi.json`: nêu lỗi nào tìm ra, lỗi nào chưa và vì sao (thiếu TC nào).

Xong việc: nhắc tester DEMO vẫn chạy nền – tắt bằng cách đóng phiên Claude Code hoặc dừng tác vụ nền.
