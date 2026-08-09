# Direction brief — §8.4 Integration of Rational Functions by Partial Fractions

Canon variant (Stewart ET 9e §7.4; cross-check Thomas 14e §8.5, Rogawski 4e §7.5). Written
2026-07-26 per PLAN-ch08 D6.

- **Canon inventory (Stewart §7.4):** proper vs improper; the four factor cases; cover-up /
  coefficient matching; \(\int\frac{dx}{x^2+a^2}\) formula; completing the square for irreducible
  quadratics; rationalizing substitutions (his concluding subsection).
- **Thinness:** canon re-teaches the decomposition algebra; this book banked it in §A.4
  (Prop A.7 + Strategy A.2 + cover-up) and spends the section on the INTEGRATION layer. Canon
  states "factor Q completely" without saying why that is always possible; this book fences the
  FTA fact explicitly (the chapter's first credit; SPEC §16.1 unnumbered-Caution fence vehicle,
  Ch2 §2.4 precedent).
- **Scope & depth (標準/計算):** no new numbered theory beyond **Strategy 8.5 (Integrating a
  rational function)**: (1) improper → divide (Strategy A.2 step 1); (2) factor \(Q\) completely
  (FTA credit); (3) decompose by Prop A.7, constants by Strategy A.2 (cover-up recalled in one
  clause); (4) integrate the fragment shapes: \(\frac{A}{x-r}\to A\ln\lvert x-r\rvert\) (§6.4),
  \(\frac{A}{(x-r)^k}\to\) power rule, \(\frac{Bx+C}{\text{quadratic}}\to\) log of the quadratic
  + arctan after completing the square (§A.5). **Tag (8.A)**: \(\int\frac{dx}{x^2+a^2} =
  \frac1a\arctan\frac xa + C\) (\(a>0\)), derived in two lines by \(u = x/a\) + §6.4's table row
  \(\int\frac{du}{1+u^2} = \arctan u + C\); referenced by Ex 8.20/8.21. Case IV (repeated
  irreducible quadratic): Prop A.7 already covers the FORM; one prose sentence on how integration
  would proceed; NO worked example (recorded deliberate). ln-consolidation only when it genuinely
  simplifies.
- **Load-bearing intuition (one):** a rational function is opaque as a whole but transparent in
  fragments. The collision: \(\int\frac{2x^2-x+4}{x^3+4x}\,dx\) matches no pattern so far; yet
  \(\frac{1}{x(x+1)} = \frac1x - \frac1{x+1}\) (§A.4's opener) integrates on sight. Partial
  fractions is the systematic version of that one observation: every proper rational function IS
  a sum of such fragments (Prop A.7), each fragment has a standard antiderivative, and §A.4
  promised exactly this payoff ("its real payoff is in integration"). The section is the promise
  kept.
- **Worked examples (6; PLAN ledger Ex 8.17–8.22, answers pre-verified, sympy at sweep):**
  - **Ex 8.17** \(\int\frac{x^3+x}{x-1}\,dx = \frac{x^3}{3}+\frac{x^2}{2}+2x+2\ln\lvert x-1\rvert
    + C\) (improper: divide first, quotient \(x^2+x+2\) remainder \(2\)).
  - **Ex 8.18** \(\int\frac{x^2+2x-1}{2x^3+3x^2-2x}\,dx = \tfrac12\ln\lvert x\rvert +
    \tfrac1{10}\ln\lvert 2x-1\rvert - \tfrac1{10}\ln\lvert x+2\rvert + C\) (three distinct linear
    factors \(x(2x-1)(x+2)\); cover-up at each root; \(A=\tfrac12, B=\tfrac15, C=-\tfrac1{10}\);
    the \(\int\frac{dx}{2x-1}=\tfrac12\ln\lvert 2x-1\rvert\) inner substitution named).
  - **Ex 8.19** \(\int\frac{x^4-2x^2+4x+1}{x^3-x^2-x+1}\,dx = \frac{x^2}{2}+x+
    \ln\lvert x-1\rvert - \frac{2}{x-1} - \ln\lvert x+1\rvert + C\) (divide: quotient \(x+1\),
    remainder \(4x\); factor by grouping \((x-1)^2(x+1)\); repeated linear; \(A=1,B=2,C=-1\)).
  - **Ex 8.20** \(\int\frac{2x^2-x+4}{x^3+4x}\,dx = \ln\lvert x\rvert + \tfrac12\ln(x^2+4)
    - \tfrac12\arctan\tfrac x2 + C\) (irreducible quadratic \(x^2+4\); \(A=1,B=1,C=-1\); split
    \(\frac{x-1}{x^2+4}\) into log part + (8.A) part; no absolute value on \(x^2+4\), positive).
  - **Ex 8.21** \(\int\frac{4x^2-3x+2}{4x^2-4x+3}\,dx = x + \tfrac18\ln(4x^2-4x+3)
    - \tfrac1{4\sqrt2}\arctan\tfrac{2x-1}{\sqrt2} + C\) (equal degrees: divide → \(1 +
    \frac{x-1}{4x^2-4x+3}\); discriminant \(16-48<0\) so irreducible; complete the square
    \((2x-1)^2+2\) per §A.5; shift \(u=2x-1\); (8.A) with \(a=\sqrt2\); discharges §A.5's
    "Chapter 8" promise explicitly).
  - **Ex 8.22** \(\int\frac{\sqrt{x+4}}{x}\,dx = 2\sqrt{x+4} +
    2\ln\left\lvert\frac{\sqrt{x+4}-2}{\sqrt{x+4}+2}\right\rvert + C\) (rationalizing
    substitution \(u=\sqrt{x+4}\), \(x=u^2-4\), \(dx=2u\,du\) → \(2\int\frac{u^2}{u^2-4}\,du\)
    → divide → partial fractions on \(\frac{4}{(u-2)(u+2)}\); solved on the component \(x>0\),
    formula checked on \((-4,0)\) by the same differentiation; the chaining takeaway:
    substitution FIRST, rational function SECOND, partial fractions THIRD).
- **History / application:** none as blocks. Recorded as deliberate (technique section; §A.4
  carries the telescoping-sum tie already).
- **figure_opportunities**: none carry weight (pure algebra section); record sparsity as
  deliberate — the figure-opportunity gate at M2 re-checks.
- **Emphasis / takeaway:** concept pivot = *every proper rational function splits into fragments
  with standard antiderivatives, so rational integrands always yield*; portable skill = the
  four-step Strategy 8.5 pipeline, including divide-first reflex and the completed-square arctan
  ending.
- **Deliberately omit (auditor's reverse check):** case-IV worked example (repeated irreducible
  quadratic — form stated via Prop A.7 + one sentence; Stewart's Example 7-level run adds length
  without a new idea at this depth); Heaviside theory beyond cover-up recall; complex-root
  factorization; Ostrogradsky / Hermite reduction; irreducibility tests beyond the discriminant
  clause \(p^2 &lt; 4q\); logistic/ODE applications (Ch9's; no forward tease beyond one clause if
  natural).
- **Length band:** ~190–230 fragment lines.
- **Env minted (per PLAN ledger):** Strategy 8.5; Examples 8.17–8.22; equation tag (8.A);
  unnumbered Caution ×2 (FTA fence, SPEC §16.1 vehicle; irreducibility check). Counters handed
  to §8.5: Strategy 8.6, Example 8.23.
