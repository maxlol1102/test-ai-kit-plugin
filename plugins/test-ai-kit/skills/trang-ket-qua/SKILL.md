---
name: trang-ket-qua
description: Tạo và đăng TRANG KẾT QUẢ KIỂM THỬ của một dự án thành Artifact trong Claude (trang web riêng tư trên claude.ai) – tiến độ 9 bước, việc tester cần làm, số liệu test case, lỗi, nhật ký, file kết quả – và cập nhật cùng một đường link sau mỗi bước. Dùng sau mỗi bước Agent tổng làm xong, khi tester hỏi "xem kết quả", "trang kết quả", "dashboard", "link báo cáo", "gửi kết quả cho trưởng nhóm".
---

# Trang kết quả kiểm thử (Artifact)

Mỗi dự án có **một** trang kết quả, luôn cùng một đường link, cập nhật sau mỗi bước. Tester mở trên claude.ai (máy tính hoặc điện thoại), và tự quyết định chia sẻ cho trưởng nhóm.

## 1. Tạo file trang

```
<python của test-ai-kit/.venv> <thư mục skill này>/scripts/tao_trang_ket_qua.py <thư mục dự án>
```
→ ghi `<dự án>/bao-cao/trang-ket-qua.html`, in JSON có `tieu_de` và `can_tester`. Script chỉ đọc file trong thư mục dự án (số liệu cùng nguồn với Biểu mẫu Excel) – **không sửa tay file HTML**, muốn đổi nội dung thì sửa dữ liệu dự án rồi chạy lại.

## 2. Đăng / cập nhật Artifact

Có công cụ **Artifact** trong phiên:
- `trang-thai.json` **chưa có** `trang_ket_qua.url` → đăng mới: `file_path` = file vừa tạo, `icon: "chart"`, `description: "Tiến độ và kết quả kiểm thử dự án <mã> – Test AI Kit"`. Ghi link trả về vào `trang-thai.json`:
  `"trang_ket_qua": {"url": "<link>", "cap_nhat": "<dd/mm/yyyy HH:MM>"}`.
- **Đã có** `url`:
  - Cùng phiên đã đăng file này → đăng lại cùng `file_path` (giữ link).
  - Phiên mới → gọi Artifact `action: "read"` với `url` đó trước, rồi đăng với `url` + `file_path` (không truyền `icon`). Không bao giờ đăng không kèm `url` khi đã có link – sẽ sinh trang mới, mất link cũ.
- Cập nhật `trang_ket_qua.cap_nhat`.

Không có công cụ Artifact (bản Claude chưa bật) → mở file trên máy: Windows `start "" "<file>"`, macOS `open "<file>"`. Báo tester đường dẫn file.

## 3. Báo tester

Một dòng kèm link, ví dụ: *"Trang kết quả đã cập nhật: <link> – còn 3 việc cần anh/chị làm (xem ô đầu trang)."* Lần đầu thêm: trang là riêng tư; muốn trưởng nhóm xem thì anh/chị tự bấm Chia sẻ trên trang.

## Khi nào cập nhật

Agent tổng chạy bước 1–2 sau khi **mỗi bước quy trình xong** (hoặc lỗi/bị chặn), sau khi tester duyệt kịch bản / xác nhận kết quả / xác nhận lỗi, và khi tester hỏi xem kết quả. Không cập nhật giữa chừng một lô đang chạy.

## Không được

- Đưa vào trang: mật khẩu, cookie, token, dữ liệu cá nhân thật (trang chỉ có mã/tiêu đề TC, lỗi và số liệu – script đã lọc sẵn).
- Tự chia sẻ trang, đổi quyền xem, hay xoá Artifact – chỉ tester làm.
