# Ch8 chapter-level direction gate ③ — Codex audit record (raw JSON gitignored)

2026-07-26. gpt-5.6-terra／max, `codex exec -s read-only`, output-schema, one round. Object =
PLAN-ch08.md (pre-draft). Session grant: user authorized standing Codex calls for this
conversation and delegated 拍板 to Claude-⇄-Codex convergence (user away; kickoff §0).

## Verdict: MODIFY — 2 blocking + 3 advisory; all 16 cross-reference claims VERIFIED

Codex confirmed sound as-planned: roster & Improper→Approximate order (no forward dependency),
numbering ledger, core imports, **Comparison-Theorem proof via Thm 4.1 integer-sequence
bracketing ("valid, fence-free, and appropriate here"; floor function already introduced in
Ch1)**, 36/38 example budget.

## Blocking (both adjudicated + fixed before drafting proceeded)

- **[B-01] D3 washer↔shell**: PLAN declined all washer–shell material in §8.1 while calling the
  Ch7 forward reference "authoritative" — but shipped **Ex 7.12** (post-M4 number; PLAN had cited
  stale "Ex 7.11") promises tools arriving "with integration by parts in Chapter 8 and change of
  variables in Chapter 15". Retaining the promise while adding nothing in Ch8 breaks the seam.
  Codex offered (a) scoped monotone-C¹ special-case proof in §8.1, or (b) backward edit to
  Ex 7.12 deferring wholly to Ch15. **Adjudication: (a)** — Ch7 is 定版 (three gate-2 passes);
  reopening a sealed chapter is the higher-risk repair, and the parts-based special case is
  instructive at §8.1's altitude. Executed as an unnumbered prose derivation (expansion:formula,
  new closing subsection of §8.1) under hypotheses: \(f\) strictly decreasing and smooth on
  \([a,b]\), \(0\le a\), \(f\ge 0\), with a smooth inverse \(g\) on \([f(b), f(a)]\); shell value
  transformed by parts (Thm 8.2) + substitution (Thm 6.7) into the washer value; general case
  explicitly left to Ch15. Zero new numbered objects (ledger unchanged). PLAN D3 + brief-8-1 +
  sec-8-1 updated; stale 7.11 → 7.12 corrected everywhere.
- **[B-02] §8.5 third credit**: PLAN declared "exactly two on-credit items" (FTA fact; error
  bounds) but §8.5 planned an on-credit *Liouville nonexistence* claim for
  \(\int e^{-x^2}\,dx\) — a third unproved credit with no proof-delivery destination.
  **Adjudication: adopt Codex's primary fix** — the mainline asserts only the honest scope
  statement (none of this chapter's techniques produces an elementary antiderivative; whether any
  exists is a question this book does not take up), pointing forward to §8.6 (convergence) and
  §8.7 (numerics). Two-credit budget stands. PLAN §8.5 row + guard rewritten.

## Advisory (all three adopted into PLAN/briefs)

- **[A-01] D5 hygiene**: added ledger line — trig-sub parameters positive (\(a>0\); ellipse
  \(a,b>0\)); each indefinite example solved on a named connected domain component; the
  \(x\le -a\) secant branch gets its alternate range \(\theta\in(\pi/2,\pi]\) (where
  \(\tan\theta\le 0\), \(\sqrt{x^2-a^2} = -a\tan\theta\)) or verification-by-differentiation,
  in the caution.
- **[A-02] D7 p-test**: explicit \(p\le 0\) branch — integrand continuous and \(\ge 1\) on
  \([1,\infty)\), so \(\int_1^t x^{-p}dx \ge t-1\) by comparison Thm 6.2(4) on finite intervals,
  hence divergence; \(0<p<1\) by the power computation; \(p=1\) by \(\ln\).
- **[A-03] D8 regularity**: Thm 8.4 states \(f''\) continuous on \([a,b]\) for T/M and
  \(f^{(4)}\) continuous for S (K/K₄ exist by EVT 4.9(a), "any bound" reading kept); rules
  defined with equal width \(h=(b-a)/n\); data-table example requires equally spaced readings +
  even \(n\) verified in-solution.

## Decision verdicts

D1 MODIFY (→B-02 fix; order + budget confirmed) · D2 ADOPT · D3 MODIFY (→B-01 fix) · D4 ADOPT ·
D5 MODIFY (→A-01) · D6 ADOPT · D7 MODIFY (→A-02; proof route confirmed) · D8 MODIFY (→A-03).

## Cross-reference check (16/16 VERIFIED)

Thm 2.6 product rule · Thm 6.4 FTC-2 · Thm 6.6/6.7 substitution · Thm 6.2(3)/(4)
additivity/comparison · Thm 4.1 monotone-bounded · Thm 5.5 L'Hôpital · Thm 4.9(a)/(b) EVT/IVT ·
Thm 4.14 (ln x)′ · Ex 3.16 arctan′ · Prop A.7 decomposition · Strategy A.2 constants · Prop A.2
product-to-sum · Prop A.1 Pythagorean companions · §A.5 completing-square closing ¶ with Chapter 8
promise · §6.4 ln|x| export · Thm 6.8 symmetric functions.

**Status: ③ CLOSED — PLAN-ch08 amended in place (D3/D5/D7/D8 + §8.5), drafting proceeds.**
