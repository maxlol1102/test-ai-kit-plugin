# Test AI Kit – plugin Claude Code (Trí Nam)

Bộ công cụ AI kiểm thử phần mềm của Trí Nam, đóng gói thành **plugin Claude Code** để tester cài một lần vào **gói Claude Max của chính mình** – không dùng Claude API.

- Tester cài đặt: xem [HUONG-DAN-CAI.md](HUONG-DAN-CAI.md).
- Repo phát triển cũ (website dùng API, đã dừng phát triển): `maxlol1102/AI_Tri_Nam`.

## Nguyên tắc của repo này

- **Không chứa bí mật**: không API key, không App Secret Lark (kết nối Lark dùng bộ cài TRINAM-Claude-Lark của công ty).
- **Không chứa tài liệu thật của khách hàng.** Tài liệu dự án nằm trong thư mục làm việc của tester (`test-ai-kit/du-an/`), không đưa vào repo.
- Repo để **private**; người dùng cần quyền đọc.

## Cách hoạt động

```
Tester ──/test-ai-kit:kiem-thu──▶ AGENT TỔNG (phiên chính: điều phối, hỏi tester, mở trình duyệt cho tester đăng nhập)
                                   │ giao việc theo thứ tự, dừng ở cổng tester quyết định
   ┌───────────────┬───────────────┼────────────────┬─────────────────┐
 1 Đọc hiểu       2 Khám phá      3 Thiết kế        4 Sinh dữ liệu    5 Kiểm tra thiết lập
   hệ thống         giao diện       kịch bản          theo chuyên đề    (validate phần dev làm)
   └───────────────┴───────────────┴────────────────┴─────────────────┘
                 6 Kiểm tra điều kiện (cổng) ─▶ 7 Thực thi (Playwright) ─▶ 8 Báo lỗi + báo cáo + Lark
```
Kết quả mỗi bước là file trong thư mục làm việc của tester: `test-ai-kit/du-an/<MÃ>/` (cấu trúc: skill `dieu-phoi-kiem-thu/references/cau-truc-du-an.md`), và được tổng hợp thành **trang kết quả dạng Artifact** trên claude.ai (một link mỗi dự án, cập nhật sau mỗi bước; tester tự quyết định chia sẻ).

## Cấu trúc repo

```
.claude-plugin/marketplace.json       marketplace "trinam"
plugins/test-ai-kit/
├── .mcp.json                         Playwright MCP (--isolated, Edge – không lưu phiên) + Figma MCP chính thức (mỗi tester đăng nhập 1 lần)
├── hooks/                            khởi động phiên (dẫn tester: cài đặt / chạy thử / làm tiếp) · chặn AI gõ vào ô mật khẩu / OTP
├── commands/                         /test-ai-kit:cai-dat · /test-ai-kit:thu-demo · /test-ai-kit:kiem-thu (Agent tổng) · /test-ai-kit:mo-he-thong
├── agents/                           8 agent con: doc-hieu-he-thong, kham-pha-giao-dien, thiet-ke-kich-ban, sinh-du-lieu,
│                                     kiem-tra-thiet-lap, kiem-tra-dieu-kien, thuc-thi, bao-loi-bao-cao
└── skills/
    ├── dieu-phoi-kiem-thu/           vai trò Agent tổng, cấu trúc dự án, trang-thai.json
    ├── quy-chuan-trinam/             quy chuẩn chung + mẫu biểu
    ├── dang-nhap-an-toan/            tester tự đăng nhập, không lưu phiên
    ├── doc-tai-lieu/                 scripts/tach_srs.py – tách SRS mẫu Trí Nam (đã thử: BTXH 233 chức năng)
    ├── doc-giao-dien/                Figma hoặc quy ước UI mặc định
    ├── sinh-test-case-trinam/        4 nhóm kịch bản, DX, xuất Excel có tự kiểm tra
    ├── sinh-du-lieu-chuyen-de/       gói chuyên đề (chung, Bảo trợ xã hội, Thủ tục hành chính), xuất Excel, tạo văn bản .docx
    ├── xuat-bao-cao/                 thống kê bằng code + Biểu mẫu kết quả (Mẫu 3)
    ├── trang-ket-qua/                trang kết quả mỗi dự án → Artifact trên claude.ai, cập nhật cùng link sau mỗi bước
    ├── day-len-lark/                 đồng bộ 4 bảng, không xoá, ≤ 500 bản ghi/lần
    ├── cai-dat-lark-base/            tạo/nối Lark Base "Quản lý kiểm thử"
    └── thu-demo/                     SRS giả lập + hệ thống DEMO có 4 lỗi cài sẵn – chạy thử ngay sau khi cài
```

Script Python chạy bằng `test-ai-kit/.venv` của tester (lệnh cài đặt tự tạo).

## Lộ trình

| Giai đoạn | Nội dung | Trạng thái |
|---|---|---|
| GĐ1 | Khung cài đặt: marketplace, lệnh cài đặt, Lark Base, đăng nhập an toàn, hướng dẫn cài | Xong (chưa thử cài thật) |
| GĐ2 | Agent tổng + 8 agent con, skill và script | Xong (chưa chạy thử trong Claude Code) |
| GĐ2.5 | Trang kết quả dạng Artifact, chạy thử DEMO ngay sau cài, hook khởi động phiên | Xong (chưa chạy thử trong Claude Code) |
| GĐ2.7 | Kèm sẵn kết nối Figma; lệnh cài đặt kiểm tra và dẫn đăng nhập Lark/Figma | Xong (chưa thử đăng nhập Figma trong Claude Code) |
| GĐ2.6 | Tiếp nhận một lần: yêu cầu + tài liệu + dữ liệu + Figma + website → tự phân loại (`tiep_nhan.py`), phiếu tiếp nhận, tự chạy đến cổng đầu | Xong (đã thử phân loại trên SRS/CSDL BTXH thật) |
| GĐ3 | Cài thử trên máy tester, chạy DEMO rồi BTXH bằng Claude Max, đo thời gian so với baseline | Tiếp theo |

## Thử plugin trên máy phát triển

```
claude --plugin-dir ./plugins/test-ai-kit
```
