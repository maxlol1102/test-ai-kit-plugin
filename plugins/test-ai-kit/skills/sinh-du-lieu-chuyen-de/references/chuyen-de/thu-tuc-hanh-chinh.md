# Chuyên đề: Thủ tục hành chính – một cửa – dịch vụ công

> Căn cứ thường gặp: Nghị định 61/2018/NĐ-CP về thực hiện cơ chế một cửa, một cửa liên thông (sửa đổi bởi Nghị định 107/2021/NĐ-CP); quy định về dịch vụ công trực tuyến. **Đối chiếu SRS và văn bản hiện hành**; quy tắc của hệ thống lấy từ SRS.

## Đối tượng nghiệp vụ chính
| Đối tượng | Trường thường có |
|---|---|
| Thủ tục hành chính | Mã thủ tục, tên, lĩnh vực, cơ quan thực hiện, thời hạn giải quyết (ngày làm việc), phí/lệ phí, thành phần hồ sơ (bắt buộc / tuỳ chọn), mức độ dịch vụ công (toàn trình / một phần) |
| Hồ sơ | **Mã hồ sơ** (thường: mã đơn vị – yymmdd – số thứ tự), thủ tục, người nộp (họ tên, định danh, SĐT, email, địa chỉ), kênh nộp (trực tiếp / trực tuyến / bưu chính), ngày tiếp nhận, **ngày hẹn trả**, trạng thái, cán bộ xử lý, thành phần đã nộp |
| Quá trình xử lý | Bước (tiếp nhận → phân công → thẩm định → trình ký → trả kết quả), người xử lý, thời điểm, ý kiến, hạn bước |
| Kết quả | Loại kết quả (giấy phép, quyết định, văn bản trả lời…), số, ngày ký, hình thức trả (trực tiếp / bưu chính / trực tuyến) |
| Phí/lệ phí | Số tiền, hình thức thanh toán, trạng thái thanh toán, biên lai |

## Vòng đời trạng thái thường gặp
Mới tiếp nhận → Chờ phân công → Đang xử lý → (Yêu cầu bổ sung ↔ Đã bổ sung) → Chờ ký → Đã có kết quả → Đã trả kết quả; nhánh: Từ chối / Rút hồ sơ / **Quá hạn** (khi qua ngày hẹn chưa có kết quả).

## Ràng buộc nhất quán
- Ngày hẹn trả = ngày tiếp nhận + thời hạn giải quyết tính theo **ngày làm việc** (trừ T7, CN, lễ); hồ sơ yêu cầu bổ sung thường tính lại thời hạn từ khi bổ sung đủ (theo SRS).
- Mã hồ sơ duy nhất, gắn đơn vị tiếp nhận; số thứ tự tăng trong ngày.
- Phân quyền theo đơn vị: cán bộ đơn vị A không xem/xử lý hồ sơ đơn vị B (trừ liên thông).
- Đủ thành phần bắt buộc mới được tiếp nhận; file đính kèm đúng định dạng/dung lượng.

## Văn bản / hồ sơ mẫu nên tạo (tao_van_ban.py)
Đơn/tờ khai đề nghị theo thủ tục; bản sao giấy tờ tuỳ thân (ghi rõ GIẢ LẬP); giấy tiếp nhận hồ sơ và hẹn trả kết quả; phiếu yêu cầu bổ sung, hoàn thiện hồ sơ; phiếu từ chối giải quyết; kết quả giải quyết (quyết định/giấy phép mẫu).

## Tình huống kiểm thử nên có dữ liệu
Tiếp nhận đủ hồ sơ; thiếu thành phần bắt buộc; tính ngày hẹn qua cuối tuần/lễ; yêu cầu bổ sung rồi bổ sung; quá hạn; từ chối; rút hồ sơ; tra cứu theo mã/họ tên (có dấu, không dấu); phân quyền đơn vị; nộp trực tuyến + thanh toán phí; danh sách lớn để test thống kê/báo cáo.
