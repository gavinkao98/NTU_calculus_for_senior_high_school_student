# Direction brief — §8.5 Strategy for Integration

Canon variant (Stewart ET 9e §7.5; cross-check Thomas 14e §8.6 intro, Rogawski 4e Ch7 review
framing). Written 2026-07-26 per PLAN-ch08 (§8.5 row as amended by ③ B-02).

- **Canon inventory (Stewart §7.5):** the 4-step strategy (simplify / obvious substitution /
  classify by form / try again); table of standard forms; "can we integrate all continuous
  functions?" closer (elementary functions; \(e^{x^2}\) named).
- **Thinness:** canon's table mixes derived and undelivered entries; this book's table lists ONLY
  results it has established, each with provenance. Canon asserts nonexistence of elementary
  antiderivatives as fact; this book (③ B-02) states scope honestly without borrowing Liouville.
- **Scope & depth (標準/計算):** no new numbered theory. **Strategy 8.6 (A four-step strategy)**:
  (1) simplify the integrand first (algebra, identities); (2) look for an obvious substitution
  (inner block with derivative present); (3) classify by form: trig powers → Strategies 8.2/8.3,
  quadratic radicals → Strategy 8.4 (complete the square first when needed), rational →
  Strategy 8.5, products of unrelated factors / lone log or inverse function → Strategy 8.1;
  (4) try again — manipulate, relate to a known integral, or chain techniques; several routes may
  succeed. Table of standard forms: unnumbered display list, provenance in parentheses (§6.4
  table; Prop 8.1; (8.A); scaled arcsin derived in one verification line via Ex 3.14 + chain
  rule before the table). Elementary-antiderivative paragraph in the ③ B-02 form: none of this
  chapter's techniques produces an elementary antiderivative for \(\int e^{-x^{2}}\,dx\);
  whether any exists is a question this book does not take up; §8.6 shows the associated improper
  integral still converges, §8.7 computes such integrals numerically. One nameless clause noting
  further systematic conversions exist (no Weierstrass name/formula).
- **Load-bearing intuition (one):** the earlier sections each answered "how does this technique
  work"; practice asks a different question, "which technique fits this integrand". The collision
  opener: four integrals that LOOK alike (\(\int\tan^{3}x/\cos^{3}x\), \(\int e^{\sqrt x}\),
  \(\int\frac{dx}{x\sqrt{\ln x}}\), \(\int\sqrt{\tfrac{1-x}{1+x}}\,dx\)) dispatch to four
  different tools; the skill is reading FORM, not running procedures. Classification is cheap
  (seconds) and failure-tolerant (step 4 loops back).
- **Worked examples (4; PLAN ledger Ex 8.23–8.26, answers pre-verified, sympy at sweep;
  solutions may compress standard sub-steps with a cross-ref — recognition is the taught skill):**
  - **Ex 8.23** \(\int\frac{\tan^{3}x}{\cos^{3}x}\,dx = \frac{\sec^{5}x}{5} - \frac{\sec^{3}x}{3}
    + C\) (step 1 rewrite → \(\tan^3 x\sec^3 x\); odd tangent → Strategy 8.3 case 2, save
    \(\sec x\tan x\), \(u = \sec x\)).
  - **Ex 8.24** \(\int e^{\sqrt x}\,dx = 2\bigl(\sqrt x - 1\bigr)e^{\sqrt x} + C\) (\(x>0\);
    **step 4** substitution \(u = \sqrt x\) to expose structure — \(du\) is NOT visibly present,
    so this is NOT step 2's visible-derivative case; then parts as in Ex 8.3; chaining).
    〔⑤ 8.5-B1 adjudication 2026-07-26: the draft's step-4 mapping is the correct semantics
    (step 2 = visible \(du\) only); this brief line originally said "step 2" in error and is
    amended to match — the defect was in the brief, not the draft.〕
  - **Ex 8.25** \(\int \frac{dx}{x\sqrt{\ln x}} = 2\sqrt{\ln x} + C\) (\(x>1\) named; step 2:
    \(dx/x\) is the derivative of \(\ln x\) — the obvious-substitution case done in two lines).
  - **Ex 8.26** \(\int\sqrt{\frac{1 - x}{1 + x}}\,dx = \arcsin x + \sqrt{1 - x^{2}} + C\) on
    \((-1, 1)\) (step 1 algebraic massage: multiply by \(\tfrac{\sqrt{1-x}}{\sqrt{1-x}}\) →
    \(\tfrac{1-x}{\sqrt{1-x^2}}\); split; arcsin table row + power-rule piece; the
    simplify-first showcase).
- **History / application:** none as blocks. Recorded deliberate.
- **figure_opportunities**: none (decision-training section); record sparsity as deliberate.
- **Emphasis / takeaway:** concept pivot = *integration is classification: read the form, then
  dispatch*; portable skill = the four-step loop, including the reflex to simplify BEFORE
  choosing and to chain techniques without ceremony.
- **Deliberately omit (auditor's reverse check):** Weierstrass \(t=\tan(x/2)\) by name or
  formula (nameless one-clause nod only); integration-by-tables/CAS (excluded by design);
  additional mixed drill examples beyond the four (the techniques sections carry the drills);
  any nonexistence claim for elementary antiderivatives (③ B-02 — scope statement only);
  erf or named special functions.
- **Length band:** ~130–170 fragment lines.
- **Env minted (per PLAN ledger):** Strategy 8.6; Examples 8.23–8.26. No Def/Thm/Prop; cautions:
  none planned (no trap native to this section; the traps live with their techniques). Counters
  handed to §8.6: Definition 8.1, Definition 8.2, Proposition 8.2, Theorem 8.3, Example 8.27.
