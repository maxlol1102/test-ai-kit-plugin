---
name: day-len-lark
description: Đồng bộ dự án, test case, lỗi và lần chạy lên Lark Base "Quản lý kiểm thử" bằng tài khoản Lark của tester – thêm bản ghi mới, cập nhật bản ghi đã có theo mã, không bao giờ xoá. Dùng khi tester nói "đẩy lên Lark", "cập nhật Lark", "đồng bộ lỗi/test case lên Base", hoặc ở bước cuối của quy trình kiểm thử.
---

# Đẩy dữ liệu lên Lark Base

Cấu hình Base nằm ở `test-ai-kit/cau-hinh.json` → `lark.app_token`, `lark.bang` (table_id của 4 bảng). Chưa có → làm skill `cai-dat-lark-base` trước.

## Quy tắc (từ quy định của công ty)
- Mọi lệnh Lark gọi với `useUAT: true`. Lỗi xác thực → nhắc tester bấm `DANG-NHAP-LAI.cmd` (bộ cài TRINAM-Claude-Lark). Lỗi quyền → nói rõ cần xin quyền gì, từ ai (chủ Base).
- **Trình bày trước, chờ tester đồng ý**: số bản ghi thêm mới / cập nhật theo từng bảng.
- Ghi nhiều bản ghi bằng `bitable_v1_appTableRecord_batchCreate` / `batchUpdate`, **tối đa 500 bản ghi/lần**; báo lại số bản ghi đã ghi.
- **Không xoá** bản ghi trong bất kỳ trường hợp nào. Lỗi bị huỷ → trạng thái "Từ chối".
- Không đổi cấu trúc bảng/trường ở bước này (thiếu trường → báo tester, dùng skill `cai-dat-lark-base`).

## Ánh xạ dữ liệu → bảng

| Bảng | Khoá so khớp | Nguồn | Trường |
|---|---|---|---|
| Dự án | `Mã dự án` | `trang-thai.json` | Mã dự án, Tên dự án, Người phụ trách, Ngày bắt đầu, Trạng thái (Đang chuẩn bị / Đang kiểm thử / …), Hệ thống test |
| Test case | `Mã TC` | `kich-ban/test-case.json` | Mã TC, Mã dự án, Mã yêu cầu (nối bằng ", "), Chức năng, Tiêu đề, Nhóm, Loại, Ưu tiên, Trạng thái (trống → "Chưa chạy") |
| Lỗi | `Mã lỗi` | `bao-cao/loi.json` | Mã lỗi, Mã dự án, Tiêu đề, Mức độ, Độ ưu tiên, Trạng thái, Nguồn phát hiện ("AI" nếu bắt đầu bằng "AI", ngược lại "Tester"), Test case liên quan, Ngày phát hiện |
| Lần chạy | `Mã lần chạy` | `thuc-thi/LC-*.json` | Mã lần chạy, Mã dự án, Ngày bắt đầu, Phạm vi, Số TC, Đạt, Không đạt, Bị chặn, Trạng thái |

Trường **Người phụ trách** (kiểu Người): chỉ điền khi biết open_id của người đó trong Lark (tra bằng công cụ Lark); không biết thì để trống, không đoán.
Trường **Ngày**: Lark nhận mốc thời gian mili-giây.

## Các bước
1. Đọc cấu hình; liệt kê bản ghi hiện có của mỗi bảng (`appTableRecord_search` lọc theo `Mã dự án`) để biết bản ghi nào đã có.
2. Lập danh sách thêm mới / cập nhật (chỉ cập nhật khi giá trị khác). Trình bày số lượng → chờ đồng ý.
3. Ghi theo lô ≤ 500. Ghi `trang-thai.json` → `buoc.lark` (`lan_day_cuoi`, số bản ghi theo bảng).
4. Báo lại số bản ghi đã thêm/cập nhật mỗi bảng và link Base.
