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
2. **§8.4 把 Prop A.7 的模板與 cover-up 整個外包給 Appendix A.4**：3 份盲測中 2 份列為全章最該修的一項
   （其一稱「換個讀者就會變 blocking」），第 3 份明確判**不算 B 類違規**（每個例題都把自己的模板寫出來了）。
   合計仍是 **0 B 類違規**，難度閘 PASS 不受影響。若要補「從因式分解怎麼寫出模板」的就地 bridge，
   屬**新的 Mode C 增補**，不在本輪使用者裁決的清單內，未自行加入。
3. **§8.3 節末 summary 的壓縮**：「With completing the square, the method reaches any \(\sqrt{px^2+qx+r}\)」
   未計入本輪補上的「前導係數要先提出來」那一步。既有 Mode A 內容，Mode C 不得重構，交 gate-2。
4. **§8.4 不可約判準口徑**：Strategy 8.5 step 2 與節末 Caution 用首一形式 \(p^2<4q\)，Ex 8.21 對
   \(4x^2-4x+3\) 改用一般判別式。3 份盲測有 2 份提出。既有內容，交 gate-2。
5. **§8.7 Ex 8.35／8.36 兩次以「the bounds below」解釋當下現象**，而 Thm 8.4 尚未登場；2 份盲測列為 slowdown。既有內容。
6. **§8.6 Ex 8.31 引 Theorem 6.2 part 4 反駁自己**，但 Thm 6.2 的前提是連續性，而該例壞掉的正是連續性
   （課文下一句「The error is upstream」有救回）。scoped 盲測提出，屬 smell-test 的自我踩線，交 gate-2。
7. **Strategy 編號比其所在節號多一**（Strategy 8.4 在 §8.3、8.5 在 §8.4、8.6 在 §8.5）：3 份盲測都因此翻錯頁。
   結構性、無法在本輪處理，記錄備查。
