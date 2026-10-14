# Mẫu biểu chuẩn kiểm thử – Trí Nam (bản nháp v0.1)

> Bản nháp. Sẽ đối chiếu với mẫu hiện có của công ty (nếu có) trước khi chốt.

## Mẫu 1 – Test case

| Cột | Mô tả | Ví dụ |
|---|---|---|
| Mã TC | `TC-<Mã chức năng>-<STT 3 số>` | TC-QLHS-001 |
| Mã yêu cầu | Mã yêu cầu/UC trong SRS (để truy vết) | UC-05 |
| Chức năng | Tên chức năng/màn hình | Thêm mới hồ sơ |
| Tiêu đề | Kiểm tra gì, trong điều kiện nào | Lưu hồ sơ khi bỏ trống trường bắt buộc |
| Loại | Chức năng / Giao diện / Phân quyền / Biên / Ngoại lệ / API / Hiệu năng / ATTT | Ngoại lệ |
| Kỹ thuật | Kỹ thuật thiết kế: PVTĐ / GTB / BQĐ / CTT / PQ / LUC / ĐL | LUC |
| Ưu tiên | Cao / Trung bình / Thấp – TC "Cao" là bộ hồi quy tối thiểu | Trung bình |
| Điều kiện trước | Trạng thái cần có trước khi test | Đăng nhập vai trò Chuyên viên |
| Bước thực hiện | Đánh số 1, 2, 3… | 1. Mở màn hình Thêm mới… |
| Dữ liệu test | Lấy từ bộ dữ liệu giả lập | Họ tên: (để trống) |
| Kết quả mong đợi | Theo SRS | Hiện thông báo "Vui lòng nhập Họ tên" |
| Mã DX | Điểm cần xác nhận liên quan (nếu kết quả mong đợi dựa trên giả định) | DX-03 |
| Kết quả thực tế | Điền khi chạy | |
| Trạng thái | Chưa chạy / Đạt / Không đạt / Bị chặn | |
| Mã lỗi | Nếu Không đạt | |
| Người thực hiện / Ngày | | |

## Mẫu 2 – Bug report

| Trường | Mô tả |
|---|---|
| Mã lỗi | `BUG-<Mã dự án>-<STT>` |
| Mã dự án | |
| Tiêu đề | [Chức năng] Hiện tượng – điều kiện. Ví dụ: "[Thêm hồ sơ] Không lưu được khi nhập địa chỉ có dấu" |
| Môi trường | Local / Staging / Online – URL, trình duyệt, phiên bản build |
| Mức độ | Critical / Major / Minor / Trivial |
| Độ ưu tiên | P1 / P2 / P3 / P4 |
| Bước tái hiện | Đánh số, đủ để người khác làm lại được |
| Kết quả mong đợi | |
| Kết quả thực tế | |
| Bằng chứng | Ảnh chụp, video, log console/network |
| Test case liên quan | Mã TC |
| Người phát hiện / Ngày | |
| Người phụ trách sửa | |
| Trạng thái | Mới → Đang sửa → Đã sửa → Đóng / Mở lại / Từ chối |
| Nguồn phát hiện | Tester / AI (agent nào) – AI phát hiện thì tester phải xác nhận |

## Mẫu 3 – Báo cáo kết quả test

1. **Thông tin chung:** dự án, module, phiên bản build, môi trường, thời gian test, người test.
2. **Phạm vi:** chức năng được test / không được test (kèm lý do).
3. **Kết quả test case:**

   | Chức năng | Tổng TC | Đạt | Không đạt | Bị chặn | Chưa chạy | Tỷ lệ đạt |
   |---|---|---|---|---|---|---|

4. **Thống kê lỗi:**

   | Mức độ | Mới | Đang sửa | Đã sửa | Đóng | Mở lại | Tổng |
   |---|---|---|---|---|---|---|

5. **Lỗi tồn đọng nghiêm trọng:** danh sách Critical/Major chưa đóng.
6. **Rủi ro và khuyến nghị:** có đủ điều kiện chuyển UAT/nghiệm thu không.
7. **Phần AI thực hiện / phần tester đã xác nhận.**

## Mẫu 4 – Biên bản test phục vụ nghiệm thu

1. Căn cứ: hợp đồng số…, tài liệu yêu cầu (SRS) phiên bản…
2. Thời gian, địa điểm, thành phần tham dự (bên A, bên B).
3. Đối tượng kiểm thử: hệ thống/phân hệ, phiên bản.
4. Nội dung và kết quả kiểm thử: tổng hợp theo Mẫu 3, đính kèm danh sách test case và kết quả.
5. Tồn tại và cam kết khắc phục (nếu có).
6. Kết luận: Đạt / Đạt có điều kiện / Không đạt.
7. Chữ ký các bên.
