# KICKOFF：Ch8 M1（canon 草擬）＋生成端兩臂對照

> **用法：** 對**對話一**（主線）貼：「讀 `handout/html/_dev-archive/ch08/KICKOFF-ch08-m1.md`，執行〈對話一〉。」
> **對話二（對照臂）**時機到了再開，貼本檔 **§4 的整段 prompt 原文**——不要叫它讀本檔其他部分（會污染對照組）。
> 本檔只是 ch08 M1 的**流程編排**；閘序權威＝[`handout/PIPELINE.md`](../../../PIPELINE.md)（canon 章 5-milestone），撰稿規則＝`CONTENT_AUTHORING_WORKFLOW.md`／`CONTENT_SPEC.md`，方向＝`CONTENT_DIRECTION.md`。判準衝突時以權威文檔為準，不在本檔另立規則。

## 0. 背景與本輪目標

- Ch1–Ch7＋appB 的內容閘、平實化回填、LaTeX 出版線均已收；appA／appC／appD 回填**暫緩**（2026-07-26 使用者裁決）。產線存量側乾淨。
- Ch8 是**平實英文條款（CONTENT_SPEC §3，RC）凍結後的第一個新章**。依 [`../../_audit/KICKOFF-plain-backfill.md`](../../_audit/KICKOFF-plain-backfill.md) §「新增章節不走本流程」：新章不做回填，改在**生成端受約束**；Ch8 前兩節兼任「**生成端兩臂對照**」試驗場，驗證此假設——這是條款升 v1.0 的最後一塊。
- 本輪範圍＝**M1（canon 草擬）全章**＋兩臂對照量測與裁決稿。M2（圖批次）–M5 之後另開輪。

## 1. 對話一必讀（依序）

1. `CLAUDE.md`（根）＋`handout/CLAUDE.md` — 紀律：Codex 調用逐次徵同意、繁中對話、fragment 唯一內容源、registry 單一真實來源。
2. `handout/PIPELINE.md` — canon 章 5-milestone 的 **M1 定義**＋通用紀律（**開長閘前先從 main 更新**、編號 ledger 手動、render 自驗、findings 留版控）。
3. `CONTENT_AUTHORING_WORKFLOW.md` — Mode A canon 變體（章層盤點 → 逐節 brief → 擴寫 → Codex ⑤）。
4. `CONTENT_DIRECTION.md` — 方向層（結構性排序、on-credit 紀律）。
5. `CONTENT_SPEC.md` — 全文，**含 §3 平實英文條款**（對話一＝條款臂，就是要整份在 context）與 §16 讀者 persona。
6. `CONTENT_ROADMAP.md` — Ch8 entry（Role／Prereq／深度＝**標準/計算**）＋全局 seam ledger＋provisional roster：8.1 by Parts｜8.2 Trig Integrals（A.2）｜8.3 Trig Substitution（GAP-F）｜8.4 Partial Fractions（A.4）｜8.5 Strategy｜8.6 Improper｜8.7 Approximate；inverse hyperbolic 可置此（收不收→盤點時提案交使用者）。
7. 前例形狀（照這個做）：`html/_dev-archive/ch07/` 的 `PLAN-ch07.md`、`brief-7-N.md`、`ch07_s7-N-codex5-audit.md`、章層 sweep／direction audit；ch06 同套。
8. `html/_audit/MATH-CORRECTNESS-RUBRIC.md`（M1–M8）＋`html/_audit/PROSE-AUDIT-RUBRIC.md`（含 R 維度）。

**引用地雷（盤點時核對 as-built）：** 附錄 A.4 部分分式現為 **Prop A.7**（A.3 插入 Prop A.6 後移）；GAP-F 完全平方已併入 §A.5 收尾段。引用一律以 as-built 編號為準，別抄 ROADMAP 舊文。

## 2. 兩臂對照設計（實驗層；開跑前凍結，中途不可改）

| | 臂 T（條款臂） | 臂 C（對照臂） |
|---|---|---|
| 場地 | **§8.1 by Parts**（對話一寫） | **§8.2 Trig Integrals**（對話二寫，全新對話） |
| 平實約束來源 | SPEC §3 全文在 context＋完稿自檢跑 `tools/prose_metrics.py` | **只給範文**（ch07 §7.1／§7.2 定稿＋§8.1 as-built）；**不得開 SPEC §3、不得開 PROSE-AUDIT-RUBRIC、寫作期間不得跑 prose_metrics** |
| 其他輸入 | 相同（brief、DIRECTION、數學紀律——兩臂只差平實 treatment） | 相同 |

- **量測點（兩臂一致）**＝「初稿完成、Codex ⑤ 與任何修正**之前**」：em-dash 密度、tic guard 四項、詞彙家族命中/千詞、段落觸發器（逐節與單元層照 `prose_metrics.py --unit ch08` 輸出記錄）。
- **比較基準**：`T_can` ≤3.0/1000；canon 章歷史初稿水位＝ch05 全章 em-dash 14.4、家族 18.8/千詞；ch06 §6.2 家族 14.7。
- **判讀（⛳ 交使用者裁決，寫進裁決稿）**：臂 T 達標＋臂 C 回到歷史水位 → 條款有效；**兩臂皆達標** → 範文就夠、條款可瘦身；**臂 T 未達標** → 生成端約束不足、新章仍需回填輪。n=1、兩節題材差異是 confound——訊號不明確時用 §8.3 依同法複製一次再議，不要硬下結論。
- **嚴格串行**：對話一完成 §8.1（含初稿量測存檔）→ **停**，使用者開對話二寫 §8.2 → 主線量臂 C → 產 `REVIEW-ch08-twoarm-plain.html`（standalone HTML、繁中框架）⛳ 裁決 → §8.2 進正常閘、續 §8.3–8.7。
- 兩臂初稿數字記進 `PLAN-ch08.md` 的「兩臂實驗紀錄」節（永久資料點，勿只留在裁決稿）。

## 3. 對話一步驟

1. `git fetch` 確認基準在最新 `main`（通用紀律）；掃一眼近期 log 有沒有人動過共用工具。
2. **章層 canon 盤點**：ROADMAP Ch8 entry＋seam ledger（import：A.2 積化和差／降冪→§8.2、GAP-F 完全平方→§8.3、Prop A.7 部分分式→§8.4；export 候選：§8.6 improper integral→Ch11 §11.3 Integral Test）＋roster 確認或提修（inverse hyperbolic 提案）。產 `PLAN-ch08.md` 初版（弧線、節 roster、編號 ledger 骨架、兩臂實驗紀錄欄）⛳ 交使用者過目後才動筆。
3. **§8.1（臂 T）**：`brief-8-1.md`（例題計畫、軟深度計畫、`figure_opportunities`——M1 不畫圖，圖在 M2 批次）→ 擴寫 `html/fragments/ch08/sec-8-1.html`（章開場併入第一個 `<article>`，見 `handout/CLAUDE.md`）→ `build.py` registry 加 ch08 → render 自驗（`shot.mjs`、`linebreak-gate.mjs`）→ **初稿量測存檔** → Codex ⑤（計費，逐次徵同意）至 0 blocking。
4. ⛳ **停**：回報使用者「臂 C 可開跑」，提醒使用者把本檔 §4 的 prompt 原文貼進全新對話。
5. 臂 C 完稿回報後：主線量臂 C 初稿 → `REVIEW-ch08-twoarm-plain.html` ⛳ 交裁決。
6. 裁決後：§8.2 進正常閘（含 Codex ⑤）→ §8.3–8.7 逐節照臂 T 同法（全掛條款＋自檢）→ 章層收尾 sweep（**sympy 全例重算＋hypothesis ledger 覆核＋章層 Codex review 明列 M1–M8 各維**）→ `REVIEW-ch08-applied.html` ⛳。
7. commit 紀律照舊：經授權才 commit、繁中、Mode B 裁決寫進 body。

## 4. 對話二 prompt（對照臂——複製以下整段到**全新對話**）

```text
這輪只做一件事：為微積分講義撰寫 Chapter 8 的 §8.2 Trig Integrals 初稿（Mode A canon 擴寫）。

必讀（依序）：
1. CLAUDE.md（根）＋ handout/CLAUDE.md
2. CONTENT_AUTHORING_WORKFLOW.md 的 Mode A canon 變體
3. CONTENT_DIRECTION.md
4. CONTENT_SPEC.md——但【跳過 §3〈平實英文條款〉整節，一個字都不要開】。這是 A/B 實驗的對照組設定，不是偷懶：本對話的英文風格只准向下列範文學。
5. handout/html/_dev-archive/ch08/PLAN-ch08.md ＋ brief-8-2.md（節內容計畫）
6. 範文（風格唯一來源）：handout/html/fragments/ch07/sec-7-1.html、sec-7-2.html 定稿，與 handout/html/fragments/ch08/sec-8-1.html as-built
7. 數學正確性契約：handout/html/_audit/MATH-CORRECTNESS-RUBRIC.md

禁止事項（違反即該臂作廢）：
- 不得開啟 CONTENT_SPEC.md §3、PROSE-AUDIT-RUBRIC.md、KICKOFF-plain-backfill.md、任何 REVIEW-*-plain-*.html。
- 寫作期間不得執行 tools/prose_metrics.py（量測由主線對話事後做）。
- 若不慎讀入上述任一內容，停下並在回報中誠實聲明（該臂作廢，實驗改在 §8.3 重跑）。

要做的事：
- 依 brief-8-2.md 擴寫 handout/html/fragments/ch08/sec-8-2.html（fragment 是唯一內容源；
  編號接續 PLAN-ch08.md 的 ledger；figure 只留 figure_opportunities 計畫、不畫圖）。
- python handout/html/build.py ch08 重建，跑 render 自驗（shot.mjs、linebreak-gate.mjs），
  修到 0 KaTeX err、0 自動斷行。
- 完稿即停：不跑任何散文閘、不跑 Codex、不 commit。回報「§8.2 初稿完成」與檔案清單即結束，
  後續量測與審閘由主線對話接手。

與使用者對話用繁體中文；課文本身是英文。
```

## 5. 硬護欄

- 臂 C 的隔離是實驗效度所繫：主線寫 `brief-8-2.md` 時**不得夾帶任何平實條款指示**（brief 只寫內容計畫：例題、軟深度、圖機會、seam import）。
- 兩臂量測點必須一致（初稿、任何修正前）；量完才准動。
- M1 其他紀律照 PIPELINE：on-credit／fence 需章層裁決、編號 ledger 先建完整地圖再動手、`*.raw.txt` 不進版控、findings 轉錄進 `ch08_*-audit.md`。
- Codex 每次調用（含 read-only review）逐次徵同意。

## 6. 產物清單（M1 收束時應齊）

- `PLAN-ch08.md`（含編號 ledger＋兩臂實驗紀錄）
- `brief-8-1.md` … `brief-8-7.md`；`html/fragments/ch08/sec-8-{1..7}.html`；registry 含 ch08
- `ch08_s8-N-codex5-audit.md` ×7＋章層 sweep audit
- `REVIEW-ch08-twoarm-plain.html`（兩臂裁決稿）＋`REVIEW-ch08-applied.html`（M1 收尾）

---
*本檔 2026-07-26 建立（Ch8 開章＋條款 v1.0 驗證合一輪）。實驗設計凍結於 §2；判準變更一律回權威文檔，不在本檔另立。*
