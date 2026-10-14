---
name: doc-tai-lieu
description: Tách tài liệu đầu vào (SRS theo mẫu Trí Nam, thiết kế CSDL, PDF/DOCX bất kỳ) thành các file gọn cho agent đọc – mục lục, mỗi chức năng một file (luồng, quy tắc, màn hình, trường nhập, ảnh giao diện, chỗ thiếu), CSDL dạng Markdown. Dùng khi đọc hiểu hệ thống, khi tester đưa SRS/CSDL mới, hoặc khi cần nội dung của một chức năng cụ thể.
---

# Đọc và tách tài liệu

Script: `scripts/tach_srs.py` (cùng thư mục với file này). Chạy bằng Python của thư mục làm việc:
- Windows: `test-ai-kit\.venv\Scripts\python.exe`
- macOS/Linux: `test-ai-kit/.venv/bin/python`

Chưa có `.venv` → chạy `/test-ai-kit:cai-dat` (cài Python và thư viện: python-docx, openpyxl, pillow, pypdf – xem `scripts/requirements.txt`).

## Lệnh

| Việc | Lệnh | Kết quả |
|---|---|---|
| SRS .docx theo mẫu Trí Nam (có mục "YÊU CẦU CHI TIẾT VỀ CHỨC NĂNG", phân hệ `IV.x`, mỗi chức năng có bảng "a. Thông tin chức năng") | `python tach_srs.py srs <SRS.docx> <thư mục ra>` | `muc-luc.md`, `chuc-nang/<mã>.md`, `anh/<mã>-<n>.png`, `chung.md`, `phi-chuc-nang.md`, `cau-truc-srs.json` |
| Thiết kế CSDL .docx | `python tach_srs.py csdl <CSDL.docx> <file.md>` | Markdown giữ thứ tự đoạn và bảng trường |
| Tài liệu khác (.docx/.pdf/.md/.txt) | `python tach_srs.py van-ban <file> <file.md>` | Chữ thuần |

Mỗi lệnh in **một dòng JSON** (số phân hệ/chức năng/ảnh hoặc `{"loi": ...}`).

## Định dạng `chuc-nang/<mã>.md`
Tiêu đề `# <mã> – <tên>`, phân hệ, mô tả, tác nhân, điều kiện trước/sau, bảng luồng chính (Bước | Hệ thống | Luồng thay thế), luồng ngoại lệ, quy tắc nghiệp vụ (BR trống ghi "(để trống)"), mỗi màn hình một bảng phần tử (Nhóm | Tên | Loại | Mặc định | Bắt buộc | Đầu vào | Mô tả), danh sách ảnh, **"Tài liệu còn thiếu"**, và nguyên văn trong SRS.
Mã chức năng: `<mã phân hệ>-CN<số 2 chữ số>` (vd `IV.1-CN19`).

Đã kiểm chứng trên SRS BTXH v0.4 (≈ 860 trang): 5 phân hệ, 233 chức năng, 221 ảnh, khoảng 20 giây.

## Lưu ý
- Ảnh EMF/WMF hoặc ảnh nhỏ (biểu tượng) bị bỏ qua; tối đa 4 ảnh/chức năng, ưu tiên ảnh ở mục Giao diện.
- SRS không theo mẫu → dùng `van-ban` rồi tự lập mục lục và file chức năng cùng định dạng (agent `doc-hieu-he-thong` làm).
