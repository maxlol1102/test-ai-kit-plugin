# TÀI LIỆU ĐẶC TẢ YÊU CẦU PHẦN MỀM (SRS)

> ⚠️ **TÀI LIỆU GIẢ LẬP** – do Test AI Kit tự sinh để thử nghiệm, không phải yêu cầu của dự án thật. Sẽ thay bằng SRS chính thức khi có.

| Mục | Nội dung |
|---|---|
| Dự án | Hệ thống thông tin giải quyết thủ tục hành chính tỉnh X (giả lập) |
| Mã dự án | GL-TTHC |
| Phân hệ | Tiếp nhận hồ sơ – Bộ phận Một cửa |
| Phiên bản tài liệu | 0.9 |
| Ngày | 01/10/2026 |

## 1. Giới thiệu

### 1.1. Mục đích
Phân hệ Tiếp nhận hồ sơ hỗ trợ cán bộ Bộ phận Một cửa tiếp nhận hồ sơ trực tiếp của công dân, tổ chức. Hồ sơ sau đó được chuyển cho phòng chuyên môn xử lý và trả kết quả đúng hạn.

### 1.2. Tác nhân

| Mã | Tác nhân | Mô tả |
|---|---|---|
| TN-01 | Cán bộ tiếp nhận (CBTN) | Cán bộ Bộ phận Một cửa của một đơn vị (sở/huyện) |
| TN-02 | Lãnh đạo phòng chuyên môn (LĐ) | Phân công cán bộ xử lý, duyệt kết quả |
| TN-03 | Chuyên viên xử lý (CVXL) | Thẩm định hồ sơ, đề xuất kết quả |
| TN-04 | Quản trị hệ thống (QTHT) | Quản lý danh mục, tài khoản |

### 1.3. Phạm vi
Tài liệu này mô tả 4 use case: UC-01 đến UC-04. Phần nộp hồ sơ trực tuyến qua Cổng dịch vụ công nằm ngoài phạm vi.

## 2. Quy tắc nghiệp vụ

| Mã | Quy tắc |
|---|---|
| BR-01 | Mã hồ sơ do hệ thống tự sinh theo định dạng `[Mã đơn vị]-[yyMMdd]-[STT]`, trong đó Mã đơn vị gồm 3 ký tự chữ in hoa, STT gồm 4 chữ số, đánh lại từ 0001 mỗi ngày. Mã hồ sơ gồm 13 ký tự. Ví dụ: `STP-261001-0001`. |
| BR-02 | Ngày hẹn trả = Ngày tiếp nhận + Thời hạn giải quyết của thủ tục (tính theo ngày làm việc). |
| BR-03 | Mỗi thủ tục có danh sách thành phần hồ sơ bắt buộc. Thiếu thành phần bắt buộc thì không được tiếp nhận. |
| BR-04 | Tệp đính kèm mỗi thành phần hồ sơ không quá 10 MB. |
| BR-05 | CBTN chỉ được xem và thao tác hồ sơ thuộc đơn vị mình. |
| BR-06 | Hồ sơ quá hạn là hồ sơ chưa ở trạng thái "Đã trả kết quả" khi đã qua Ngày hẹn trả. Hồ sơ quá hạn hiển thị màu đỏ. |
| BR-07 | Hồ sơ đã chuyển xử lý thì CBTN không được sửa thông tin người nộp. |

## 3. Trạng thái hồ sơ

| Trạng thái | Mô tả |
|---|---|
| Mới tiếp nhận | CBTN vừa lưu hồ sơ |
| Chờ phân công | Đã chuyển cho LĐ phòng chuyên môn |
| Đang xử lý | LĐ đã phân công CVXL |
| Yêu cầu bổ sung | CVXL yêu cầu công dân bổ sung giấy tờ |
| Chờ trả kết quả | LĐ đã duyệt kết quả |
| Đã trả kết quả | CBTN đã trả kết quả cho công dân |
| Đã hủy | Hồ sơ bị hủy |

Chuyển trạng thái:
- Mới tiếp nhận → Chờ phân công (UC-03)
- Chờ phân công → Đang xử lý (UC-03)
- Đang xử lý → Yêu cầu bổ sung (CVXL thực hiện)
- Đang xử lý → Chờ trả kết quả (LĐ duyệt)
- Chờ trả kết quả → Đã trả kết quả (UC-04)

## 4. Đặc tả use case

### UC-01. Tiếp nhận hồ sơ mới

| Mục | Nội dung |
|---|---|
| Tác nhân | CBTN |
| Điều kiện trước | CBTN đã đăng nhập |
| Điều kiện sau | Hồ sơ được lưu ở trạng thái "Mới tiếp nhận", có Mã hồ sơ và Ngày hẹn trả |

**Thông tin nhập:**

| Trường | Bắt buộc | Ràng buộc |
|---|---|---|
| Thủ tục hành chính | Có | Chọn từ danh mục thủ tục của đơn vị |
| Họ tên người nộp | Có | Không quá dài |
| Số CCCD | Có | 12 chữ số |
| Ngày sinh | Có | Không lớn hơn ngày hiện tại |
| Số điện thoại | Có | |
| Email | Không | Đúng định dạng email |
| Địa chỉ – Tỉnh/Thành phố | Có | Chọn từ danh mục |
| Địa chỉ – Xã/Phường | Có | Chọn từ danh mục, lọc theo Tỉnh/Thành phố đã chọn |
| Địa chỉ chi tiết | Có | Tối đa 255 ký tự |
| Thành phần hồ sơ | Theo thủ tục | Đính kèm tệp cho từng thành phần |
| Ghi chú | Không | Tối đa 1000 ký tự |

**Luồng chính:**
1. CBTN chọn chức năng "Tiếp nhận hồ sơ".
2. Hệ thống hiển thị form tiếp nhận.
3. CBTN chọn Thủ tục hành chính.
4. Hệ thống hiển thị danh sách thành phần hồ sơ của thủ tục, đánh dấu thành phần bắt buộc.
5. CBTN nhập thông tin người nộp và đính kèm tệp.
6. CBTN nhấn "Lưu".
7. Hệ thống kiểm tra dữ liệu, sinh Mã hồ sơ (BR-01), tính Ngày hẹn trả (BR-02), lưu hồ sơ trạng thái "Mới tiếp nhận".
8. Hệ thống hiển thị thông báo "Tiếp nhận hồ sơ thành công" và nút "In phiếu hẹn".

**Luồng thay thế:**
- 6a. CBTN nhấn "Lưu và chuyển xử lý": hệ thống lưu hồ sơ rồi thực hiện UC-03 bước 3.
- 8a. CBTN nhấn "In phiếu hẹn": hệ thống xuất phiếu hẹn dạng PDF gồm Mã hồ sơ, tên thủ tục, người nộp, Ngày hẹn trả.

**Luồng ngoại lệ:**
- 7a. Thiếu trường bắt buộc hoặc sai định dạng: hệ thống hiển thị thông báo lỗi dưới trường tương ứng, không lưu.
- 7b. Thiếu thành phần hồ sơ bắt buộc (BR-03): hệ thống thông báo "Hồ sơ chưa đủ thành phần bắt buộc", không lưu.
- 5a. Tệp vượt quá dung lượng (BR-04): hệ thống thông báo lỗi, không đính kèm tệp đó.

**Giao diện:** Form có các nút "Lưu", "Lưu và chuyển xử lý", "Hủy".

### UC-02. Tra cứu hồ sơ

| Mục | Nội dung |
|---|---|
| Tác nhân | CBTN, LĐ |
| Điều kiện trước | Đã đăng nhập |

**Luồng chính:**
1. Người dùng chọn chức năng "Tra cứu hồ sơ".
2. Hệ thống hiển thị toàn bộ hồ sơ trong hệ thống, sắp xếp theo Ngày tiếp nhận mới nhất, 20 hồ sơ/trang.
3. Người dùng nhập điều kiện tìm kiếm: Mã hồ sơ (chính xác), Họ tên người nộp (tìm gần đúng), Số CCCD, Trạng thái, Khoảng ngày tiếp nhận.
4. Người dùng nhấn "Tìm kiếm".
5. Hệ thống hiển thị danh sách kết quả gồm: Mã hồ sơ, Thủ tục, Người nộp, Ngày tiếp nhận, Ngày hẹn trả, Trạng thái.

**Luồng ngoại lệ:**
- 5a. Không có kết quả: hệ thống hiển thị "Không tìm thấy hồ sơ phù hợp".
- 3a. Ngày bắt đầu lớn hơn ngày kết thúc: hệ thống thông báo lỗi.

### UC-03. Chuyển xử lý và phân công hồ sơ

| Mục | Nội dung |
|---|---|
| Tác nhân | CBTN, LĐ |
| Điều kiện trước | Hồ sơ ở trạng thái "Mới tiếp nhận" (bước 1–4) hoặc "Chờ phân công" (bước 5–8) |

**Luồng chính:**
1. CBTN mở chi tiết hồ sơ trạng thái "Mới tiếp nhận".
2. CBTN nhấn "Chuyển xử lý".
3. Hệ thống hiển thị danh sách phòng chuyên môn được cấu hình cho thủ tục. CBTN chọn phòng.
4. Hệ thống chuyển hồ sơ sang "Chờ phân công", gửi thông báo cho LĐ phòng được chọn.
5. LĐ mở hồ sơ "Chờ phân công".
6. LĐ chọn CVXL trong phòng và nhập ý kiến chỉ đạo (không bắt buộc).
7. LĐ nhấn "Phân công".
8. Hệ thống chuyển hồ sơ sang "Đang xử lý", gửi thông báo cho CVXL.

### UC-04. Trả kết quả

| Mục | Nội dung |
|---|---|
| Tác nhân | CBTN |
| Điều kiện trước | Hồ sơ ở trạng thái "Chờ trả kết quả" |

**Luồng chính:**
1. CBTN tìm hồ sơ (UC-02) và mở chi tiết.
2. CBTN nhấn "Trả kết quả", nhập Ngày trả thực tế và Hình thức trả (Trực tiếp / Bưu chính).
3. Hệ thống chuyển hồ sơ sang "Đã trả kết quả", ghi nhận trả đúng hạn hoặc trễ hạn.

**Luồng ngoại lệ:**
- 2a. Ngày trả thực tế nhỏ hơn Ngày tiếp nhận: hệ thống thông báo lỗi.

## 5. Yêu cầu phi chức năng

| Mã | Yêu cầu |
|---|---|
| NFR-01 | Hệ thống phải phản hồi nhanh, thân thiện với người dùng. |
| NFR-02 | Hỗ trợ trình duyệt Chrome, Edge, Firefox phiên bản mới nhất. |
| NFR-03 | Mọi thao tác thêm/sửa/chuyển trạng thái hồ sơ phải được ghi nhật ký (người, thời gian, nội dung). |
