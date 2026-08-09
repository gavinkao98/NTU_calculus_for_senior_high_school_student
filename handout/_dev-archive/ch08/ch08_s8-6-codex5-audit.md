# §8.6 Improper Integrals — Codex ⑤ audit record (raw JSON gitignored)

2026-07-26. gpt-5.6-terra／max, read-only, output-schema, post-generation batch.

## Round 1 — 2 blocking, 0 advisory

- **[8.6-B1｜direction-conformance｜BLOCKING → adjudicated as a PLAN-guard over-specification]**
  PLAN's §8.6 seam guard said "Definitions FIRST (both types), then computation examples"; the
  draft interleaves (Def 8.1 → Ex 8.27–8.29 + caution → Def 8.2 → Ex 8.30–8.31 …). The guard's
  *intent* — no example before its governing definition — holds in the as-built structure, which
  is also the canon-standard (Stewart) per-type-block order and reads better. **Adjudication
  (delegated 拍板): PLAN guard amended** to the per-type-block wording with an inline
  adjudication note; fragment unchanged. Every example verified to follow the definition it
  depends on.
- **[8.6-B2｜math｜BLOCKING]** Opener attributed "continuous integrand" as a standing assumption
  of Definition 6.2 — false to the shipped ch06 text (Def 6.2 assumes only \(f\) defined on
  \([a,b]\); Thm 6.1 moreover covers bounded integrands with finitely many discontinuities), an
  M7 misattribution. **Fix**: opener rewritten — Def 6.2 credited with the bounded-interval
  Riemann-sum construction, Thm 6.1 with convergence for the continuous integrands this book
  evaluates.

Auditor-verified clean: Def 8.1/8.2 statements (incl. split-point independence sentence);
Prop 8.2 proof all branches (p&gt;1, p=1, p&lt;1, explicit p≤0); **Thm 8.3 Comparison proof
verified sound** (monotonicity via 6.2(3)/(4); increasing-below-limit argument; Thm 4.1 sequence;
⌊t−a⌋ bracketing); Ex 8.27–8.32 recomputed; both cautions; combined-type paragraph; Ch11 §11.3
export clause.

## Round 2 (scoped regression) — see `ch08_chapter-sweep-audit.md` §regression

**Status: §8.6 ⑤ CLOSED — 0 blocking after repair/adjudication + regression.**
