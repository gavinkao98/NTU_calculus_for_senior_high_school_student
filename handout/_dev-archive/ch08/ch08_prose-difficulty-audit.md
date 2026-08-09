# Ch8 M3 — 散文＋難度合一輪 audit record（gate-1＋裁決＋修補＋回歸）

2026-07-26。使用者指令「開 M3」；裁決點使用者親裁（AskUserQuestion）：**照建議套用**。
散文 gate-2（Codex S·A·V 複核）依「三閘 M4 後批次」規則不在本輪。

## gate-1 佈署

B 類先備 grep 機械預檢（PASS：csc/cot/sec→Def A.1、反三角→§1.2、ln→§6.4、積化和差→Prop A.2、
部分分式→§A.4 全數有就地 bridge；無冪次和／行列式／複數）→ **`handout-prose-audit` ×7**（U／
F／S·A·V／R 四維，S/A/V 掛 svc-exemplars 錨）＋ **`learner-sim` ×3 全章盲測**（§16.2 persona，
未預告難點）同批平行。

## 結果

- **散文：七節全部 0 blocking**（U、S/A、R 三類 blocking 皆零）。advisory 合計約 94 條
  （tighten 57／optional 30／voice 7），含 4 條節級 R-pass 旗（§8.4 figurative compression、
  §8.5、§8.6 程序性覆核已就地執行判仍可讀、§8.7 章總結漂移）。
- **盲測：3/3 全 0 stuck、0 B 類違規**。難度曲線（A/B/C）：尖峰 §8.3／§8.6 ≈3.5（局部 4）、
  全章主體 ≈3 檔、§8.5/§8.7 ≈2.5——**低於 Ch4 §4.2 的 4.5，「標準/計算」深度裁定成立、無弧線
  層異常**。三份共識 slowdown：§8.1 shell–washer 小節、§8.6 Thm 8.3「為何沿整數取樣」只隱含、
  §8.1 Thm 8.2 繞 H 路線未說理由——全數排入修補。正面觀察（sim B）：「引用＋就地重抄」紀律使
  讀者幾乎免翻附錄。
- **紅旗 1 條（列必修）**：G1-8.6-10——§8.6 兩處把「\(e^{-x^2}\) 無反導函數」寫成斷言，逾越
  ③ B-02 的 scope-statement 紀律（§8.5 刻意不主張不存在）。

## 裁決（使用者：照建議套用）與修補

**套用裁決項 66 條**（裁決稿 §3 逐節 10／6／8／10／11／12／9）**＋必修 1（2 loci）**，落地為
**96 處文字替換**（批次腳本 94＋2 處 anchor MISS 手補；下方回歸另加 2 處 ＝ 98）。全散文層、
不動數學、不動教學順序、未新增任何 em-dash。

> **口徑更正（2026-07-27）：** 本輪最初的紀錄與 commit `7bb9b37` 寫「69＋2 編輯點」，那是
> 壓縮前的粗估（修補腳本 docstring 亦自寫「~70」），與兩個可驗證口徑都對不上——裁決項＝66＋1、
> 文字替換＝96＋2。原因：上下文壓縮後沿用了摘要裡的估計值而未重推。下列大類分佈同屬重建的
> **估計**（合計 ≈70，係項級口徑），逐條權威清單以裁決稿 §3 表與修補腳本為準。

大類（估計，項級）：F3 garden-path／誤掛 ×12、F4 兩動作句與 ≥150 詞段落切分 ×9（含
§8.1 shell–washer 首段、§8.5 limits 段、Thm 8.2 證明句、Thm 8.3 MCT 句）、R1 不透明慣用語
×~25（workhorse／dividend／closer／size(v.)／pedantry／in series（撞 series 術語）／all the
way out／discipline+impropriety／reached its limit（撞 limit 術語）等）、R2 指涉 ×3（the
series→Chapter 11's infinite series 等）、R3 術語漂移 ×6（spend/save/donate 對齊、inner
block→inner function、stray→spare、deeper→darker、the elementary table→§6.4's、Strategy
8.3 具名）、U 補解釋 ×5（spared why、evaluation-bar 字面化、compensate→as Figure 8.12 shows、
component of the domain、**Thm 8.2 證明補「Theorem 6.4 cannot be cited directly…」句＋
Thm 8.3 證明補「since Theorem 4.1 speaks of sequences」句**＝三 sim 共識點）、sim 專項 ×4
（Ex 8.3 的 −2C₁ 吸收句、Ex 8.18/8.19/8.20 積分常數改 \(K\)（與分解常數 A,B,C 撞名）、Fig 8.1
caption 補 uv-plane、Figure 8.2 指句）、V1 導航暖 ×6（§8.5 四例過渡句、§8.6 opener 回收句、
§8.4 completing-square 橋句、§8.3 a>0 理由、Ex 8.3 選 u 理由、§8.7 章總結平實化 pass）。

**不採／延後（記錄）**：`recentred` 英式拼法 DEFER 書層 sweep（2026-07-11 既定：-re/-ll 單章
不逕改；§A.5 上游同拼）；Fig 8.8 caption 三連擬人 KEEP（字面錨在場、稽核自判合規）；§8.7
Thm 8.4 讀式導航句不加（Ex 8.34 已載尺度句）；voice tier-3 ×7 與 taste 級記錄不動；Strategy
8.3 step 3 雙路徑壓縮記錄不動（⑤ 修後版已兩句、稽核 clean、sim 判 minor 可重建）。

## 修後機械閘

build ✔ · quote_lint clean ×7 · linebreak-gate 0 · prose N=8189、**em-dash 仍 0 raw（0.0/1000）**、
tics 等比微增無轉嫁（colon 110／semi 37／paren 88／comma 65）。

## 回歸（scoped）

① 乾淨盲測 sim **×3 獨立實例**（重修最重三節 §8.1／§8.6／§8.7；裁決計畫 §5 要求「各補一份」
＝三份獨立實例）＋② 散文 scoped 複核 ×1（修補句逐點驗無新缺陷）。判決：

> **盲測回歸 A（sim，2026-07-26）：VERDICT 0 blocking／0 stuck／0 B 類**。三節總判定全 ok，
> 難度 §8.1=3、§8.6=3、§8.7=2.5（尖峰＝Thm 8.3 證明局部 4，被預告＋分段＋Fig 8.9 撐住），
> 「與 Ch1–Ch4 基線相比持平偏低……全程無需外援」。4 條 slowdown 全落在 gate-1 已知重段
> （Thm 8.2 證明、shell–washer 小節、Thm 8.3 證明、Fig 8.12 切線論證——末者屬 enrichment
> 可跳過），且 sim 逐字引用本輪新補的導航句（「Theorem 6.4 cannot be cited directly…」、
> 「since Theorem 4.1's monotone principle speaks of sequences」）並判「行內有給理由，
> 走得完」「取樣的理由有講清楚」——共識修補確認生效，無新卡點。
>
> **盲測回歸 B（2026-07-27，獨立實例）：0 blocking／13 slowdown／8 minor**；三節 ok–effortful，
> 難度 §8.1=3.5、§8.6=3、§8.7=2.5；局部尖峰 shell–washer ≈4.5、Thm 8.2 證明 ≈4、Thm 8.3
> 證明 ≈4；判「整體持平偏低……唯一觸及 §4.2 尖峰量級的是 shell–washer 小節，但它是課文自陳的
> by-product、後文不承重」。加分觀察：「每一個裁決都追得到來源……沒有出現一次 obviously」。
> **盲測回歸 C（2026-07-27，獨立實例）：0 blocking／7 slowdown／9 minor**；難度 §8.1=3.5、
> §8.6=3.5、§8.7=3.0，判「持平——略高於 Ch1–3、明顯低於 Ch4 與其尖峰 §4.2」。
>
> 〔實例數補正：2026-07-26 當日只跑了 1 份涵蓋三節的 sim，與計畫「三節各補一份」的三份獨立
> 實例不符（上下文壓縮後的執行落差）；B、C 兩份於 2026-07-27 補派，同 scope、同盲測協定、
> 互不知情。**三份合計：0 blocking／0 stuck／0 B 類——gate 判定不變（PASS）。**〕
>
> **散文複核（scoped，2026-07-26）：0 blocking——「整章 prose gate 回歸通過」**；修補句
> 「未引入任何新 garden-path、語意漂移、量詞/條件拆散或與鄰句失聯」，B-02 兩處＋§8.5
> boundary 段確認已無「不存在」斷言。殘項 3：1 tighten（§8.5 新過渡句 from–through 介係詞
> 誤 chunk）＋2 optional（§8.3 "elementary antiderivative" 孤例未定義準術語、與 B-02 拼寫形
> 跨節不一致；§8.4 K 首用宣告——複核自判**非 finding**、K 槽位自明）。

**殘項處置（裁決權限內小輪）**：採 2／記錄不動 1——§8.5 改「We now run the opening's four
integrals through the strategy, in order.」、§8.3 改「…whose antiderivative is built from
the functions we have named」（對齊 §8.5/§8.6 的 B-02 scope 形），兩處均**逐字採複核者自建議
措辭**（回歸＝手動比對確認 1:1，符合「Codex 或手動比對均可」規則）；§8.4 K 記錄不動（加宣告
句反增雜訊，sim 亦無此卡點）。修後機械閘複跑：build ✔ · quote_lint clean · linebreak 0 ·
**em-dash 仍 0.0/1000**（N=8193、tics 不變）。

### 補測新發現的 7 條客觀缺陷（使用者親裁「7 條全修」，2026-07-27）

單一實例漏掉、兩獨立實例才浮現的項；逐條回檔驗證屬實後修補（全散文層、不動數學、未新增
em-dash；性質為「把隱含步驟寫出來」與「消除撞義用詞」）：

| # | locus | 共識 | 缺陷（已驗證） | 修法 |
|---|-------|------|----------------|------|
| 1 | §8.7 Ex 8.33 收尾 | 2/3（兩位都以為書寫錯） | 「the midpoint bound's constant is **half** the trapezoidal bound's」與同節 Ex 8.35「the constant \(24\)」撞義——在後者口徑下該句讀起來為假 | 改為「has \(24\) in its denominator where the trapezoidal bound has \(12\), making it half the size」 |
| 2 | §8.6 Thm 8.3 證明 | 2/3 | 「the monotone convergence theorem (Theorem 4.1)」是**未宣告的別名**：Thm 4.1 全書正名 *Completeness of the real numbers*，該別名僅此一處（R3） | 改為「so by Theorem 4.1 …」（同段前句已說明其為數列原理） |
| 3 | §8.1 shell–washer | 3/3 鄰域 | \(f(x)\ge y \Leftrightarrow x\ge g(y)\) 用到嚴格遞增卻未明說（U3） | 補「and since \(f\) is strictly increasing this says exactly that \(x \ge g(y)\)」 |
| 4 | §8.1 同小節收尾 | 2/3 | 「which is the same number」略過關鍵抵消 | 補「since \(b^{2}c + b^{2}(d-c) = b^{2}d\)」 |
| 5 | §8.7 Simpson 拼裝句 | 2/3 | \(i\) 未給範圍，權重 1,4,2,…,4,1 要讀者自推 | 補「for \(i = 1, 3, \dots, n-1\)」 |
| 6 | §8.1 Thm 8.2 證明首句 | 2/3 | 前文剛說「hypotheses match those of the Fundamental Theorem」，證明首句即說 6.4 不能引——轉折未承認，讀者付的是「懷疑自己讀錯」的成本 | 首句改「**Even with these hypotheses,** Theorem 6.4 cannot be cited directly…」 |
| 7 | §8.1 章開場 | 1/3 但可查證 | 「the **one** differentiation rule we have not yet run backwards」不成立：Thm 2.7 商法則亦為具名微分法則且全書從未倒著跑 | 去唯一性宣稱：「the *product rule*, a rule we have not yet run backwards」 |

**駁回（非 finding）**：兩位都提「正文很少指到圖」（§8.6 五圖零指涉）——查 ch07＝23 圖／0 次
正文指涉、ch05＝11／1，屬本書既有慣例，不動（CLAUDE.md review 四級之④）。
**記錄不動（低共識或結構性）**：§8.1 shell–washer 假設句五條件一句、Thm 6.7 模板的 \(f,g\)
與本小節角色對調、§8.6 「cannot overshoot」缺「固定正距離」半步、§8.6 Def 8.1(c) 分割點
無關性壓縮句、§8.6 Prop 8.2 的 \(p\le 0\) 雙重論證、Ex 8.28 §1.2 未明寫 \(y=\pi/2\)、
Fig 8.1 caption 只涵蓋原點特例——全部 1–2/3 且三位皆自力通過，留 M4 一併衡量。

**7 修的 scoped 複核（2026-07-27）：0 blocking**——「此 7 處修補本身乾淨，未引入新的 garden-path、
語意漂移、量詞／條件拆散或跨句失聯，scoped 複核通過 gate 1」。3 條 advisory 全落在剛改的三句
自身，依同一「客觀缺陷全修」標準逐字採複核者措辭補上：

- **G1-3R-1（F4，§8.1 L262）**：補單調性後全句 ~53 詞、兩分號、三獨立子句，且 `this` 先行詞
  可再明確 → 切為三句、`this`→`that condition`。
- **G1-3R-2（F3，§8.7 L67）**：尾掛分詞 `making it half the size` 的 `it` 最近 NP 是
  trapezoidal bound／\(12\)，**誤讀方向恰與事實相反** → 改 `which makes the midpoint bound
  half the size.` 並斷句。（複核同時確認：24／12 與 Thm 8.4 顯示式逐字對得上、與 Ex 8.35 的
  `constant` 撞義已消解。）
- **G1-3R-3（R3/R1，§8.7 L83）**：同句先 `triples`（節點三元組）後 `each pair`（切片對）、
  `the totals assemble into` 主語無先行詞 → `each pair of slices` ／ `an interior
  even-indexed node` ／ `the sum of all the contributions is`。

回歸＝三處與複核建議手動 1:1 比對相符。終值機械閘：build ✔ · quote_lint clean · linebreak 0 ·
N=8214、**em-dash 仍 0 raw（0.0/1000）**、tics colon 110／semi 35／paren 87／comma 66
（分號因兩處斷句淨減 2）。

## 產物

`_audit/REVIEW-ch08-prose-difficulty.html`（合併裁決稿：盲測表＋必修＋逐節採用清單＋不採理由）。

**Status：M3 收案（2026-07-26 主體；2026-07-27 補正輪）——66 裁決項＋必修 1（＝96 處替換）
＋回歸殘項 2＋補測 7 修＋複核 3 修全落地（合計 108 處文字替換）、機械閘全綠（N=8214、
em-dash 0.0/1000）、盲測 ×3 獨立實例 0 blocking／0 stuck／0 B 類、散文複核 ×3 0 blocking。** 散文 gate-2（Codex S·A·V）依三閘規則待 M4 後批次。
