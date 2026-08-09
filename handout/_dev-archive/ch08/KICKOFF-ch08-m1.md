# KICKOFF：Ch8 M1（canon 草擬・整章一次生成）＋條款生成端驗證

> **用法：** 對新對話貼：「讀 `handout/html/_dev-archive/ch08/KICKOFF-ch08-m1.md` 並執行。」
> 本檔只是 ch08 M1 的**流程編排**；閘序權威＝[`handout/PIPELINE.md`](../../../PIPELINE.md)（canon 章 5-milestone），撰稿規則＝`CONTENT_AUTHORING_WORKFLOW.md`／`CONTENT_SPEC.md`，方向＝`CONTENT_DIRECTION.md`。判準衝突時以權威文檔為準，不在本檔另立規則。

## 0. 背景與本輪目標（含兩筆使用者裁決，2026-07-26）

- Ch1–Ch7＋appB 的內容閘、平實化回填、LaTeX 出版線均已收；appA／appC／appD 回填**暫緩**。產線存量側乾淨，Ch8 是**平實英文條款（CONTENT_SPEC §3，RC）凍結後的第一個新章**。
- **裁決一：取消「生成端兩臂對照」**（原規劃一臂只給範文——太耗資源）。改**單臂**：全章直接掛 SPEC §3 生成，**生成完成後再跑平實度與 em-dash 測試**驗收（§2）。
- **裁決二：整章一次生成。** 不走「一節寫完閘一節」——盤點與 PLAN 定案後，**§8.1–§8.7 連續生成到底，中途不設使用者停點**；免費自驗閘全跑完才一次交付。逐節 Codex ⑤ 相應改為**生成後批次跑**（見 §3 步驟 5）；其餘 M1 要求（brief、⑤ 至 0 blocking、章層 sweep）不變，僅執行順序重排。
- 本輪範圍＝**M1 全章**＋生成端驗證報告。M2（圖批次）–M5 之後另開輪。

## 1. 必讀（依序）

1. `CLAUDE.md`（根）＋`handout/CLAUDE.md` — 紀律：Codex 調用徵同意、繁中對話、fragment 唯一內容源、registry 單一真實來源。
2. `handout/PIPELINE.md` — canon 章 5-milestone 的 **M1 定義**＋通用紀律（**開長閘前先從 main 更新**、編號 ledger 手動、render 自驗、findings 留版控）。
3. `CONTENT_AUTHORING_WORKFLOW.md` — Mode A canon 變體（章層盤點 → 逐節 brief → 擴寫 → Codex ⑤）。
4. `CONTENT_DIRECTION.md` — 方向層（結構性排序、on-credit 紀律）。
5. `CONTENT_SPEC.md` — 全文，**§3 平實英文條款整份在 context 寫作**（這就是「新模式」），§16 讀者 persona。
6. `CONTENT_ROADMAP.md` — Ch8 entry（Role／Prereq／深度＝**標準/計算**）＋全局 seam ledger＋provisional roster：8.1 by Parts｜8.2 Trig Integrals（A.2）｜8.3 Trig Substitution（GAP-F）｜8.4 Partial Fractions（A.4）｜8.5 Strategy｜8.6 Improper｜8.7 Approximate。
7. 前例形狀（照這個做）：`html/_dev-archive/ch07/` 的 `PLAN-ch07.md`、`brief-7-N.md`、`ch07_s7-N-codex5-audit.md`、章層 sweep／direction audit；ch06 同套。
8. `html/_audit/MATH-CORRECTNESS-RUBRIC.md`（M1–M8）＋`html/_audit/PROSE-AUDIT-RUBRIC.md`（含 R 維度）。

**引用地雷（盤點時核對 as-built）：** 附錄 A.4 部分分式現為 **Prop A.7**（A.3 插入 Prop A.6 後移）；GAP-F 完全平方已併入 §A.5 收尾段。引用一律以 as-built 編號為準，別抄 ROADMAP 舊文。

**Roster 叉路預設（免停點）：** inverse hyperbolic **預設不收**（比照 Ch7「選材節制」先例），在 PLAN-ch08 記為 open question 交章末裁決；若使用者屆時要收，以**章末追加 §8.8** 方式補（不 cascade 既有編號）。其他盤點層叉路同理：取保守預設、記錄、不停下來等。

## 2. 生成端驗證（單臂；取代原兩臂設計）

- **寫作中**：照 SPEC §3 既有要求做**逐節完稿自檢**（`python tools/prose_metrics.py --unit ch08`），逐節數字順手記進 `PLAN-ch08.md` 的「生成端驗證紀錄」欄（standing 自檢，非額外實驗步驟；不計費、直接跑）。
- **章完成後**：全章跑 `prose_metrics --unit ch08`＋詞彙家族掃描，對照兩把尺：
  - 密度目標 **`T_can` ≤ 3.0/1000**＋tic guard 四項＋段落觸發器（SPEC §3）。
  - **歷史「無條款時代」canon 章初稿水位**＝ch05 em-dash 14.4/1000、家族 18.8/千詞；ch06 §6.2 家族 14.7——新章應顯著低於此。
- 結果寫進 `REVIEW-ch08-applied.html` 的「生成端驗證」小節 ⛳ 交使用者裁決：
  - **達標** → 「生成端就受約束」成立：回填輪對新章正式退役，作為條款升 v1.0 的證據。
  - **超標** → 就地依 SPEC §3 palette／執行序修到達標（散文層修補，護欄照 §3），並**如實記錄**「生成端仍不足、超標多少」供條款層再議——不可只修不記。

## 3. 對話步驟（整章一次；⛳ 僅兩處）

1. `git fetch` 確認基準在最新 `main`；掃一眼近期 log 有沒有人動過共用工具。
2. **章層 canon 盤點 → `PLAN-ch08.md`**：弧線、節 roster（叉路照 §1 預設）、seam import／export（A.2→§8.2、GAP-F→§8.3、Prop A.7→§8.4；export 候選：§8.6 improper integral→Ch11 §11.3 Integral Test）、**完整編號 ledger 先建**（Definition／Theorem／Example／Strategy／Figure 各型跨節連續；一次生成七節，cascade 風險最高，動筆前把號碼表定死、逐節照表用號）、生成端驗證紀錄欄。**不停，直接進 3。**
3. **整章連續生成**：依序 §8.1→§8.7，每節 `brief-8-N.md`（例題計畫、軟深度計畫、`figure_opportunities`——M1 不畫圖）→ 擴寫 `html/fragments/ch08/sec-8-N.html`（章開場併入第一節第一個 `<article>`；§8.1 時 `build.py` registry 加 ch08）。節與節之間只跑免費自檢（build＋`prose_metrics`），**不停、不徵詢**。
4. **章層免費驗收批次**：render 自驗（`shot.mjs`、`linebreak-gate.mjs`，0 KaTeX err／0 自動斷行）＋ sympy 全例重算＋ hypothesis ledger 覆核＋編號連續性 grep＋§2 全章平實度驗收。
5. ⛳ **停（第一次）**：交付初稿包——`REVIEW-ch08-applied.html` 初版（逐節內容＋locus＋`[source:]`＋驗證小節）＋PLAN＋open questions 清單；**同時徵詢 Codex 批次**：明列調用清單（逐節 ⑤ ×7＋章層 review M1–M8 ×1，每輪 ~120k tok）與預估用量，經同意才跑。
6. Codex 批次跑完 → findings 修補＋回歸審核（修過的項目重審）→ 更新 applied 報告 ⛳ **停（第二次）**：最終過目 GO。
7. commit 紀律照舊：經授權才 commit、繁中、Mode B 裁決寫進 body。

## 4. 硬護欄

- **編號 ledger 先建再動筆**（§3 步驟 2）；生成中不得插入計畫外的編號物件——要加就回 PLAN 改 ledger 再寫。
- M1 紀律照 PIPELINE：on-credit／fence 需章層裁決、`*.raw.txt` 不進版控、findings 轉錄進 `ch08_*-audit.md`。
- Codex 調用經徵詢同意才跑（§3 步驟 5 的批次徵詢須明列全部調用與用量；使用者要求逐次分開徵詢則照辦）。
- 驗收超標時的修補屬散文層：不動數學、成對破折號走四步仲裁、不機械拆句（SPEC §3 護欄全套適用）。

## 5. 產物清單（M1 收束時應齊）

- `PLAN-ch08.md`（含編號 ledger＋生成端驗證紀錄＋open questions）
- `brief-8-1.md` … `brief-8-7.md`；`html/fragments/ch08/sec-8-{1..7}.html`；registry 含 ch08
- `ch08_s8-N-codex5-audit.md` ×7＋章層 sweep audit
- `REVIEW-ch08-applied.html`（含生成端驗證小節）

---
*本檔 2026-07-26 建立；同日兩筆使用者裁決改版：取消兩臂對照（改單臂生成後驗收）＋整章一次生成（本版 v3）。判準變更一律回權威文檔，不在本檔另立。*
