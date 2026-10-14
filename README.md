# Test AI Kit – plugin Claude Code (Trí Nam)

Bộ công cụ AI kiểm thử phần mềm của Trí Nam, đóng gói thành **plugin Claude Code** để tester cài một lần vào **gói Claude Max của chính mình** – không dùng Claude API.

- Tester cài đặt: xem [HUONG-DAN-CAI.md](HUONG-DAN-CAI.md).
- Repo phát triển cũ (website dùng API, đã dừng phát triển): `maxlol1102/AI_Tri_Nam`.

## Nguyên tắc của repo này

- **Không chứa bí mật**: không API key, không App Secret Lark (kết nối Lark dùng bộ cài TRINAM-Claude-Lark của công ty).
- **Không chứa tài liệu thật của khách hàng.** Tài liệu dự án nằm trong thư mục làm việc của tester (`test-ai-kit/du-an/`), không đưa vào repo.
- Repo để **private**; người dùng cần quyền đọc.

## Cấu trúc

```
.claude-plugin/marketplace.json     marketplace "trinam"
plugins/test-ai-kit/
├── .claude-plugin/plugin.json
├── .mcp.json                       Playwright MCP (--isolated, Edge) – không lưu phiên đăng nhập
├── hooks/                          chặn AI gõ vào ô mật khẩu / OTP
├── commands/                       /test-ai-kit:cai-dat, /test-ai-kit:mo-he-thong
├── skills/                         dang-nhap-an-toan, cai-dat-lark-base
└── agents/                         (GĐ2) Agent tổng + 8 agent con
```

## Lộ trình

| Giai đoạn | Nội dung | Trạng thái |
|---|---|---|
| GĐ1 | Khung cài đặt: marketplace, lệnh cài đặt, Lark Base, đăng nhập an toàn, hướng dẫn cài | Đang làm |
| GĐ2 | Agent tổng + 8 agent: đọc hiểu hệ thống, khám phá giao diện, thiết kế kịch bản, sinh dữ liệu theo chuyên đề, kiểm tra thiết lập, kiểm tra điều kiện, thực thi, báo lỗi + báo cáo | Chưa |
| GĐ3 | Chạy thật trên BTXH bằng Claude Max, đo thời gian so với baseline | Chưa |

## Thử plugin trên máy phát triển

```
claude --plugin-dir ./plugins/test-ai-kit
```
