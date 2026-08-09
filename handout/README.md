# handout —— 講義產線（LaTeX 統一）

> 本資料夾是**生產用講義**（2026-06-15 自 `experiments/handout_kit/` 升格；2026-07-17 曾依
> 兩線分工重整；**2026-08-09 LaTeX 統一**——HTML 撰稿線退役移入 [`../legacy/html_handout/`](../legacy/html_handout/)，
> 拍板與遷移紀錄見 [`latex/KICKOFF-latex-unification.md`](latex/KICKOFF-latex-unification.md)）。
> 完成一章的閘序與各章狀態見 [`PIPELINE.md`](PIPELINE.md)；撰稿模式見
> [`../CONTENT_AUTHORING_WORKFLOW.md`](../CONTENT_AUTHORING_WORKFLOW.md)；本資料夾特有的
> 架構約束見 [`CLAUDE.md`](CLAUDE.md)。

## 佈局

| 夾 | 角色 |
|---|---|
| [`latex/`](latex/) | **唯一內容源＋出版線**：`src/<ch>/<name>.tex` 撰稿、`build.py` 編譯、`dist/<ch>/` 成品 PDF（線導覽＝[`latex/README.md`](latex/README.md)） |
| [`figkit/`](figkit/) | **JS 畫圖 kit**：`figs-<ch>.html` harness（圖源）＋`shot.mjs`（圖閘截圖）＋`export_figs.mjs`（在 `latex/`，匯向量 PDF） |
| [`_audit/`](_audit/) | 內容閘 rubric＋REVIEW 審核報告（活資產） |
| [`_dev-archive/`](_dev-archive/) | 各章 PLAN／as-built ledger／歷次稽核紀錄（歷史錨） |

HTML 時代的 fragment／standalone／`build.py`／撰寫契約在 [`../legacy/html_handout/`](../legacy/html_handout/)；
HTML→LaTeX 轉換產線工具在 [`../legacy/html2latex/`](../legacy/html2latex/)（皆僅供參照）。
