---
name: cai-dat-lark-base
description: Tạo Lark Base "Quản lý kiểm thử" (4 bảng Dự án, Test case, Lỗi, Lần chạy) trong tài khoản Lark của tester, hoặc nối với Base đã có, rồi lưu mã Base vào cấu hình làm việc. Dùng khi chạy /test-ai-kit:cai-dat, khi tester nói "tạo Base kiểm thử", "nối Lark", hoặc khi cần đẩy dữ liệu lên Lark mà chưa có cấu hình Base.
---

# Cài đặt Lark Base cho Test AI Kit

Cấu trúc chuẩn: [cau-truc-base.json](cau-truc-base.json) – không tự ý thêm/bớt/đổi tên trường.

## Điều kiện

- Kết nối `lark-base` (MCP) có sẵn. Không có → tester cài **bộ cài TRINAM-Claude-Lark** của công ty (bấm `CAI-DAT.cmd`, đăng nhập Lark, Authorize), thoát hẳn Claude rồi mở lại. Không tự cài thay, không hỏi App ID/Secret.
- Mọi lệnh Lark gọi với `useUAT: true` (tài khoản Lark của chính tester).
- Lỗi xác thực / hết phiên → nhắc tester bấm `DANG-NHAP-LAI.cmd` trong thư mục bộ cài.
- Lỗi quyền → nói rõ cần xin quyền gì, từ ai (chủ Base).

## Các bước

1. Đọc `test-ai-kit/cau-hinh.json` trong thư mục làm việc. Đã có `lark.app_token` → hỏi tester dùng tiếp Base đó hay tạo mới; dùng tiếp thì chỉ kiểm tra 4 bảng còn đủ, xong.
2. Hỏi tester: **tạo Base mới** hay **nối Base có sẵn** (tester dán link Base).
3. **Trình bày cấu trúc** (tên Base, 4 bảng, trường và loại trường, các lựa chọn) dạng bảng ngắn và **chờ tester đồng ý** trước khi tạo bất cứ thứ gì.
4. Tạo mới: tạo Base (`bitable_v1_app_create`, tên "Quản lý kiểm thử – <tên nhóm/dự án>"), rồi tạo 4 bảng kèm trường (`bitable_v1_appTable_create` / `bitable_v1_appTable_batchCreate`; trường thiếu thì `bitable_v1_appTableField_create`).
   Nối Base có sẵn: liệt kê bảng/trường, so với cấu trúc chuẩn, báo phần thiếu/khác; **chỉ thêm** phần thiếu khi tester đồng ý; **không xoá, không đổi tên** bảng/trường có sẵn.
5. Ghi vào `test-ai-kit/cau-hinh.json`:
   `{"lark": {"app_token": "...", "url": "...", "bang": {"Dự án": "tbl...", "Test case": "tbl...", "Lỗi": "tbl...", "Lần chạy": "tbl..."}}}` (giữ nguyên các khoá khác trong file).
6. Báo lại: link Base, số bảng/trường đã tạo hoặc đã thêm.

Không ghi bản ghi mẫu vào Base. Không xoá bảng, trường, bản ghi trong mọi trường hợp.
