# ch08 M4 — Mode C 條件式 gap-check（偵察／裁決／落地紀錄）

> PIPELINE M4。gate-1 唯讀偵察 ×4 獨立實例 → 單一裁決稿 → ⛳ 使用者裁決 → 落地 → 範圍限定 Mode B ＋ scoped 盲測回歸。
> 裁決稿（含全部候選卡片與駁回理由）：[`../../_audit/REVIEW-ch08-modec-gapcheck.html`](../../_audit/REVIEW-ch08-modec-gapcheck.html)。
> 本檔記可 `git log --grep` 撈回的摘要；Codex／agent 原始輸出落 gitignored scratchpad，不進版控。

日期：2026-07-27。基準線＝M3 收案（`N=8214`、em-dash 0.0/1000、Example 8.1–8.36、build/linebreak/quote_lint 全綠、工作樹 clean）。

## 1. gate-1 偵察配置（為何派四份）

| 實例 | agent | 範圍 | 波 |
|---|---|---|---|
| A | `mode-c-gapwalk` | §8.1→§8.7 順序全章 | ②軟深度 |
| B | `mode-c-gapwalk` | §8.7→§8.1 **逆序**全章 | ②軟深度 |
| C | `example-supplement` | §8.1–§8.4 | ①補例 |
| D | `example-supplement` | §8.5–§8.7 | ①補例 |

派**兩份獨立實例**跑同一件事，是照 M3 補正輪的實證教訓（單一實例會漏；當時補派的兩個實例另抓出 7 條客觀缺陷，見
`ch08_prose-difficulty-audit.md`）。四份都餵同一組硬邊界：PLAN `§Excluded`、**恰兩筆 on-credit 不得增加**、
§8.5 的 \(e^{-x^2}\) B-02 scope 紀律（M3 唯一紅旗）、**Example 硬上限 38（當時 36，只剩 2 格）**、
編號 cascade 成本須逐筆揭露、SPEC §3 平實語域。

## 2. 偵察結果

**①波 4 筆候選，全部 Layer 1，沒有一筆是「題目不夠多」**——四個都是「本書自己陳述或證明了某件事，卻從未示範」：

| id | 缺口 | cascade |
|---|---|---|
| `8.7-E1` | **Thm 8.4 的 Simpson 界全章零使用**（grep 覆核：`K_4`／`E_S` 只出現在定理陳述兩行）；且 §8.7 開場點名的三個 client 一個都沒被服務。這條界正是本章**兩筆 on-credit 之一** | 1 |
| `8.6-E1` | **Thm 8.3(b) 零示範**（grep 覆核：全章 `Theorem 8.3` 只在 Ex 8.32 被引一次，引的是 (a)） | 4 |
| `8.1-E1` | **Ex 8.6 的 reduction formula 被證明、被 spot-check、從未被使用**；§8.1 導言與 §8.2 Ex 8.8 收尾兩處明講的 payoff 都沒有實例 | **30** |
| `8.2-E1` | Strategy 8.2 step 2 零示範（但機械動作是 Ex 8.7 的鏡像） | 29 |

**§8.3／§8.4／§8.5 三節判定為乾淨、零例題候選**（每個 strategy row／fragment shape 都已有實例）。

**②波 48 筆原始候選，去重後 34 筆，全部為不編號物件（零 cascade）。12 個缺口被兩份獨立實例命中。**
章層事實（兩份實例各自 grep 得出、我複核）：Ch8 的 `expansion:application` ＝ 0、`expansion:history` ＝ 0，
Ch1–Ch7 每章都有。

**跨波命中一筆，是本輪最強訊號**：§8.1 的 reduction formula payoff 被 ①波報成「Layer 1 例題缺口」（cascade 30）、
被 ②波報成「intuition 缺口」（cascade 0）——同一缺口、兩種交付形態。

## 3. 我在裁決稿裡做的三個裁斷（兩份實例意見相反處）

1. **Simpson 命名史脈**：B 想具名 Kepler／Gregory，A 警告來源沒點名。我讀了 repo 內的
   `problem_banks/APEXCalculusV5/ptx/sec_numerical_integration.ptx` L574–576，原句是
   *"named after Thomas Simpson (1710-1761), even though others had used this rule as much as 100 years prior"*
   ——**確實沒有點名任何前人**。採 A 的無具名版 ＝ 零查證負擔。
2. **「Simpson 對三次式精確」的路線**：A 走 Thm 8.4 取 \(K_4=0\)，B 走本節**已證**引理的對稱區間代數。
   本章對「什麼是借來的、什麼是證過的」極度敏感（恰兩筆 credit 是章層設計），**採 B 的自足路線**，
   A 的 Thm 8.4 對照句另置於 fence Caution 之後（不動既有 env）。
3. **`8.1-E1` 改用零成本形態**：缺口成立且兩波命中，但 30 個 Example 重編號是本輪最大的機械風險。
   本章已有兩個不編號 tagged 推導先例（§8.1 shell–washer、§8.7 Simpson 引理），故改以
   `expansion:formula` 推導段交付，payoff 照樣落地、cascade 歸零。

## 4. 使用者裁決（2026-07-27）

- **①波**：採 `8.7-E1` ＋ `8.6-E1`；`8.1-E1` 轉不編號推導段；`8.2-E1` 不採（僅保留其 parity 診斷做成散文註）。
- **②波**：採到 **T3**（T1 十筆＋T2 三筆＋T3 九筆）。
- **四個品味題全採**：`8.6-d` 重力功寫進 §8.6（明知該節是 M3 難度尖峰）、`8.6-f` Gabriel's horn 一句、
  `8.2-E1` 的 parity 診斷做成 §8.2 散文註、**授權先上網查證再落筆** `8.2-a` 麥卡托史脈。

## 5. 落地明細（26 處增補：2 個 worked example ＋ 24 段不編號內容）

| § | 增補 | 形態 |
|---|---|---|
| 8.1 | `8.1-b/d` 合併（\(v\) 的常數：為何可丟＋何時值得用掉，\(\int\ln(x+1)dx\)）· `8.1-a`（多輪分部反轉角色 → \(J=J\)）· `8.1-c`（\([0,\pi/2]\) 上 \(I_n=\frac{n-1}{n}I_{n-2}\)，\(I_6=\frac{5\pi}{32}\)） | 散文 · Caution · **不編號推導**（取代 8.1-E1） |
| 8.2 | `8.2-f`（parity 診斷）· `8.2-a`（\(\int\sec\) 與麥卡托海圖）· `8.2-c`（cot–csc 鏡像家族） | 散文 ×3 |
| 8.3 | `8.3-a`（領導係數 ≠ 1 先提出來，接上 Strategy 8.4 三列） | 散文 |
| 8.4 | `8.4-b`（存在 ≠ 找得到）· `8.4-a`（代值抽驗常數）· `8.4-c`（重根模板要寫滿，三行無解反例） | 散文 ×2 · Caution |
| 8.5 | `8.5-a/b` 合併（改寫要說區間；多路線答案只差常數 Cor 4.4） | 散文（**刻意不用 env-caution**——該節 header 記錄不放 Caution 方塊） |
| 8.6 | `8.6-b`（divergent ≠ ∞）· `8.6-d`（重力功）· `8.6-f`（Gabriel's horn 一句）· `8.6-e`（變號被積函數不在射程）· **Ex 8.33** · `8.6-a`（兩個「無結論」組合）· `8.6-c`（收斂只取決於尾巴） | Caution ×3 · 散文 ×3 · **worked example** |
| 8.7 | `8.7-e`（只有 M 不碰端點）· `8.7-c`（Simpson 命名）· `8.7-b`（對三次式精確）＋Thm 8.4 對照句 · **Ex 8.37** · `8.7-d`（資料不等距）· `8.7-a`（無窮區間要先截斷） | 散文 ×4 · Caution ×2 · **worked example** |

**編號 cascade（實際執行）**：新 Ex 8.33 插在 §8.6 Fig 8.10 之後 → 舊 8.33–8.35 → 8.34–8.36；
新 Ex 8.37 插在 Ex 8.36 之後 → 舊 8.36 → 8.38。共 **4 個 Example 位移 ＋ 5 處 rendered cross-ref ＋
5 處 in-source ledger 註解**。最終 **8.1–8.38 ＝ 38 ＝ D1 硬上限**。

**一條 guard 誠實修訂**：`sec-8-6.html` 的 header 原寫 `NO Gabriel's horn`，比 PLAN `§Excluded` 的
「§8.6 one-sentence aside at most」更嚴。使用者裁決採 `8.6-f` 後，header 依 **8.6-B1 先例**修訂為
「恰一句、且寫在**截斷**立體上」，並記明理由；課文措辭維持 \([1,t]\) 與「隨 \(t\) 無界增長」，
故 Theorem 7.4（只在 \([a,b]\) 上陳述）未被套用到無窮曲面。

**查證紀錄（`8.2-a`，使用者授權後執行）**：兩個獨立來源一致——Wikipedia「Integral of the secant function」
＋ V. F. Rickey & P. M. Tuchinsky, *Mathematics Magazine* 53 (1980) 162–166。確認：麥卡托海圖 1569；
Edward Wright 1599（*Certaine Errors in Navigation*）以逐段求和造表；Henry Bond 約 1645 由對照 Gunter 的
對數正切表提出猜想；James Gregory 1668 證明（*Exercitationes Geometricae*）；Barrow 1670 給出更清楚的證明。
**兩份實例都警告、查證亦確認：麥卡托本人沒有計算或使用這個積分**——課文據此措辭，且刻意不寫出 Bond 的
對數正切形式（本書的形式是 Prop 8.1 的）。

## 6. 機械閘與 sympy（落地後）

- `build.py ch08` ✔ · `quote_lint` clean ×7 · **linebreak-gate 0 自動斷行**
  （中途抓到 1 條：新 Ex 8.37 的 \(S_{10}\) 顯示式被 MathJax 自動硬斷，已依本章慣例手動斷成 `aligned`）
- **prose_metrics（含全部回歸修補後的終值）：N 8214 → 10502，em-dash 仍 `0 → 0.0/1000`**。
  四個 tic guard 密度全部**下降**：colon 13.4→12.7、semi 4.3→4.2、parens 10.6→10.6、
  paired-comma 8.0→7.5 /1000 ——增補沒有把 em-dash 換成別的標點（「兩閘不可互相豁免」成立）。
- **render 自驗（瀏覽器實測，終值）**：math **1007 → 1378**、MathJax err **0**、未渲染 `\(` **0**、
  渲染後散文 em-dash **0**、Example env-num 連續 **8.1–8.38（38 個）**、Theorem 8.1–8.4／
  Def 8.1–8.2／Prop 8.1–8.2／Strategy 8.1–8.6／Figure 8.1–8.13 全在、**13/13 圖 hydrate**、
  **cross-ref dangling 0**。不編號 Caution 10 → 17。
- **sympy sweep：59/59 PASS**（本輪寫進課文的每一個數字與恆等式）。涵蓋：
  Ex 8.37 的 \(S_{10}=0.746824948\)／\(f^{(4)}\) 形式／\(K_4=36\) 為有效界（\([0,1]\) 上實際極大值 12，
  刻意示範「粗略界也合法」）／界 \(2\times10^{-5}\)／區間兩端四捨五入皆 0.7468／真值確實落在區間內；
  Ex 8.33 的三個不等式與兩個發散；`8.1-c` 的遞迴、邊界項歸零、\(I_6=5\pi/32\)；`8.1-b` 兩種 \(v\) 只差常數；
  `8.4-a` 的 \(x=1\) 抽驗兩邊皆 2；`8.4-c` 縮寫模板**確實無解**（sympy `solve` 回傳 `[]`）而完整模板有解；
  `8.6-d` 的 \(GMm(1/R-1/t)\to GMm/R\)；`8.6-f` 的體積 \(\to\pi\) 與 \(2\pi\ln t\) 下界；
  `8.7-b` 的三次式精確（generic 引理＋\(S_4\) 實例）。

## 7. 回歸閘（gate-1；三閘 gate-2 依 PIPELINE 留 M5 前批次，屆時另徵同意）

### 7a. 範圍限定 Mode B（Mode C 的必接後續，PIPELINE 硬規則）×3

只審新的 `[pass: enrichment]` 標記，不重審 Mode A 內容。

| 範圍 | 首輪 | 內容 |
|---|---|---|
| §8.1–8.3 | **0 blocking**／14 advisory | 5 條判為客觀缺陷全修：`8.1-c` 敘述範圍過寬（「any particular power … ending at \(I_0\)」對**奇次冪不成立**，改 *every even power*——依紅線縮小敘述而非補 \(I_1\) 的值）、`8.2-f` 指涉指錯（Ex 8.7 做的是**對的**選擇）、`8.2-a` 代詞歧義、`8.3-a` 與 Ex 8.16 收尾「the one algebraic step」正面對撞、`8.2-c` 微分記號漏 `dx`。另修 §8.1 三處商業隱喻（*spend／discard a freedom*、*what … buys*）——正是 M1 生成端自查掃掉的那個 family。 |
| §8.4–8.5 | **1 blocking**／12 advisory | blocking＝`8.4-b` 末句「When the **roots resist**, … the whole **pipeline stalls**, and no integration technique **repairs** it」：條件與後果**全由擬人＋機械隱喻承載、字面表述缺席**，踩 SPEC §3 MUST。整段重寫為字面說法。§8.5 段落由 150 詞拆為兩段（`belong together` 宣稱了未兌現的關聯；Ex 8.15 被誤歸為「多路線」情形）。 |
| §8.6–8.7 | **3 blocking**／20 advisory | ① `8.6-f` U3：Gabriel's horn 的 `is at least` 是全節唯一無理由的不等式（需自行想起 Thm 7.4 被積函數→\(\sqrt{1+x^{-4}}\ge1\)→Thm 6.2(4) 三步）。② `8.6-c` R2：條件靠 `awkward`／`well behaved` 承載，而在剛教完 Type 2 的節裡 *awkward* 最自然讀成「無界」，那樣配方裡的 \(\int_a^b f\) 就**不是** proper integral、與相鄰段落自相矛盾；且把 Example 8.32 歸類成它不是的情形（8.32 的整函數在 \([0,1]\) 毫無問題，只在**比較式**在 \(x<1\) 不成立）。③ `8.7-a` U4：**`quadrature` 全書讀者可見散文從未出現過**（唯一命中在 ch06 的 HTML 註解裡），出現在誤差帳的關鍵句。三條全修。 |

**四條紅線經逐字複驗全部成立**：③ B-02 的 \(e^{-x^2}\) scope（新內容只說本書技巧產不出、未斷言不存在；措辭並已對齊 §8.5 canon 由「this chapter's」改為「this book's」）／恰兩筆 on-credit 無新 fence（`8.6-e` 未用 Ch11 詞彙、未承諾 Ch11；`8.7-d` 不給替代公式）／`8.6-f` **恰一句**且全寫在截斷體 \([1,t]\)／`8.6-d` 止於「功是有限的」，無脫離速度。

### 7b. 回歸複核（CLAUDE.md：修完 finding 不可直接宣告完成）×2

| 範圍 | 結果 |
|---|---|
| §8.1–8.5 | **0 blocking**，`8.4-b` 的 R1 blocking 逐字確認消除、未引入新的隱喻承載／先用後定義／相鄰衝突。另抓到**我的修補自己造成的一條前指落空**（「the quadratic formula in Example 8.18」——該例並未寫出用了公式解），已改寫。 |
| §8.6–8.7 | **0 blocking**，三條原 blocking 逐條確認歸零。另抓到 **6 條我的修補引入的新 advisory**，其中兩條是客觀錯誤：「multiplying by \(e^{-x^{2}}\) **cannot enlarge it**」照字面為假（\(-36e^{-1} > -36\)；應為「不放大**絕對值**」）、以及一處懸垂分詞。全修。並確認移位後 Definition 8.1 的「see the caution below」線性讀第一個遇到的就是 principal-value Caution、Ex 8.28 與該 Caution 恢復相鄰、「In every case the procedure is the same」仍是收尾拍。 |

### 7c. 盲測 learner-sim（全章線性重讀 ×3 獨立實例，未告知改動）

**3/3 全 0 blocking／0 stuck／0 B 類先備違規 → 難度閘 PASS。**

| 實例 | 判定 | 難度曲線 §8.1→§8.7 | 與 Ch1–Ch4 基線 |
|---|---|---|---|
| 1 | 0 blocking／7 slowdown | `4 / 3 / 3.5 / 3 / 2 / 4 / 2.5`（均 3.1） | 持平；未觸及 §4.2 的 4.5 |
| 2 | 0 blocking／9 slowdown | `3.5 / 3 / 3 / 3.5 / 2 / 4 / 3`（均 3.1） | **持平偏低**，明顯低於 Ch4 |
| 3 | 0 blocking／12 slowdown | `4 / 3 / 4 / 3 / 2 / 4 / 3` | 持平於 Ch1–3、明顯低於 Ch4 |

**scoped §8.6 回歸盲測（位置修補後）**：0 blocking／4 slowdown，難度 **3.5/5**，仍低於 Ch4。三個導覽問題的回答確認位置修補生效——「see the caution below」**零次走錯**；五個 Caution 讀者全部複述得出；`8.6-a` 改寫後的開場被明確認出是與 `8.6-e` 的防呆。

**盲測抓到、落在 M4 新內容上並已修的**：`8.2-f` 的 \(\int u^3\cos x\,du\) 混變數讀來像印錯（補「the substitution is not yet complete」）／`8.1-c` 的 \(I_6\) 鏈第三個等號吃掉兩步（補 \(I_0\) 那一步）／Ex 8.37 的 \(K_4\) 逐項取界機制未說（補「Bounding each term … separately」）。

**盲測抓到、我造成的導覽 regression 並已修**：`8.6-b` 原插在 principal-value Caution 之前，害 Definition 8.1 的「see the caution below」指標落到錯的方塊。三個新增區塊重排（只動本輪新增的區塊，未動任何既有內容）。

## 8. 交給後續閘的既有內容發現（本輪不修，Mode C 無權限）

1. **【最重要】Theorem 6.5 與 Theorem 8.2 證明的跨章矛盾**（第 3 份盲測提出，我已逐字驗證兩章原文）：
   `ch06/sec-6-4.html` 的 **Theorem 6.5（Net Change Theorem）** 只假設「\(F'\) 在 \([a,b]\) 連續」，而該節給它的證成是一句
   「applies **verbatim** from Theorem 6.4」；但 `ch08/sec-8-1.html` 的 **Theorem 8.2 證明**明說
   「Theorem 6.4 **cannot be cited directly**, because it asks for an antiderivative on an open interval larger than
   \([a,b]\)」，並花一整段用 FTC-1＋Cor 4.4 建構 \(H\)。**兩者不能同時成立**：若 Thm 6.4 真需開區間，
   Thm 6.5 的「verbatim」就是超額宣稱（它缺的那一步正是 §8.1 做的建構）；若 Thm 6.5 站得住，§8.1 大可一行引用它。
   判讀：**§8.1 是嚴謹的一邊，§6.4 的「verbatim」是超額宣稱。** 不在 M4 權限內（跨章、動既有證明），
   且 Ch6 已定版（含 LaTeX 出版線）→ **交數學 gate-2**（PIPELINE 排在 M4 後、M5 前）由第二個模型獨立判過再決定是否動 Ch6。
2. **§8.4 把 Prop A.7 的模板與 cover-up 整個外包給 Appendix A.4** → **模板側已於 2026-07-27 補上
   就地 bridge（使用者裁決），見 §9；求常數側與 cover-up 一詞仍未處理，見本節第 6 條。** 原始判讀：
   3 份盲測中 2 份列為全章最該修的一項
   （其一稱「換個讀者就會變 blocking」），第 3 份明確判**不算 B 類違規**（每個例題都把自己的模板寫出來了）。
   合計仍是 **0 B 類違規**，難度閘 PASS 不受影響。若要補「從因式分解怎麼寫出模板」的就地 bridge，
   屬**新的 Mode C 增補**，不在本輪使用者裁決的清單內，未自行加入。
3. **§8.3 節末 summary 的壓縮**：「With completing the square, the method reaches any \(\sqrt{px^2+qx+r}\)」
   未計入本輪補上的「前導係數要先提出來」那一步。既有 Mode A 內容，Mode C 不得重構，交 gate-2。
4. **§8.4 不可約判準口徑（升級：現累計 3 份盲測命中，且會讓讀者得出相反結論）**：Strategy 8.5
   step 2 與節末 Caution 都只寫首一形式「\(x^2+px+q\) is irreducible exactly when \(p^2<4q\)」，
   Ex 8.21 卻對非首一的 \(4x^2-4x+3\) 改用一般判別式 \((-4)^2-4\cdot4\cdot3<0\)。**2026-07-27 的
   scoped §8.4 盲測示範了實害**：讀者照 Strategy 8.5 背下的規則代入 \(p=-4,q=3\) 得 \(16<12\) 不成立
   → 結論「可分解」，與課文**相反**；且課文從未提醒該式僅適用首一二次式，Caution 末句
   「When in doubt, compute the discriminant first」等於在同一頁混用兩種形式。既有內容，交 gate-2。
5. **§8.4「方法必成功」與 case IV 刻意省略的正面衝突（M4 後續輪新發現，且我方增補提高了它的暴露度）**：
   三處無條件宣稱——L41「For rational integrands … **the method always succeeds**」、L49 FTA Caution
   「**everything else in the section is proved or computed in full**」、L241 收尾「Strategy 8.5's four
   steps … **always terminate**, and the only borrowed ingredient is the factorization fact」，
   以及 Strategy 8.5 step 4 本身也是無條件寫的——對上 L184 的「this book **leaves that case as
   stated**」（重根不可約二次式）。scoped 盲測具體示範：拿到 \((x^2+4)^2\) 它能寫模板、能求常數、
   能積前五個碎片，**第六個積不出來**。**注意**：2026-07-27 補的模板 bridge 讓 case IV 的模板首次
   「寫得出來」，因此把這個既有衝突從「讀者碰不到」變成「讀者會撞上」；bridge 已在自己那句就地補上
   scope 註記（與 L184 同性質、非新 credit）作為緩解，但三處無條件宣稱本身是既有 Mode A 內容，
   Mode C 不得重構，交 gate-2 定奪。
6. **§8.4 求常數無就地規則、cover-up 一詞未解釋**：兩度外包給 Strategy A.2，讀者只能從
   Ex 8.18/8.19/8.20 反推；*cover-up* 在本節出現三次卻從未說明它為何叫 cover-up（課文示範的動作是
   「通分後代入各因式的根」，並沒有「掩蓋」任何東西）。scoped 盲測不判 blocking（三個例題把整套
   動作做完了），但依 §16.2 字面是否算「就地建立」該盲測自陳判斷不了。與已補的模板 bridge 是
   **相鄰但不同**的缺口，未在本輪裁決範圍內；記為 PLAN open question #6。
7. **§8.7 Ex 8.35／8.36 兩次以「the bounds below」解釋當下現象**，而 Thm 8.4 尚未登場；2 份盲測列為 slowdown。既有內容。
8. **§8.6 Ex 8.31 引 Theorem 6.2 part 4 反駁自己**，但 Thm 6.2 的前提是連續性，而該例壞掉的正是連續性
   （課文下一句「The error is upstream」有救回）。scoped 盲測提出，屬 smell-test 的自我踩線，交 gate-2。
9. **Strategy 編號比其所在節號多一**（Strategy 8.4 在 §8.3、8.5 在 §8.4、8.6 在 §8.5）：4 份盲測都因此翻錯頁。

## 9. M4 後續輪 — §8.4 部分分式模板的就地 bridge（2026-07-27，使用者裁決後追加）

上節第 2 條的模板側。使用者於 M5 收尾時裁決「補那段 bridge」，遂以一段
`expansion:intuition [pass: enrichment]` 落在 (8.A) 之後、「With (8.A) in hand…」之前。

**內容**：就地陳述 Prop A.7 的模板規則（因式 → 該配哪些 fragment，四種情形），用本章記號 \(r,k\)
（附錄用 \(a,m\)；\(a\) 在本節已被 (8.A) 佔為 arctan 尺度參數，沿用會當場撞車）。
**刻意不做**：不重教存在性／唯一性（留 §A.4）、不教求常數（留 Strategy A.2／Strategy 8.5 step 3）、
不重教 cover-up。`sec-8-4.html` header 的 SEAM GUARD 依 **8.6-B1 先例**同批修訂：原「Prop A.7 …
imported by cross-ref + one-line recall, NOT re-taught」在 M1 被讀成「完全不必就地陳述模板形式」，
而 CONTENT_SPEC §16.2 的處置慣例是「就地保留最短 bridge 並 cross-ref 附錄，**不因附錄存在而省去**」；
guard 修訂後仍完整保護它真正要保護的（why 與常數兩層）。

**scoped 盲測（設定：讀者沒讀過附錄）— 0 blocking／6 slowdown，難度 4/5**（讀者自陳其中約一半來自
「沒讀過附錄」的設定，讀過的話給 3/5；前三份全章盲測給 §8.4 的是 3／3.5／3）。
**驗收命中**：理解測驗要它對新分母 \((x-2)^3(x^2+1)(x^2+4)^2\) 寫模板，它完整寫出並指認
「**課文直接給的**，就是這一段」，不再是從 Ex 8.18/8.19/8.20 反推——這正是原缺口的定義。

**盲測驅動的修補（含我方自查）**：
- 通則句「numerator sits one degree below its own **denominator**」對 \(A_2/(x-r)^2\) **字面為假**
  （分母二次、分子零次）。我自查先修為「below that of the **factor it sits over**」；盲測獨立指出
  同一條並給出**逐字相同**的正確說法（「比那個因式本身低一次」）。
- 同類殘留「the numerator now linear because the **denominator** is quadratic」→ 改 `factor`。
- 模板只寫 \(x-r\)，Ex 8.18 卻用 \(\frac{B}{2x-1}\)，讀者停頓 → 補一句非首一線性因式同樣處理。
- 我寫的「those are **the next step**」讓讀者期待下一段講求常數，但下一段講積分 → 改為精確指向
  Strategy 8.5 step 3。
- §8.3 我在 M4 寫的「such as \(u=2x\) … as in Example 8.21」與該例實際用的 \(u=2x-1\) 不符 → 改寫。
- **主動加的 scope 子句**：bridge 讓 case IV 的模板首次「寫得出來」，於是把上節第 5 條的既有衝突
  從「讀者碰不到」變成「讀者會撞上」；在 bridge 自己那句就地補 scope 註記（與 L184 同性質、非新 credit）。

**scoped Mode B（第一輪）：0 blocking／5 advisory 全採**——通則句仍有「factor＝\(x-r\) 或 \((x-r)^k\)」
的歧義（還原 Prop A.7 的兩項 gloss 修正）；「**every example** … carries that step out in full」是可查核的
過度宣稱（Ex 8.17／8.21／8.22 都沒完整做 step 3）→ 改「Examples 8.18 through 8.20」；31 詞＋分號黏住
Case III 與 Case IV 且 \((x^2+px+q)^k\) 從未寫在紙上 → 拆句並寫出該形式；`fixes` 撞書內既有的
「固定住」義 → `determines`；**既有句因插入而失效**——「Before the fragments can be **listed**」插入後
指向一段完全沒用到 (8.A) 的文字 → 一詞修為 `integrated`（清理自己造成的破壞，非重構）。
新段分號由 3 降回 1，章層分號 47→45。

**回歸複核（第二輪，對重寫版）：0 blocking／2 tighten／1 voice** — 三條全採。
① 通則句尾的 gloss「a linear \(Bx+C\) over a **quadratic**」未加限定，而 \((x-r)^2\) 字面上也是 quadratic，
留了最後一條側路 → 加 **irreducible**（這是對 Prop A.7 的嚴格細化，A.7 的 bullet 本就只把 \(Bx+C\) 配給
irreducible）；順手把「the power **that factor** is raised to」改為「the power **it** is raised to」，
免除 *that* 被先讀成關係代詞的 garden-path。② 31 詞句把**物件層規則**（case IV 模板）與**書層 scope 聲明**
黏在同一句 → 拆為兩句。③〔voice〕開場補導航「Once the denominator is factored, …」（factoring 的討論隔了
(8.A) 一段），並把「its rule」拆成獨立短句以免同句內 it／its 指向兩個不同先行詞。

**該輪逐一驗證且值得記下的兩點**：(a) 歧義**確實歸零**——複核者拿 \(A_2/(x-r)^2\) 與
\((Bx+C)/(x^2+px+q)^k\) 逐一套新句，兩條推理路徑同結論，舊句可推出的「分母二次⇒分子一次」已被字面封死；
(b) 新加的 scope 子句**不逾越**——不是新 credit（未主張任何未證命題，只是覆蓋範圍揭示，性質同 L184）、
不是新 fence、與 L184 一致且相隔約 120 行功能不同，故章層「恰兩筆 credit」的口徑不變。
另確認 `listed`→`integrated` 後依賴鏈成 A–B–A′：L56 立承諾 → (8.A) 交付 → bridge 回答另一個問題
（有哪些碎片，不消費 (8.A)）→ L64「With (8.A) in hand, every fragment shape…」兌現承諾，且**正好量化
bridge 剛列出的那組形狀**（沒有 bridge 時「every fragment shape」是欠指定的）。

**終值**：build ✔／quote_lint clean ×7／linebreak 0／prose **N=10651、em-dash 仍 0.0/1000**（章層分號 45、
冒號 134）／render **math 1389、MathJax err 0、未渲染 `\(` 0、Example 連續 8.1–8.38、13/13 圖、
cross-ref dangling 0、渲染後散文 em-dash 0**。**三輪散文閘（首輪＋兩輪回歸）blocking 全 0。**
   結構性、無法在本輪處理，記錄備查。
