---
name: xuat-bao-cao
description: Thống kê kết quả kiểm thử bằng code (không để AI tự đếm) và xuất Biểu mẫu kết quả kiểm thử theo Mẫu 3 Trí Nam ra Excel – tổng hợp theo nhóm kịch bản, thống kê lỗi theo mức độ/trạng thái, đánh giá, danh sách TC và lỗi kèm bằng chứng. Dùng khi tester cần báo cáo kết quả, biểu mẫu nghiệm thu, hoặc số liệu tiến độ thực thi.
---

# Xuất báo cáo kết quả kiểm thử

Script: `scripts/xuat_bao_cao.py` (cùng thư mục file này), chạy bằng Python của `test-ai-kit/.venv`.

| Lệnh | Kết quả |
|---|---|
| `python xuat_bao_cao.py thong-ke <thư mục dự án>` | In JSON số liệu: tổng TC, theo trạng thái, tỷ lệ đạt, TC ưu tiên Cao chưa chạy, kết quả AI chưa xác nhận, theo nhóm, theo chức năng, lỗi theo mức độ, lỗi nghiêm trọng còn mở, lỗi chưa xác nhận |
| `python xuat_bao_cao.py excel <thư mục dự án> <file.xlsx>` | Biểu mẫu 3 sheet: **Tổng hợp** (thông tin, kết quả theo nhóm, thống kê lỗi, đánh giá), **Kết quả test case**, **Danh sách lỗi** |

Script đọc: `trang-thai.json`, `kich-ban/test-case.json`, `bao-cao/loi.json`, `bao-cao/danh-gia.json`.

## Quy tắc
- Số liệu trong báo cáo **chỉ lấy từ script**; đánh giá bằng lời (`danh-gia.json`) không được mâu thuẫn với số liệu.
- Kết luận: còn lỗi Critical chưa đóng hoặc > 20% TC ưu tiên Cao chưa chạy → "Chưa đủ điều kiện"; còn lỗi Major mở hoặc kết quả AI chưa xác nhận → tối đa "Đủ điều kiện có điều kiện".
- Báo cáo luôn ghi phần AI thực hiện và phần tester đã xác nhận (Mẫu 3 mục 7).
- Biên bản nghiệm thu (Mẫu 4): dùng số liệu Mẫu 3; phần căn cứ hợp đồng, thành phần tham dự, chữ ký do tester điền.
