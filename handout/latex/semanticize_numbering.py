#!/usr/bin/env python3
r"""semanticize_numbering.py —— P2 編號語意化的一次性確定性轉換（U3）。

    python semanticize_numbering.py ch03           # dry-run：只印統計
    python semanticize_numbering.py ch03 --write   # 寫回 src/<ch>/<name>.tex

把字面編號轉為 auto-counter＋\label/\ref（模板端機制見 calcbook.sty「編號語意層」）：
  1. 編號環境第 2 參：{Theorem}{8.1}{…} → {Theorem}{thm:8.1}{…}
  2. \figcaption{Figure 8.3} → \figcaption{fig:8.3}
  3. \begin{document} 後注入 \cbchapter{<章號>}（冪等）
  4. 章內散文引用：Example 8.10 → Example \ref{ex:8.10}（普通空格保留＝版面保真）；
     複數列表（and／through／en-dash／逗號）逐號轉；款式 4.9(a) 的 (a) 留在 \ref 外。
     跨章引用一律不動（字面）。
轉完後跑 verify_numbering.py：印出編號序列必須與轉換前 PDF 逐一相同（U3 硬閘）。
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

UNITS = {
    "appA": ("appendixA", "A"), "appB": ("appendixB", "B"),
    "appC": ("appendixC", "C"), "appD": ("appendixD", "D"),
    "ch01": ("chapter1", "1"), "ch02": ("chapter2", "2"), "ch03": ("chapter3", "3"),
    "ch04": ("chapter4", "4"), "ch05": ("chapter5", "5"), "ch06": ("chapter6", "6"),
    "ch07": ("chapter7", "7"), "ch08": ("chapter8", "8"),
}

PREFIX = {
    "Example": "ex", "Theorem": "thm", "Definition": "def", "Proposition": "prop",
    "Strategy": "strat", "Remark": "rem", "Corollary": "cor", "Lemma": "lem",
    "Caution": "caut", "Figure": "fig",
}
PLURAL = {
    "Examples": "Example", "Theorems": "Theorem", "Definitions": "Definition",
    "Propositions": "Proposition", "Strategies": "Strategy", "Remarks": "Remark",
    "Corollaries": "Corollary", "Lemmas": "Lemma", "Figures": "Figure",
    "Cautions": "Caution",
}


def semanticize(ch, write):
    name, chnum = UNITS[ch]
    path = HERE / "src" / ch / f"{name}.tex"
    tex = path.read_text(encoding="utf-8")
    stats = {}

    # 1. env definition sites --------------------------------------------------
    def env_repl(m):
        env, kicker, num = m.groups()
        if not num or ":" in num:
            return m.group(0)
        stats[f"env:{kicker}"] = stats.get(f"env:{kicker}", 0) + 1
        return f"\\begin{{{env}}}{{{kicker}}}{{{PREFIX[kicker]}:{num}}}"

    tex = re.sub(r"\\begin\{(env[a-z]+)\}\{([A-Za-z]*)\}\{([0-9.A-Z]*)\}", env_repl, tex)

    # 2. figcaption definition sites ------------------------------------------
    n_fig = len(re.findall(r"\\figcaption\{Figure ([0-9.A-Z]+)\}", tex))
    tex = re.sub(r"\\figcaption\{Figure ([0-9.A-Z]+)\}", r"\\figcaption{fig:\1}", tex)
    if n_fig:
        stats["figcaption"] = n_fig

    # 3. \cbchapter injection --------------------------------------------------
    if "\\cbchapter{" not in tex:
        tex = tex.replace("\\begin{document}", f"\\begin{{document}}\n\\cbchapter{{{chnum}}}", 1)
        stats["cbchapter"] = 1

    # 4. in-chapter prose references -------------------------------------------
    num_pat = rf"{re.escape(chnum)}\.\d+"

    def ref_of(kicker, num):
        return f"\\ref{{{PREFIX[kicker]}:{num}}}"

    # plural lists first: each bare in-chapter number inside the list -> \ref
    plural_names = "|".join(PLURAL)
    list_re = re.compile(
        rf"\b({plural_names})(\s+)({num_pat}(?:(?:,\s*|\s+and\s+|\s+through\s+|–|—|-)\s*(?:{num_pat}))*)")

    def plural_repl(m):
        pl, sp, lst = m.groups()
        kicker = PLURAL[pl]
        out = re.sub(num_pat, lambda n: ref_of(kicker, n.group(0)), lst)
        k = f"ref-plural:{kicker}"
        stats[k] = stats.get(k, 0) + len(re.findall(num_pat, lst))
        return f"{pl}{sp}{out}"

    tex = list_re.sub(plural_repl, tex)

    # singular: Kicker N.M with optional (a) clause kept outside the \ref
    sing_names = "|".join(PREFIX)
    sing_re = re.compile(rf"\b({sing_names})(\s+)({num_pat})(\([a-z]\))?")

    def sing_repl(m):
        kicker, sp, num, clause = m.groups()
        k = f"ref:{kicker}"
        stats[k] = stats.get(k, 0) + 1
        return f"{kicker}{sp}{ref_of(kicker, num)}{clause or ''}"

    tex = sing_re.sub(sing_repl, tex)

    # residual bare in-chapter numbers preceded by a kicker word should be zero
    residual = re.findall(rf"\b(?:{sing_names}|{plural_names})\s+{num_pat}", tex)

    total = sum(stats.values())
    print(f"{ch}: {total} rewrites  {dict(sorted(stats.items()))}")
    if residual:
        print(f"{ch}: WARNING {len(residual)} residual bare refs: {residual[:5]}")
    if write:
        path.write_text(tex, encoding="utf-8", newline="\n")
        print(f"{ch}: written")
    return residual


def main():
    args = [a for a in sys.argv[1:] if a != "--write"]
    write = "--write" in sys.argv
    if len(args) != 1 or (args[0] != "all" and args[0] not in UNITS):
        sys.exit(__doc__)
    targets = list(UNITS) if args[0] == "all" else [args[0]]
    bad = []
    for ch in targets:
        if semanticize(ch, write):
            bad.append(ch)
    if bad:
        sys.exit("residual refs in: " + ",".join(bad))


if __name__ == "__main__":
    main()
