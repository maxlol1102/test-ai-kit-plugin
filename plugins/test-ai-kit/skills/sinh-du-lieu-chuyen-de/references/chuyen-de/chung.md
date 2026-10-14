# Quy ước dữ liệu giả lập chung

## Định danh cá nhân (giả lập – NĐ 13/2023/NĐ-CP)
| Trường | Quy ước giả lập | Ví dụ |
|---|---|---|
| Họ tên | Tên giả dễ nhận biết, đủ dấu; có cả tên dài (biên) và tên có ký tự đặc biệt (sai) | Nguyễn Văn Thử, Trần Thị Mẫu, Lê Hoàng Kiểm |
| CCCD / mã định danh cá nhân | 12 chữ số, **bắt đầu `000`** (không trùng mã tỉnh thật) | 000190012345 |
| Số điện thoại | `0900000` + 3 số | 0900000123 |
| Email | `@example.com` | thu.nguyen@example.com |
| Mã số BHXH | 10 chữ số, bắt đầu `00` | 0012345678 |
| Số tài khoản ngân hàng | Bắt đầu `0000`, ghi ngân hàng "Ngân hàng Thử nghiệm" | 0000123456789 |
| Địa chỉ | "Số <n>, <thôn/tổ giả>, Xã Thử Nghiệm, Tỉnh Mẫu" | Số 12, Thôn Một, Xã Thử Nghiệm, Tỉnh Mẫu |

Nếu hệ thống bắt buộc chọn địa giới thật từ danh mục: chọn giá trị có sẵn trong danh mục của hệ thống test, nhưng số nhà/thôn vẫn giả.

## Địa giới hành chính
Từ 01/7/2025 chính quyền địa phương tổ chức **2 cấp: tỉnh – xã** (không còn cấp huyện). Dữ liệu mới chỉ có Tỉnh/Thành phố và Xã/Phường/Đặc khu; tài liệu cũ còn trường Quận/Huyện → ghi điểm cần xác nhận. *(Đối chiếu danh mục của hệ thống test.)*

## Ngày giờ, số, tiền
- Ngày `dd/mm/yyyy`, giờ `HH:mm`; kiểm biên: 29/02 năm nhuận, 31/04 (sai), ngày tương lai, ngày quá xa (01/01/1900).
- Tuổi tính từ ngày sinh tới ngày nghiệp vụ, không tới ngày hiện tại nếu quy tắc nêu khác.
- Tiền: số nguyên VNĐ, hiển thị phân cách hàng nghìn bằng dấu chấm (1.500.000); biên: 0, âm, số rất lớn.
- Ngày làm việc: trừ Thứ Bảy, Chủ nhật và ngày lễ (Tết Dương lịch, Tết Nguyên đán, 10/3 âm lịch, 30/4, 1/5, 2/9 và ngày liền kề theo quy định).

## Bộ ký tự kiểm thử (dùng cho bộ Sai)
`<script>alert(1)</script>`, `' OR '1'='1`, chuỗi chỉ khoảng trắng, emoji 😀, ký tự tổ hợp dấu tiếng Việt (NFD), chuỗi dài hơn giới hạn 1 ký tự, số có khoảng trắng đầu/cuối.

## File đính kèm
Hợp lệ: PDF/DOCX/JPG nhỏ (< 1 MB). Biên: đúng giới hạn dung lượng. Sai: `.exe`, file 0 byte, vượt dung lượng, đổi đuôi sai định dạng.
