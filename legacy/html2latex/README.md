# html2latex —— 已退役的 HTML→LaTeX 轉換產線（2026-08-09 移入 legacy）

> 兩線時代（2026-07-17 拍板）把 fragment 確定性轉換成出版 LaTeX 的工具組。
> **LaTeX 統一 P1（2026-08-09）完成 12 單元最後一批首轉後全數退役**；`.tex` 自此是唯一
> 內容源，無轉換可跑。僅供參照（或未來反向考古）。沿革＝
> [`../../handout/latex/KICKOFF-latex-unification.md`](../../handout/latex/KICKOFF-latex-unification.md)、
> [`../../handout/latex/KICKOFF-latex-pilot.md`](../../handout/latex/KICKOFF-latex-pilot.md)。

| 工具 | 當年職責 |
|---|---|
| `convert.py` | fragment → 語意層 LaTeX（IR＋emitter；數學逐位元組 pass-through、表外標記硬錯） |
| `test_convert.py` | golden tests＋數學逐位元組不變式 |
| `dialect_inventory.py` | 逐章方言盤點（差集 → DIALECT-*.md，表留 `handout/latex/chapters/<ch>/`） |
| `check_prose.py` | 完整性閘：pdftotext 散文子序列＋圖內文字（驗「轉換不丟內容」，隨轉換退役） |
| `make_dist.py` | 轉換＋內嵌＋編譯＋三閘 → dist 兩檔（現行編譯入口＝`handout/latex/build.py`） |
| `print_html.mjs` | HTML 印 A4 PDF（HTML vs LaTeX 對照報告用） |
