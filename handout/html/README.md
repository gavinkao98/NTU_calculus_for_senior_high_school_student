# html —— 已凍結的 HTML 撰稿線（2026-08-09 起）

> **本線已凍結**（LaTeX 統一拍板 U1，權威計畫＝
> [`../latex/KICKOFF-latex-unification.md`](../latex/KICKOFF-latex-unification.md)）：
> 12 單元內容源已全數升格至 **`../latex/src/<ch>/<name>.tex`**，**改課文一律改那裡**——
> 本夾的 `fragments/`、`standalone/`、`build.py` 不再更新（歷史快照＝升格時點的內容）。

仍在服役的部分：

- **`_audit/`**——內容閘 rubric 與 REVIEW 報告（活資產，新報告照舊放這裡）。
- **`_dev-archive/`**——各章 PLAN／as-built ledger（活資產）。
- **`_render/shot.mjs`**——圖閘 render 工具（輸入改吃 [`../figkit/`](../figkit/README.md)
  的 figs harness 頁；`figures` 模式逐圖截 PNG 餵 `handout-figure-audit`）。
- `quote_lint.py`——P3 改造為掃 `.tex` 散文前，暫對凍結 fragment 維持 CI 綠。

圖的繪製（原 standalone 內的 `FIGS` JS）已縮編至 [`../figkit/`](../figkit/README.md)
（harness 頁＝圖源；`linebreak-gate.mjs` 隨分頁器退役——TeX 原生斷行＋overfull 閘接手）。
