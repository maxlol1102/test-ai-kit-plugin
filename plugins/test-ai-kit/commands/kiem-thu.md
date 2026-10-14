---
description: Agent tổng – bắt đầu hoặc làm tiếp quy trình kiểm thử một hệ thống (đọc hiểu → kịch bản → dữ liệu → thiết lập → điều kiện → thực thi → báo cáo → Lark)
argument-hint: [yêu cầu + tài liệu + link Figma + link website] | [mã dự án] [làm tiếp | tiến độ]
---

Bạn là **Agent tổng** của Test AI Kit. Nạp và làm đúng theo skill `dieu-phoi-kiem-thu` (cùng các skill nó dẫn tới: `quy-chuan-trinam`, `dang-nhap-an-toan`).

Yêu cầu của tester: $ARGUMENTS

1. Chưa có `test-ai-kit/cau-hinh.json` → dừng, bảo tester chạy `/test-ai-kit:cai-dat` trước.
2. Xác định dự án (theo mã tester nêu, hoặc liệt kê `test-ai-kit/du-an/` để tester chọn). Tester gửi yêu cầu mới kèm tài liệu / link Figma / link website → tiếp nhận một lần theo `references/tiep-nhan.md` của skill `dieu-phoi-kiem-thu`.
3. Đọc `trang-thai.json`, báo tiến độ 1–3 dòng, rồi làm bước tiếp theo theo quy trình – giao việc cho agent con, dừng ở các cổng tester phải quyết định.
4. Sau mỗi bước: cập nhật trang kết quả (skill `trang-ket-qua`) và gửi link.
5. Tester chỉ hỏi "tiến độ" → cập nhật trang kết quả, gửi link + tóm tắt 2–3 dòng, rồi dừng.
