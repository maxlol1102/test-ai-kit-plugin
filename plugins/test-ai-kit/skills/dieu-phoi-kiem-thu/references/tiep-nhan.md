# Tiếp nhận yêu cầu kiểm thử (đầu mỗi quy trình)

Tester thường gửi **một lần** tất cả những thứ này, theo bất kỳ thứ tự nào, trong tin nhắn (có thể kèm lệnh `/test-ai-kit:kiem-thu`):
- **Yêu cầu**: chữ tự do – hệ thống gì, phân hệ/chức năng cần test, vai trò, hạn, lưu ý của trưởng nhóm/BA.
- **Tài liệu và dữ liệu**: file kéo thả vào ô chat, đường dẫn file, hoặc đường dẫn cả thư mục (SRS, thiết kế CSDL, dữ liệu mẫu/danh mục Excel, checklist thiết lập của dev, ảnh màn hình).
- **Link Figma** (`figma.com/design/…`, `/file/…`, `/proto/…`, `/make/…`).
- **Link website** hệ thống cần kiểm thử (môi trường test).

Không hỏi lần lượt từng thứ. Nhận hết, tự phân loại, chỉ hỏi **một lần** những gì còn thiếu.

## Các bước

1. **Tách tin nhắn**:
   - URL chứa `figma.com` → Figma (có thể nhiều link). URL khác → website (nhiều link → hỏi cái nào là hệ thống cần test, cái nào là tài liệu tham khảo).
   - Đường dẫn file/thư mục (kể cả file kéo thả hiện dưới dạng đường dẫn) → tài liệu.
   - Phần chữ còn lại → yêu cầu: rút ra tên hệ thống, phạm vi, vai trò, hạn, lưu ý.
   - Tester dán mật khẩu/tài khoản vào tin nhắn → **không ghi vào đâu cả**, nhắc tester: không cần gửi mật khẩu, anh/chị sẽ tự đăng nhập trên trình duyệt; nên đổi mật khẩu đó sau buổi test.
2. **Mã dự án**: tester chưa nêu → tự đề xuất từ tên hệ thống (chữ không dấu viết hoa, gạch nối, ≤ 12 ký tự, vd "Bảo trợ xã hội" → `BTXH`); trùng thư mục đã có → hỏi làm tiếp dự án cũ hay tạo mã mới.
3. **Tạo thư mục dự án** (theo `cau-truc-du-an.md`) rồi chạy:
   ```
   <python .venv> <skill doc-tai-lieu>/scripts/tiep_nhan.py <thư mục dự án> "<đường dẫn 1>" "<đường dẫn 2>" ...
   ```
   Script chép vào `dau-vao/`, phân loại (SRS | CSDL | Yêu cầu kiểm thử | Dữ liệu mẫu | Checklist thiết lập | Ảnh giao diện | Khác), ghi `dau-vao/danh-muc.json`, cảnh báo file có vẻ chứa CCCD/SĐT thật.
4. **Ghi lại**:
   - `dau-vao/yeu-cau.md` – nguyên văn phần yêu cầu tester gửi + các ý đã rút ra.
   - `he-thong.md` – tên, URL, vai trò, link Figma, chuyên đề (đoán từ tên/tài liệu, ghi "dự đoán"), phạm vi, hạn.
   - `trang-thai.json` – thêm khối `dau_vao`:
     `{"website": "...", "figma": ["..."], "tai_lieu": [{"file": "...", "loai": "..."}], "yeu_cau": "<1–2 câu>", "tiep_nhan_luc": "..."}`
5. **Phiếu tiếp nhận** – trình tester một bảng ngắn:

   | Đầu vào | Đã nhận | Ghi chú |
   |---|---|---|
   | Yêu cầu / phạm vi | … | |
   | Tài liệu đặc tả (SRS) | tên file | |
   | Thiết kế CSDL | … | thiếu → dữ liệu theo SRS/giao diện, ràng buộc là giả định |
   | Dữ liệu mẫu / danh mục | … | cảnh báo dữ liệu thật nếu có |
   | Checklist thiết lập (dev) | … | |
   | Figma | link | |
   | Website + vai trò test | URL – vai trò | |

   Kèm **một câu hỏi gộp** cho những mục bắt buộc còn thiếu: vai trò test (nếu có website), xác nhận đây là môi trường test được phép thao tác, file loại "Khác" là gì. Thiếu cả SRS lẫn website → không làm được, hỏi tester bổ sung.
   Mục không bắt buộc thiếu (CSDL, checklist, Figma) → chỉ ghi chú, **không chặn**.
6. **Tester xác nhận** (hoặc trả lời câu hỏi) → đăng trang kết quả (skill `trang-ket-qua`) rồi **tự chạy liền mạch** đến cổng đầu tiên:
   - Giao `doc-hieu-he-thong` (đưa `dau-vao/danh-muc.json` để agent biết file nào là SRS/CSDL/ảnh; có link Figma thì agent đọc qua kết nối Figma theo skill `doc-giao-dien`).
   - Song song, nếu có website: mở trình duyệt cho tester đăng nhập (skill `dang-nhap-an-toan`) – tester đăng nhập trong lúc agent đọc tài liệu – rồi giao `kham-pha-giao-dien`.
   - Dừng ở cổng **xác nhận bản đọc hiểu + chọn phạm vi kịch bản**.

## Figma

- Plugin kèm sẵn máy chủ Figma; tester chỉ cần đăng nhập một lần (lệnh cài đặt đã dẫn). Thử gọi `whoami` của kết nối Figma (claude.ai hoặc `plugin:test-ai-kit:figma`); chưa đăng nhập → ghi chú trong phiếu tiếp nhận "Chưa đăng nhập Figma – gõ /mcp → plugin:test-ai-kit:figma → Authenticate", vẫn chạy tiếp bằng ảnh/SRS/quy ước UI, khi tester bật xong thì giao `doc-hieu-he-thong` cập nhật riêng phần `ui.md`.
- Link cả file (không có `node-id`) → agent liệt kê trang/frame bằng `get_metadata` rồi ánh xạ frame ↔ chức năng; link tới một frame → chỉ frame đó và các frame con.
- Link Figma riêng tư mà tài khoản Figma của tester không có quyền → báo cần xin quyền xem từ người sở hữu file.

## Tester gửi bổ sung sau

Tài liệu/link mới giữa chừng → chạy lại `tiep_nhan.py` với đường dẫn mới, cập nhật `dau_vao`, báo các bước đã làm có thể cần làm lại (vd SRS mới → hồ sơ, kịch bản; Figma mới → `ui.md`, TC nhóm UI/UX) và hỏi có làm lại không.
