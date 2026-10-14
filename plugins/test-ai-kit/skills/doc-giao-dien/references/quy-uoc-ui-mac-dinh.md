# Quy ước giao diện mặc định (khi không có Figma/thiết kế)

Chuẩn tối thiểu để viết và chấm test case nhóm **UI/UX** cho hệ thống phần mềm của Trí Nam. Thiết kế của dự án (Figma, ảnh SRS) luôn ưu tiên hơn quy ước này.

## Chung
- Tiếng Việt có dấu, đúng chính tả, nhất quán thuật ngữ giữa menu, tiêu đề màn, nút, thông báo.
- Tiêu đề màn hình trùng tên chức năng trên menu; có đường dẫn (breadcrumb) hoặc menu đang chọn được đánh dấu.
- Không vỡ bố cục ở độ rộng 1366 px và 1920 px; không thanh cuộn ngang ngoài ý muốn.

## Form nhập liệu
- Trường bắt buộc có dấu `*` (màu đỏ) cạnh nhãn; nhãn rõ nghĩa, có placeholder gợi ý định dạng (vd `dd/mm/yyyy`).
- Lỗi nhập hiển thị **ngay dưới trường** sai, nội dung nói rõ cách sửa (vd "Số CCCD gồm 12 chữ số"); focus chuyển tới trường lỗi đầu tiên.
- Ngày dạng `dd/mm/yyyy`; số tiền có phân cách hàng nghìn bằng dấu chấm; giới hạn độ dài thể hiện (đếm ký tự hoặc chặn nhập vượt).
- Nút chính (Lưu/Gửi) nổi bật nhất; nút Huỷ/Đóng luôn có; Huỷ khi có dữ liệu chưa lưu → hỏi xác nhận.
- Tải file: ghi rõ định dạng và dung lượng tối đa; báo lỗi khi sai định dạng/quá dung lượng.

## Danh sách / lưới dữ liệu
- Có tìm kiếm và/hoặc bộ lọc; nút Tìm kiếm và Làm mới/Xoá lọc.
- Có phân trang (số bản ghi/trang, tổng số); không có dữ liệu → thông báo "Không có dữ liệu" thay vì bảng trống.
- Cột STT, cột thao tác (xem/sửa/xoá) nhất quán vị trí; thao tác không được phép với vai trò → ẩn hoặc mờ.

## Thông báo
- Thành công: thông báo ngắn, tự ẩn sau vài giây (toast) hoặc chuyển màn kèm thông báo.
- Xoá / thao tác không hoàn tác: hộp thoại xác nhận nêu rõ đối tượng.
- Lỗi hệ thống: thông báo thân thiện, không lộ thông tin kỹ thuật (stack trace, câu SQL).

## Phân quyền trên giao diện
- Menu/chức năng ngoài quyền vai trò không hiển thị; truy cập trực tiếp bằng URL → trang "Không có quyền" (không lộ dữ liệu).
