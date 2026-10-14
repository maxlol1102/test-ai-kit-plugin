// SessionStart: cho Claude biết thư mục này đã cài Test AI Kit chưa và đang có dự án nào,
// để tester mở Claude là được dẫn ngay (cài đặt / chạy thử / làm tiếp) – không phải nhớ lệnh.
const fs = require("fs");
const path = require("path");

let vao = "";
process.stdin.on("data", (d) => (vao += d));
process.stdin.on("end", () => {
  let cwd = process.cwd();
  try { cwd = JSON.parse(vao).cwd || cwd; } catch {}
  const goc = path.join(cwd, "test-ai-kit");
  let ghiChu;
  if (!fs.existsSync(path.join(goc, "cau-hinh.json"))) {
    ghiChu = "Test AI Kit đã cài nhưng thư mục làm việc này chưa thiết lập. Khi tester bắt đầu nói chuyện (chào, hỏi dùng thế nào, muốn kiểm thử), " +
      "giới thiệu 1–2 câu và đề nghị chạy cài đặt (/test-ai-kit:cai-dat, khoảng 5 phút); tester đồng ý thì làm luôn theo lệnh đó.";
  } else {
    const duAn = [];
    try {
      for (const ma of fs.readdirSync(path.join(goc, "du-an"))) {
        try {
          const st = JSON.parse(fs.readFileSync(path.join(goc, "du-an", ma, "trang-thai.json"), "utf8"));
          const buoc = Object.entries(st.buoc || {});
          const xong = buoc.filter(([, b]) => b.trang_thai === "Xong").length;
          duAn.push(`${ma} (${xong}/${buoc.length} bước xong${st.trang_ket_qua?.url ? ", trang kết quả: " + st.trang_ket_qua.url : ""})`);
        } catch {}
      }
    } catch {}
    ghiChu = "Test AI Kit đã thiết lập ở thư mục này. " +
      (duAn.length ? `Dự án đang có: ${duAn.join("; ")}. Tester muốn làm tiếp, hoặc gửi yêu cầu kèm tài liệu / link Figma / link website → làm Agent tổng theo skill dieu-phoi-kiem-thu.`
        : "Chưa có dự án nào – gợi ý /test-ai-kit:thu-demo (chạy thử trên hệ thống DEMO) hoặc /test-ai-kit:kiem-thu (hệ thống thật).");
  }
  process.stdout.write(JSON.stringify({ hookSpecificOutput: { hookEventName: "SessionStart", additionalContext: ghiChu } }));
});
