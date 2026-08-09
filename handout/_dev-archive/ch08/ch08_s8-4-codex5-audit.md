# §8.4 Partial Fractions — Codex ⑤ audit record (raw JSON gitignored)

2026-07-26. gpt-5.6-terra／max, read-only, output-schema, post-generation batch.

## Round 1 — 1 blocking, 0 advisory

- **[8.4-B1｜direction-conformance｜BLOCKING]** brief + PLAN env ledger required **two**
  unnumbered Cautions (FTA fence; irreducibility check) and the fragment header claimed both,
  but only the FTA fence existed as an `env-caution` — the irreducibility test lived only inside
  Strategy 8.5's step 2. Environment count/type violation. **Fix**: irreducibility Caution added
  after Ex 8.20 (discriminant test + the \(x^2-x-6=(x-3)(x+2)\) trap example).

Auditor-verified clean (math and hygiene 0 blocking): Ex 8.17–8.22 all divisions, factorizations,
constants, and antiderivatives recomputed; (8.A) derivation; FTA fence wording (first credit);
case-IV statement-only handling; interval-of-validity lines; rationalizing-substitution chaining;
§A.4/§A.5 imports and promise discharges.

## Round 2 (scoped regression) — see `ch08_chapter-sweep-audit.md` §regression

**Status: §8.4 ⑤ CLOSED — 0 blocking after repair + regression.**
