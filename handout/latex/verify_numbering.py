#!/usr/bin/env python3
r"""verify_numbering.py —— P2 語意化的 U3 硬閘：編號輸出必須與轉換前逐一相同。

    python verify_numbering.py ch03 --before <轉換前.pdf>

三道檢查（任一不過＝非零退出）：
  1. aux 的 \newlabel：每個 <prefix>:<num> label 的印值＝<num>
     （語意化完成時點的 key 沿歷史號；此檢查只在遷移驗收時有意義，之後插入新內容
     會令 key 尾號≠印值——那是預期行為，不再跑本檢查）。
  2. 編號序列：pdftotext 抽新舊 PDF 的全部「Kicker N.M」token 序列，必須逐一相同。
  3. log 無 undefined reference。
"""

import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
UNITS = {
    "appA": "appendixA", "appB": "appendixB", "appC": "appendixC", "appD": "appendixD",
    "ch01": "chapter1", "ch02": "chapter2", "ch03": "chapter3", "ch04": "chapter4",
    "ch05": "chapter5", "ch06": "chapter6", "ch07": "chapter7", "ch08": "chapter8",
}
KICKERS = ("Example|Theorem|Definition|Proposition|Strategy|Remark|Corollary|"
           "Lemma|Caution|Figure")


def tokens(pdf):
    txt = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True,
                         text=True, encoding="utf-8", errors="replace").stdout
    return re.findall(rf"\b(?:{KICKERS})\s+[0-9A-D]+\.\d+", txt.replace("\u00a0", " "))


def main():
    if len(sys.argv) != 4 or sys.argv[2] != "--before" or sys.argv[1] not in UNITS:
        sys.exit(__doc__)
    ch, before = sys.argv[1], Path(sys.argv[3])
    name = UNITS[ch]
    after = HERE / "dist" / ch / f"{name}.pdf"
    aux = HERE / "build" / f"aux-{ch}" / f"{name}.aux"
    log = HERE / "build" / f"aux-{ch}" / f"{name}.log"
    ok = True

    labels = re.findall(r"\\newlabel\{([a-z]+:([0-9.A-Z]+))\}\{\{([^}]*)\}",
                        aux.read_text(encoding="utf-8", errors="replace"))
    mismatch = [(key, printed) for key, num, printed in labels if printed != num]
    print(f"{ch}: {len(labels)} labels; key-vs-print mismatch = {len(mismatch)}")
    if mismatch:
        ok = False
        for key, printed in mismatch[:10]:
            print(f"   {key} printed as {printed}")

    t_old, t_new = tokens(before), tokens(after)
    if t_old == t_new:
        print(f"{ch}: numbering token sequence identical ({len(t_new)} tokens)")
    else:
        ok = False
        print(f"{ch}: SEQUENCE MISMATCH old={len(t_old)} new={len(t_new)}")
        for i, (a, b) in enumerate(zip(t_old, t_new)):
            if a != b:
                print(f"   first diff at #{i}: old={a!r} new={b!r}")
                break

    logtxt = log.read_text(encoding="utf-8", errors="replace")
    undef = logtxt.count("undefined")
    if re.search(r"Reference .* undefined|There were undefined references", logtxt):
        ok = False
        print(f"{ch}: undefined references in log")
    else:
        print(f"{ch}: no undefined references")

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
