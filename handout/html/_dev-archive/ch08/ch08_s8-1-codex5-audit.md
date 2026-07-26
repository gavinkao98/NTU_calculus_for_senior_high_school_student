# §8.1 Integration by Parts — Codex ⑤ audit record (raw JSON gitignored)

2026-07-26. gpt-5.6-terra／max, `codex exec -s read-only`, output-schema, post-generation batch
(kickoff v3 order). Session grant: user authorized standing Codex calls + delegated 拍板.

## Round 1 — 1 blocking, 1 advisory

- **[8.1-B1｜hypothesis-hygiene｜BLOCKING]** Shell–washer subsection claimed to "settle the case
  that covers every example of §7.3", but the derivation assumed strictly *decreasing* smooth
  \(f\) with a *smooth* inverse — which covers **none** of §7.3's shipped examples: Ex 7.12 (the
  promise site) uses \(f(x)=x^2\), increasing, with \(g(y)=\sqrt y\) whose derivative blows up at
  \(0\) (not smooth); Ex 7.10/7.11 are nonmonotone. Same defect flagged at chapter level (CH-B1).
  **Fix**: block reworked to the strictly **increasing** smooth case with a merely **continuous**
  inverse (continuity is all any step uses — Thm 6.7 needs only the outer function \(g^2\)
  continuous; nothing differentiates \(g\)); Ex 7.12 instantiated explicitly (common value
  \(\pi/2\) shown); scope sentence now honest ("the solid §7.3 actually compared, and every solid
  of that monotone kind"); decreasing case = mirror note; nonmonotone case explicitly → Ch15.
- **[8.1-A1｜hypothesis-hygiene｜Advisory→applied]** Thm 8.2's proof invoked FTC-2 (Thm 6.4),
  whose shipped statement requires an antiderivative on an **open interval containing** \([a,b]\);
  §7.6-smoothness supplies only C¹ on \([a,b]\) (one-sided at endpoints) — hypothesis bridge gap.
  **Fix**: proof rewritten without FTC-2: accumulation antiderivative
  \(H(x)=\int_a^x(f'g+fg')\), FTC-1 (Thm 6.3) + product rule on the interior + Corollary 4.4
  (constant difference) + endpoint evaluation. All cited hypotheses now met exactly.

Auditor-verified clean: Thm 8.1 statement+proof; Strategy 8.1; Ex 8.1–8.6 all recomputed correct
(incl. the wrong-choice display, the solve-back constant discipline, the n=2 §A.2 spot-check);
opener bullets; §6.5-promise discharge; cross-refs.

## Round 2 (scoped regression, all-fixes call) — see `ch08_chapter-sweep-audit.md` §regression

**Status: §8.1 ⑤ CLOSED — 0 blocking after repair + regression.**
