# PLAN-ch08 — Chapter 8: Techniques of Integration

Chapter-level direction anchor + cross-session state. Fourth manuscript-free chapter (canon variant;
5-milestone sequence per [`../../PIPELINE.md`](../../PIPELINE.md)). **First chapter generated under
CONTENT_SPEC §3 plain-register RC** — this round doubles as the generation-side validation of the
clause set (single-arm; see §Generation-side verification below and `KICKOFF-ch08-m1.md`).

## Workflow (manuscript-free, autonomous)

- **Spine = canon** (Stewart ET 9e Ch7 primary; Thomas 14e Ch8 / Rogawski 4e cross-check), authored
  to full-gate tier. No teacher manuscript exists Ch5–16.
- **Session grant (2026-07-26):** the user authorized standing Codex calls for this whole
  conversation and delegated final 拍板 to Claude-⇄-Codex convergence (user away from keyboard;
  per-call consent not required within this conversation; the CLAUDE.md per-call-consultation rule
  stays in force for future sessions). Both ⛳ stops of the kickoff are therefore replaced by
  recorded adjudications in this file + the applied report.
- **M1 execution order (kickoff v3, user decisions 2026-07-26):** whole-chapter continuous
  generation §8.1→§8.7 with free self-checks between sections; Codex ⑤ runs as a **post-generation
  batch** (×7) + chapter-level review (M1–M8) ×1. Chapter-level direction gate ③ still runs BEFORE
  drafting (one Codex round on this PLAN — direction errors are cheapest before seven sections
  exist).
- **Provenance:** each fragment carries `<!-- section-source: … -->`; pedagogical add-ons keep the
  `expansion:<cat>` tag system.
- **Anti-hallucination backstops:** (1) per-section brief + hypothesis ledger; (2) Codex
  adversarial ⑤ (direction-conformance + math + hypothesis hygiene) to 0 blocking; (3) chapter-end
  sympy recompute of all worked examples.
- **Depth: 標準/計算 (standard/computational)** — the lightest tier so far (ROADMAP 2026-07-04).
  This is the toolbox chapter: rules are still derived honestly (parts from the product rule;
  Simpson's parabola lemma by algebra; p-test and the Comparison Theorem proved), but the chapter's
  center of mass is worked examples + strategy boxes, not theory. Exactly **two on-credit items**
  (D6 FTA factorization, D8 error bounds), both explicitly fenced — see decisions below.
- **Plain register (SPEC §3 RC) is a drafting constraint, not a post-pass:** neutral verbs for
  math objects; no metaphor-only explanations; stable terminology; em-dash avoided at the source
  (target well under T_can ≤ 3.0/1000) without inflating colon-clauses / semicolons / parentheses;
  warm sentences must pass the four-condition test.

## Roster (roadmap §8 provisional, adopted as-is) — ③ RESOLVED 2026-07-26 (Codex, one round; audit: `ch08_ch-direction-codex3-audit.md`)

| § | Title | new machinery | key imports |
|---|---|---|---|
| 8.1 | Integration by Parts | **Thm 8.1** (parts, indefinite; proved from product rule) + **Thm 8.2** (parts, definite; via FTC-2); Strategy 8.1 (choosing \(u\), \(dv\)); \(\sin^n\) reduction formula (example) | product rule **Thm 2.6**; Def 6.3/6.4 (antiderivative); FTC-2 **Thm 6.4**; \((\ln x)'\) **Thm 4.14**; arctan deriv **Ex 3.16** |
| 8.2 | Trigonometric Integrals | **Prop 8.1** (antiderivatives of tan/cot/sec/csc); Strategy 8.2 (\(\sin^m\cos^n\)); Strategy 8.3 (\(\tan^m\sec^n\)) | **Prop A.1** (Pythagorean companions), **Prop A.2** (product-to-sum), §A.2 power-reduction (unnumbered); substitution **Thm 6.6**; \(\ln\lvert x\rvert\) export §6.4; sec/tan derivs (Ch3) |
| 8.3 | Trigonometric Substitution | inverse-substitution discipline (θ-ranges); Strategy 8.4 (the three substitutions) | inverse trig §1.2 (principal ranges); **Thm 6.6/6.7**; completing the square (§A.5 close); Prop A.1; §8.2 (\(\int\sec\), \(\int\sec^3\)) |
| 8.4 | Integration of Rational Functions by Partial Fractions | Strategy 8.5 (integrating a rational function); FTA factorization fence (on credit) | **Prop A.7** (decomposition), **Strategy A.2** (constants); long division (A-class); \(\ln\lvert x\rvert\) §6.4; \(\int\frac{dx}{x^2+a^2}=\frac1a\arctan\frac xa\) derived in place (u-sub + Ex 3.16); §A.5 completing the square |
| 8.5 | Strategy for Integration | Strategy 8.6 (four-step attack); table of standard forms (unnumbered display); elementary-antiderivative honesty as a **scope statement only** (③ B-02: this chapter's techniques do not produce one for \(e^{-x^2}\); whether any exists, the book does not take up — NO Liouville credit) | §§8.1–8.4 + Ch6 toolkit |
| 8.6 | Improper Integrals | **Def 8.1** (Type 1), **Def 8.2** (Type 2); **Prop 8.2** (\(p\)-test, proved); **Thm 8.3** (Comparison Theorem, **proved** via Thm 4.1 bracketing — zero new fences) | limits at infinity §1.4; L'Hôpital **Thm 5.5**; monotone-bounded **Thm 4.1**; Thm 6.2 (additivity/comparison); FTC-2 |
| 8.7 | Approximate Integration | Midpoint/Trapezoidal/Simpson rules (tagged displays (M)/(T)/(S)); Simpson's parabola lemma (proved by algebra); **Thm 8.4** (error bounds, **stated on credit**, forward fence → Ch11 Taylor) | Riemann sums §6.1–6.2 (midpoint sample points Def 6.2); §8.5 (why approximation is needed); §7.6 arc-length integrals as motivating clients |

**Excluded (recorded, per kickoff defaults + 選材節制):** inverse hyperbolic functions (kickoff
roster default: NOT included; open question for the user at chapter close — if wanted later, append
as §8.8, zero cascade); integration using tables/CAS (Stewart 7.6 — outside this book's design);
partial-fraction case IV worked example (repeated irreducible quadratic: Prop A.7 states the form;
one prose sentence + deliberate-omission record, no worked example); Weierstrass \(t=\tan(x/2)\)
substitution (one-line mention at most in §8.5, no worked example); Gabriel's horn digression
(§8.6 one-sentence aside at most); Romberg / adaptive quadrature (beyond scope); probability
integrals (Ch:none — \(e^{-x^2}\) appears only as convergence/comparison client).

## Cross-chapter EXPORT (forward contract; keep exact)

- **Def 8.1 + Prop 8.2 (\(p\)-test) + Thm 8.3 (Comparison)** §8.6 → **Ch11 §11.3 Integral Test**
  (the seam-ledger export candidate; kickoff §3 step 2). Ch11 will cite these numbers verbatim.
- **\(\int\frac{dx}{x^2+a^2}=\frac1a\arctan\frac xa\)** (§8.4 in-place derivation) → Ch9 (linear
  ODE integrating factors), Ch10.
- **Trig-substitution patterns** §8.3 → Ch10 (polar/conic integrals), Ch15 (polar double
  integrals, soft).
- **Simpson/Trapezoid rules** §8.7 → soft clients anywhere a definite integral resists the
  toolkit (Ch7 arc length flagged this; Ch10 ellipse perimeter echo).
- **Error-bound DEBT (import direction):** Thm 8.4 proofs arrive with **Ch11 §11.9 Taylor's
  theorem** (forward fence, Ch2→Ch4 precedent). Ch11 must discharge or re-fence explicitly.

## Chapter-level direction decisions — ③ RESOLVED 2026-07-26 (Codex one round; record `ch08_ch-direction-codex3-audit.md`)

- **[D1 roster/order/budget]** 7 sections in ROADMAP order (Strategy → **Improper → Approximate**;
  deviates from Stewart's 7.7/7.8 order deliberately: §8.5 ends on "some antiderivatives do not
  exist", §8.6 extends what the integral *means*, §8.7 closes with what to do when symbolic methods
  fail — the chapter ends on an honest, practical note). Worked-example budget: **36 planned, hard
  cap 38** (6+5+5+6+4+6+4). More than Ch7's 23 because this chapter's examples ARE the content
  (every technique needs its worked instances; Stewart Ch7 carries ~60), still capped to keep the
  audit surface finite.
- **[D2 inverse hyperbolic — default NOT collected]** Per kickoff §1: not included, recorded as
  open question for the user; if later wanted, lands as appended §8.8 (no cascade). Rationale: Ch7
  選材節制 precedent; the three radical patterns are fully served by trig substitution; NTU 甲
  syllabus does not require the hyperbolic-substitution track.
- **[D3 parts]** **Theorem 8.1 (Integration by Parts)**: for \(f, g\) differentiable on an open
  interval, \(\int f(x)g'(x)\,dx = f(x)g(x) - \int f'(x)g(x)\,dx\), read as an identity between
  antiderivative families; proof = product rule (Thm 2.6) + Def 6.3, three lines, honest statement
  that the identity asserts: any antiderivative of \(f'g\) subtracted from \(fg\) is an
  antiderivative of \(fg'\). **Theorem 8.2 (parts for definite integrals)**: \(f', g'\) continuous
  on \([a,b]\) ⇒ \(\int_a^b fg' = [fg]_a^b - \int_a^b f'g\); proof via FTC-2 (Thm 6.4) applied to
  \((fg)'\) (continuity of \((fg)' = f'g + fg'\) named). Mirrors the Ch6 pair Thm 6.6/6.7.
  \(u\)-\(dv\) notation introduced AFTER the theorem (notation, not new math; \(du = u'\,dx\) ties
  to §5.3 differentials). Examples: \(\int x\cos x\); \(\int\ln x\) (the \(dv = dx\) move);
  \(\int t^2 e^t\) (repeated parts); \(\int e^x\sin x\) (solve-back); \(\int_0^1\arctan x\)
  (definite; boundary term); \(\sin^n\) reduction formula (feeds §8.2's \(\sin^4\) cross-check).
  **Washer↔shell promise (shipped Ex 7.12 closing remark): DISCHARGED here, scoped** (③ B-01
  adjudication — repairing the sealed Ch7 fragment was the higher-risk alternative). Closing
  subsection of §8.1: unnumbered prose derivation (expansion:formula) under hypotheses \(f\)
  strictly decreasing and smooth on \([a,b]\), \(0\le a\), \(f\ge0\), with a smooth inverse \(g\)
  on \([f(b), f(a)]\) — parts (Thm 8.2, \(dv = 2x\,dx\)) + substitution (Thm 6.7) turn the shell
  integral into the washer value \(\pi\{b^2 c - a^2 d + \int_c^d g(y)^2 dy\}\) with \(c = f(b)\),
  \(d = f(a)\); the general (non-monotone) agreement stays with Ch15, said explicitly. Zero new
  numbered objects.
- **[D4 trig integrals]** **Proposition 8.1 (antiderivatives of the remaining trig functions)**:
  \(\int\tan = \ln\lvert\sec\rvert\), \(\int\cot = \ln\lvert\sin\rvert\),
  \(\int\sec = \ln\lvert\sec + \tan\rvert\), \(\int\csc = -\ln\lvert\csc + \cot\rvert\), each
  \(+C\), valid on any interval where the integrand is continuous. Proof: tan/cot by \(u\)-sub
  (Thm 6.6, \(u=\cos\)/\(u=\sin\), \(\ln\lvert x\rvert\) export §6.4); sec presented with the
  multiply-by-\(\frac{\sec+\tan}{\sec+\tan}\) device **honestly labeled as a found trick** whose
  correctness is then **verified by differentiation** (a complete proof); csc "same pattern, check
  by differentiating" (one line). Strategies: 8.2 (\(\sin^m\cos^n\): odd exponent → save one
  factor + Pythagorean + \(u\)-sub; both even → power-reduction §A.2), 8.3 (\(\tan^m\sec^n\):
  \(n\) even → save \(\sec^2\); \(m\) odd → save \(\sec\tan\); neither → fall back on
  \(\sec\)-powers/parts). Examples: \(\int\sin^3 x\cos^2 x\); \(\int\sin^4 x\) (power-reduction
  twice, cross-checked against the §8.1 reduction formula); \(\int\tan^6 x\sec^4 x\);
  \(\int\sec^3 x\) (parts + Prop 8.1 — the load-bearing §8.3 client); \(\int\sin 4x\cos 5x\)
  (Prop A.2). Product-to-sum family cited to Prop A.2/A.3, power-reduction to §A.2 prose (its
  identities restated inline where used — B-class hygiene, cross-ref not bare citation).
- **[D5 trig substitution]** Inverse substitution legitimacy handled ONCE in prose before the
  examples: setting \(x = g(\theta)\) with \(g\) one-to-one (θ restricted to the stated range) is
  the Substitution Rule (Thm 6.6) read right-to-left, and back-substitution θ = arcsin(x/a) etc.
  is well defined exactly because the range was restricted; on those ranges the radical resolves
  with a DEFINITE sign (\(\cos\theta \ge 0\) on \([-\pi/2,\pi/2]\), etc.) — this sentence is the
  section's hypothesis-hygiene anchor. **Strategy 8.4** = the three-pattern table
  (\(\sqrt{a^2-x^2}\): \(x=a\sin\theta\), \(\theta\in[-\pi/2,\pi/2]\); \(\sqrt{a^2+x^2}\):
  \(x=a\tan\theta\), \(\theta\in(-\pi/2,\pi/2)\); \(\sqrt{x^2-a^2}\): \(x=a\sec\theta\),
  \(\theta\in[0,\pi/2)\) for the \(x\ge a\) branch — the \(x\le -a\) branch handled by one caution
  note, not doubled machinery). Right-triangle back-substitution taught as the standard reading.
  Definite integrals: change the θ-limits (Thm 6.7) OR back-substitute fully, never mix — caution.
  Examples: \(\int\frac{\sqrt{9-x^2}}{x^2}\,dx\); area of the ellipse
  \(\frac{x^2}{a^2}+\frac{y^2}{b^2}=1\) (definite, limits changed; the πab payoff; ties §A.5);
  \(\int\frac{dx}{x^2\sqrt{x^2+4}}\); \(\int\frac{dx}{\sqrt{x^2-a^2}}\) (sec branch discipline,
  answer \(\ln\lvert x+\sqrt{x^2-a^2}\rvert - \ln a + C\) folded to \(\ln\bigl\lvert x+\sqrt{x^2-a^2}\bigr\rvert + C_1\));
  \(\int\frac{x}{\sqrt{3-2x-x^2}}\,dx\) (completing the square §A.5 + shift + sin-sub).
- **[D6 partial fractions]** Integration layer only — the algebra layer lives in §A.4 and is
  imported, not re-taught: Prop A.7 (decomposition form), Strategy A.2 (finding constants), with
  the appendix's cover-up shortcut recalled in one sentence. **FTA factorization fence (on
  credit)**: one unnumbered remark-note stating that every real polynomial factors into linear and
  irreducible quadratic factors (consequence of the Fundamental Theorem of Algebra; proof outside
  this book — the chapter's first of two explicitly-fenced credits; ROADMAP seam-hunt premise
  discharged by naming). **Strategy 8.5 (integrating a rational function)**: improper → divide;
  factor; decompose (§A.4); integrate the four fragment shapes (\(\ln\lvert x-a\rvert\); negative
  powers; \(\arctan\) after completing the square §A.5; \(\ln\) of the quadratic for the \(Bx\)
  part). \(\int\frac{dx}{x^2+a^2} = \frac1a\arctan\frac xa + C\) derived in place (u = x/a, cite
  Ex 3.16), display tagged for reuse. Case IV (repeated irreducible quadratic): form stated via
  Prop A.7 + one sentence on how the integration would proceed; NO worked example (recorded).
  Examples: improper-fraction divide-first (\(\int\frac{x^3+x}{x-1}\,dx\)); distinct linear
  (Stewart-type \(\int\frac{x^2+2x-1}{2x^3+3x^2-2x}\,dx\)); repeated linear
  (\(\int\frac{x^4-2x^2+4x+1}{x^3-x^2-x+1}\,dx\)); irreducible quadratic
  (\(\int\frac{2x^2-x+4}{x^3+4x}\,dx\) → ln + arctan); completing the square
  (\(\int\frac{4x^2-3x+2}{4x^2-4x+3}\,dx\) — also revisits divide-first with degree-equal
  fractions, discharging the §A.5 "Chapter 8" promise); rationalizing substitution
  (\(\int\frac{\sqrt{x+4}}{x}\,dx\) — u²-substitution turns a radical integrand rational; the
  bridge that widens §8.4 beyond literal rational functions).
- **[D7 improper]** **Definition 8.1 (Type 1)**: \(f\) continuous on \([a,\infty)\),
  \(\int_a^\infty f = \lim_{t\to\infty}\int_a^t f\) if the limit exists as a finite number (then
  *convergent*, else *divergent*); mirror clause for \((-\infty,b]\); for \((-\infty,\infty)\):
  split at any convenient \(c\), BOTH halves must converge, and the value is independent of the
  split point (one-sentence justification via additivity Thm 6.2(3)). **Definition 8.2 (Type 2)**:
  \(f\) continuous on \([a,b)\), unbounded near \(b\) (mirror at \(a\); interior singularity:
  split, both halves). **Prop 8.2 (\(p\)-test)**: \(\int_1^\infty x^{-p}\,dx\) converges iff
  \(p>1\) (value \(\frac1{p-1}\)); proved by direct computation + limit cases (p=1 separately via
  \(\ln\)). The 0-endpoint mirror (\(\int_0^1 x^{-p}\), converges iff \(p<1\)) is a worked example
  with its takeaway named, NOT a second proposition. **Theorem 8.3 (Comparison Theorem)**:
  \(f, g\) continuous, \(0\le f(x)\le g(x)\) for \(x\ge a\): \(\int g\) converges ⇒ \(\int f\)
  converges; \(\int f\) diverges ⇒ \(\int g\) diverges. **Proved on the spot with mainline tools
  only**: \(F(t)=\int_a^t f\) is increasing (comparison Thm 6.2(4) + additivity 6.2(3)); bounded
  above by \(\lim\int_a^t g\); the increasing-bounded function has a limit — proved by bracketing
  \(F\) between the integer-indexed sequence values \(F(a+n)\), which converge by **Thm 4.1**
  (monotone bounded sequences), and squeezing \(F(t)\) between \(F(a+\lfloor t-a\rfloor)\) and
  \(F(a+\lfloor t-a\rfloor+1)\). Zero new fences, no LUB import (Lemma D.1 stays appendix-local).
  Caution: \(\int_{-\infty}^{\infty} \ne \lim_{t\to\infty}\int_{-t}^{t}\) (principal-value trap,
  with \(\int x\,dx\) as the two-line counterexample). The interior-singularity trap
  (\(\int_{-1}^{3}\frac{dx}{x^2}\) "= −4/3" absurdity) is a MUST example (negative answer for a
  positive integrand = the alarm bell). Examples: \(\int_1^\infty \frac{dx}{x}\) vs
  \(\int_1^\infty\frac{dx}{x^2}\) (the contrast pair, one example two parts);
  \(\int_{-\infty}^{\infty}\frac{dx}{1+x^2}\) (=π); \(\int_0^\infty t e^{-t}\,dt\) (parts +
  L'Hôpital Thm 5.5 for \(te^{-t}\to 0\)); Type-2 \(\int_2^5\frac{dx}{\sqrt{x-2}}\) + the
  \(\int_0^1 x^{-p}\) mirror; the interior-singularity trap; comparison
  \(\int_1^\infty e^{-x^2}\,dx\) converges (compare \(e^{-x}\) on \([1,\infty)\)) — closes the
  §8.5 arc: no elementary antiderivative, yet the improper integral demonstrably exists.
- **[D8 approximate]** Rules derived honestly: \(M_n\) IS a Riemann sum (Def 6.2 midpoint sample
  points — echo §6.2's comment); \(T_n\) = average of left/right sums = trapezoid areas (both
  readings shown, one display each); Simpson: the three-point parabola integral
  \(\int_{-h}^{h}(Ax^2+Bx+C)\,dx = \frac h3(y_0+4y_1+y_2)\) **proved by direct algebra** (the
  section's one small lemma, kept in prose flow as a tagged derivation, not a numbered env), then
  pattern-summed to (S); \(n\) even REQUIRED (caution). **Theorem 8.4 (error bounds)**:
  \(\lvert E_T\rvert\le\frac{K(b-a)^3}{12n^2}\), \(\lvert E_M\rvert\le\frac{K(b-a)^3}{24n^2}\)
  (\(K\ge\lvert f''\rvert\) on \([a,b]\)), \(\lvert E_S\rvert\le\frac{K_4(b-a)^5}{180n^4}\)
  (\(K_4\ge\lvert f^{(4)}\rvert\)) — **stated on credit, proof fenced FORWARD to Ch11 Taylor's
  theorem** (unnumbered Caution note in the Ch2§2.4→Ch4 precedent form; the chapter's second and
  last credit; NOT an Appendix D entry because the proof genuinely arrives in mainline Ch11 §11.9).
  Motivation opener: §8.5 proved some integrands have no elementary antiderivative, and §7.6's arc
  lengths already ran into them (the ellipse's perimeter integral named as the classic instance —
  its AREA fell to §8.3, its PERIMETER is non-elementary; source-tagged). Examples:
  \(\int_1^2\frac{dx}{x}\) by \(T_5\) and \(M_5\) vs the true \(\ln 2\) (error signs and sizes
  observed); the SAME integral by \(S_{10}\) (accuracy jump); error-budget planning ("how large
  must \(n\) be for \(\lvert E_T\rvert<10^{-4}\)?" — worked from Thm 8.4); a data-table integral
  (velocity readings → distance via Simpson; the no-formula-at-all client). All numeric values
  recomputed by sympy at sweep time.

## Per-section seam / fence guards (read before drafting each brief)

- **§8.1:** Product rule is Thm 2.6 — cite, do not re-derive. State the antiderivative-family
  reading of the indefinite identity honestly (both sides denote families; equality up to the one
  constant absorbed in the remaining integral sign). \(du/dv\) notation ties to §5.3 differentials
  (one clause). Reduction-formula example ends with the n=2 spot-check \(\int\sin^2\) against
  §A.2's power-reduction antiderivative (consistency, and a preview hook for §8.2). NO washer↔shell
  material (D3). NO \(\int e^{ax}\sin bx\) general formula (one concrete solve-back example only).
- **§8.2:** Every identity used is restated inline at point of use AND cited (Prop A.1 / Prop A.2 /
  §A.2 power-reduction) — B-class hygiene: the reader must not need to leave the page to follow.
  \(\ln\lvert\cdot\rvert\) domains: "on any interval avoiding the zeros of the denominator" — one
  blanket sentence at Prop 8.1, echoed per-example only when an example's interval matters.
  \(\int\sec^3\) example placed LAST (uses parts — cross-technique; name that explicitly). The
  \(\sin 4x\cos 5x\) example keeps Prop A.2's exact identity form (verbatim restated). No
  orthogonality/Fourier digression (one forward clause at most, unsourced claims prohibited).
- **§8.3:** The θ-range table is Strategy 8.4 and the SINGLE authority — every example's solution
  opens by naming its pattern + range, then resolves the radical with the range-justified sign
  (the per-example hygiene line ⑤ will check). Back-substitution by right triangle: label sides
  from the substitution, read off the needed ratios; state once that the triangle is a mnemonic
  for the identities, valid because θ sits in the stated range. Ellipse example: even-function
  symmetry (Thm 6.8) allowed but keep the computation direct (quarter-ellipse ×4). Completing the
  square: cite §A.5's identity, show the shift substitution explicitly (u = x+1 type). NO
  hyperbolic substitutions (D2). NO \(\int\sqrt{x^2+a^2}\) full derivation if it balloons — if
  included it must land on \(\sec^3\) (§8.2) cleanly; prefer the \(\frac{dx}{x^2\sqrt{x^2+4}}\)
  shape which stays short.
- **§8.4:** The algebra (finding constants) is REVIEWED in one opening example at most —
  §A.4 taught it; here every example's center of mass is the INTEGRATION of the fragments.
  FTA fence note placed before the case walk-through (it licenses "factor completely"). Cover-up
  gets one recalling clause with cross-ref, not a re-teach. \(\ln\) answers combined via log rules
  only when it genuinely simplifies (no forced consolidation — arbitrary-constant honesty).
  Rationalizing-substitution example explicitly frames the move: substitution FIRST (u² = x+4),
  rational function SECOND, partial fractions THIRD — technique chaining is the takeaway. NO
  Heaviside general theory beyond cover-up; NO complex-root factoring.
- **§8.5:** The four-step strategy box distills §§8.1–8.4 + Ch6 — it must cite, not restate, each
  technique's home. Table of standard forms: unnumbered display list, every entry already
  established in this book, each with its provenance in parentheses (§6.4 table, Prop 8.1, §8.4
  tag). Elementary-function honesty (③ B-02 form): none of this chapter's techniques produces an
  elementary antiderivative for \(\int e^{-x^2}\,dx\), and whether ANY elementary antiderivative
  exists is a question this book does not take up — no impossibility asserted, no credit taken;
  the constructive payoffs are §8.6 (the integral still converges) and §8.7 (numerics), one
  forward sentence each. Mixed examples chosen so the CLASSIFICATION is the work; solutions
  may compress standard sub-steps with a cross-ref (altitude: this section trains recognition,
  not re-execution).
- **§8.6:** Each type's definition precedes its own computation examples (Type 1 block: Def 8.1 →
  Ex 8.27–8.29 + principal-value caution; Type 2 block: Def 8.2 → Ex 8.30–8.31 + singularity
  caution), then p-test, then Comparison. 〔⑤ 8.6-B1 adjudication 2026-07-26: the original guard
  sentence "Definitions FIRST (both types), then computation examples" over-specified the order;
  the intent — no example before its governing definition — holds in the as-built interleaved
  (canon-standard) structure, and the guard is amended to match. Every example follows the
  definition it depends on.〕 Every convergence verdict must come from the definition or a named
  result — no "obviously converges". \(t\)-limit computations cite their tools (L'Hôpital Thm 5.5
  for \(te^{-t}\); basic limits §1.4). The split-point independence for \(\int_{-\infty}^\infty\)
  gets its one-sentence justification (additivity), not hand-waving. Comparison proof: the
  bracketing argument in full (it is short); the phrase "increasing and bounded above" must
  connect explicitly to Thm 4.1's sequence statement. Improper + unbounded-at-endpoint COMBINED
  cases (e.g. \(\int_0^\infty\)) — one sentence: split into one integral of each type. NO
  absolute/conditional convergence vocabulary (Ch11's); NO integral test statement (Ch11 §11.3
  cites OUR results, not vice versa; one forward clause allowed).
- **§8.7:** Approximation error defined (exact − approximate, sign convention stated). Midpoint
  rectangles = Def 6.2 Riemann sums with midpoint choice (cite; §6.2's header comment reserved
  the RULES for here — discharge). Trapezoid derived as BOTH average-of-L/R and sum-of-trapezoid
  areas (two short displays, then (T)). Simpson parabola lemma proved (algebra only; the
  \(x\)-symmetric setup \([-h,h]\) + shift argument); weights pattern 1,4,2,…,2,4,1 summed
  explicitly; \(n\) even caution. Thm 8.4 stated with \(K\) as ANY bound for \(\lvert f''\rvert\)
  on \([a,b]\) (existence guaranteed for continuous \(f''\) by EVT Thm 4.9(a) — one clause);
  fence note immediately after the theorem. Error-planning example must round \(n\) UP and say
  why. Data-table example: units tracked; Simpson chosen (n even verified). NO Richardson/Romberg;
  NO probabilistic error talk.

## Numbering ledger (Ch8 counters reset fresh; per-type continuous across sections) — LOCKED BEFORE DRAFTING

Cautions are UNNUMBERED (house convention). Objects NOT in this table MUST NOT be minted; a needed
addition goes through this table first (kickoff hard guardrail).

| type | §8.1 | §8.2 | §8.3 | §8.4 | §8.5 | §8.6 | §8.7 | total |
|---|---|---|---|---|---|---|---|---|
| Definition | — | — | — | — | — | **8.1** (Improper integral, Type 1) · **8.2** (Improper integral, Type 2) | — | 2 |
| Theorem | **8.1** (Integration by Parts, proved) · **8.2** (Parts for definite integrals, proved) | — | — | — | — | **8.3** (Comparison Theorem, proved) | **8.4** (Error bounds, on credit → Ch11) | 4 |
| Proposition | — | **8.1** (Antiderivatives of tan, cot, sec, csc; proved) | — | — | — | **8.2** (\(p\)-test, proved) | — | 2 |
| Corollary | — | — | — | — | — | — | — | 0 |
| Strategy | **8.1** (Choosing \(u\) and \(dv\)) | **8.2** (\(\sin^m\cos^n\)) · **8.3** (\(\tan^m\sec^n\)) | **8.4** (Trigonometric substitution) | **8.5** (Integrating a rational function) | **8.6** (A four-step strategy) | — | — | 6 |
| Example | **8.1–8.6** | **8.7–8.11** | **8.12–8.16** | **8.17–8.22** | **8.23–8.26** | **8.27–8.33** | **8.34–8.38** | **38 = cap** (M1 36 + M4 ×2) |
| Figure | **8.1** parts-uv-rectangle · **8.2** washer-split-monotone | **8.3** sin-squared-midline | **8.4** trig-sub-triangles (triple) · **8.5** ellipse-quarter-area | — | — | **8.6** tail-comparison · **8.7** type2-truncation · **8.8** interior-singularity · **8.9** monotone-sampling · **8.10** comparison-trap | **8.11** three-rules-panel (triple) · **8.12** midpoint-tangent-trap · **8.13** simpson-data-speed | **13**（M2 adopt-all-13 使用者裁決 2026-07-26；§8.4/§8.5 刻意零圖經 gate 覆核成立） |
| Equation tags | — | — | — | one tagged display for \(\int\frac{dx}{x^2+a^2}\) (tag **(8.A)**) | — | — | **(M)**, **(T)**, **(S)** | 4 tags |

Per-section example allocation (planned): §8.1 ×6 (x cos x · ln x · t²eᵗ · eˣ sin x · ∫₀¹ arctan ·
sinⁿ reduction) — §8.2 ×5 (sin³cos² · sin⁴ · tan⁶sec⁴ · sec³ · sin4x cos5x) — §8.3 ×5 (√(9−x²)/x² ·
ellipse area · 1/(x²√(x²+4)) · 1/√(x²−a²) · completing-the-square) — §8.4 ×6 (divide-first ·
distinct linear · repeated linear · irreducible quadratic · equal-degree+complete-square ·
rationalizing √(x+4)/x) — §8.5 ×4 (tan³/cos³ · e^√x · 1/(x√(ln x)) · √((1−x)/(1+x))) — §8.6 ×6
(1/x vs 1/x² · 1/(1+x²) over ℝ · te⁻ᵗ · type-2 pair · interior-singularity trap · comparison
e^{−x²}) — §8.7 ×4 (T₅/M₅ for ∫₁²dx/x · S₁₀ same · error planning · data table).

**As-built after M4 (2026-07-27), Example row only** — §8.6 ×**7** (the six above **+ Ex 8.33**,
∫₃^∞ dx/√(x²−x) diverges, the Thm 8.3**(b)** direction) — §8.7 ×**5** (T₅/M₅ · S₁₀ · error
planning · **+ Ex 8.37**, ∫₀¹e^{−x²} by S₁₀ with K₄ = 36 → four guaranteed decimals · data table).
Cascade actually performed: old 8.33–8.36 → **8.34–8.36 and 8.38**; 5 rendered cross-refs +
5 in-source ledger comments updated, env-num continuity 8.1–8.38 grep-verified.

> Chapter opener (chapter-head + lead + "By the end…") lives in **sec-8-1.html** (first
> `<article>`), per handout convention. `build.py` CHAPTERS registry gains `"ch08"` when
> `sec-8-1.html` first exists.

## Chapter opener — "By the end of this chapter you will be able to" (five bullets)

- integrate products, logarithms, and inverse trigonometric functions by parts;
- evaluate trigonometric integrals with the standard identities, and integrals containing quadratic radicals by trigonometric substitution;
- integrate rational functions by partial fractions, and choose an attack for an unfamiliar integral;
- decide whether an improper integral converges, by evaluation or by comparison, and evaluate it when it does;
- approximate a definite integral with the Midpoint, Trapezoidal, and Simpson's rules, and bound the error.

## Hypothesis-ledger themes (chapter-wide; per-section briefs instantiate)

- \(\ln\lvert\cdot\rvert\) antiderivatives valid per interval avoiding the singularity; constants
  differ per component interval (the §6.4 convention carries).
- θ-range discipline for inverse substitutions (sign of the resolved radical justified by range).
- Trig-sub parameters positive (③ A-01): \(a>0\) throughout, ellipse \(a,b>0\); each indefinite
  example solved on a NAMED connected domain component; the \(x\le-a\) secant branch handled in
  the caution via the alternate range \(\theta\in(\pi/2,\pi]\) (\(\tan\theta\le0\),
  \(\sqrt{x^2-a^2}=-a\tan\theta\)) or verification by differentiation.
- \(p\)-test covers ALL \(p\) (③ A-02): \(p\le0\) diverges by comparison with \(\int 1\,dx\)
  (Thm 6.2(4) on finite intervals); \(0<p\ne1\) by the power computation; \(p=1\) by \(\ln\).
- §8.7 regularity (③ A-03): Thm 8.4 hypotheses \(f''\) continuous on \([a,b]\) (T/M) and
  \(f^{(4)}\) continuous (S), bounds exist by EVT 4.9(a); equal width \(h=(b-a)/n\) built into
  the rules; data examples equally spaced, even \(n\) verified.
- Irreducibility test \(p^2<4q\) before declaring a quadratic irreducible.
- "Converges" = the defining limit exists as a finite number; every verdict traces to Def 8.1/8.2
  or Prop 8.2/Thm 8.3.
- Comparison needs \(0\le f\le g\) on the actual tail used; continuity keeps every finite piece an
  integral (Thm 6.1).
- Error bounds need a bound \(K\) valid on ALL of \([a,b]\); Simpson needs even \(n\).
- Parts on definite integrals needs \(f', g'\) continuous on \([a,b]\).

## Generation-side verification record (kickoff §2; single-arm)

Standing self-check after each section: `python handout/html/build.py ch08` +
`python tools/prose_metrics.py --unit ch08`. Record per-section numbers here as drafted; chapter
verdict after §8.7 against: **T_can ≤ 3.0/1000** em-dash density + four tic guards (colon-clause /
semicolon / parenthesis / paired-comma) + paragraph triggers; family-scan for lexical AI-tells.
Historical no-clause baselines to beat decisively: ch05 first-draft em-dash **14.4/1000**, family
**18.8/1000**; ch06 §6.2 family **14.7/1000**.

| unit (cumulative) | words (N) | em-dash /1000 | colon-clause | semicolon | parens | paired-comma | note |
|---|---|---|---|---|---|---|---|
| after §8.1 | 1162 | **0 → 0.0** | 18 | 2 | 5 | 13 | paired-comma 11.2/1000 noted; tightened from §8.2 on |
| after §8.2 | 2051 | 0 → 0.0 | 23 | 3 | 11 | 17 | §8.2 delta: colon 5.6/1000, comma 4.5/1000 ✓ |
| after §8.3 (+B-01 block) | 3279 | 0 → 0.0 | 38 | 11 | 20 | 29 | solution-style display-introducing colons dominate |
| after §8.4 | 4201 | 0 → 0.0 | 49 | 17 | 27 | 33 | semicolon 4.0/1000 = house range |
| after §8.6 (incl. §8.5) | 6345 | 0 → 0.0 | 82 | 28 | 66 | 54 | parens include the (Theorem N.M, part k) citation load |
| **after §8.7 (chapter, post self-edit + quote/linebreak fixes)** | **7751** | **0 → 0.0/1000** | 100 (12.9/1000) | 34 (4.4) | 84 (10.8) | 62 (8.0) | list/caption side-table N=639, 0 dash |

**Family scan (lexical R1 families; honest record, kickoff §2 「不可只修不記」):** drafting under
the clause set still leaked **15 family hits** in ~7.7k words (≈**1.9/1000** pre-self-edit) —
transaction metaphors (*earn their keep*, *banked*, *debts…repays*, *collects an asset*, *price/
reward*, "A debt repaid" heading), personification-lite (*deserves its reputation*, *saves the
integral*, *advertise*, *creeps*, *dies* for decay ×3), idioms (*ran on rails*, *the game is*,
*confident nonsense*). All 15 rewritten plain at the chapter sweep (self-caught, before any gate);
post-edit residue: the house-mechanism *on credit / borrowed / delivers* vocabulary (SPEC §16.1
protected) and the §8.2 *spend a factor / manufactured* device, which is introduced WITH its
literal statement in place (§3-compliant). Historical no-clause baselines: ch05 em-dash 14.4 /
family 18.8 per 1000; ch06 §6.2 family 14.7.

**Verdict ⛳ (recorded for the user, decision delegated this session): 達標.**
Em-dash 0.0/1000 vs target ≤3.0 (ch05 first-draft 14.4) — the clause set constrained generation
at the source, with zero dash-repair debt. Family leakage 1.9/1000 raw vs ch05's 18.8 (≈10×
lower), and self-edit at sweep took it to ≈0 outside protected mechanism vocabulary. Tic guard:
semicolons in house range; colon-clause 12.9/1000 and parens 10.8/1000 sit at the top of the
house band (appB 12.7; ch06 9.1) — driven by display-introducing solution colons and by
citation parentheses, not by dash-compensation; recorded for the clause layer to watch, no
rebalance performed (兩閘不可互相豁免 honored: no em-dash was traded into these). Paragraph
triggers: no paragraph ≥150 words. **Recommendation carried to the applied report: 「生成端就
受約束」成立 — the backfill round can retire for new chapters; evidence for clause v1.0.**

## Per-section status

| § | stage | env minted | Codex ⑤ (post-generation batch, 2026-07-26) |
|---|---|---|---|
| 8.1 Integration by Parts (+ch opener, +shell–washer block) | ✅ draft | Thm 8.1, Thm 8.2 (proved); Strategy 8.1; Ex 8.1–8.6 | **CLOSED 0 blocking**（r1: 1B shell–washer scope 重寫遞增情形＋1A Thm 8.2 改證 FTC-1＋Cor 4.4；回歸 R1/R2 clean）`ch08_s8-1-codex5-audit.md` |
| 8.2 Trigonometric Integrals | ✅ draft | Prop 8.1 (proved); Strategy 8.2, 8.3; Ex 8.7–8.11 | **CLOSED 0 blocking**（r1: 3B——cot 定義、Strategy 8.3 step 3 矛盾、csc³ 缺句；回歸 R3–R5 clean）`ch08_s8-2-codex5-audit.md` |
| 8.3 Trigonometric Substitution | ✅ draft | Strategy 8.4; Ex 8.12–8.16 | **CLOSED 0 blocking**（r1: 1B 圓情形反例＋1A 兩橋接；回歸 R6/R7 clean）`ch08_s8-3-codex5-audit.md` |
| 8.4 Partial Fractions | ✅ draft | Strategy 8.5; Ex 8.17–8.22; tag (8.A); 兩不編號 Caution（FTA fence＋irreducibility） | **CLOSED 0 blocking**（r1: 1B Caution 數量；回歸 R8 clean）`ch08_s8-4-codex5-audit.md` |
| 8.5 Strategy for Integration | ✅ draft | Strategy 8.6; Ex 8.23–8.26 | **CLOSED 0 blocking**（r1: 1B 裁決＝brief 錯標 step 2，brief 修訂；回歸 R9 clean）`ch08_s8-5-codex5-audit.md` |
| 8.6 Improper Integrals | ✅ draft | Def 8.1, 8.2; Prop 8.2 (proved); Thm 8.3 (proved); Ex 8.27–8.32 | **CLOSED 0 blocking**（r1: 2B——順序裁決＝guard 過度指定（本檔已修）＋開場歸因 M7 重寫；回歸 R10/R11 clean）`ch08_s8-6-codex5-audit.md` |
| 8.7 Approximate Integration (+ch summary) | ✅ draft | Thm 8.4 (on credit → Ch11); Ex 8.33–8.36; tags (M)(T)(S); fence caution | **CLOSED 0 blocking**（r1: 5B——括號語句、兩處 bound 過度宣稱、門檻數字、L/R display、42 km/h；回歸 R12–R15 clean）`ch08_s8-7-codex5-audit.md` |

> **章層 review（M1–M8 逐維明列）＋回歸**：M1/M2/M3/M4/M5/M6/M8 clean、M7＝CH-B1（＝8.1-B1，已修）；Ledger／Credit（恰兩筆）／Seams 全 clean；scoped 回歸 R1–R15 全 clean。`ch08_chapter-sweep-audit.md`

## M2 圖批次（2026-07-26，gate-1 側 CLOSED）

使用者指令開 M2、裁決 **adopt-all-13**（機會覆核 7 subagent：9 標記→13 候選／32 駁回；
§8.4/§8.5 刻意零圖成立）。Figure 8.1–8.13 全繪（ledger 表已回填；kit 擴充 fill-ghost／
fill-aux＋triple 版面 3×176px；作者自查修 9 處——含 Fig 8.11 區間 [1,3] 對機會閘 [1,2] 的
記錄性偏離）。**D1–D8 gate-1：13/13 視覺 blocking 歸零**（4 條 D1 advisory 全修：3× vline
越軸擦 tick 字同根因＋1× label 擦線）＋ **scoped 回歸 R1–R4 全 clean**。紀錄
`ch08_figure-audit.md`；報告 `_audit/REVIEW-ch08-figure-opportunity.html`（applied banner）＋
`_audit/REVIEW-ch08-figure-audit.html`（13 圖內嵌）。視覺 gate-2 依三閘規則留 M4 後批次。

> Free-gate terminal values at M1 draft close (2026-07-26): build ✔ · quote_lint clean ×7 ·
> linebreak-gate **0** auto-breaks (13 wide displays hand-broken) · render **math=979,
> katex-errors=0** · sympy **64/64 PASS** (all 36 examples + Prop 8.1 ×4 + (8.A) + p-test cases +
> Simpson lemma + shell–washer instance) · ledger continuous (Def ×2 / Thm ×4 / Prop ×2 /
> Strategy ×6 / Ex 8.1–8.36) · cross-refs 48 used, **0 dangling** · figure-opportunity markers
> ×9 · expansion markers ×21.

## M3 — 散文＋難度合一輪（2026-07-26）

Gate-1：`handout-prose-audit` ×7 ＋ `learner-sim` ×3 全章盲測（B 類 grep 預檢 PASS）。結果：
散文七節 **0 blocking**（advisory ≈94）；盲測 **3/3 零 stuck、零 B 類**，難度尖峰 §8.3／§8.6
≈3.5 ＜ Ch4 的 4.5——「標準/計算」深度成立、無弧線異常；紅旗 1（G1-8.6-10：§8.6 兩處逾越
③ B-02 的 e^{−x²} scope 紀律→列必修）。裁決（使用者親裁「照建議套用」）：**套用裁決項 66
＋必修 1（2 loci）＝落地 96 處文字替換**（腳本 94＋手補 2；spelling DEFER 書層 sweep、taste
級記錄不動）。〔口徑更正 2026-07-27：原記「69 編輯點」為壓縮前粗估，可驗證口徑為項級 66＋1／
文字級 96，詳 `ch08_prose-difficulty-audit.md`。〕修後機械閘：
build ✔ · quote_lint clean · linebreak 0 · **em-dash 仍 0.0/1000**。Scoped 回歸：**盲測
0 blocking／0 stuck／0 B 類**（三節全 ok、難度 3/3/2.5 持平偏低基線、sim 逐字引用新導航句判
「行內有給理由，走得完」）＋**散文複核 0 blocking**（69 修補句無新缺陷、B-02 措辭驗證乾淨）；
複核殘項採 2（§8.5 過渡句重排、§8.3 對齊 B-02 用語，均逐字採複核者措辭）／記錄 1（§8.4 K
非 finding）。**補正輪（2026-07-27）**：盲測實例數補齊為 **3 份獨立實例**（原只跑 1 份涵蓋
三節，係壓縮後執行落差）——三份合計 **0 blocking／0 stuck／0 B 類，gate PASS 不變**；兩新
實例另抓出 7 條單一實例漏掉的客觀缺陷（使用者親裁「7 條全修」：§8.7「constant 一半」撞義、
§8.6 未宣告別名 monotone convergence theorem、§8.1 shell–washer 單調性缺步與收尾抵消、
§8.7 Simpson 的 \(i\) 範圍、§8.1 Thm 8.2 轉折未承認、章開場「唯一沒倒著跑的法則」不成立），
其 scoped 複核 **0 blocking**＋3 條 advisory 就地再修。終值 **N=8214、em-dash 0.0/1000**、
semi 35（斷句淨減 2）。**M3 收案。**
逐條裁決與不採理由見 `ch08_prose-difficulty-audit.md`＋`_audit/REVIEW-ch08-prose-difficulty.html`。
散文 gate-2 依三閘規則留 M4 後批次。

## M4 — Mode C 條件式 gap-check（2026-07-27，CLOSED）

Gate-1 偵察 **4 份獨立實例**（`mode-c-gapwalk` ×2 順序／逆序全章＋`example-supplement` ×2 分半章），
依 M3 補正輪的教訓派雙實例。結果：①波 **4 候選全部 Layer 1**（沒有一筆是「題目不夠多」，全是
「本書自己陳述或證明了某件事卻從未示範」）；②波 48 筆去重後 **34 筆、全零 cascade**，其中
**12 個缺口被兩份實例獨立命中**，另有 **1 個跨波命中**（§8.1 的 reduction formula payoff 同時被報成
Layer 1 例題缺口與 intuition 缺口）。§8.3／§8.4／§8.5 三節例題判定為乾淨、零候選。
裁決稿 `_audit/REVIEW-ch08-modec-gapcheck.html`；完整紀錄 `ch08_modec-gapcheck-audit.md`。

**使用者裁決（2026-07-27）**：①波採 `8.7-E1`＋`8.6-E1`、`8.1-E1` 轉不編號推導、`8.2-E1` 不採；
②波採到 **T3**；四個品味題全採（含 `8.6-d` 重力功寫進難度尖峰節、`8.6-f` Gabriel's horn 一句、
`8.2-E1` 的 parity 診斷改做散文註、授權先查證再落筆 `8.2-a`）。

**落地 26 處**（2 worked example ＋ 24 段不編號內容）：§8.1 ×3・§8.2 ×3・§8.3 ×1・§8.4 ×3・
§8.5 ×1・§8.6 ×7・§8.7 ×6。**Example 收在 8.1–8.38 ＝ 38 ＝ D1 硬上限**，cascade 僅 4 個位移
（把 `8.1-E1` 轉成不編號推導段省掉了 30 個重編號，是本輪最大的一筆風險削減）。
一條 guard 依 8.6-B1 先例**誠實修訂**：`sec-8-6.html` header 原寫 `NO Gabriel's horn`，比 PLAN
`§Excluded` 的「至多一句」更嚴；採 `8.6-f` 後修訂該 guard 並記明理由，課文措辭維持在截斷體 \([1,t]\)。

**回歸（gate-1）**：範圍限定 Mode B ×3 → **4 blocking**（`8.4-b` 隱喻承載條件／`8.6-f` 不等式無理由／
`8.6-c` 條件靠模糊形容詞＋Ex 8.32 誤歸類／`8.7-a` `quadrature` 全書未定義）**全修**；
回歸複核 ×2 → **0 blocking**，四條原 blocking 逐條確認歸零，並抓出 **7 條我的修補自身引入的新缺陷**
（含「multiplying by \(e^{-x^2}\) cannot enlarge it」字面為假、一處懸垂分詞、一處前指落空）全修。
盲測 `learner-sim` ×3 全章 → **3/3 零 stuck／零 B 類**，曲線 `[4,3,3.5,3,2,4,2.5]`／`[3.5,3,3,3.5,2,4,3]`／
`[4,3,4,3,2,4,3]`，三份皆判與 Ch1–Ch4 基線持平或持平偏低、峰值未觸及 §4.2 的 4.5；
scoped §8.6 回歸盲測 **0 stuck、難度 3.5/5**，並確認位置修補後 Definition 8.1 的「see the caution below」
**零次走錯**。

**終值**：build ✔・quote_lint clean ×7・**linebreak 0**・sympy **59/59 PASS**（本輪寫進課文的每個數字與恆等式）・
render **math 1007→1378、MathJax err 0、未渲染 `\(` 0、13/13 圖 hydrate、cross-ref dangling 0**・
prose **N 8214→10502、em-dash 仍 0.0/1000**（四個 tic guard 密度全部下降，未發生標點代償）。
不編號 Caution 10→17。**M4 收案。三閘 gate-2 依 PIPELINE 留 M5 前批次。**

> **交給 gate-2 的既有內容發現（本輪不修，Mode C 無權限）** 共 7 條，詳見
> `ch08_modec-gapcheck-audit.md` §8。最重要一條：**Theorem 6.5（Ch6）與 Theorem 8.2 證明（Ch8）互斥**
> ——§6.4 說 Thm 6.5「applies verbatim from Thm 6.4」，§8.1 卻說 Thm 6.4「cannot be cited directly」
> 並自行建構 \(H\)。已逐字驗證兩章原文；判 §8.1 嚴謹、§6.4 超額宣稱，交數學 gate-2 定奪
> （Ch6 已定版含 LaTeX 線，動它須二模型確認）。

## Open questions (for the user, at chapter close)

1. **Inverse hyperbolic functions**: default NOT collected (D2). If wanted: appended §8.8, zero
   cascade. (kickoff §1 default; awaiting user.)
2. **Example budget: M4 closed the chapter at 38/38, the hard cap** (was 36 at M1). Both slots went
   to Layer-1 gaps where a numbered result had been stated and never exercised: Thm 8.4's Simpson
   clause (Ex 8.37) and Thm 8.3(b) (Ex 8.33). A third Layer-1 gap of the same kind (Ex 8.6's
   reduction formula, proved and never used) was discharged **without a slot**, as an unnumbered
   tagged derivation — see the M4 section. Ch7 by comparison closed at 23; the gap is the D1
   rationale (this chapter's examples ARE the content). **No headroom remains**: any example that
   the three gate-2 passes turn up must either replace one or go through D1 first.
3. **Thm 8.4 error bounds fenced forward to Ch11 §11.9** rather than Appendix D (D8 rationale);
   Ch11 must discharge — recorded in EXPORT section and to be echoed in ROADMAP Ch11 notes at M5.

## Scaffolding notes

- `chapter8-print-standalone.html` cloned from chapter7 per the 7-loci recipe (PLAN-ch06):
  title + brand + runningHead → Chapter 8 / Techniques of Integration; `FIGS` emptied to `{}`;
  content region cleared (build.py refills); dead `--fig-7-*` CSS width vars stripped; MathJax
  config + macros + paginator carried verbatim.
- `build.py` CHAPTERS registry: add `"ch08"` when `sec-8-1.html` first exists; fragments appended
  incrementally (ch05 pattern).
- M2 figure debt: `[FIGURE-OPPORTUNITY]` markers only at M1 (planned ~9–10: §8.1 uv-area diagram
  (optional) · §8.2 sin² midline · §8.3 right-triangle 3-panel (essential) + ellipse · §8.6 tail
  comparison (essential) + type-2 region + comparison squeeze · §8.7 three-rules panel (essential)
  + midpoint-tangent trapezoid); when figures land, fresh `--fig-8-*` width vars.
