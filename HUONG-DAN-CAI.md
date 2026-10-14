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
Claude kiểm tra Node.js, trình duyệt, kết nối Lark, tạo thư mục làm việc và **Lark Base "Quản lý kiểm thử"** (hỏi bạn đồng ý trước khi tạo). Làm theo các mục báo ⚠️/❌ nếu có.

## Dùng thử

```
/test-ai-kit:mo-he-thong http://127.0.0.1:8766  Cán bộ tiếp nhận
```
Cửa sổ Edge mở ra – **bạn tự đăng nhập**, xong nhắn "xong". Claude không bao giờ nhập hay nhìn thấy mật khẩu, và phiên đăng nhập mất khi đóng trình duyệt.

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
