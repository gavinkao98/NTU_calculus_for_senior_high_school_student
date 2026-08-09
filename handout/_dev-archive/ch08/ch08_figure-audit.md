# Ch8 M2 圖批次 — audit record（機會覆核＋繪製＋D1–D8 gate-1＋回歸）

2026-07-26。使用者指令「開 M2 圖批次」；裁決點由使用者親自裁（AskUserQuestion）：**全採 13 張**。
視覺 gate-2（Codex `-i` 餵 PNG）依「三閘 M4 後批次」規則**不在本輪**（ch07 同例）。

## ① 機會覆核（gate-1，7 subagent 平行）

`handout-figure-opportunity-audit` ×7（每節一個，rubric 雙鏡頭＋D1–D6 預設駁回）覆核 M1 的
9 個 `[FIGURE-OPPORTUNITY]` 標記＋掃漏。結果：**13 候選（high 3／medium 10；掃漏新增 4）＋
駁回 32**；§8.4／§8.5 的「刻意零圖」判斷經對抗式構造覆核成立（各 4–5 個最強候選全數 D1/D2/
D3/D4/D6 駁回）。標記層 findings：8.1 標記的兩區域標籤依其自宣告軸向寫反（落筆前修正）；
8.7 兩標記各帶 MODIFY（釘 concave-up f=1/x；等積圖移位至 Ex 8.33 後）；8.6 兩 MODIFY
（sliver hatch→ghost fill；transversal 非相切）。裁決稿：`_audit/REVIEW-ch08-figure-opportunity.html`。

## ② 繪製（fragment＋FIGS 兩處同改）

Figure 8.1–8.13 依文序編號；`build.py` 不動（圖屬 shell FIGS＋fragment figure 元素）。
kit 擴充：`fill-ghost`／`fill-aux` 兩個淡填色 class＋章別 `figure[data-fig]` 寬度規則＋
`figure-art--triple` 版面收斂至 3×176px（紙寬 567px 內三欄不折行）。helper：`lag3`（三點
Lagrange）、`lerpNodes`（分段線性）、`triPanel`（參考三角形 panel）。

**作者自查（SPEC §10 落地前自檢，逐 PNG 親視）修 9 處**：triple 折行（CSS）；Fig 8.11 區間
[1,2]→**[1,3]**（弦–曲線 gap ≈0.016 在印刷尺寸不可見，教學功能失效；n=4 與 f=1/x 依機會閘
釘住不動，偏離記錄於 fragment 來源註解）＋第二組節點改空心點＋caption 把「第二段弧與曲線
不可分」明說為教學點；Fig 8.12 slice 加寬＋label 移位；Fig 8.13 ymax 提高；Fig 8.8 ghost
填色延伸至畫框（消「柱狀」截斷）；Fig 8.3 label 離線；Fig 8.5 a-tick 字避 ghost 弧。

## ③ D1–D8 gate-1（4 subagent：§8.1×2／§8.2–8.3×3／§8.6×5／§8.7×3）

**13/13 視覺 blocking 歸零；advisory 4（全在 §8.6 批）**：

- [D1 adv] Fig 8.6／8.7／8.9 同根因——`buildPlot` 的 `vline` 畫滿 ymin..ymax，`ymin<0` 時
  越軸下探、擦到同 x 的 tick 字頂（t／「2」／a+n、a+n+1）。**修**：三處改 `seg` 自 y=0 起。
- [D1 adv] Fig 8.10 「y = e^{−x²}」label 尾端與藍曲線下切段相接。**修**：label 移 (1.18, 0.058)。

稽核員另確認：Fig 8.1 標籤方位正確（機會閘的對調 finding 未復發）；Fig 8.4 三 panel 邊長
逐字符合 Strategy 8.4 與 Ex 8.12/8.14/8.15；Fig 8.11 的 [1,3] 偏離判合理（[1,2] gap ≈2px
不可見）；Fig 8.11 第二段弧視覺重合＝caption 明說之教學點，不判 D5；Fig 8.9 的 hollow-t＝
「generic 點 vs 整數樣本」的 §10 marker 分工，非「未定義」語義誤用。

## ④ scoped 回歸（第二輪，1 subagent）

**R1–R4 全 clean、0 blocking、無新 finding**——四處修法逐一回源碼核對落地（L2219／L2242／
L2287–2288／L2315），語義（截斷、漸近線全高、夾擠、label 歸屬）均保持。

## 終值

build ✔（全 registry）· linebreak-gate **0** · quote_lint clean ×7 · render **math=1171／
katex-errors=0** · 13/13 PNG 出圖 · PLAN-ch08 Figure ledger 已回填（8.1–8.13）。
產物：`_audit/REVIEW-ch08-figure-opportunity.html`（裁決稿＋applied banner）、
`_audit/REVIEW-ch08-figure-audit.html`（13 圖內嵌成品報告）。

**Status: M2 CLOSED（gate-1 側）——13 圖 blocking 歸零＋4 advisory 修復＋回歸 clean；
視覺 gate-2 留 M4 後三閘批次。**
