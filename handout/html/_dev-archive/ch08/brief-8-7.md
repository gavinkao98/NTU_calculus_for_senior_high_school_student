# Direction brief — §8.7 Approximate Integration

Canon variant (Stewart ET 9e §7.7; cross-check Thomas 14e §8.7, Rogawski 4e §7.8). Written
2026-07-26 per PLAN-ch08 D8 + ③ A-03 (C²/C⁴ hypotheses; equal spacing; even n).

- **Canon inventory (Stewart §7.7):** why approximate (no antiderivative / data-only); L_n, R_n,
  M_n, T_n; Simpson via parabolas; the three error bounds; error-planning examples; data-table
  example.
- **Thinness:** canon states the rules and bounds with light derivation; this book derives M
  (Riemann sum, Def 6.2), T (average of L/R AND trapezoid areas, both shown), and S honestly
  (the three-point parabola lemma PROVED by algebra + shift), fencing ONLY the error bounds
  (the chapter's second and last credit, forward to Ch11 Taylor — Ch2 §2.4 precedent vehicle).
- **Scope & depth (標準/計算):** equal width \(h = \tfrac{b-a}{n}\), nodes \(x_i = a + ih\),
  values \(y_i = f(x_i)\); error \(=\) exact \(-\) approximation (sign convention stated).
  **Tagged displays**: (M) midpoint rule; (T) trapezoidal rule; (S) Simpson's rule (n EVEN).
  M is a Riemann sum with midpoint sample points (Def 6.2; §6.2's header reserved the RULES for
  here — discharge in one clause); T = average of left/right sums = sum of trapezoid areas
  (both derivations, two short displays); Simpson: lemma \(\int_{-h}^{h}(Ax^2+Bx+C)\,dx =
  \tfrac h3(y_0+4y_1+y_2)\) proved by direct computation + the shift remark (substitution moves
  any node triple to \([-h,h]\)), then pairwise summation → the 1,4,2,…,2,4,1 weights.
  **Theorem 8.4 (Error bounds, ON CREDIT)**: if \(f''\) continuous on \([a,b]\) and
  \(\lvert f''\rvert\le K\) there, \(\lvert E_T\rvert\le\tfrac{K(b-a)^3}{12n^2}\),
  \(\lvert E_M\rvert\le\tfrac{K(b-a)^3}{24n^2}\); if \(f^{(4)}\) continuous and
  \(\lvert f^{(4)}\rvert\le K_4\), \(\lvert E_S\rvert\le\tfrac{K_4(b-a)^5}{180n^4}\) (n even).
  K exists by EVT 4.9(a) (one clause); "any bound serves" reading. Fence note (unnumbered
  Caution, SPEC §16.1 vehicle): proofs need Taylor's theorem, arriving in Ch11; second and last
  credit of the chapter. NO <table> element anywhere (book-wide: fragments contain zero tables;
  data presented as displays).
- **Load-bearing intuition (one):** §8.6 certified numbers that no formula reaches (e^{−x²};
  §8.3's ellipse perimeter; §7.6's arc lengths); a number you cannot name exactly can still be
  BRACKETED as tightly as you please. Collision opener: for a decreasing integrand the left sum
  overshoots and the right sum undershoots — the truth sits between two computable numbers, and
  averaging them (T) already beats both. The whole section is one idea upgraded twice: replace
  f on each slice by something integrable exactly (a constant at the midpoint; a chord; a
  parabola), and the error bounds convert "better" into "provably within ε".
- **Worked examples (4; PLAN ledger Ex 8.33–8.36; values recomputed to 6 dp, sympy at sweep):**
  - **Ex 8.33** \(\int_1^2 \tfrac{dx}{x}\) with \(n=5\): \(T_5 \approx 0.695635\),
    \(M_5 \approx 0.691908\); true value \(\ln 2 \approx 0.693147\); errors
    \(E_T \approx -0.002488\), \(E_M \approx +0.001239\) — observations: M's error about half
    of T's, opposite sign (bounds' 24 vs 12 foreshadowed).
  - **Ex 8.34** same integral, \(S_{10} \approx 0.693150\), error \(\approx -3\times10^{-6}\):
    the fourth-order jump made visible against Ex 8.33.
  - **Ex 8.35** error planning: n for \(\lvert E_T\rvert &lt; 10^{-4}\) on the same integral:
    \(f''(x) = 2/x^3 \le 2 = K\) on [1,2]; \(\tfrac{2}{12n^2}&lt;10^{-4}\) → \(n &gt; 40.8\) →
    \(n = 41\) (round UP, say why); midpoint: \(n = 29\).
  - **Ex 8.36** data integral (self-authored; readings invented, plausibility checked):
    speedometer readings every 30 s for 3 min (equally spaced ✓, n = 6 even ✓), v in m/s:
    8, 10, 12, 11, 13, 14, 12; distance ≈ Simpson \(= \tfrac{30}{3}[8+40+24+44+26+56+12]
    = 2100\) m (≈ 42 km/h average — sanity line); the no-formula-at-all client; NO error bound
    claimable (no derivative information — honesty line ties to Thm 8.4's hypotheses).
- **History / application:** Ex 8.36 IS the applied payoff. No history blocks. Recorded.
- **figure_opportunities** (mark now, draw at M2): (a) three-panel comparison on one arch of a
  decreasing curve: midpoint rectangles / trapezoids / one shaded parabola through three nodes
  (essential; the three rules AS PICTURES; domain facts: same f, same interval, same n in all
  panels; parabola panel must show the parabola hugging the curve, not coinciding); (b) the
  midpoint rectangle re-read as a tangent-line trapezoid (the area-equal tilt picture that
  explains why M beats T; supporting; domain fact: tangent at the midpoint, areas equal —
  caption states the equality, drawing shows the tilt).
- **Emphasis / takeaway:** concept pivot = *approximation with a guaranteed error bound is as
  good as evaluation, to any stated accuracy*; portable skill = run T/M/S on values (formula or
  data), and size n in advance from Theorem 8.4.
- **Deliberately omit (auditor's reverse check):** proofs of the error bounds (the fenced
  credit); Romberg/adaptive/Gauss quadrature; the S=(T+2M)/3 identity; probabilistic error
  discussion; L_n/R_n as named tagged rules (they appear in T's derivation only); any <table>
  markup (zero-table book invariant).
- **Length band:** ~200–240 fragment lines (chapter summary follows in this fragment).
- **Env minted (per PLAN ledger):** Theorem 8.4 (on credit, fenced); Examples 8.33–8.36; tags
  (M), (T), (S). Cautions unnumbered (two: even-n for Simpson folded into its intro or caution;
  the fence note itself). Chapter summary (unnumbered, h3) closes the fragment per SPEC §4.
