# Chuyên đề: Bảo trợ xã hội (trợ giúp xã hội)

> Căn cứ thường gặp: Nghị định 20/2021/NĐ-CP về chính sách trợ giúp xã hội đối với đối tượng bảo trợ xã hội, được sửa đổi bởi Nghị định 76/2024/NĐ-CP (mức chuẩn trợ giúp xã hội 500.000 đồng/tháng từ 01/7/2024). **Luôn đối chiếu SRS và văn bản hiện hành** – số liệu dưới đây chỉ để sinh dữ liệu hợp lý, không phải quy tắc kiểm thử; quy tắc của hệ thống lấy từ SRS, thiếu thì ghi điểm cần xác nhận.

## Đối tượng nghiệp vụ chính
| Đối tượng | Trường thường có |
|---|---|
| Đối tượng bảo trợ xã hội | Mã đối tượng, họ tên, ngày sinh, giới tính, dân tộc, mã định danh, nơi thường trú (tỉnh, xã), **loại đối tượng**, tình trạng (đang hưởng / tạm dừng / thôi hưởng / đã chết), ngày bắt đầu hưởng, hệ số, mức trợ cấp, hình thức chi trả (tiền mặt / tài khoản), mã thẻ BHYT |
| Hồ sơ đề nghị trợ giúp | Mã hồ sơ, đối tượng, loại trợ giúp (hàng tháng / đột xuất / nuôi dưỡng tại cơ sở), ngày nộp, thành phần hồ sơ, trạng thái xử lý, người xử lý |
| Quyết định | Số quyết định, ngày ký, người ký, loại (hưởng / điều chỉnh / thôi hưởng / truy lĩnh), đối tượng, mức hưởng, ngày hiệu lực |
| Chi trả | Kỳ chi trả (tháng/năm), đối tượng, số tiền, truy lĩnh, đơn vị/kênh chi trả, trạng thái (chưa chi / đã chi / hoàn trả) |
| Người khuyết tật | Dạng tật (vận động, nghe nói, nhìn, thần kinh–tâm thần, trí tuệ, khác), mức độ (đặc biệt nặng / nặng / nhẹ), số giấy xác nhận khuyết tật, ngày cấp |
| Cơ sở trợ giúp xã hội | Mã cơ sở, tên, loại (công lập / ngoài công lập), địa chỉ, sức chứa, số đối tượng đang nuôi dưỡng |

## Nhóm đối tượng hưởng trợ cấp hàng tháng (để sinh "loại đối tượng")
Trẻ em không có nguồn nuôi dưỡng; người từ 16 đến 22 tuổi đang đi học thuộc diện trên; trẻ em nhiễm HIV/AIDS thuộc hộ nghèo; người đơn thân thuộc hộ nghèo đang nuôi con nhỏ; **người cao tuổi** (thuộc hộ nghèo/cận nghèo không có người phụng dưỡng, người cao tuổi đủ tuổi theo quy định không có lương hưu/trợ cấp BHXH…); **người khuyết tật** đặc biệt nặng / nặng; trẻ em dưới 3 tuổi thuộc hộ nghèo/cận nghèo… *(ngưỡng tuổi và điều kiện cụ thể: theo SRS/văn bản hiện hành)*.

Mức trợ cấp hàng tháng = **mức chuẩn trợ giúp xã hội × hệ số** của loại đối tượng (hệ số thường từ 1,0 đến 3,0). Một người thuộc nhiều diện thường chỉ hưởng một mức cao nhất (theo quy định – đối chiếu SRS).

## Ràng buộc nhất quán khi sinh dữ liệu
- Tuổi tại ngày bắt đầu hưởng phải khớp loại đối tượng (trẻ em < 16; người cao tuổi đủ ngưỡng…).
- Người khuyết tật phải có giấy xác nhận khuyết tật, mức độ khớp hệ số.
- Ngày quyết định ≥ ngày nộp hồ sơ; ngày hiệu lực thường là tháng ký quyết định; có trường hợp **truy lĩnh** từ tháng nộp đủ hồ sơ.
- Tình trạng "thôi hưởng/đã chết" → có ngày thôi hưởng, không phát sinh chi trả sau ngày đó.
- Chuyển nơi cư trú → thôi hưởng nơi cũ, hưởng nơi mới từ tháng tiếp theo (không chi trùng kỳ).

## Văn bản / hồ sơ mẫu nên tạo (tao_van_ban.py)
- Tờ khai đề nghị trợ giúp xã hội (theo loại đối tượng: trẻ em, người cao tuổi, người khuyết tật…).
- Giấy xác nhận khuyết tật (dạng tật, mức độ, ngày cấp).
- Quyết định hưởng / điều chỉnh / thôi hưởng trợ cấp xã hội hàng tháng (số, ngày, người ký giả lập, danh sách đối tượng).
- Danh sách chi trả theo kỳ (bảng: STT, họ tên, mã đối tượng, mức hưởng, truy lĩnh, ký nhận).
- Biên bản họp xét duyệt (Hội đồng xét duyệt cấp xã) – khi SRS có quy trình xét duyệt.

## Tình huống kiểm thử nên có dữ liệu
Hưởng mới đủ điều kiện; thiếu giấy tờ bắt buộc; sai độ tuổi so với loại đối tượng; thuộc nhiều diện (chọn mức cao nhất); điều chỉnh hệ số; thôi hưởng giữa kỳ; chuyển nơi cư trú; truy lĩnh; trùng mã định danh (một người hai hồ sơ); chi trả qua tài khoản sai số tài khoản; danh sách lớn để test phân trang/xuất Excel.
