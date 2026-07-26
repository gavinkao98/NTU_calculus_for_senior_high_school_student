# Direction brief — §8.6 Improper Integrals

Canon variant (Stewart ET 9e §7.8; cross-check Thomas 14e §8.8, Rogawski 4e §7.7). Written
2026-07-26 per PLAN-ch08 D7 + ③ A-02 (p≤0 branch). The chapter's one genuinely theoretical
section; still zero new fences.

- **Canon inventory (Stewart §7.8):** Type 1 (infinite interval) definition via limits;
  convergent/divergent; 1/x vs 1/x²; p-test; Type 2 (discontinuous integrand) definition;
  interior-discontinuity trap; Comparison Theorem (stated, plausibility only) with e^{−x²}.
- **Thinness:** canon never proves the Comparison Theorem; this book proves it with mainline
  tools (③-confirmed route: Thm 4.1 + integer bracketing — "valid, fence-free, appropriate").
  Canon leaves split-point independence for ∫_{−∞}^∞ unaddressed; this book gives the
  one-sentence additivity justification. Canon's p-test skips p≤0 nuance; A-02 branch added.
- **Scope & depth (標準/計算 with one proof highlight):** **Definition 8.1 (Type 1)**: (a) f
  continuous on [a,∞): ∫_a^∞ f = lim_{t→∞}∫_a^t f if the limit exists as a finite number; then
  convergent, else divergent; (b) mirror on (−∞,b]; (c) both directions: split at any c, BOTH
  halves converge, value = sum; independence of c justified by additivity Thm 6.2(3) one
  sentence after the definition. **Definition 8.2 (Type 2)**: (a) f continuous on [a,b),
  unbounded near b: lim_{t→b⁻}∫_a^t f; (b) mirror at a; (c) interior singularity: split, both
  halves. **Proposition 8.2 (p-test)**: ∫_1^∞ x^{−p} dx converges iff p>1, value 1/(p−1);
  proof by power computation, p=1 by ln, p≤0 explicit sentence (integrand ≥1, ∫ ≥ t−1 by
  Thm 6.2(4); the power computation covers it too). **Theorem 8.3 (Comparison)**: f, g continuous
  on [a,∞), 0 ≤ f(x) ≤ g(x) for x ≥ a: ∫g converges ⇒ ∫f converges (value ≤ ∫g); ∫f diverges ⇒
  ∫g diverges. Proof: F(t)=∫_a^t f increasing (6.2(3)+(4)); F(t) ≤ G(t) ≤ M = ∫_a^∞ g (increasing
  G sits below its limit — one-line contradiction argument); sequence F(a+n) increasing bounded
  → converges to L by Thm 4.1, every F(a+n) ≤ L; for t ≥ a let n = ⌊t−a⌋ (greatest integer not
  exceeding t−a, glossed inline): F(a+n) ≤ F(t) ≤ F(a+n+1) ≤ L pins F(t) between numbers
  approaching L → lim F(t) = L. Part (b) = contrapositive, one line. Combined-type sentence
  (∫_0^∞ with endpoint singularity: split into one integral of each type). Introduce-before-use:
  limits at infinity are house-informal since §1.4/§5.8 — stay in that register; lim arctan =
  π/2 cited to §1.2's horizontal-asymptote reading.
- **Load-bearing intuition (one):** Definition 6.2 needs a closed interval and a continuous
  integrand; drop either and the symbol ∫ has NO meaning yet. Collision: the region under
  1/x² over [1,∞) is endless in extent, yet every truncation ∫_1^t has value 1 − 1/t, and those
  values settle. The integral's meaning is EXTENDED by the only device the book has for
  "settling": take a limit of proper integrals. Everything in the section is that one move,
  applied at ∞ or at a blow-up point; "convergent" is a verdict about the limit, not the region's
  size. The 1/x vs 1/x² contrast carries the intuition: both tails shrink to 0, but one shrinks
  fast enough to hold finite area and the other does not — how fast the integrand dies is the
  whole question (exported to Ch11 as the germ of series convergence).
- **Worked examples (6; PLAN ledger Ex 8.27–8.32, answers pre-verified, sympy at sweep):**
  - **Ex 8.27** (a) ∫_1^∞ dx/x diverges (ln t → ∞); (b) ∫_1^∞ dx/x² = 1 (1 − 1/t → 1). The
    contrast discussed in-solution: same shape, different tail speed.
  - **Ex 8.28** ∫_{−∞}^∞ dx/(1+x²) = π (split at 0; arctan limits ±π/2 via §1.2; both halves
    π/2).
  - **Ex 8.29** ∫_0^∞ t e^{−t} dt = 1 (parts Thm 8.2 on [0,s]; s e^{−s} → 0 by L'Hôpital
    Thm 5.5; e^{−s} → 0).
  - **Ex 8.30** Type 2 pair: (a) ∫_2^5 dx/√(x−2) = 2√3 (blow-up at left endpoint); (b) ∫_0^1
    x^{−p} dx converges iff p<1 with value 1/(1−p) (the 0-endpoint mirror of the p-test — its
    takeaway sentence names the mirror-image relation; p≥1 divergence shown).
  - **Ex 8.31** the trap: ∫_{−1}^3 dx/x² — blind FTC gives −4/3, negative for a positive
    integrand (alarm bell); x=0 is an interior singularity; Def 8.2(c) splits; ∫_0^3 piece
    diverges (Ex 8.30(b) with p=2 mirror argument / direct limit) → integral diverges.
  - **Ex 8.32** ∫_1^∞ e^{−x²} dx converges by comparison with e^{−x} (x ≥ 1 ⇒ x² ≥ x ⇒ e^{−x²}
    ≤ e^{−x}; ∫_1^∞ e^{−x} = 1/e computed); closes §8.5's arc — a number exists though no
    formula does; one sentence: ∫_0^∞ adds a proper piece ∫_0^1.
- **History / application:** none as blocks; Gabriel's-horn-type digressions excluded (PLAN).
  Recorded deliberate.
- **figure_opportunities** (mark now, draw at M2): (a) tails of 1/x and 1/x² over [1,∞) on one
  axis, region under each shaded to a movable cutoff t — the contrast picture (essential;
  domain facts: curves cross nowhere on (1,∞), 1/x on top; both → 0); (b) Type-2 region for
  1/√(x−2) on (2,5] with the vertical asymptote at x=2 dashed and the truncated region from t>2
  shaded (supporting); (c) comparison picture: e^{−x²} under e^{−x} on [1,∞), the finite area
  under the upper curve capping the lower (supporting; curves touch at x=1).
- **Emphasis / takeaway:** concept pivot = *an improper integral is a limit of proper ones, and
  "convergent" is a statement about that limit*; portable skill = classify the impropriety
  (type, location), split so each piece has ONE issue at ONE end, then evaluate or compare.
- **Deliberately omit (auditor's reverse check):** absolute/conditional convergence vocabulary
  (Ch11's); the Integral Test statement (Ch11 §11.3 cites US — one forward clause in summary
  only); Cauchy principal value as a named concept (the caution shows the trap, no name);
  Gabriel's horn / painter's paradox; limit-comparison test (Ch11); Γ function (te^{−t} stays
  an integral, not Γ(2)).
- **Length band:** ~230–270 fragment lines.
- **Env minted (per PLAN ledger):** Definition 8.1, Definition 8.2; Proposition 8.2 (proved);
  Theorem 8.3 (proved); Examples 8.27–8.32. Cautions unnumbered (two: principal-value trap with
  ∫x dx counterexample; hidden-singularity check before FTC). Counters handed to §8.7:
  Theorem 8.4, Example 8.33; tags (M)/(T)/(S) minted in §8.7.
