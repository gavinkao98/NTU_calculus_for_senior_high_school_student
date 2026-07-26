# §8.7 Approximate Integration — Codex ⑤ audit record (raw JSON gitignored)

2026-07-26. gpt-5.6-terra／max, read-only, output-schema, post-generation batch. Heaviest finding
load of the batch (5 blocking) — all in claim-precision and mandated-derivation coverage, none in
the rules' or examples' arithmetic.

## Round 1 — 5 blocking, 0 advisory

- **[8.7-B1｜math｜BLOCKING]** "their average cancels most of both errors" was an unconditional
  overclaim (the average need not beat either endpoint rule in general). **Fix**: honest
  bracketing statement — for a monotone integrand the integral lies between \(L_n\) and \(R_n\),
  \(T_n\) is the bracket's midpoint, so \(|E_T|\) ≤ half the bracket width.
- **[8.7-B2｜math｜BLOCKING]** Ex 8.33/8.34 closers implied Thm 8.4 *guarantees* the observed
  sign/ratio pattern and that doubling \(n\) divides the actual errors by 4/16. The bounds
  control magnitudes only. **Fix**: both closers now speak of the bounds' constants and
  \(1/n^2\)-vs-\(1/n^4\) scales, with the magnitude-only caveat explicit.
- **[8.7-B3｜math｜BLOCKING]** Ex 8.35 wrote the thresholds as "n ≥ 40.9"/"n ≥ 28.9", which are
  not equivalent to the preceding inequalities (\(\sqrt{10^4/6}=40.824…\),
  \(\sqrt{10^4/12}=28.867…\)). **Fix**: exact forms \(n \ge \sqrt{10^4/6} \approx 40.82\) /
  \(\approx 28.87\); integer conclusions 41/29 unchanged (and were correct).
- **[8.7-B4｜direction-conformance｜BLOCKING]** brief/PLAN mandated BOTH trapezoid derivations
  with a display each; the averaging route was only asserted inline. **Fix**: termwise-average
  display \(\tfrac12(L_n+R_n) = \tfrac h2[y_0+2y_1+\cdots+2y_{n-1}+y_n] = T_n\) added.
- **[8.7-B5｜direction-conformance｜BLOCKING]** brief specified the ≈42 km/h sanity line in
  Ex 8.36; draft gave only 11.7 m/s. **Fix**: "or 42 km/h" added.

Auditor-verified clean: (M)/(T)/(S) formulas; Simpson three-point lemma proof + shift argument +
weight assembly + even-\(n\) caution; Thm 8.4 statement with C²/C⁴ hypotheses and EVT-existence
clause; the fence caution (second credit, → Ch11); Ex 8.33/8.34/8.35/8.36 arithmetic (values
match to 6 dp); chapter summary's claims.

## Round 2 (scoped regression) — see `ch08_chapter-sweep-audit.md` §regression

**Status: §8.7 ⑤ CLOSED — 0 blocking after repair + regression.**
