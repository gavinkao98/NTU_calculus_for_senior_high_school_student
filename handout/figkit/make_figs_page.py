#!/usr/bin/env python3
r"""make_figs_page.py -- 從 print-standalone 生成 figs-only harness 頁（圖 kit 縮編，U2）。

LaTeX 統一（handout/latex/KICKOFF-latex-unification.md）後，HTML 撰稿線退役，
但 105 張圖仍由 JS FIGS 函數繪製。本工具把 standalone 變換成「只有圖、沒有課文」的
harness 頁，供既有的兩個消費端照舊使用：

  - handout/latex/export_figs.mjs  <harness.html> <outDir>   # LaTeX 嵌圖（向量 PDF）
  - handout/html/_render/shot.mjs  <harness.html> <out> figures  # 圖閘 render（PNG）

變換內容（其餘 head/CSS/MathJax/buildPlot/FIGS/hydrate 全部 verbatim 保留，
量測語境與 standalone 完全一致——#source 的 683px 版心、.paper 變數鏈照舊）：
  1. 內容區（BEGIN/END-CONTENT-FRAGMENTS）→ 僅保留全部 <figure data-fig> 元素，
     收進 <template id="figs-only">。
  2. paginator <script>（含 function paginate 的塊）→ 簡化 boot：
     填 #page → hydrateFigures → MathJax typeset → fonts.ready → 移除 #boot
     （#boot 的移除語義與 standalone 相同，export/shot 的就緒偵測不用改）。

用法：
    python make_figs_page.py ../html/standalone/chapter3-print-standalone.html figs-ch03.html
"""

import re
import sys
from pathlib import Path

CONTENT_RE = re.compile(
    r"<!-- BEGIN-CONTENT-FRAGMENTS -->.*?<!-- END-CONTENT-FRAGMENTS -->", re.DOTALL
)
# data-fig figures hydrate from FIGS; inline-SVG figures (id= without data-fig, e.g.
# ch01 fig-map) carry their drawing in the markup itself — both must reach the harness,
# or the figure-audit population and re-export both silently lose the inline ones.
FIGURE_RE = re.compile(r'<figure\b[^>]*\b(?:data-fig|id)="[^"]+"[^>]*>.*?</figure>', re.DOTALL)
PAGINATOR_RE = re.compile(
    r"<script>(?:(?!</script>).)*function paginate(?:(?!</script>).)*</script>", re.DOTALL
)

BOOT_JS = """<script>
(function () {
  function waitFor(test, tries) {
    return new Promise(function (res) {
      var i = 0;
      (function tick() {
        if (test()) return res(true);
        if (++i > tries) return res(false);
        setTimeout(tick, 150);
      })();
    });
  }
  function build() {
    var page = document.getElementById("page");
    var tpl = document.getElementById("figs-only");
    page.innerHTML = tpl ? tpl.innerHTML : "";
    if (window.hydrateFigures) window.hydrateFigures(page);
    waitFor(function () { return window.MathJax && window.MathJax.typesetPromise; }, 400)
      .then(function (ok) {
        if (!ok) { document.getElementById("boot").textContent = "MathJax load timeout"; return; }
        return MathJax.typesetPromise([page]).catch(function (e) { console.warn("mathjax", e); });
      })
      .then(function () {
        return document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve();
      })
      .then(function () {
        var boot = document.getElementById("boot");
        if (boot) boot.remove();
      });
  }
  window.addEventListener("DOMContentLoaded", build);
})();
</script>"""


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src, out = Path(sys.argv[1]), Path(sys.argv[2])
    html = src.read_text(encoding="utf-8")

    m = CONTENT_RE.search(html)
    if not m:
        sys.exit("FAIL: content-fragment markers not found in " + str(src))
    figures = FIGURE_RE.findall(m.group())
    if not figures:
        sys.exit("FAIL: no <figure data-fig> found in content region of " + str(src))
    replacement = (
        "<!-- BEGIN-CONTENT-FRAGMENTS -->\n"
        '<template id="figs-only">\n' + "\n".join(figures) + "\n</template>\n"
        "<!-- END-CONTENT-FRAGMENTS -->"
    )
    html = html[: m.start()] + replacement + html[m.end():]

    html, n = PAGINATOR_RE.subn(BOOT_JS, html)
    if n != 1:
        sys.exit(f"FAIL: expected exactly 1 paginator script, found {n}")

    out.write_text(html, encoding="utf-8", newline="\n")
    print(f"OK: {out}  ({len(figures)} figures)")


if __name__ == "__main__":
    main()
