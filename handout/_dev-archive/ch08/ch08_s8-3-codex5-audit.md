# §8.3 Trigonometric Substitution — Codex ⑤ audit record (raw JSON gitignored)

2026-07-26. gpt-5.6-terra／max, read-only, output-schema, post-generation batch.

## Round 1 — 1 blocking, 1 advisory

- **[8.3-B1｜math｜BLOCKING]** The post-Ex-8.13 forward paragraph claimed the ellipse perimeter
  "resists the entire toolkit" — false in the example's own allowed case \(a=b=r\) (a circle, as
  the solution itself notes): there the arc length integrand reduces to \(r/\sqrt{r^2-x^2}\),
  which row 1 of Strategy 8.4 handles in one line. **Fix**: claim scoped to \(a\ne b\), circle
  exception stated with its one-line resolution; phrasing kept as a toolkit-scope statement (no
  nonexistence assertion — consistent with the ③ B-02 discipline).
- **[8.3-A1｜direction-conformance｜Advisory→applied]** Two brief-mandated bridges were missing:
  the lead-in's plain-u-sub check did not forward-reference Strategy 8.6 step 2, and no clause
  linked the deliberately-unworked \(\int\sqrt{x^2+a^2}\,dx\) path to Ex 8.10's \(\sec^3\).
  **Fix**: both added (lead-in sentence; new one-sentence paragraph after Ex 8.14).

Auditor-verified clean: Ex 8.12–8.16 recomputed (incl. component naming, sign resolutions,
triangle back-substitutions, completing-the-square domain \((-3,1)\)); Strategy 8.4 ranges;
inverse-substitution honesty paragraph; sec-branch caution incl. the \(x\le-a\) alternate range;
definite-limits caution; ellipse area \(\pi ab\) with Thm 6.7/6.8 citations.

## Round 2 (scoped regression) — see `ch08_chapter-sweep-audit.md` §regression

**Status: §8.3 ⑤ CLOSED — 0 blocking after repair + regression.**
