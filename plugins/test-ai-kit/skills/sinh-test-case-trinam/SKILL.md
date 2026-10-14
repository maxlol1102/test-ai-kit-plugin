---
name: sinh-test-case-trinam
description: Đọc đặc tả chức năng (file chức năng tách từ SRS, URD, use case), rà điểm mơ hồ/thiếu/mâu thuẫn, rồi sinh bộ test case theo 4 nhóm Happy case / Chức năng / UI-UX / Hiệu năng theo mẫu chuẩn Trí Nam kèm ma trận truy vết, xuất Excel có tự kiểm tra. Dùng khi sinh/viết test case, rà SRS, lập ma trận truy vết; hoặc khi BA đã trả lời điểm cần xác nhận và cần cập nhật test case; hoặc cần bộ gọn để test nhanh.
---

# Sinh test case – Trí Nam (v1.0)

Đầu ra: `kich-ban/test-case.json` + Excel 4 sheet **Thông tin**, **Điểm cần xác nhận**, **Test case**, **Ma trận truy vết**.
Quy tắc chung (dữ liệu giả lập, mã, giá trị hợp lệ): skill `quy-chuan-trinam`.

| Việc | Làm theo |
|---|---|
| Sinh mới cho các chức năng | Bước 1–6 dưới đây |
| BA đã trả lời DX / tester đưa Excel đã điền cột trả lời | [references/cap-nhat-theo-tra-loi.md](references/cap-nhat-theo-tra-loi.md) (đọc trả lời từ Excel: `scripts/doc_tra_loi.py`) |

## Chế độ
| Chế độ | Khác biệt |
|---|---|
| **Đầy đủ** | Mọi TC theo quy tắc bao phủ |
| **Gọn** | Chỉ ưu tiên Cao/Trung bình, gộp TC cùng kiểu (xem Bước 3), khoảng 1/3 số TC của bộ Đầy đủ |

Ghi chế độ vào `thong_tin.che_do`.

## Bước 1 – Đọc đặc tả của chức năng
Nguồn chính là `ho-so/srs/chuc-nang/<mã>.md` (luồng chính/thay thế/ngoại lệ, quy tắc BR, màn hình và trường nhập có cột Bắt buộc, ảnh giao diện, mục "Tài liệu còn thiếu"). Bổ sung: ảnh `ho-so/srs/anh/`, `ho-so/csdl.md` (độ dài/kiểu trường), `ho-so/ui.md`, `giao-dien/ban-do-giao-dien.md` (giao diện thực tế).
Yêu cầu: mã chính `<mã CN>` (vd `IV.1-CN19`); quy tắc `<mã CN>-BR1`…; màn hình con `<mã CN>-MH1`… ; NFR đo được `<mã CN>-NFR1`.

## Bước 2 – Rà điểm cần xác nhận (DX)
Theo [references/checklist-ra-soat.md](references/checklist-ra-soat.md), thêm các điểm đặc thù SRS mẫu Trí Nam: BR để trống, luồng ngoại lệ trống, bảng GUI trống/thiếu cột Bắt buộc, ảnh giao diện lệch bảng GUI, đặc tả ↔ CSDL lệch độ dài/kiểu, giao diện thực tế khác tài liệu, vai trò trong tài liệu không có tài khoản test.
Mỗi DX: mã `DX-<mã CN>-NN`, vị trí, loại, nội dung, ảnh hưởng tới test, câu hỏi gửi BA, mức ảnh hưởng. Mâu thuẫn → tự đếm/tính lại trước khi kết luận.

## Bước 3 – Thiết kế test case theo 4 nhóm
Kỹ thuật + quy tắc bao phủ: [references/ky-thuat-thiet-ke.md](references/ky-thuat-thiet-ke.md).

| Nhóm | Tối thiểu |
|---|---|
| `Happy case` | Mỗi luồng chính thành công ≥ 1 TC, ưu tiên Cao |
| `Chức năng` | Mỗi luồng thay thế/ngoại lệ ≥ 1; mỗi trường bắt buộc có TC bỏ trống; trường có giới hạn → biên min/max/max+1; định dạng → hợp lệ + sai; mỗi BR ≥ 1 dương + 1 âm; chuyển trạng thái hợp lệ và không hợp lệ; mỗi quy tắc phân quyền ≥ 1 TC âm |
| `UI/UX` | So với `ui.md`/ảnh/quy ước UI: nhãn, dấu `*` bắt buộc, thông báo lỗi, trạng thái nút, phân trang, chính tả |
| `Hiệu năng` | Chỉ khi có NFR đo được; không có → DX "Không kiểm chứng được" |

**Chế độ Gọn – gộp bắt buộc:** bỏ trống bắt buộc 1 TC/form; biên 1 TC/trường; sai định dạng 1 TC/trường; chuyển trạng thái không hợp lệ 1 TC; phân quyền âm 1 TC/quy tắc; bỏ TC ưu tiên Thấp; vẫn giữ mọi luồng và mọi yêu cầu đo được.

Kết quả mong đợi dựa trên giả định → ghi `[CẦN XÁC NHẬN DX-…]` và `ma_dx`. Dữ liệu test giả lập.

## Bước 4 – Ghi JSON
Theo [references/schema-json.md](references/schema-json.md) – mã TC `TC-<mã CN>-NNN`, có trường `nhom`. Khi file đã có chức năng khác: chỉ thay phần của các chức năng đang làm, giữ kết quả chạy của TC còn giữ mã.

## Bước 5 – Xuất Excel và tự kiểm tra
```
<python của test-ai-kit/.venv> scripts/xuat_excel.py <dự án>/kich-ban/test-case.json <dự án>/kich-ban/kich-ban-kiem-thu.xlsx
```
Script kiểm tra trùng mã, mã yêu cầu/DX không tồn tại, trường trống, giá trị không hợp lệ (loại, kỹ thuật, ưu tiên, **nhóm**), `[CẦN XÁC NHẬN` khớp `ma_dx`, chế độ Gọn không có TC Thấp; in yêu cầu chưa có TC. Còn lỗi → sửa JSON, chạy lại.

## Bước 6 – Báo cáo
Mỗi chức năng: số TC theo 4 nhóm, số DX theo mức; yêu cầu chưa có TC và lý do; TC dựa trên giả định cần tester xem lại. Nhắc: **kịch bản cần tester duyệt** trước khi thực thi.
