/* team-node.js - runs the browser engine (assets/team-live.js) in node and compares it with the
 * Python reference. Usage: node materials/team-node.js            prints the node canon as JSON
 *                          node materials/team-node.js --compare  also runs the Python reference
 *                          (--raw) and reports every value that differs (exact equality). */
var fs = require("fs"), path = require("path"), cp = require("child_process");
var repo = path.join(__dirname, "..");
var src = fs.readFileSync(path.join(repo, "assets", "northline-data.js"), "utf8");
var win = {}; new Function("window", src)(win);
var eng = require(path.join(repo, "assets", "team-live.js"));
eng.setData(win.NORTHLINE);
var c = eng.canon();
if (process.argv.indexOf("--compare") < 0) { console.log(JSON.stringify(c, null, 1)); process.exit(0); }
var py = JSON.parse(cp.execFileSync("python3", [path.join(__dirname, "team_reference.py"), "--raw"], { encoding: "utf8" }));
var n = 0, bad = [];
function walk(a, b, k) {
  if (typeof a === "number" || typeof b === "number") { n++; if (a !== b) bad.push(k + ": node " + a + " python " + b); return; }
  if (typeof a === "string" || typeof b === "string") { n++; if (a !== b) bad.push(k + ": node " + a + " python " + b); return; }
  if (Array.isArray(a) || Array.isArray(b)) {
    if (!Array.isArray(a) || !Array.isArray(b) || a.length !== b.length) { bad.push(k + ": length"); return; }
    a.forEach(function (x, i) { walk(x, b[i], k + "[" + i + "]"); }); return;
  }
  var ks = Object.keys(a).concat(Object.keys(b)).filter(function (x, i, s) { return s.indexOf(x) === i; });
  ks.forEach(function (x) { if (!(x in a) || !(x in b)) bad.push(k + "." + x + ": missing"); else walk(a[x], b[x], k + "." + x); });
}
walk(c, py, "canon");
console.log(n + " values compared, " + bad.length + " differ");
bad.slice(0, 20).forEach(function (x) { console.log("  " + x); });
process.exit(bad.length ? 1 : 0);
