# LaTeX writing contract — 講義章節源（`src/<ch>/<name>.tex`）

> **權威撰稿標記契約（2026-08-09 LaTeX 統一起）**，取代 HTML 時代的
> [`../html/CONTRACT-html-writing.md`](../html/CONTRACT-html-writing.md)（後者隨 fragment 凍結，
> 留檔供讀歷史源）。Register 與 correctness 規則與舊契約**逐字等義**（它們與格式無關）；
> 變的只有表層標記——以及編號：**手寫編號時代結束，一律語意化**（見 §Numbering）。
> 內容撰寫規則（用語、密度、§16 難度、圖規範）仍以 [`../../CONTENT_SPEC.md`](../../CONTENT_SPEC.md)
> 為準；本檔只管「怎麼把內容寫成合法的 `.tex` 源」。

---

## Output shape

一章一檔：`src/<ch>/<name>.tex`，自足可編譯（模板由 `\usepackage{calcbook}` 供給，
語意指令定義在 [`template/calcbook.sty`](template/calcbook.sty)——**只用語意層指令，
不手排樣式**：不寫 `\vspace`／`\textbf` 調版面、不 invent 環境；樣式歸模板管）。

```latex
\documentclass[a4paper,12pt,oneside]{memoir}
\makeatletter\def\input@path{{../../template/}}\makeatother
\def\cbfontsdir{../../template/fonts/inter/}
\usepackage{calcbook}
\graphicspath{{../../chapters/}}
\begin{document}
\cbchapter{8}                       % 章號（附錄用字母：\cbchapter{A}）；counter 語意層的錨
\chapteropener{Chapter 8}{Techniques of Integration}
\begin{lead} … \end{lead}
\parahead{By the end of this chapter, you will be able to:}
\begin{objectives} \item …；\item … \end{objectives}
\sechead{8.1}{Integration by Parts}
Prose. Inline math \(a^2+b^2=c^2\); display \[ \int_0^1 x^2\,dx=\tfrac13. \]
% environments follow
\end{document}
```

附錄開場用 `\appendixopener{Appendix B}{…}`。節標題 `\sechead{N.M}{Title}`、
小節 `\subsechead{Title}`、段落小標 `\parahead{…}`——**節號目前仍為字面**（章結構在
brief 期凍結，插節極罕見；環境與圖才是 cascade 痛點、已語意化）。

## Register（與舊契約逐字等義）

- Stewart／Rogawski 自學語域：a motivated high-schooler 讀得動；完整句、顯式連接詞；
  直覺先於形式；warm but not chatty；預設代名詞 **we**。
- 每個形式陳述（definition／theorem／proposition／corollary）**之前**要有 1–2 段直覺
  說明為什麼值得引入。定義主體結尾可加一段 *“Informally, …”* gloss——用
  `\begin{informal} … \end{informal}`。

## Semantic environments — 只用這些，不 invent

環境三參數簽名一律 `{kicker}{num-or-key}{name}`（皆必填、可空 `{}`）：

```latex
\begin{workedexample}
\begin{envexample}{Example}{ex:parts-tabular}{Optional descriptive name}
  Prompt prose …
\end{envexample}
\begin{envsolution}{Solution}{}{}
  … \qedmark
\end{envsolution}
\end{workedexample}
```

| 環境 | 教學角色 | 備註 |
|---|---|---|
| `envdefinition` | concept（teal） | 被定義詞用 `\emph`；選配 `informal` gloss |
| `envtheorem`／`envproposition`／`envcorollary` | result（blue） | 主體自動斜體、數學保持直立；Lemma＝`envtheorem` 配 kicker `Lemma` |
| `envexample`＋`envsolution` | practice（green） | **一律成對**包在 `workedexample` 內，無 solo example |
| `envremark` | aside（gray） | 短附註；具名輕量規則用 name 參數 |
| `envproof` | subordinate | 結尾 `\qedmark`；qualified proof（*Proof of Theorem …（⇒ direction）*）kicker 保持 `Proof`、qualifier 放 name 參數 |
| `envcaution` | ⚠ red solid box | 一個陷阱、1–3 句；**不編號**（num 參數空；ch01 的 8 個編號 Caution 為歷史保留） |
| `envstrategy` | violet solid box | 有號方法；步驟用 `\begin{steps} \item … \end{steps}` |
| exercise | **不得出現** | 講義不收習題（獨立習題本；`CONTENT_SPEC.md` §14，2026-06-12 定案） |

清單語彙：`steps`（方法步驟）／`sol-list`（解答分步）／`warmup`（(a)(b)(c) 觀察）／
`objectives`（章目標）；一般列表用標準 `itemize`／`enumerate`。QED：解答與證明的結尾
一律 `\qedmark`（`calcbook.sty`：`\unskip\nobreak\hfill\qedsymbol`）。

## Math（LuaLaTeX——真 TeX，無白名單問題）

- Inline `\( … \)`；display `\[ … \]`。**一個局部單元一種 display mode**——不要在同一步
  混用行內結果與多行推導。
- 多行對齊推導：`\[ \begin{aligned} a &= b \\ &= c. \end{aligned} \]`
- **寬顯示式一律手動斷行**（`aligned` 分行；權威規則＝`CONTENT_SPEC.md` §數學排版
  「寬顯示式的斷行」——TeX 不會像 MathJax 自動硬斷，超寬直接 overfull，由版面閘抓）。
- 式子標記用具名 `\tag{8.A}`／`\tag{M}`（不進序列編號系統）；散文引用寫字面 “(8.A)”。

## Numbering and cross-references —— 與 HTML 時代**相反**：一律語意化（U3）

模板機制（`calcbook.sty` 編號語意層）：num 參數**含 `:` ＝ label key**——自動
refstep 該 kicker 的 counter（每型獨立、章內連續、`\cbchapter` 供章號）、印「章號.序」、
`\label{key}`。純字面數字照印（僅供歷史相容，**新內容不得手寫編號**）。

- **新環境**：num 參數給語意 key——`{thm:ibp-definite}`、`{ex:parts-tabular}`、
  `{fig:tail-comparison}`。prefix 表：`def:`／`thm:`／`prop:`／`cor:`／`lem:`／`ex:`／
  `strat:`／`rem:`／`caut:`（僅歷史）／`fig:`。key 用小寫-連字號描述**教學重點**，
  不含編號（key 不承諾等於印值；2026-08-09 語意化遷移產生的 `ex:8.3` 型歷史 key 除外）。
- **圖**：`\figcaption{fig:<key>}{Sentence-case caption ending with a period.}`——模板印
  「Figure 章號.序」並 `\label`。
- **章內引用**：`Theorem \ref{thm:ibp}`、`Examples \ref{ex:a} and \ref{ex:b}`——kicker
  單詞字面寫出＋`\ref`（普通空格）。款式引用把款留在外面：`Theorem \ref{thm:mvt}(a)`。
- **跨章引用一律字面**（`Theorem 6.4`——單章獨立編譯，不引 xr/zref 機制）；被引章若
  重編號，跨章字面引用要跟著批改（罕見；書層 sweep 處理）。
- **插入新環境不再 cascade**：counter 自動後移、`\ref` 自動解析——這正是語意化買到的
  紅利。驗證：`python verify_numbering.py <ch> --before <舊 PDF>`（遷移期）；日常改稿後
  `python build.py <ch>` 的 log 無 undefined reference 即可。

## Marking expansion（LaTeX 註解形式）

超出 spine／brief 的每處增添，前一行掛 LaTeX 註解（categories 與 HTML 時代同：
`history`／`application`／`formula`／`summary`／`figure`／`example`／`intuition`／
`strategy`／`caution`；`[pass:]` 在 `[source:]` 前）：

```latex
% expansion:intuition [pass: enrichment] [source: canon §7.2] — one-line description
```

**存量 provenance 的家＝凍結 fragment**（12 單元的 `<!-- expansion:… -->` 與
`<!-- section-source: -->` header 在 `../html/fragments/`，轉換時未帶進 `.tex`——查歷史
標記去那裡 grep）；**增量從本規則起在 `.tex` 註解**。

## Prose typography

- 強調一律 `\emph`——散文不用 `\textbf`。
- 散文直書真 Unicode（檔案 UTF-8、LuaLaTeX 原生）：曲引號 “ ” ’、en/em dash – —、×、≤。
  數學符號走數學模式，不用 Unicode 替身。`quote_lint.py` 掃散文 ASCII 直引號（P3 起掃 `.tex`）。
- 平實條款（em-dash 密度等）：`CONTENT_SPEC.md` §3 為準，生成端達標（Ch8 先例）。

## Figures

圖的**繪製**不在 `.tex`：JS 圖 kit（[`../figkit/`](../figkit/README.md) harness 的 `FIGS`）
畫 SVG → `export_figs.mjs` 匯向量 PDF 到 `chapters/<ch>/figs/`。`.tex` 裡只有版位與說明：

```latex
\begin{figureblock}
  \includegraphics[width=79.9mm]{ch08/figs/tail-comparison}
\figcaption{fig:tail-comparison}{Sentence-case caption ending with a period.}
\end{figureblock}
```

- `width` 由作者定（mm；`figures.json` 的量測 mm 供初值參考）——排版決策住 `.tex`。
- **Label economy**：圖面上只留最少（軸標、曲線名、至多一個短錨），區域命名、公式、
  延伸說明放 caption 與正文（權威規則＝`CONTENT_SPEC.md` §10）。
- 多 panel：`export_figs` 每 panel 一檔（`-1`／`-2` 後綴），`figureblock` 內並排多個
  `\includegraphics`＋panel note 由圖 kit 的 note 機制供給。

## Correctness（hard constraint，與舊契約逐字等義）

Every mathematical claim MUST be correct and standard. Do NOT invent theorems, identities,
named results, or historical attributions. If unsure a claim is true, omit it rather than
guess. Named results, subtle proofs, and historical notes are human-checked.

## 驗收與工具鏈

改完源必跑 `python build.py <ch>`（編譯閘＋overfull 列表＋字形閘→成品進 dist）；
內容閘鏈（數學 M1–M8／散文 S·A·V／難度 sim／圖 D1–D8）讀 `.tex` 源與 harness 圖 PNG，
閘序見 [`../PIPELINE.md`](../PIPELINE.md)。
