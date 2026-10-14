# Cài Test AI Kit vào Claude (gói Claude Max)

Làm **một lần** trên mỗi máy, khoảng 10 phút. Test AI Kit chạy bằng gói Claude Max của chính bạn – **không cần API key, không tốn thêm tiền**.

## Cần có

- Máy Windows (hoặc macOS), **không dùng WSL**.
- Ứng dụng **Claude Desktop**, đăng nhập tài khoản **Claude Max**.
- Trình duyệt **Microsoft Edge** (Windows có sẵn).
- Được nhóm B05 cấp quyền xem repo GitHub `maxlol1102/test-ai-kit-plugin` (repo riêng tư).

## Bước 1 – Kết nối Lark (bỏ qua nếu máy đã cài)

Cài **bộ cài TRINAM-Claude-Lark** của công ty: giải nén → bấm đúp `CAI-DAT.cmd` → đăng nhập Lark → **Authorize** → thấy "XONG!" thì thoát hẳn Claude (chuột phải biểu tượng Claude ở taskbar → Quit) rồi mở lại.
Bộ cài này cũng tự cài **Node.js** – Test AI Kit cần Node.js để mở trình duyệt kiểm thử.

## Bước 2 – Cho máy đọc được repo riêng tư trên GitHub

Mở **PowerShell** và chạy lần lượt:
```
winget install --id GitHub.cli -e
gh auth login          # chọn GitHub.com → HTTPS → Login with a web browser
gh auth setup-git
```

## Bước 3 – Cài plugin trong Claude Code

1. Mở Claude Desktop → tab **Code** → chọn một thư mục làm việc, ví dụ `Documents\KiemThu`.
2. Gõ lần lượt vào ô chat:
   ```
   /plugin marketplace add maxlol1102/test-ai-kit-plugin
   /plugin install test-ai-kit@trinam
   ```
   (Hoặc bấm **+ → Plugins**, thêm marketplace `maxlol1102/test-ai-kit-plugin`, cài `test-ai-kit`.)
3. Khởi động lại phiên Claude Code khi được nhắc.

## Bước 4 – Cài đặt và kiểm tra

Gõ:
```
/test-ai-kit:cai-dat
```
Claude kiểm tra Node.js, cài Python và thư viện (hỏi trước khi cài), kiểm tra trình duyệt, kết nối Lark, **kết nối Figma** (đã kèm sẵn trong plugin – bạn chỉ đăng nhập Figma một lần: gõ `/mcp` → `plugin:test-ai-kit:figma` → Authenticate → Allow), tạo thư mục làm việc và **Lark Base "Quản lý kiểm thử"** (hỏi bạn đồng ý trước khi tạo). Làm theo các mục báo ⚠️/❌ nếu có.

Không nhớ lệnh cũng được: mở phiên mới trong thư mục làm việc và gõ "chào" – Claude tự nhận biết đã cài đặt chưa, có dự án nào đang dở, và gợi ý bước tiếp.

## Dùng thử

1. **Chạy thử ngay** trên hệ thống DEMO giả lập đi kèm (có 4 lỗi cài sẵn, không cần tài liệu hay hệ thống thật):
   ```
   /test-ai-kit:thu-demo
   ```
   Claude tự bật DEMO, tạo dự án mẫu và dẫn bạn đi hết quy trình. Tài khoản thử hiện ngay trên trang đăng nhập DEMO.
2. **Hệ thống thật** được giao – gõ `/test-ai-kit:kiem-thu` rồi gửi **một tin** gồm tất cả những gì bạn có, ví dụ:
   ```
   /test-ai-kit:kiem-thu Kiểm thử phân hệ Tiếp nhận hồ sơ, vai trò cán bộ xã, hạn 25/10.
   Website: https://test.hethong.vn
   Figma: https://www.figma.com/design/...
   Tài liệu: D:\DuAn\BTXH   (hoặc kéo thả file SRS, CSDL, dữ liệu mẫu, checklist của dev vào ô chat)
   ```
   Claude tự phân loại tài liệu, trình **phiếu tiếp nhận**, chỉ hỏi một lần phần còn thiếu, rồi tự chạy. Không cần gửi mật khẩu – bạn tự đăng nhập trên trình duyệt.
   **Agent tổng** dẫn từng bước: đọc hiểu tài liệu → kịch bản (bạn duyệt) → dữ liệu → kiểm tra thiết lập → kiểm tra điều kiện → chạy test trên trình duyệt (bạn xác nhận kết quả) → báo cáo → Lark.
3. Khi cửa sổ Edge mở trang đăng nhập – **bạn tự đăng nhập**, xong nhắn "xong". Claude không bao giờ nhập hay nhìn thấy mật khẩu; phiên đăng nhập mất khi đóng trình duyệt.
4. Hỏi tiến độ bất cứ lúc nào: `/test-ai-kit:kiem-thu tiến độ`.

**Trang kết quả:** mỗi dự án có một trang web riêng tư trên claude.ai (Artifact) – tiến độ, việc bạn cần làm, test case, lỗi – Claude gửi link và cập nhật sau mỗi bước, mở được cả trên điện thoại. Muốn trưởng nhóm xem thì bấm **Chia sẻ** trên trang.

File gốc nằm trong `test-ai-kit/du-an/<mã>/` của thư mục làm việc (Excel kịch bản, dữ liệu, biểu mẫu kết quả, ảnh bằng chứng).

## Cập nhật bản mới

```
/plugin marketplace update trinam
```

## Gặp lỗi

| Hiện tượng | Cách xử lý |
|---|---|
| Không thêm được marketplace / báo không có quyền | Chưa được cấp quyền repo, hoặc chưa làm Bước 2 |
| Không thấy lệnh `/test-ai-kit:...` | Khởi động lại phiên Claude Code; kiểm tra `/plugin` đã bật `test-ai-kit` |
| Lark báo lỗi đăng nhập / hết phiên | Bấm đúp `DANG-NHAP-LAI.cmd` trong thư mục bộ cài TRINAM-Claude-Lark |
| Không mở được trình duyệt | Cần Node.js (Bước 1) và Microsoft Edge |
