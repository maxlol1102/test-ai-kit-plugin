---
name: doc-giao-dien
description: Lấy chuẩn giao diện (UI/UX) để thiết kế và chấm test case nhóm UI/UX – đọc thiết kế từ Figma qua kết nối Figma, hoặc dùng ảnh thiết kế / ảnh trong SRS / quy ước UI chung của Trí Nam khi không có Figma. Dùng khi đọc hiểu hệ thống, khi tester đưa link Figma, hoặc khi cần đối chiếu màn hình thực tế với thiết kế.
---

# Đọc chuẩn giao diện

Kết quả ghi vào `<dự án>/ho-so/ui.md`, theo thứ tự ưu tiên nguồn:

## 1. Có link Figma (trong `he-thong.md` hoặc tester đưa)
- Dùng kết nối **Figma** của Claude (công cụ `get_metadata`, `get_screenshot`, `get_design_context`… của Figma MCP). Chưa có kết nối → báo tester: vào claude.ai → Settings → Connectors → bật Figma và đăng nhập, rồi chạy lại; trong lúc chờ dùng nguồn 2–3.
- Với mỗi frame tương ứng chức năng trong phạm vi: tên màn, bố cục (vùng tiêu đề, bộ lọc, lưới, form, nút), danh sách trường (nhãn, loại, bắt buộc, placeholder), nút và trạng thái (mờ/ẩn), thông báo, màu/kiểu chữ nếu có token thiết kế. Lưu ảnh chụp frame vào `<dự án>/ho-so/ui-anh/`.
- Ghi bảng ánh xạ **frame Figma ↔ mã chức năng**.

## 2. Có ảnh thiết kế / prototype trong `dau-vao/` hoặc ảnh tách từ SRS (`ho-so/srs/anh/`)
Mô tả tương tự từ ảnh; ghi rõ nguồn từng màn.

## 3. Không có thiết kế
Dùng [references/quy-uoc-ui-mac-dinh.md](references/quy-uoc-ui-mac-dinh.md) làm chuẩn tối thiểu cho nhóm UI/UX, và ghi điểm cần xác nhận "Thiếu thiết kế giao diện cho …".

## Cấu trúc `ui.md`
`# Chuẩn giao diện` → Nguồn (Figma link / ảnh / quy ước) → Quy ước chung áp dụng → Mỗi màn hình: mã chức năng, nguồn, bố cục, trường, nút, thông báo, khác biệt với SRS (nếu có).
