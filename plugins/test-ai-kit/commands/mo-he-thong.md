---
description: Mở hệ thống cần kiểm thử trong trình duyệt Edge riêng, để tester tự đăng nhập an toàn (không lưu phiên)
argument-hint: <URL hệ thống> [vai trò]
---

Mở hệ thống kiểm thử theo đúng skill `dang-nhap-an-toan`.

Đầu vào của tester: $ARGUMENTS

1. Nếu chưa có URL thì hỏi URL; hỏi vai trò sẽ dùng nếu chưa nêu.
2. Mở URL bằng Playwright, đưa tester tự đăng nhập, chờ tester nhắn "xong".
3. Xác nhận đã vào đúng vai trò, rồi tóm tắt cho tester (ngắn gọn, tiếng Việt):
   - Tên hệ thống / tiêu đề trang, người dùng và vai trò đang đăng nhập.
   - Các mục menu chính nhìn thấy trên trang.
4. Hỏi tester muốn làm gì tiếp (khám phá giao diện, chạy test case…). Giữ nguyên phiên trình duyệt cho đến khi tester bảo xong, rồi đóng trình duyệt.
