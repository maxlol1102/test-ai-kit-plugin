# Checklist rà soát tài liệu yêu cầu

Đi qua **từng mục** cho **từng UC, trường nhập, quy tắc**. Mỗi chỗ trả lời "không" hoặc "không rõ" là một điểm cần xác nhận.

## 1. Trường dữ liệu
- [ ] Có độ dài tối thiểu/tối đa bằng **con số** cụ thể? ("không quá dài", "hợp lý" = mơ hồ)
- [ ] Có định dạng rõ ràng? (SĐT: số chữ số, đầu số, có +84 không; email; mã)
- [ ] Có kiểm tra ngoài định dạng? (CCCD: mã tỉnh, khớp năm sinh/giới tính, trùng)
- [ ] Ngày tháng: có giới hạn trên **và** dưới? Có ràng buộc giữa các ngày?
- [ ] Danh mục: lọc phụ thuộc (tỉnh → xã) đã rõ? Đổi cha thì con có xoá không?
- [ ] Trường có ràng buộc nhưng **bị bỏ trống cột ràng buộc**?

## 2. Tệp đính kèm
- [ ] Định dạng cho phép? Số tệp tối đa? Tổng dung lượng?
- [ ] Biên dung lượng: "không quá X MB" → đúng X có được không? 1 MB = 1000 hay 1024 KB?

## 3. Quy tắc nghiệp vụ / tính toán
- [ ] **Tự tính lại các ví dụ** trong tài liệu: đếm ký tự, cộng ngày, đối chiếu định dạng. Ví dụ có khớp với mô tả không?
- [ ] Tính ngày làm việc: thứ 7, nghỉ lễ, ngày bắt đầu có tính không, tiếp nhận ngoài giờ?
- [ ] Bộ đếm/số thứ tự: khi vượt giới hạn chữ số thì sao? Reset khi nào?
- [ ] Mô tả hiển thị ("màu đỏ", "nổi bật"): hiển thị ở màn hình nào?

## 4. Phân quyền
- [ ] Mỗi vai trò xem/sửa được dữ liệu phạm vi nào (đơn vị mình, cấp dưới, toàn bộ)?
- [ ] **Đối chiếu quy tắc phân quyền với từng UC**: có UC nào nói ngược lại không (vd "hiển thị toàn bộ")?
- [ ] Vai trò được nêu trong tác nhân nhưng không rõ quyền?

## 5. Trạng thái và luồng
- [ ] Vẽ lại sơ đồ trạng thái: **mỗi trạng thái có đường vào VÀ đường ra** (trừ trạng thái kết thúc)?
- [ ] Mỗi chuyển trạng thái có UC/chức năng thực hiện, có người thực hiện?
- [ ] Trạng thái tạm dừng (bổ sung, chờ) có ảnh hưởng thời hạn không?
- [ ] Hủy/xóa: ai được hủy, ở trạng thái nào, có khôi phục không?
- [ ] Mỗi UC có luồng ngoại lệ cho: dữ liệu cấu hình thiếu, người nhận không tồn tại, bị từ chối/trả lại, thao tác đồng thời?
- [ ] Nút trên giao diện có hành vi được đặc tả không (vd nút "Hủy")?

## 6. Thông báo và tích hợp
- [ ] "Gửi thông báo": qua kênh nào (trong hệ thống, email, SMS)? Nội dung?
- [ ] Xuất file (PDF/Excel): mẫu, trường, khổ giấy?

## 7. Tìm kiếm và danh sách
- [ ] "Tìm gần đúng": có phân biệt dấu, hoa/thường, khoảng trắng?
- [ ] Phân trang, sắp xếp, kết hợp nhiều điều kiện (AND/OR)?
- [ ] Phạm vi dữ liệu trong danh sách có khớp phân quyền?

## 8. Yêu cầu phi chức năng
- [ ] Có chỉ số đo được (giây, số người dùng đồng thời, %)? Từ định tính ("nhanh", "thân thiện") → **Không kiểm chứng được**.
- [ ] Trình duyệt "phiên bản mới nhất" tại thời điểm nào?
