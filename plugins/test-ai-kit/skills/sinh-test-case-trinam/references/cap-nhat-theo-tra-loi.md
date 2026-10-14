# Cập nhật test case theo trả lời của BA/khách hàng

Dùng khi tester đã điền cột **"Trả lời của BA/KH"** trong sheet "Điểm cần xác nhận" của file Excel.

## Bước 1 – Gộp trả lời vào JSON
```
python scripts/doc_tra_loi.py <file.xlsx> <json_cu.json> <json_moi.json>
```
Script làm 3 việc:
- chép câu trả lời vào JSON;
- giữ lại kết quả chạy test mà tester đã điền;
- in danh sách DX có trả lời mới, kèm các TC đang gắn DX đó.

**Mọi bước sau làm trên `json_moi.json`.** Không làm trên JSON cũ, nếu không sẽ mất kết quả chạy của tester.

## Bước 2 – Xử lý từng DX có trả lời mới

Đọc câu trả lời rồi xếp vào **một** trong ba trường hợp:

| Trường hợp | Nhận biết | Việc làm |
|---|---|---|
| **A. Đã chốt** | Câu trả lời đưa ra quy tắc/giá trị cụ thể | Sửa TC (Bước 3). Đặt `trang_thai` của DX = `Đã cập nhật TC` |
| **B. Chưa chốt** | "Chờ khách hàng", "chưa rõ", "để sau", hoặc không trả lời đúng câu hỏi | Không sửa TC. Đặt lại `trang_thai` = `Chờ trả lời` và giữ nguyên `tra_loi` làm ghi chú |
| **C. Chốt một phần** | Trả lời được một số ý, còn ý khác chưa rõ | Sửa TC theo phần đã chốt. Tạo **DX mới** (mã tiếp theo) cho phần còn lại và chuyển các TC liên quan sang DX mới. Đặt DX cũ = `Đã cập nhật TC` |

## Bước 3 – Sửa test case (trường hợp A, C)

Với **mỗi TC đang gắn DX**:
1. Viết lại `ket_qua_mong_doi` theo câu trả lời. Bỏ đoạn `[CẦN XÁC NHẬN DX-xx]` và phần giả định đi kèm.
2. Sửa `du_lieu_test`, `buoc_thuc_hien`, `dieu_kien_truoc` nếu câu trả lời làm thay đổi chúng.
3. Bỏ mã DX khỏi `ma_dx`. Nếu TC còn gắn DX khác thì giữ `[CẦN XÁC NHẬN` cho các DX đó.
4. Ghi `cap_nhat`: `"<ngày> – Sửa theo <DX>: <tóm tắt 1 dòng>"`.
5. TC không còn ý nghĩa (vd kiểm tra một giả định đã bị bác bỏ) thì **không xoá**. Đổi `tieu_de` thành `[LOẠI BỎ] …` và ghi lý do vào `cap_nhat`. Tester sẽ quyết định xoá hay giữ.

**Rà thêm các TC KHÔNG gắn DX nhưng bị ảnh hưởng.** Ví dụ: trả lời "không phân biệt dấu" ảnh hưởng mọi TC tìm kiếm theo họ tên. Tìm theo mã yêu cầu tại vị trí của DX và theo từ khoá liên quan.

**Thêm TC mới** khi câu trả lời đưa ra quy tắc mới có thể test được. Ví dụ: "SĐT 10 chữ số, bắt đầu bằng 0" → thêm TC biên 9/10/11 chữ số và TC đầu số khác 0. Áp dụng quy tắc bao phủ trong `ky-thuat-thiet-ke.md`. Mã TC mới nối tiếp STT lớn nhất hiện có, **không dùng lại mã cũ**. Ghi `cap_nhat`: `"<ngày> – Thêm mới theo <DX>"`.

**Không động vào** các trường `ket_qua_thuc_te`, `trang_thai`, `ma_loi`, `nguoi_thuc_hien`. Nếu TC đã chạy rồi mà kết quả mong đợi thay đổi, ghi thêm vào `cap_nhat`: `"– CẦN CHẠY LẠI"`.

## Bước 4 – Gợi ý sửa tài liệu
Nếu câu trả lời cho thấy SRS cần sửa (vd mâu thuẫn được giải quyết theo một phía), ghi gợi ý vào báo cáo cuối: "Đề nghị BA sửa <vị trí>: <nội dung>".

## Bước 5 – Xuất lại và báo cáo
- Đặt `thong_tin.lan_cap_nhat` = `"<ngày> – theo trả lời BA (<n> DX)"`.
- Chạy `xuat_excel.py`. Script sẽ báo lỗi nếu còn TC gắn DX đã có trả lời, hoặc còn `[CẦN XÁC NHẬN` mà không có DX.
- Báo lại cho tester:
  - số DX theo từng trường hợp A/B/C;
  - số TC đã sửa, thêm mới, đánh dấu loại bỏ, cần chạy lại;
  - các gợi ý sửa SRS.
