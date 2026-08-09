# Direction brief — §8.3 Trigonometric Substitution

Canon variant (Stewart ET 9e §7.3; cross-check Thomas 14e §8.4, Rogawski 4e §7.3). Written
2026-07-26 per PLAN-ch08 D5 + ③ A-01 (positive parameters; connected components; sec-branch rule).

- **Canon inventory (Stewart §7.3):** the three inverse substitutions for \(\sqrt{a^2-x^2}\),
  \(\sqrt{a^2+x^2}\), \(\sqrt{x^2-a^2}\) with restricted θ-ranges; right-triangle
  back-substitution; ellipse area; completing the square to reach the patterns.
- **Thinness:** canon asserts "the substitution is legitimate because the new variable's range is
  restricted" in one line; this book spends one honest paragraph: inverse substitution is Thm 6.6
  read right-to-left, the restriction makes θ ↦ x one-to-one so θ = arcsin(x/a) is well defined,
  and on the stated range the radical resolves with a DEFINITE sign. That paragraph is the
  section's hypothesis-hygiene anchor; each solution then opens by naming pattern + range + sign.
- **Scope & depth (標準/計算):** no new numbered theory. **Strategy 8.4 (Trigonometric
  substitution)** = the three-pattern table, each row: radical → substitution → θ-range →
  identity used → resolved radical. Convention sentence before the table: \(a\) denotes a
  positive constant throughout (③ A-01). Right-triangle reading taught once (label sides from
  the substitution; the triangle is a mnemonic for identities valid on the stated range).
  Definite integrals: transform the limits (Thm 6.7) or back-substitute fully; never mix
  (caution). \(x = a\sec\theta\) primary branch \(x \ge a\) with \(\theta\in[0,\pi/2)\),
  \(\tan\theta\ge0\); the \(x\le-a\) branch via caution: alternate range
  \(\theta\in(\pi/2,\pi]\), where \(\tan\theta\le0\) and \(\sqrt{x^2-a^2} = -a\tan\theta\), or
  verify the final formula by differentiation on that component. Each indefinite example names
  its connected domain component. Introduce-before-use: arcsin/arctan principal ranges are §1.2's;
  completing the square recalled from §A.5 with the identity restated.
- **Load-bearing intuition (one):** substitution so far REPLACED a visible inner block; here the
  variable itself is REPARAMETRIZED. The collision: \(\sqrt{9-x^2}\) contains no inner function
  whose derivative is present, and no algebraic u-sub removes a square root sitting over a sum or
  difference of squares. But the Pythagorean identity is exactly a statement about sums of
  squares: setting \(x = 3\sin\theta\) turns \(9 - x^2\) into the perfect square
  \(9\cos^2\theta\), and the root disappears. The three radicals correspond to the three
  Pythagorean rearrangements (Prop A.1). Geometrically each substitution names the angle in a
  right triangle whose sides realize the radical.
- **Worked examples (5; PLAN ledger Ex 8.12–8.16, answers pre-verified, sympy at sweep):**
  - **Ex 8.12** \(\int\frac{\sqrt{9-x^2}}{x^2}\,dx = -\frac{\sqrt{9-x^2}}{x} - \arcsin\frac{x}{3}
    + C\) on \((0,3)\) (sin-sub; \(\cot^2 = \csc^2 - 1\); component named; triangle
    back-substitution shown in full as the template).
  - **Ex 8.13** ellipse \(\frac{x^2}{a^2}+\frac{y^2}{b^2}=1\) (\(a,b>0\)) area \(= \pi ab\)
    (definite; quarter-ellipse ×4 by symmetry Thm 6.8 or direct even-function argument — use
    Thm 6.8; limits transformed by Thm 6.7; power reduction §A.2 for \(\cos^2\); discharges the
    §A.5-adjacent conic thread and gives the chapter its one geometry payoff).
  - **Ex 8.14** \(\int\frac{dx}{x^2\sqrt{x^2+4}} = -\frac{\sqrt{x^2+4}}{4x} + C\) (tan-sub;
    \(\sec\theta>0\) on \((-\pi/2,\pi/2)\); solved on \(x>0\), formula checked to hold on
    \(x<0\) too by differentiation — one clause).
  - **Ex 8.15** \(\int\frac{dx}{\sqrt{x^2-a^2}} = \ln\bigl(x+\sqrt{x^2-a^2}\bigr) + C_1\) on
    \(x>a\) (sec-sub on the primary branch; \(\ln\lvert\sec\theta+\tan\theta\rvert\) via Prop 8.1;
    absolute value drops since \(x>a\) makes the argument positive — hygiene line; the \(x<-a\)
    component handled in the caution's verification remark).
  - **Ex 8.16** \(\int\frac{x}{\sqrt{3-2x-x^2}}\,dx = -\sqrt{3-2x-x^2} - \arcsin\frac{x+1}{2}
    + C\) on \((-3,1)\) (completing the square §A.5: \(3-2x-x^2 = 4-(x+1)^2\); shift \(u=x+1\);
    split into power-rule piece (\(w = 4-u^2\)) + sin-sub piece; domain interval named).
- **History / application:** none as blocks; the ellipse example IS the applied payoff. One
  forward clause allowed after Ex 8.13: the ellipse's perimeter, unlike its area, resists every
  technique of this chapter (→ §8.7 motivation; no elliptic-integral vocabulary). Recorded.
- **figure_opportunities** (mark now, draw at M2): (a) the three reference right triangles, one
  per substitution, sides labeled from the substitution (x, a, radical in correct positions),
  θ marked — 3-panel diagram, essential tier (the section's back-substitution device drawn;
  domain facts: sin-panel hypotenuse a, legs x and √(a²−x²); tan-panel legs x and a, hypotenuse
  √(a²+x²); sec-panel hypotenuse x, legs a and √(x²−a²); θ always at the a-adjacent vertex).
  (b) the quarter-ellipse with the region shaded (supporting; a,b marked on axes, curve through
  (a,0),(0,b)). Record others as deliberate sparsity.
- **Emphasis / takeaway:** concept pivot = *a restricted trigonometric reparametrization turns a
  quadratic radical into a perfect square*; portable skill = pattern-match the radical to the
  Strategy 8.4 row, run the substitution with its range, return by the labeled triangle.
- **Deliberately omit (auditor's reverse check):** hyperbolic substitutions (PLAN D2);
  \(\int\sqrt{x^2+a^2}\,dx\) and \(\int\sqrt{x^2-a^2}\,dx\) as worked examples (they land on
  \(\sec^3\); Ex 8.10 + one clause note the path, no second full run); rationalizing
  \(t=\tan(x/2)\) (not this section); direct u = a²−x² substitutions when a stray x makes them
  available (mentioned in Strategy 8.4's lead-in: check for a plain u-sub FIRST — one sentence,
  cross-ref Strategy 8.6's step 2 forward); arcsec-based antiderivative forms (§1.2 defined
  arcsec but the book's sec-sub returns via ln forms, not arcsec — silent, standard).
- **Length band:** ~180–220 fragment lines.
- **Env minted (per PLAN ledger):** Strategy 8.4; Examples 8.12–8.16. No Def/Thm/Prop. Cautions
  unnumbered (two: definite-integral limits discipline; sec-branch / radical-sign rule).
  Counters handed to §8.4: Strategy 8.5, Example 8.17; equation tag (8.A) minted in §8.4.
