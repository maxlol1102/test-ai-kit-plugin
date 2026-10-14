// Hook PreToolUse: AI không được gõ vào ô mật khẩu / OTP / mã PIN trên hệ thống kiểm thử.
// Tester tự đăng nhập trong cửa sổ trình duyệt (xem skill dang-nhap-an-toan). Lớp chặn thứ hai, phòng khi agent quên quy tắc.
// Chặn bằng exit code 2 – nội dung stderr được trả lại cho Claude.
const NHAY_CAM = /m[aậ]t\s*kh[aẩ]u|password|passwd|pass\s*word|\bpwd\b|\bpin\b|\botp\b|m[aã]\s*x[aá]c\s*(th[uự]c|nh[aậ]n)|captcha/i;

let du_lieu = "";
process.stdin.on("data", (c) => (du_lieu += c));
process.stdin.on("end", () => {
  let vao = {};
  try { vao = JSON.parse(du_lieu).tool_input || {}; } catch { process.exit(0); }
  // browser_type: { element, ref, text } ; browser_fill_form: { fields: [{ name, type, ref, value }] }
  const mo_ta = [vao.element, ...(vao.fields || []).map((f) => `${f.name || ""} ${f.type || ""}`)].join(" | ");
  if (NHAY_CAM.test(mo_ta)) {
    process.stderr.write(
      "Bị chặn: không được tự nhập mật khẩu / OTP / mã xác thực (" + mo_ta.slice(0, 120) + "). " +
      "Hãy dừng lại và nhờ tester tự đăng nhập trong cửa sổ trình duyệt, chờ tester báo xong rồi chụp lại trang (browser_snapshot)."
    );
    process.exit(2);
  }
  process.exit(0);
});
