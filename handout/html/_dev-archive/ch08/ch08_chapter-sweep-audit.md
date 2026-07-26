# Ch8 M1 chapter-closing sweep — audit record (raw JSON gitignored)

2026-07-26. Codex gpt-5.6-terra／max, `codex exec -s read-only`, output-schema. Batch order per
kickoff v3: whole-chapter generation → free gates → **⑤ ×7 (post-generation batch) → chapter
review (M1–M8 explicit) → repairs → one scoped regression call**. Session grant: user authorized
standing Codex calls for this conversation + delegated 拍板 (recorded in PLAN-ch08 §Workflow).

## Mechanical sweep terminal values (post-repair)

build ✔ · quote_lint clean ×7 (78 ASCII quotes auto-fixed then re-verified) · linebreak-gate
**0** auto-breaks (13 wide displays hand-broken at first check; +1 new display in the 8.7-B4
repair re-verified 0) · render **math=979 → re-render after repairs: see applied report**,
katex-errors=0 · **sympy 65/65 PASS** (36 examples + Prop 8.1 ×4 + (8.A) + p-test branches +
Simpson lemma + shell–washer increasing instance \(f=x^2\) → \(\pi/2\)) · ledger continuous
(Def ×2／Thm ×4／Prop ×2／Strategy ×6／Ex 8.1–8.36) · cross-refs 48 used, 0 dangling ·
figure-opportunity markers ×9 · expansion markers ×21 · prose N=8002, em-dash **0.0/1000**.

## Chapter-level Codex review — M1–M8 explicit (per PIPELINE M1「不可只稱已吸收」)

| 維 | verdict |
|---|---|
| M1 定義 | clean — Def 8.1/8.2 domains, truncation limits, finiteness, separate-half requirements correct |
| M2 定理陳述 | clean — Thm 8.1–8.4, Prop 8.1–8.2 hypotheses adequate, conclusions correct |
| M3 邏輯結構 | clean — quantifiers, split conditions, comparison contraposition sound |
| M4 推導計算 | clean at chapter scope (per-example recomputation ran in the ⑤ batch + sympy) |
| M5 邊界域 | clean — ln domains, θ-ranges, improper endpoints, components, even-n consistent |
| M6 記號 | clean — u/w/θ usage and C/C₁ conventions stable across sections |
| M7 跨節一致 | **1 blocking CH-B1**（＝⑤ 8.1-B1，shell–washer seam vs Ex 7.12）→ repaired（見下）；其餘 intra-Ch8 引用、Strategy 8.1–8.6、Prop 8.1、tags (8.A)/(M)/(T)/(S) 全解析 |
| M8 隱性前提 | clean — no unstated prerequisite makes a chapter claim unsound |
| Ledger | clean — continuous, matches PLAN, no unledgered mint |
| Credit audit | clean — **exactly two** fenced credits (§8.4 FTA; §8.7 Thm 8.4); §8.5 = scope statement; Comparison proof fully mainline |
| Seams/structure | clean — §6.5／§6.2 header／§A.5／§6.4 promises discharged; Ch11 §11.3 export stated; opener + summary meet SPEC §4 |

## Batch findings roll-up (⑤ ×7 + chapter review)

**15 blocking + 3 advisory** total: §8.1 1B+1A · §8.2 3B · §8.3 1B+1A · §8.4 1B · §8.5 1B ·
§8.6 2B · §8.7 5B · chapter 1B (= §8.1's, same root). Adjudications: **13 repaired in fragments**
(loci in the per-section records `ch08_s8-N-codex5-audit.md`); **2 adjudicated as defects in the
governing documents, documents amended with inline notes** (8.5-B1: brief-8-5's step-2 label was
wrong, draft correct; 8.6-B1: PLAN §8.6 guard over-specified the order, as-built canon-standard
structure kept). All 3 advisory applied (8.1-A1 proof-route rewrite; 8.3-A1 two bridge clauses;
chapter review had 0 advisory).

The two adjudicated-in-document findings are the delegated-拍板 calls of this session; the user
can reverse either by reverting the document amendment and requesting the corresponding
fragment restructure.

## Round 2 — scoped regression (one call, R1–R15 over every repair)

**Verdict (verbatim): "clean" — 0 blocking／0 advisory；R1–R15 每項逐一 "clean"＋"Overall
regression verdict: clean".** Auditor confirmed per item: R1 the increasing-case algebra, slice
description, continuity-suffices claim, and the \(\pi/2\) match to Ex 7.12; R2 the FTC-1＋Cor 4.4
proof's citations all met; R3–R15 each repair resolves its finding with no new defect.
Post-regression mechanical terminal values: build ✔ · quote_lint clean ×7 · linebreak 0 ·
render **math=1007／katex-errors=0** · sympy **65/65** · prose N=8002, em-dash 0.0/1000.

## Usage

Codex calls this round: ③ ×1 + ⑤ ×7 + chapter review ×1 + regression ×1 = **10 calls**,
wall-clock 18:04–19:46 for the 8-call batch (7–10 min/call) + ③ + regression; est. total
~1.2–1.5M tokens (per-call ~120–150k; cf. Ch7 M1 = 1.41M/9 calls). All `codex exec -s read-only`
under the session grant; raw JSON in gitignored scratchpad, adjudications transcribed here.

**Status: M1 closing sweep CLOSED — chapter at 0 blocking across ⑤ ×7 ＋ chapter review ＋
scoped regression（R1–R15 全 clean）.**
