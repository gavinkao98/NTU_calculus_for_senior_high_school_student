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

**套用 69 個編輯點**（必修 1＋客觀 advisory＋6 句導航暖；全散文層、不動數學、不動教學順序、
未新增任何 em-dash）。大類：F3 garden-path／誤掛 ×12、F4 兩動作句與 ≥150 詞段落切分 ×9（含
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

① 乾淨盲測 sim ×1（重修最重三節 §8.1／§8.6／§8.7）＋② 散文 scoped 複核 ×1
（69 個修補句逐點驗無新缺陷）。判決：

> **盲測回歸（sim，2026-07-26）：VERDICT 0 blocking／0 stuck／0 B 類**。三節總判定全 ok，
> 難度 §8.1=3、§8.6=3、§8.7=2.5（尖峰＝Thm 8.3 證明局部 4，被預告＋分段＋Fig 8.9 撐住），
> 「與 Ch1–Ch4 基線相比持平偏低……全程無需外援」。4 條 slowdown 全落在 gate-1 已知重段
> （Thm 8.2 證明、shell–washer 小節、Thm 8.3 證明、Fig 8.12 切線論證——末者屬 enrichment
> 可跳過），且 sim 逐字引用本輪新補的導航句（「Theorem 6.4 cannot be cited directly…」、
> 「since Theorem 4.1's monotone principle speaks of sequences」）並判「行內有給理由，
> 走得完」「取樣的理由有講清楚」——共識修補確認生效，無新卡點。
> **散文複核（scoped，2026-07-26）：0 blocking——「整章 prose gate 回歸通過」**；69 修補句
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

## 產物

`_audit/REVIEW-ch08-prose-difficulty.html`（合併裁決稿：盲測表＋必修＋逐節採用清單＋不採理由）。

**Status：M3 收案（2026-07-26）——69＋2 編輯點全落地、機械閘全綠、盲測回歸 0 stuck、
散文回歸 0 blocking。** 散文 gate-2（Codex S·A·V）依三閘規則待 M4 後批次。
