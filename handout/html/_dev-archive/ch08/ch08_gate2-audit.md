# ch08 三閘 gate-2 稽核紀錄（P5，2026-08-09）

> **這是什麼**：Ch8 定版前的三閘 gate-2（數學 M1–M8／散文 S·A·V／圖視覺 D1–D8）跨模型
> 獨立複核紀錄——**首個在 LaTeX 源上跑的 gate-2**（LaTeX 統一 U4/P5，
> [`../../../latex/KICKOFF-latex-unification.md`](../../../latex/KICKOFF-latex-unification.md)）。
> Ch8 自 2026-07-27 M5 收尾起帶 gate-2 債（PIPELINE dashboard「⚠️ 尚未定版」），本輪償清。
>
> **執行**：Codex `gpt-5.6-terra`／`max`（config 預設）、`codex exec -s read-only
> --output-schema`；輸入＝`latex/src/ch08/chapter8.tex` 全文 inline（126KB；PROSE rubric
> 工程坑：不讓模型自讀檔）＋既有發現 7 條（`ch08_modec-gapcheck-audit.md` §8）分派兩閘裁決；
> 圖閘 `-i` 餵 figkit harness 截的 13 張 2× PNG。raw 輸出落 scratchpad 不進版控，
> 本檔為轉錄（PIPELINE「findings 留版控」紀律）。

## 1. 數學 M1–M8 gate-2 — **1 blocking＋1 advisory；M1–M6 全 clean**

- **[Blocking] G2M-1（M7）§8.4** — 三處無條件宣稱（“the method always succeeds”／“everything else … proved or computed in full”／“Strategy 8.5's four steps … always terminate”）與同節明示的 case-IV 留白（“this book leaves that case as stated”＝重根不可約二次式無 reduction 示範）**章內直接矛盾**。＝既有發現 EF5 的獨立確認。修法二擇：把宣稱限定到實際發展的情形（qualify），或補 case-IV 推導。
- **[Advisory] G2M-2（M8）§8.6 Ex 8.31** — 引 “Theorem 6.2, part 4” 反駁錯誤計算，但該定理前提是連續性，此處被積函數正是不連續（\(1/x^2\) 跨 \([-1,3]\)）——引用局部不可用；周邊 improper-integral 論證正確（divergence 成立），缺陷限於該次引用。＝EF8 確認 advisory。
- clean dimensions：M1／M2／M3／M4／M5／M6。

## 2. 散文 S·A·V gate-2 — **0 blocking、0 新 finding；2 advisory＝既有發現確認**

- 無任何新 finding（gate-1 applied 後的散文與 M4 增補句乾淨）。
- EF7（§8.7 “the bounds below” 前引 Thm 8.4）確認 **advisory**：短暫未解懸念、不阻完成例題。
- EF9（Strategy 編號比節號超前）確認 **advisory**：全書「每型連續編號」慣例可留；建議引用處配描述性措辭（如 “the strategy below”）降低翻錯頁率。

## 3. 圖視覺 gate-2 — **13/13 全 clean（0 blocking／0 advisory）**

Figure 8.1–8.13（17 panel）逐圖判 D1–D8 全數乾淨；輸入＝figkit harness（`figs-ch08.html`）
經 `shot.mjs figures` 模式截的 2× PNG——**首次以 harness 為圖閘 render 載體的 gate-2**，
截圖品質經人眼抽驗（trig-sub-triangles：MathJax 標籤／panel note／caption 全渲染）。

## 4. 既有發現裁決（§8 的 EF1/EF3/EF4/EF5/EF8 → 數學閘；EF7/EF9 → 散文閘）

| # | gate-2 裁決 | 理由（轉錄） |
|---|---|---|
| EF1 Thm 6.5 “verbatim” 跨章矛盾 | **needs_user_decision** | Thm 8.2 正確且自足（FTC-1 建構 H、不依賴 Thm 6.4）；依 Ch6 現行措辭，“verbatim” 與 §8.1 指出的開區間要求**不相容**——衝突為真，修法屬已定版的 Ch6（含 LaTeX 線），交使用者 |
| EF3 §8.3 summary 壓縮 | not_a_defect | 前段已明說先提出 leading coefficient；summary 是可接受的能力宣稱壓縮 |
| EF4 §8.4 不可約判準口徑 | not_a_defect（數學層） | 判準明寫 monic 形式 \(x^2+px+q\)，\(4x^2-4x+3\) 不是該公式的合法輸入；Ex 8.21 正確用一般判別式——**無數學矛盾**。〔註：scoped 盲測示範過「讀者硬代非 monic 得反結論」的教學隱患——數學閘判 clean 不等於教學層無風險，裁決權留使用者〕 |
| EF5 §8.4 無條件宣稱 vs case-IV | **confirm_defect_blocking**（=G2M-1） | 章內直接矛盾（見 §1） |
| EF7 §8.7 bounds 前引 | confirm_defect_advisory | 見 §2 |
| EF8 §8.6 Ex 8.31 引 Thm 6.2 | confirm_defect_advisory（=G2M-2） | 見 §1 |
| EF9 Strategy 編號超前 | confirm_defect_advisory | 見 §2；慣例可留、引用措辭緩解 |

## 5. 修補與回歸（2026-08-09，使用者逐題裁決後落地）

使用者裁決：G2M-1＝**qualify 三處**（不補 case-IV 推導）；EF1＝**修 Ch6 那一句**；
G2M-2＝修；polish 三項（EF4／EF7／EF9）＝全修。落地九處：

| # | 檔 | 修法 |
|---|---|---|
| G2M-1a | ch08 §8.4 開場 | “the method always succeeds” → “…always succeeds **in producing the decomposition**, and every fragment it produces—except one, flagged where it arises—is then integrated in full” |
| G2M-1b | ch08 §8.4 FTA credit 段 | “everything else … proved or computed in full” 前加 “apart from the one fragment integral left as stated below (repeated irreducible quadratic factors)” |
| G2M-1c | ch08 §8.4 收尾 | “always terminate” → “always terminate **in every case this section carries out**”；borrowed ingredient 單數改複數、把 case-IV fragment integral 列為第二筆 |
| G2M-2 | ch08 §8.6 Ex 8.31 | 刪 “(Theorem 6.2, part 4)” 引用，改非形式陳述 “an integral that adds up positive values can never come out negative”（後續 improper 論證不動） |
| EF4 | ch08 §8.4 Caution | “compute the discriminant first” 後補 “—\(p^2-4q\) for the monic form above; for a general \(ax^2+bx+c\), factor out \(a\) first or use \(b^2-4ac\), as Example \ref{ex:8.21} does” |
| EF7×2 | ch08 §8.7 Ex 8.35／8.36 | “the (error) bounds below” → “the (error) bounds of Theorem \ref{thm:8.4} below” |
| EF9 | ch08 §8.5 Strategy 8.6 dispatch 行 | 跨節引用配位置：“Strategies … (both in §8.2)”、“Strategy … (§8.3)”（L787 同節已覆蓋、章末 summary 自帶 “Section 8.1” 語境，不另標） |
| EF1 | **ch06** §6.4 Thm 6.5 證成句 | “\(F\) is an antiderivative of \(F'\), so the theorem applies verbatim” → “…an antiderivative of \(F'\) on \([a,b]\). Strictly, Theorem \ref{thm:6.4} asks for an antiderivative on an open interval around \([a,b]\), and the one-step construction that closes this gap is carried out in the proof of Theorem 8.2 (§8.1)”——超額宣稱改如實描述＋指向 §8.1 的完整建構 |

**回歸**：ch08＋ch06 重編譯全綠（0 error／0 missing char／字形閘 PASS／log 0 undefined
reference＝全部 `\ref` 解析；ch06 既有 overfull 1 條為修句前即在的待裁項，非本輪引入）。
修補全屬措辭級（宣稱 qualify／引用替換／位置標記），不動任何計算與定理內容——sympy 重算
不適用。修補句逐條轉錄如上表供覆核（PIPELINE「修完必回歸」以手動比對＋編譯驗證形式執行）。

**三閘收斂**：數學 blocking 1→0（G2M-1 已修）、散文 0、圖 0 → **blocking 全歸零，Ch8 定版**。
