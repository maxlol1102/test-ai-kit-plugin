---
name: sinh-du-lieu-chuyen-de
description: Sinh dữ liệu kiểm thử giả lập hiểu nghiệp vụ theo chuyên đề (Bảo trợ xã hội, Thủ tục hành chính, …) và bám khung cơ sở dữ liệu – bộ dữ liệu Hợp lệ/Biên/Sai/Lớn, văn bản/hồ sơ mẫu Word (tờ khai, giấy xác nhận, quyết định), bước nạp dữ liệu và yêu cầu kỹ thuật; xuất Excel có tự kiểm tra CCCD/SĐT giống thật. Dùng khi sinh dữ liệu test, tạo hồ sơ mẫu để đính kèm, hoặc tester hỏi dữ liệu cho một chức năng/chuyên đề.
---

# Sinh dữ liệu theo chuyên đề

Script (cùng thư mục file này, chạy bằng Python của `test-ai-kit/.venv`):
- `scripts/xuat_du_lieu.py <du-lieu.json> <file.xlsx>` – kiểm tra + xuất Excel (Tổng quan, mỗi bộ 1 sheet, Bước thực hiện, Yêu cầu kỹ thuật, Văn bản mẫu).
- `scripts/tao_van_ban.py <van-ban.json> <thư mục>` – tạo văn bản .docx giả lập (định dạng đầu vào ở đầu file script).

## Gói kiến thức chuyên đề
| Chuyên đề | File |
|---|---|
| Quy ước chung mọi hệ thống (địa giới, định danh, ngày, tiền…) | [references/chuyen-de/chung.md](references/chuyen-de/chung.md) – **luôn đọc** |
| Bảo trợ xã hội / trợ giúp xã hội | [references/chuyen-de/bao-tro-xa-hoi.md](references/chuyen-de/bao-tro-xa-hoi.md) |
| Thủ tục hành chính / một cửa / dịch vụ công | [references/chuyen-de/thu-tuc-hanh-chinh.md](references/chuyen-de/thu-tuc-hanh-chinh.md) |

Chuyên đề chưa có gói → dùng `chung.md` + kiến thức nghiệp vụ, ghi mọi quy tắc tự suy luận vào `can_xac_nhan`. Có thể bổ sung gói mới theo cùng cấu trúc (đối tượng, trường dữ liệu, ràng buộc, văn bản nghiệp vụ, tình huống test).

## Quy trình
1. **Hiểu chuyên đề**: đối tượng nghiệp vụ, vòng đời trạng thái, quy tắc nghiệp vụ, văn bản/hồ sơ đi kèm (đọc gói chuyên đề + hồ sơ hệ thống).
2. **Bám khung CSDL** (`ho-so/csdl.md`): dùng đúng tên bảng/cột; tôn trọng kiểu, độ dài, bắt buộc, khoá ngoại, giá trị danh mục. Không có CSDL → dùng trường trên giao diện (`chuc-nang/<mã>.md`), ghi `can_xac_nhan`.
3. **Sinh dữ liệu nhất quán**: khoá ngoại khớp; ngày tháng hợp lý (ngày sinh → tuổi → điều kiện hưởng; ngày tiếp nhận ≤ ngày hẹn trả); trạng thái theo đúng vòng đời; mỗi bản ghi Hợp lệ phải **thoả mọi quy tắc** của chuyên đề, mỗi bản ghi Sai/Biên **chỉ sai một điểm** để TC xác định được nguyên nhân.
4. **Văn bản mẫu**: tạo các giấy tờ mà TC cần đính kèm/đối chiếu (tối thiểu 1 văn bản mỗi loại hồ sơ trong phạm vi), dữ liệu trong văn bản **khớp** với bộ dữ liệu Hợp lệ.
5. **Bước thực hiện + yêu cầu kỹ thuật**: thứ tự nạp (danh mục → đối tượng → hồ sơ → giao dịch), cách nạp (giao diện / import / dev dựng sẵn), ràng buộc kỹ thuật (UTF-8, định dạng ngày, độ dài, định dạng/dung lượng file).
6. Xuất Excel, sửa đến khi script không còn lỗi.

## Định dạng `du-lieu.json`
```json
{
  "chuyen_de": "Bảo trợ xã hội",
  "quy_uoc": "Họ tên giả 'Nguyễn Văn Thử…'; CCCD 000…; SĐT 0900000xxx; địa giới giả lập 2 cấp",
  "bo_du_lieu": [
    {"ten": "Đối tượng hưởng trợ cấp hợp lệ", "loai": "Hợp lệ|Biên|Sai|Lớn", "bang_lien_quan": "BTXH_DoiTuong",
     "mo_ta": "…", "cot": ["MaDoiTuong", "HoTen", "NgaySinh"], "dong": [["DT0001", "Nguyễn Văn Thử", "01/01/1950"]],
     "so_dong_sinh_them": 0, "tc_lien_quan": ["TC-IV.2-CN05-001"]}
  ],
  "van_ban": [{"file": "to-khai-01.docx", "loai": "Tờ khai đề nghị trợ giúp xã hội", "dung_cho": "Đính kèm hồ sơ DT0001", "tc_lien_quan": ["…"]}],
  "buoc_thuc_hien": ["Bước 1: …"],
  "yeu_cau_ky_thuat": ["Ngày dạng dd/mm/yyyy", "…"],
  "can_xac_nhan": ["…"]
}
```
Bộ `Lớn`: ≤ 5 dòng mẫu + `so_dong_sinh_them` (vd 1000) – script tự nhân bản và đánh số cột đầu. Mỗi bộ khác ≤ 30 dòng.
