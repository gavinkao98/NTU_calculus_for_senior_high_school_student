# CLAUDE.md — handout 子目錄指引

本檔案補充根目錄 [`../CLAUDE.md`](../CLAUDE.md) 的專案層級指引，僅涵蓋 `handout/` 特有的架構約束。

內容撰寫規則（用語、密度、數學排版、圖表規範等）以 [`../CONTENT_SPEC.md`](../CONTENT_SPEC.md) 為準；`.tex` 標記契約以 [`latex/CONTRACT-latex-writing.md`](latex/CONTRACT-latex-writing.md) 為準。

## 結構（2026-08-09 LaTeX 統一；拍板＝[`latex/KICKOFF-latex-unification.md`](latex/KICKOFF-latex-unification.md)）

- [`latex/`](latex/)＝**唯一內容源＋唯一工作線**：`src/<ch>/<name>.tex`（手改／LLM 改的源）、`template/calcbook.sty`（語意＋樣式層）、`dist/<ch>/<name>.pdf`（成品，`build.py` 產）、`chapters/<ch>/figs/`（圖匯出品，gitignored 可重現）。
- [`figkit/`](figkit/)＝**JS 畫圖 kit**：`figs-<ch>.html` harness（圖源——`FIGS` 函數＋inline-SVG 住這裡）＋`make_figs_page.py`（自凍結 standalone 初始生成的一次性工具）。
- [`_audit/`](_audit/)＝內容閘 rubric＋REVIEW 報告（活資產）；[`_dev-archive/`](_dev-archive/)＝各章 PLAN ledger（歷史錨）。HTML 撰稿線已整體移入 [`../legacy/html_handout/`](../legacy/html_handout/)（fragment／standalone／`build.py`／舊契約，僅供參照）；轉換產線工具在 [`../legacy/html2latex/`](../legacy/html2latex/)。

## 改課文一律改 `latex/src/<ch>/<name>.tex`

```bash
cd handout/latex
python build.py ch08     # 編譯＋log 閘＋字形閘 → dist/ch08/chapter8.pdf（overfull 列出待裁決）
```

**不要改 `../legacy/html_handout/fragments/`**（凍結；CI 的凍結強制會抓）。編號一律語意化——環境 num 參數
給 label key（`{thm:ibp}`），文內引用 `Theorem \ref{thm:ibp}`；**不得手寫編號**（詳
[`latex/CONTRACT-latex-writing.md`](latex/CONTRACT-latex-writing.md) §Numbering）。

## 章節結構

一章一檔 `src/<ch>/<name>.tex`：`\cbchapter{N}` → `\chapteropener`＋`lead`＋`objectives` →
逐節 `\sechead{N.M}{Title}`＋內容環境。新增一章＝新增 `src/<ch>/` 一檔＋`build.py` 的
`UNITS` 表補一行。章開場直接寫在章檔開頭（不設獨立 intro 檔）。

## 圖表系統

- `.tex` 放版位：`figureblock` 內 `\includegraphics[width=<mm>]{<ch>/figs/<stem>}`＋
  `\figcaption{fig:<key>}{caption}`。
- 圖形內容在 `figkit/figs-<ch>.html` 的 `FIGS` 物件（或 inline-SVG `<figure>`）。
- **新增圖表需要改兩處：** `.tex`（`figureblock`）＋ figkit harness（`FIGS` 函數）。
  然後 `node latex/export_figs.mjs figkit/figs-<ch>.html latex/chapters/<ch>/figs` 匯
  向量 PDF、重跑 `build.py <ch>`。圖閘 PNG＝`figkit/shot.mjs <harness> <out> figures`。

## 驗收閘

`build.py` 內建：編譯閘（0 error／0 missing char）＋版面閘（overfull 逐條列出）＋字形閘
（`check_glyphs.py`）。內容閘鏈（數學／散文／難度／圖）讀 `.tex` 源與 harness PNG，閘序
見 [`PIPELINE.md`](PIPELINE.md)。改動含編號時 log 不得有 undefined reference。
