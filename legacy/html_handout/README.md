# html_handout —— 已封存的 HTML 撰稿線（2026-08-09 移入 legacy）

> **這夾是什麼**：講義 HTML 撰稿線的完整歷史快照（2026-06-15 升格正式版 → 2026-07-17
> 兩線分工 → **2026-08-09 LaTeX 統一後凍結、同日佈局重構移入 legacy**）。拍板與遷移紀錄＝
> [`../../handout/latex/KICKOFF-latex-unification.md`](../../handout/latex/KICKOFF-latex-unification.md)。
> **僅供參照，不再更新**；改課文一律改 `handout/latex/src/<ch>/<name>.tex`。

## 內容物

| 檔／夾 | 說明 |
|---|---|
| `fragments/ch{NN}/sec-*.html` | 歷史內容源（凍結＝2026-08-09 升格時點）。**存量 provenance 的家**：`<!-- section-source: -->` header 與 `<!-- expansion:… -->` 標記在這裡 grep（增量自統一起改在 `.tex` 的 `%` 註解） |
| `standalone/chapter{N}-print-standalone.html` | 組裝後的列印版快照（figkit harness 的初始生成源；harness 自此獨立演化） |
| `build.py` | fragment→standalone 組裝器（CHAPTERS registry＝當時的章節清單） |
| `CONTRACT-html-writing.md` | HTML 時代的權威撰寫契約（現行契約＝[`../../handout/latex/CONTRACT-latex-writing.md`](../../handout/latex/CONTRACT-latex-writing.md)） |
| `TYPESETTING_GUIDE.md` | HTML 排版指南（版心／字體拍板的歷史依據，LaTeX 模板設計曾錨定它） |
| `linebreak-gate.mjs` | MathJax 自動斷行偵測閘（隨分頁器退役；TeX 原生＋overfull 閘接手） |

轉換產線（fragment→LaTeX 的 `convert.py`／`make_dist.py`／`check_prose.py`／
`dialect_inventory.py`／`test_convert.py`／`print_html.mjs`）在 [`../html2latex/`](../html2latex/)；
方言凍結表（DIALECT-*.md）留在 `handout/latex/chapters/<ch>/`（與各章圖匯出資產同住）。
活資產的新家：rubric＋REVIEW＝`handout/_audit/`、章 PLAN＝`handout/_dev-archive/`、
`shot.mjs`＝`handout/figkit/`、`quote_lint.py`＝`tools/`。
