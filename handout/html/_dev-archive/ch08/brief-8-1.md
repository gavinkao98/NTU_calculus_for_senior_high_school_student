# Direction brief — §8.1 Integration by Parts

Canon variant (Stewart ET 9e §7.1; cross-check Thomas 14e §8.2, Rogawski 4e §7.1). Written
2026-07-26 per PLAN-ch08 D3. First section drafted under SPEC §3 plain register (generation-side).
Chapter opener (chapter-head + lead + five outcome bullets, PLAN §opener) rides in this fragment's
first `<article>`.

- **Canon inventory (Stewart §7.1):** the parts formula from the product rule; \(u\)-\(dv\)
  notation; examples x sin x / ln x / t²eᵗ / eˣ sin x (solve-back); definite-integral version with
  boundary term; reduction formula for \(\sin^n\).
- **Thinness:** canon states the indefinite identity without saying what an equation between
  indefinite integrals MEANS (families of antiderivatives; the one constant absorbed into the
  remaining integral). This book says it in one honest sentence. Canon also under-explains WHY the
  parts trade helps (derivative of the chosen \(u\) simpler; \(dv\) integrable in isolation) —
  Strategy 8.1 carries it.
- **Scope & depth (標準/計算):** **Theorem 8.1 (Integration by Parts)**: \(f, g\) differentiable
  on an open interval \(I\), \(\int f(x)g'(x)\,dx = f(x)g(x) - \int f'(x)g(x)\,dx\), meaning: on
  \(I\), \(fg\) minus any antiderivative of \(f'g\) is an antiderivative of \(fg'\). Proof = 3
  lines from product rule (Thm 2.6) + Def 6.3. Then \(u\)-\(dv\) notation (\(du = u'\,dx\) ties to
  §5.3 differentials, one clause). **Theorem 8.2 (parts for definite integrals)**: \(f', g'\)
  continuous on \([a,b]\) ⇒ \(\int_a^b f g' = [fg]_a^b - \int_a^b f' g\); proof: \((fg)' = f'g +
  fg'\) is continuous, apply FTC-2 (Thm 6.4) and rearrange (linearity Thm 6.2(2)). Mirrors the Ch6
  pair 6.6/6.7. Introduce-before-use: nothing B-class new.
- **Load-bearing intuition (one):** substitution (Ch6) undoes the chain rule, but a product like
  \(x\cos x\) has no inner function whose derivative is present — substitution has nothing to
  grab. Collision shown on \(\int x\cos x\,dx\) BEFORE the theorem. The product rule is the rule
  we have not yet run backwards; running it backwards trades one integral for another, and the
  trade is progress when \(u\) simplifies under differentiation. Parts = "trade the integral, not
  solve it" — the first technique that transforms rather than evaluates.
- **Worked examples (6; PLAN ledger Ex 8.1–8.6, answers pre-verified, sympy at sweep):**
  - **Ex 8.1** \(\int x\cos x\,dx = x\sin x + \cos x + C\) (first trade; also shows the wrong
    choice \(u=\cos x\) making the integral worse — inside solution prose, one display).
  - **Ex 8.2** \(\int\ln x\,dx = x\ln x - x + C\) (the \(dv = dx\) move; \(x>0\) domain named;
    cites \((\ln x)' = 1/x\), Thm 4.14).
  - **Ex 8.3** \(\int t^{2}e^{t}\,dt = (t^{2}-2t+2)e^{t} + C\) (parts twice; degree drops each
    round).
  - **Ex 8.4** \(\int e^{x}\sin x\,dx = \tfrac{1}{2}e^{x}(\sin x - \cos x) + C\) (parts twice
    reproduces the unknown integral; solve for it — the solve-back move; check by differentiating,
    one line).
  - **Ex 8.5** \(\int_0^1 \arctan x\,dx = \tfrac{\pi}{4} - \tfrac{\ln 2}{2}\) (Thm 8.2 with
    boundary term; inner integral \(\int_0^1 \frac{x}{1+x^2}\,dx = \tfrac12\ln 2\) by substitution
    Thm 6.7; arctan derivative cited to Ex 3.16).
  - **Ex 8.6** reduction formula \(\int\sin^{n}x\,dx = -\tfrac{1}{n}\cos x\sin^{n-1}x +
    \tfrac{n-1}{n}\int\sin^{n-2}x\,dx\) (integer \(n\ge 2\); Pythagorean identity + solve-back;
    spot-check \(n=2\) against §A.2's power-reduction antiderivative \(\tfrac{x}{2} -
    \tfrac{\sin 2x}{4}\) — consistency line + preview hook for §8.2).
- **History / application:** none as blocks (technique section; §8.7's data example carries the
  chapter's applied weight). Recorded as deliberate.
- **figure_opportunities** (mark now, draw at M2): (a) the uv-rectangle diagram — area of the
  \([0,u]\times[0,v]\) rectangle split by the curve \((u(t),v(t))\) into \(\int u\,dv\) and
  \(\int v\,du\) (optional tier; diagram; why-the-formula-balances picture; requires monotone
  parametrization — domain fact for the drawing). No other figure carries weight here (algebraic
  section). Record sparsity as deliberate.
- **Emphasis / takeaway:** concept pivot = *parts trades \(\int u\,dv\) for \(\int v\,du\); the
  product rule run backwards*; portable skill = choose \(u\) by "simpler under differentiation"
  (Strategy 8.1), recognize the \(dv=dx\) and solve-back patterns.
- **Shell–washer discharge (③ B-01, added post-audit):** closing subsection "A debt repaid" —
  unnumbered prose derivation (expansion:formula) proving shell = washer for \(f\) strictly
  decreasing + smooth with smooth inverse \(g\) (parts Thm 8.2 with \(dv=2x\,dx\) + substitution
  Thm 6.7 + §6.2 sign convention); Ex 7.12's Ch8 promise discharged, general case explicitly left
  to Ch15. Zero new numbered objects.
- **Deliberately omit (auditor's reverse check):** washer↔shell in FULL generality (Ch15's change
  of variables, said explicitly in the discharge block); general \(\int e^{ax}\sin bx\) formula
  (one concrete solve-back only);
  tabular/DI-method shortcut (not house style); reduction formulas beyond \(\sin^n\) (cos/sec
  variants mentioned in one clause, not derived); any improper-integral use (§8.6's).
- **Length band:** ~200–250 fragment lines (chapter opener included).
- **Env minted (per PLAN ledger):** Theorem 8.1, Theorem 8.2 (both proved); Strategy 8.1;
  Examples 8.1–8.6. Cautions unnumbered (candidates: sign slip in \(-\int v\,du\); the constant
  of integration appears once, at the last integral). Counters handed to §8.2: Proposition 8.1,
  Strategy 8.2, Example 8.7.
