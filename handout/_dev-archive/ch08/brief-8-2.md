# Direction brief — §8.2 Trigonometric Integrals

Canon variant (Stewart ET 9e §7.2; cross-check Thomas 14e §8.3, Rogawski 4e §7.2). Written
2026-07-26 per PLAN-ch08 D4.

- **Canon inventory (Stewart §7.2):** \(\sin^m\cos^n\) with odd/even exponent cases; power
  reduction for even/even; \(\tan^m\sec^n\) cases; \(\int\tan\), \(\int\sec\) (Stewart's boxed
  1 and its sec trick); product-to-sum for \(\sin mx\cos nx\) family.
- **Thinness:** canon presents the sec trick bare ("multiply numerator and denominator by
  \(\sec x + \tan x\)") with no honesty about its status; this book labels it a found device and
  completes the proof by differentiation. Canon also scatters the identities; this book cites its
  own appendix (Prop A.1/A.2, §A.2 power-reduction) and restates each identity inline at point of
  use (B-class hygiene).
- **Scope & depth (標準/計算):** **Proposition 8.1 (antiderivatives of the remaining trigonometric
  functions)**: \(\int\tan x\,dx = \ln\lvert\sec x\rvert + C\), \(\int\cot x\,dx =
  \ln\lvert\sin x\rvert + C\), \(\int\sec x\,dx = \ln\lvert\sec x + \tan x\rvert + C\),
  \(\int\csc x\,dx = -\ln\lvert\csc x + \cot x\rvert + C\), each valid on any interval where the
  integrand is continuous. Proof: tan by \(u = \cos x\) (Thm 6.6 + §6.4's \(\ln\lvert x\rvert\));
  cot same pattern one line; sec by the multiply-by-\(\tfrac{\sec+\tan}{\sec+\tan}\) device
  (honestly labeled) + verification by differentiation (complete proof); csc "check by
  differentiating" one line. Two strategy boxes: **Strategy 8.2** (\(\sin^m\cos^n\): odd → save a
  factor + Pythagorean + u-sub; both even → power reduction §A.2), **Strategy 8.3**
  (\(\tan^m\sec^n\): \(n\) even → save \(\sec^2 x\), convert rest to tan; \(m\) odd → save
  \(\sec x\tan x\), convert rest to sec; neither → rewrite in sec powers, use parts / Prop 8.1,
  as in \(\int\sec^3\)). Introduce-before-use: \(\sec/\csc/\cot\) are B-class — defined in §A.1
  (Def A.1); recall-in-one-clause + cross-ref at first use here.
- **Load-bearing intuition (one):** substitution needs \(du\) present, and trigonometry can
  MANUFACTURE the missing \(du\): identities convert one trig function into another, so a factor
  of \(\sin x\) can be spent as \(du = -\sin x\,dx\) for \(u = \cos x\) while the Pythagorean
  identity rewrites what remains in terms of \(u\). Collision opener: \(\int\sin^3 x\,dx\) has no
  visible inner-function structure, yet splitting off one sine turns it into a polynomial in
  \(\cos x\). The section's whole method: spend one factor as \(du\), convert the rest with an
  identity; when no factor can be spared (even powers), lower the degree with power reduction.
- **Worked examples (5; PLAN ledger Ex 8.7–8.11, answers pre-verified, sympy at sweep):**
  - **Ex 8.7** \(\int\sin^{3}x\cos^{2}x\,dx = \tfrac{\cos^{5}x}{5} - \tfrac{\cos^{3}x}{3} + C\)
    (odd sine: save one, convert via \(\sin^2 = 1-\cos^2\), \(u=\cos x\)).
  - **Ex 8.8** \(\int\sin^{4}x\,dx = \tfrac{3x}{8} - \tfrac{\sin 2x}{4} + \tfrac{\sin 4x}{32} + C\)
    (even/even: power reduction twice, §A.2 identities restated inline; cross-check via Ex 8.6
    reduction formula, agreement noted in one sentence).
  - **Ex 8.9** \(\int\tan^{6}x\sec^{4}x\,dx = \tfrac{\tan^{7}x}{7} + \tfrac{\tan^{9}x}{9} + C\)
    (\(n\) even: save \(\sec^2\), convert via \(\sec^2 = 1+\tan^2\) (Prop A.1), \(u=\tan x\)).
  - **Ex 8.10** \(\int\sec^{3}x\,dx = \tfrac{1}{2}\bigl(\sec x\tan x + \ln\lvert\sec x +
    \tan x\rvert\bigr) + C\) (neither case applies: parts with \(u=\sec x\), \(dv=\sec^2 x\,dx\) +
    Pythagorean + solve-back (Ex 8.4 pattern) + Prop 8.1; placed LAST; named as §8.3's workhorse).
  - **Ex 8.11** \(\int\sin 4x\cos 5x\,dx = \tfrac{\cos x}{2} - \tfrac{\cos 9x}{18} + C\)
    (product-to-sum, Prop A.2 identity restated verbatim; the \(\sin(-x) = -\sin x\) step named).
- **History / application:** none as blocks (one forward clause allowed: integrals of
  \(\sin mx\cos nx\) type return in the study of periodic phenomena; no Fourier name-drop without
  source — keep it plain or omit). Recorded as deliberate.
- **figure_opportunities** (mark now, draw at M2): (a) \(y = \sin^2 x\) with its midline
  \(y = \tfrac12\) over \([0, 2\pi]\) — the power-reduction identity as a picture: the graph
  oscillates symmetrically about its average, so \(\int_0^{2\pi}\sin^2 = \pi\) by inspection
  (supporting tier; graph; domain fact: midline exactly \(\tfrac12\), crossings at multiples of
  \(\tfrac{\pi}{4}\) shifted — the drawing must not mislabel the period, which is \(\pi\)).
  Sparse otherwise (identity-driven section). Record as deliberate.
- **Emphasis / takeaway:** concept pivot = *identities manufacture the \(du\) that substitution
  needs*; portable skill = the two case-analyses (Strategy 8.2/8.3): check exponent parity, save
  the right factor, convert the remainder.
- **Deliberately omit (auditor's reverse check):** \(\sin mx\sin nx\) and \(\cos mx\cos nx\)
  worked examples (Prop A.2/A.3 cover the identities; one clause says the same method applies —
  no example); general \(\sec^n\)/\(\tan^n\) reduction formulas (one clause after Ex 8.10 at
  most); half-angle Weierstrass substitution (§8.5 one-line mention only, per PLAN exclusions);
  hyperbolic analogues (D2: not collected); orthogonality relations / Fourier coefficients
  (outside scope); \(\int\csc^3\) (pattern named as mirroring Ex 8.10, not worked).
- **Length band:** ~170–210 fragment lines.
- **Env minted (per PLAN ledger):** Proposition 8.1 (proved); Strategy 8.2, Strategy 8.3;
  Examples 8.7–8.11. Cautions unnumbered (candidate: the \(u\)-sub sign trap — \(u = \cos x\)
  gives \(du = -\sin x\,dx\), the minus is the most-dropped symbol of the section). Counters
  handed to §8.3: Strategy 8.4, Example 8.12 (no new Def/Thm/Prop in §8.3).
