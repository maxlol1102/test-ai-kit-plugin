# Kỹ thuật thiết kế test case

| Kỹ thuật | Dùng khi | Cách làm |
|---|---|---|
| Phân vùng tương đương (PVTĐ) | Trường nhập có tập giá trị hợp lệ/không hợp lệ | Chia vùng, mỗi vùng chọn 1 giá trị đại diện |
| Giá trị biên (GTB) | Có độ dài, khoảng số, khoảng ngày | Test min−1, min, max, max+1 |
| Bảng quyết định (BQĐ) | Nhiều điều kiện kết hợp quyết định kết quả | Liệt kê tổ hợp điều kiện → kết quả, mỗi cột 1 TC |
| Chuyển trạng thái (CTT) | Đối tượng có vòng đời trạng thái | 1 TC cho mỗi chuyển hợp lệ; chọn các chuyển không hợp lệ có rủi ro cao |
| Phân quyền (PQ) | Có vai trò, phạm vi đơn vị | Ma trận vai trò × chức năng; TC âm cho ô "không được phép" |
| Luồng use case (LUC) | Có luồng chính/thay thế/ngoại lệ | 1 TC mỗi luồng |
| Đoán lỗi (ĐL) | Theo kinh nghiệm | Ký tự đặc biệt, tiếng Việt có dấu, khoảng trắng đầu/cuối, bấm lưu 2 lần, dán chuỗi dài, script `<script>` |

## Phân loại TC (cột "Loại")

Chỉ dùng: `Chức năng`, `Giao diện`, `Phân quyền`, `Biên`, `Ngoại lệ`, `API`, `Hiệu năng`, `ATTT`.

## Ưu tiên TC (cột "Ưu tiên")

- **Cao:** luồng chính, quy tắc nghiệp vụ cốt lõi, phân quyền, mất/sai dữ liệu. Đây là bộ hồi quy tối thiểu.
- **Trung bình:** luồng thay thế, ngoại lệ, biên.
- **Thấp:** giao diện, đoán lỗi phụ.

## Viết bước và kết quả

- Bước: đánh số, mỗi bước 1 hành động, dùng đúng tên nút/trường trong tài liệu.
- Kết quả mong đợi: cụ thể, kiểm chứng được. Dùng nguyên văn thông báo trong tài liệu nếu có. Nếu tài liệu không nêu nguyên văn thì ghi "hiển thị thông báo lỗi tại trường X, không lưu".
- Điều kiện trước: vai trò đăng nhập, dữ liệu cần có sẵn (vd "có hồ sơ ở trạng thái Chờ phân công thuộc đơn vị STP").
