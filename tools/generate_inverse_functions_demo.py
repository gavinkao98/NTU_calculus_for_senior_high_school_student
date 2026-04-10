from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_FILE = REPO_ROOT / "chapters" / "ch01_foundations.tex"
SCHEMA_FILE = REPO_ROOT / "schemas" / "slide_deck.schema.json"

DECK_ID = "ch01_inverse_functions"
SECTION_TITLE = "Inverse Functions and One-to-One Functions"

SLIDE_SPEC_PATH = REPO_ROOT / "artifacts" / "slide_spec" / f"{DECK_ID}.json"
SLIDES_TEX_PATH = REPO_ROOT / "artifacts" / "slides" / f"{DECK_ID}.tex"
SLIDES_PDF_PATH = REPO_ROOT / "artifacts" / "slides" / f"{DECK_ID}.pdf"
SCRIPT_MD_PATH = REPO_ROOT / "artifacts" / "scripts" / f"{DECK_ID}.md"


def ensure_file_exists(path: Path, description: str) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Missing {description}: {path}")
    if not path.is_file():
        raise FileNotFoundError(f"Expected a file for {description}: {path}")


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def read_text(path: Path) -> str:
    ensure_file_exists(path, "input LaTeX source")
    return path.read_text(encoding="utf-8")


def extract_named_block(text: str, command: str, title: str) -> str:
    pattern = re.compile(
        rf"\\{command}\{{{re.escape(title)}\}}(.*?)(?=\\{command}\{{|\\chapter\{{|\Z)",
        re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        raise ValueError(f"Unable to find {command} '{title}' in source.")
    return match.group(1).strip()


def extract_environment_contents(text: str, environment: str) -> list[str]:
    pattern = re.compile(
        rf"\\begin\{{{environment}\}}(?:\[[^\]]*\])?\s*(.*?)\\end\{{{environment}\}}",
        re.DOTALL,
    )
    return [match.group(1).strip() for match in pattern.finditer(text)]


def extract_titled_environment_content(
    text: str, environment: str, title: str
) -> str:
    pattern = re.compile(
        rf"\\begin\{{{environment}\}}\[{re.escape(title)}\]\s*(.*?)\\end\{{{environment}\}}",
        re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        raise ValueError(f"Unable to find {environment} titled '{title}'.")
    return match.group(1).strip()


def extract_environment_blocks(text: str, environment: str) -> list[str]:
    pattern = re.compile(
        rf"\\begin\{{{environment}\}}(?:\[[^\]]*\])?\s*.*?\\end\{{{environment}\}}",
        re.DOTALL,
    )
    return [match.group(0).strip() for match in pattern.finditer(text)]


def extract_display_math(block: str) -> list[str]:
    pattern = re.compile(r"\\\[(.*?)\\\]", re.DOTALL)
    matches: list[str] = []
    for match in pattern.finditer(block):
        body = match.group(1).strip()
        matches.append("\\[\n" + body + "\n\\]")
    return matches


def first_paragraph(text: str) -> str:
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    if not paragraphs:
        raise ValueError("Unable to extract the first paragraph from the section.")
    return paragraphs[0]


def sanitize_figure_block(block: str) -> str:
    without_begin = re.sub(r"^\\begin\{figure\}\[[^\]]*\]\s*", "", block, count=1)
    before_caption = without_begin.split("\\caption{", 1)[0]
    without_end = re.sub(r"\\end\{figure\}\s*$", "", before_caption)
    return without_end.strip()


def require_list_length(items: list[Any], expected_minimum: int, label: str) -> None:
    if len(items) < expected_minimum:
        raise ValueError(
            f"Expected at least {expected_minimum} {label}, found {len(items)}."
        )


def build_deck(source_text: str) -> dict[str, Any]:
    section_text = extract_named_block(source_text, "section", SECTION_TITLE)

    definitions = extract_environment_contents(section_text, "definition")
    examples = extract_environment_contents(section_text, "example")
    solutions = extract_environment_contents(section_text, "solution")
    remarks = extract_environment_contents(section_text, "remark")
    theorems = extract_environment_contents(section_text, "theorem")
    propositions = extract_environment_contents(section_text, "proposition")
    figures = extract_environment_blocks(section_text, "figure")

    require_list_length(definitions, 2, "definitions")
    require_list_length(examples, 3, "examples")
    require_list_length(solutions, 3, "solutions")
    require_list_length(remarks, 4, "remarks")
    require_list_length(theorems, 1, "theorems")
    require_list_length(propositions, 1, "propositions")
    require_list_length(figures, 1, "figures")

    definition_math = extract_display_math(definitions[0])
    student_example_math = extract_display_math(examples[0])
    student_solution_math = extract_display_math(solutions[0])
    math_example_math = extract_display_math(examples[1])
    math_solution_math = extract_display_math(solutions[1])
    horizontal_line_math = extract_display_math(
        extract_titled_environment_content(section_text, "remark", "Horizontal Line Test")
    )
    inverse_definition_math = extract_display_math(definitions[1])
    inverse_example_math = extract_display_math(solutions[2])
    proposition_math = extract_display_math(propositions[0])
    horizontal_line_tikz = sanitize_figure_block(figures[0])

    slides = [
        {
            "slide_number": 1,
            "slide_id": "section_overview",
            "source_section": SECTION_TITLE,
            "title": "Inverse Functions and One-to-One Functions",
            "learning_goal": "Understand why invertibility begins with one-to-one behavior.",
            "slide_type": "overview",
            "bullets": [
                "A function can be viewed as a process that sends an input \\(x\\) to an output \\(y=f(x)\\).",
                "To reverse that process, each output must point back to exactly one input.",
                "This section introduces one-to-one functions, inverse functions, and a graphical test for invertibility."
            ],
            "math_blocks": [],
            "tikz_code": None,
            "script": (
                "In this section, we start with a simple question: when can a function be reversed? "
                "If a function takes an input x and produces an output y equals f of x, then an inverse function "
                "should recover the original input from that output. But this only works when each output comes "
                "from one input and not from several different inputs. So the main idea of the section is that "
                "invertibility is really about uniqueness. We will define one-to-one functions, test them with "
                "examples, and then connect that idea directly to inverse functions."
            ),
            "render_hints": {
                "tikz_scale_mode": "none",
                "max_width": "\\textwidth",
                "max_height_ratio": 0.58,
                "allow_frame_breaks": False
            }
        },
        {
            "slide_number": 2,
            "slide_id": "one_to_one_definition",
            "source_section": SECTION_TITLE,
            "title": "Definition of a One-to-One Function",
            "learning_goal": "Recognize the formal condition that makes a function invertible.",
            "slide_type": "definition",
            "bullets": [
                "Different inputs must produce different outputs.",
                "The equivalent implication form is often the easier test in practice.",
                "This is the key property that allows a function to have an inverse."
            ],
            "math_blocks": definition_math,
            "tikz_code": None,
            "script": (
                "Here is the formal definition. A function is one-to-one when unequal inputs never give the same output. "
                "You can also say the same thing in reverse: if two outputs are equal, then the inputs must already be equal. "
                "These two statements are logically equivalent, and the second version is often more convenient when we want to prove "
                "a function is one-to-one. The big reason this matters is that an inverse function must send an output back to one specific input. "
                "If two different inputs lead to the same output, that reversal becomes ambiguous."
            ),
            "render_hints": {
                "tikz_scale_mode": "none",
                "max_width": "\\textwidth",
                "max_height_ratio": 0.58,
                "allow_frame_breaks": False
            }
        },
        {
            "slide_number": 3,
            "slide_id": "student_id_example",
            "source_section": SECTION_TITLE,
            "title": "A Real-World One-to-One Test",
            "learning_goal": "Apply the definition to ordinary processes before moving to algebraic functions.",
            "slide_type": "example",
            "bullets": [
                "Student ID numbers are unique, so the function is one-to-one.",
                "Blood types repeat across students, so that function is not one-to-one.",
                "The test is always the same: can one output belong to more than one input?"
            ],
            "math_blocks": student_example_math + student_solution_math,
            "tikz_code": None,
            "script": (
                "This example shows that the idea is not limited to algebra. If we map each student to that student's ID number, "
                "the function is one-to-one because every ID is assigned to exactly one student. But if we map each student to a blood type, "
                "the function is not one-to-one, because many students can share the same output. So when you check whether a function is one-to-one, "
                "you should not focus on the symbols first. Focus on the matching rule. Ask whether one output can be traced back to more than one input."
            ),
            "render_hints": {
                "tikz_scale_mode": "none",
                "max_width": "\\textwidth",
                "max_height_ratio": 0.58,
                "allow_frame_breaks": False
            }
        },
        {
            "slide_number": 4,
            "slide_id": "mathematical_example",
            "source_section": SECTION_TITLE,
            "title": "A Mathematical Example",
            "learning_goal": "See how repeated outputs block inverse functions on a concrete interval.",
            "slide_type": "example",
            "bullets": [
                "\\(f(x)=x\\) on \\([0,1]\\) is one-to-one because output order matches input order.",
                "\\(g(x)=x^2\\) on \\([-1,1]\\) is not one-to-one because opposite inputs can share the same output.",
                "A single repeated output is enough to destroy invertibility."
            ],
            "math_blocks": math_example_math + math_solution_math,
            "tikz_code": None,
            "script": (
                "Now we move to a standard mathematical example. The identity function f of x equals x is one-to-one on the interval from zero to one, "
                "because each input keeps its own value. In contrast, g of x equals x squared is not one-to-one on minus one to one. "
                "For example, one half and minus one half both produce one fourth. That means one output value comes from two different inputs, "
                "so an inverse would not know which original input to choose. This is exactly why the one-to-one condition is necessary."
            ),
            "render_hints": {
                "tikz_scale_mode": "none",
                "max_width": "\\textwidth",
                "max_height_ratio": 0.58,
                "allow_frame_breaks": False
            }
        },
        {
            "slide_number": 5,
            "slide_id": "horizontal_line_test_rule",
            "source_section": SECTION_TITLE,
            "title": "The Horizontal Line Test",
            "learning_goal": "Connect the definition of one-to-one with a geometric test on the graph.",
            "slide_type": "definition",
            "bullets": [
                "A horizontal line represents a fixed output value \\(y=c\\).",
                "If the graph is hit twice, then two inputs share the same output.",
                "So a function is one-to-one exactly when every horizontal line meets the graph at most once."
            ],
            "math_blocks": horizontal_line_math,
            "tikz_code": None,
            "script": (
                "The horizontal line test is the geometric version of the definition. A horizontal line means that the output value is fixed at y equals c. "
                "If that line intersects the graph at two different points, then the same output c comes from two different x-values, so the function is not one-to-one. "
                "If every horizontal line intersects at most once, then each output corresponds to at most one input, which is exactly the definition we want. "
                "This is often the fastest way to judge invertibility from a graph."
            ),
            "render_hints": {
                "tikz_scale_mode": "none",
                "max_width": "\\textwidth",
                "max_height_ratio": 0.58,
                "allow_frame_breaks": False
            }
        },
        {
            "slide_number": 6,
            "slide_id": "horizontal_line_test_figure",
            "source_section": SECTION_TITLE,
            "title": "Horizontal Line Test: Visual Check",
            "learning_goal": "Read the horizontal line test directly from a graph.",
            "slide_type": "figure",
            "bullets": [],
            "math_blocks": [],
            "tikz_code": horizontal_line_tikz,
            "script": (
                "This picture shows the horizontal line test in action. On the left, the horizontal line meets the graph only once, so the function can still be one-to-one. "
                "On the right, the same kind of line meets the parabola twice, so one output value is coming from two different inputs. "
                "That is the exact visual signal that an inverse function cannot be defined on that whole interval."
            ),
            "render_hints": {
                "tikz_scale_mode": "none",
                "max_width": "\\textwidth",
                "max_height_ratio": 0.62,
                "allow_frame_breaks": False
            }
        },
        {
            "slide_number": 7,
            "slide_id": "inverse_function_definition",
            "source_section": SECTION_TITLE,
            "title": "Definition of an Inverse Function",
            "learning_goal": "Describe an inverse as a function that reverses the original correspondence.",
            "slide_type": "definition",
            "bullets": [
                "If \\(f\\) sends \\(x\\) to \\(y\\), then \\(f^{-1}\\) sends \\(y\\) back to \\(x\\).",
                "The domain and range switch roles when we pass to the inverse.",
                "Using \\(x\\) as the input variable for \\(f^{-1}\\) is only a notation change, not a new idea."
            ],
            "math_blocks": inverse_definition_math,
            "tikz_code": None,
            "script": (
                "Once a function is one-to-one, we can define its inverse. The idea is simple: if f maps x to y, then the inverse maps y back to x. "
                "That is why the domain and range exchange roles. The outputs of the original function become the inputs of the inverse. "
                "You will also see the notation rewritten with x as the independent variable for the inverse. That is just a relabeling of variables. "
                "The main mathematical idea is still the same: the inverse reverses the original function."
            ),
            "render_hints": {
                "tikz_scale_mode": "none",
                "max_width": "\\textwidth",
                "max_height_ratio": 0.58,
                "allow_frame_breaks": False
            }
        },
        {
            "slide_number": 8,
            "slide_id": "inverse_theorem_and_examples",
            "source_section": SECTION_TITLE,
            "title": "When Does an Inverse Exist?",
            "learning_goal": "Use the theorem and simple examples to compute inverses in practice.",
            "slide_type": "theorem",
            "bullets": [
                "A function has an inverse function if and only if it is one-to-one.",
                "The identity function is its own inverse.",
                "For \\(g(x)=x^3\\), solving for \\(x\\) gives \\(g^{-1}(x)=\\sqrt[3]{x}\\)."
            ],
            "math_blocks": [
                inverse_example_math[0],
                inverse_example_math[-1]
            ],
            "tikz_code": None,
            "script": (
                "This theorem gives the complete answer: a function has an inverse exactly when it is one-to-one. "
                "So the property we studied earlier is not just useful; it is the whole criterion. "
                "The examples here show how that criterion becomes a calculation. The identity function stays the same when reversed, so its inverse is still x. "
                "For g of x equals x cubed, we write y equals x cubed, solve for x, and then interchange x and y. "
                "That process produces g inverse of x equals the cube root of x."
            ),
            "render_hints": {
                "tikz_scale_mode": "none",
                "max_width": "\\textwidth",
                "max_height_ratio": 0.58,
                "allow_frame_breaks": False
            }
        },
        {
            "slide_number": 9,
            "slide_id": "composition_identities",
            "source_section": SECTION_TITLE,
            "title": "How to Check an Inverse",
            "learning_goal": "Use composition identities to verify that the inverse really reverses the function.",
            "slide_type": "recap",
            "bullets": [
                "Composing a function with its inverse returns the original input.",
                "\\(f^{-1}(f(x))=x\\) is checked on the domain of \\(f\\).",
                "\\(f(f^{-1}(x))=x\\) is checked on the range of \\(f\\).",
                "These identities are the practical verification step after solving for an inverse."
            ],
            "math_blocks": proposition_math,
            "tikz_code": None,
            "script": (
                "To finish the section, we record the two identities that confirm an inverse is correct. "
                "If you start with an input in the domain of f, apply f, and then apply the inverse, you must return to the same input. "
                "Likewise, if you start with a value in the range of f, apply the inverse first, and then apply f, you must again return to the starting value. "
                "These formulas are not just abstract facts. They give you the standard way to check whether the inverse you found is actually correct."
            ),
            "render_hints": {
                "tikz_scale_mode": "none",
                "max_width": "\\textwidth",
                "max_height_ratio": 0.58,
                "allow_frame_breaks": False
            }
        }
    ]

    return {
        "deck_id": DECK_ID,
        "source_file": SOURCE_FILE.relative_to(REPO_ROOT).as_posix(),
        "source_section": SECTION_TITLE,
        "language": "English",
        "slides": slides
    }


def validate_deck(deck: dict[str, Any], schema: dict[str, Any]) -> None:
    expected_top_level = set(schema["required"])
    actual_top_level = set(deck.keys())
    if actual_top_level != expected_top_level:
        raise ValueError(
            f"Deck keys do not match schema. Expected {sorted(expected_top_level)}, "
            f"found {sorted(actual_top_level)}."
        )

    for field in ("deck_id", "source_file", "source_section", "language"):
        if not isinstance(deck[field], str) or not deck[field]:
            raise ValueError(f"{field} must be a non-empty string.")
    if not isinstance(deck["slides"], list) or not deck["slides"]:
        raise ValueError("slides must be a non-empty list.")

    slide_schema = schema["properties"]["slides"]["items"]
    required_slide_keys = set(slide_schema["required"])
    required_render_hint_keys = set(
        slide_schema["properties"]["render_hints"]["required"]
    )

    for index, slide in enumerate(deck["slides"], start=1):
        if set(slide.keys()) != required_slide_keys:
            raise ValueError(
                f"Slide keys do not match schema on slide {index}: {sorted(slide.keys())}"
            )
        if slide["slide_number"] != index:
            raise ValueError(
                f"slide_number must be sequential. Expected {index}, found {slide['slide_number']}."
            )
        for field in (
            "slide_id",
            "source_section",
            "title",
            "learning_goal",
            "slide_type",
            "script",
        ):
            if not isinstance(slide[field], str) or not slide[field].strip():
                raise ValueError(f"{field} must be a non-empty string on slide {index}.")
        if not isinstance(slide["bullets"], list) or not all(
            isinstance(item, str) for item in slide["bullets"]
        ):
            raise ValueError(f"bullets must be a list of strings on slide {index}.")
        if not isinstance(slide["math_blocks"], list) or not all(
            isinstance(item, str) for item in slide["math_blocks"]
        ):
            raise ValueError(f"math_blocks must be a list of strings on slide {index}.")
        if slide["tikz_code"] is not None and not isinstance(slide["tikz_code"], str):
            raise ValueError(f"tikz_code must be null or a string on slide {index}.")

        render_hints = slide["render_hints"]
        if set(render_hints.keys()) != required_render_hint_keys:
            raise ValueError(
                f"render_hints keys do not match schema on slide {index}: {sorted(render_hints.keys())}"
            )
        if render_hints["tikz_scale_mode"] not in {"none", "fit_width"}:
            raise ValueError(f"Unsupported tikz_scale_mode on slide {index}.")
        if not isinstance(render_hints["max_width"], str) or not render_hints["max_width"]:
            raise ValueError(f"max_width must be a non-empty string on slide {index}.")
        max_height_ratio = render_hints["max_height_ratio"]
        if not isinstance(max_height_ratio, (int, float)) or not (0 < max_height_ratio <= 1):
            raise ValueError(
                f"max_height_ratio must be a number in (0, 1] on slide {index}."
            )
        if not isinstance(render_hints["allow_frame_breaks"], bool):
            raise ValueError(f"allow_frame_breaks must be a boolean on slide {index}.")


def render_bullets(bullets: list[str]) -> str:
    if not bullets:
        return ""
    lines = ["\\begin{itemize}"]
    for bullet in bullets:
        lines.append(f"  \\item {bullet}")
    lines.append("\\end{itemize}")
    return "\n".join(lines)


def render_math_blocks(math_blocks: list[str]) -> str:
    return "\n\n".join(math_blocks)


def render_tikz_block(tikz_code: str | None, render_hints: dict[str, Any]) -> str:
    if not tikz_code:
        return ""
    if render_hints["tikz_scale_mode"] != "fit_width":
        return tikz_code
    max_width = render_hints["max_width"]
    return (
        "\\begin{center}\n"
        f"\\resizebox{{{max_width}}}{{!}}{{%\n"
        f"{tikz_code}\n"
        "}\n"
        "\\end{center}"
    )


def render_frame(slide: dict[str, Any]) -> str:
    frame_options = "[t]"
    if slide["render_hints"]["allow_frame_breaks"]:
        frame_options = "[t,allowframebreaks]"

    body_parts = [f"\\textbf{{Goal.}} {slide['learning_goal']}"]

    bullet_block = render_bullets(slide["bullets"])
    if bullet_block:
        body_parts.append(bullet_block)

    math_block = render_math_blocks(slide["math_blocks"])
    if math_block:
        body_parts.append(math_block)

    tikz_block = render_tikz_block(slide["tikz_code"], slide["render_hints"])
    if tikz_block:
        body_parts.append(tikz_block)

    frame_body = "\n\n".join(body_parts)
    return (
        f"\\begin{{frame}}{frame_options}{{{slide['title']}}}\n"
        f"{frame_body}\n"
        "\\end{frame}"
    )


def render_beamer_tex(deck: dict[str, Any]) -> str:
    frames = "\n\n".join(render_frame(slide) for slide in deck["slides"])
    return (
        "\\documentclass[aspectratio=169]{beamer}\n\n"
        "\\usetheme{Madrid}\n"
        "\\usecolortheme{default}\n"
        "\\setbeamertemplate{navigation symbols}{}\n"
        "\\setbeamertemplate{footline}[frame number]\n"
        "\\setbeamercolor{structure}{fg=blue!60!black}\n"
        "\\setbeamercolor{frametitle}{fg=black,bg=blue!8}\n"
        "\\setbeamersize{text margin left=0.8cm, text margin right=0.8cm}\n\n"
        "\\usepackage[T1]{fontenc}\n"
        "\\usepackage[utf8]{inputenc}\n"
        "\\usepackage{lmodern}\n"
        "\\usepackage{amsmath}\n"
        "\\usepackage{amssymb}\n"
        "\\usepackage{mathtools}\n"
        "\\usepackage{graphicx}\n"
        "\\usepackage{tikz}\n"
        "\\usepackage{xcolor}\n\n"
        "\\title{Inverse Functions and One-to-One Functions}\n"
        "\\author{Prototype Deck}\n"
        "\\date{}\n\n"
        "\\begin{document}\n\n"
        f"{frames}\n\n"
        "\\end{document}\n"
    )


def render_script_markdown(deck: dict[str, Any]) -> str:
    sections = [
        f"# {deck['source_section']} Script",
        "",
        f"Source file: `{deck['source_file']}`",
        "",
    ]
    for slide in deck["slides"]:
        sections.extend(
            [
                f"## Slide {slide['slide_number']}: {slide['title']}",
                "",
                f"Learning goal: {slide['learning_goal']}",
                "",
                slide["script"],
                "",
            ]
        )
    return "\n".join(sections).strip() + "\n"


def find_command_path(command: str) -> Path | None:
    resolved = shutil.which(command)
    return Path(resolved).resolve() if resolved else None


def detect_beamer_cls() -> Path | None:
    command_paths = [find_command_path("pdflatex"), find_command_path("latexmk")]
    candidates: list[Path] = []
    for command_path in command_paths:
        if not command_path:
            continue
        for parent in (command_path.parent, *command_path.parents):
            candidates.append(parent / "tex" / "latex" / "beamer" / "beamer.cls")

    seen: set[Path] = set()
    for candidate in candidates:
        normalized = candidate.resolve()
        if normalized in seen:
            continue
        seen.add(normalized)
        if normalized.exists() and normalized.is_file():
            return normalized
    return None


def compile_beamer(tex_path: Path, compile_mode: str) -> str:
    latexmk_path = find_command_path("latexmk")
    pdflatex_path = find_command_path("pdflatex")
    beamer_cls_path = detect_beamer_cls()

    missing: list[str] = []
    if not latexmk_path:
        missing.append("latexmk")
    if not pdflatex_path:
        missing.append("pdflatex")
    if not beamer_cls_path:
        missing.append("beamer.cls")

    if missing:
        message = (
            "Skipped PDF compilation because required prerequisites were not found: "
            + ", ".join(missing)
            + "."
        )
        if compile_mode == "require":
            raise RuntimeError(message)
        return message

    command = [
        str(latexmk_path),
        "-pdf",
        "-interaction=nonstopmode",
        "-halt-on-error",
        tex_path.name,
    ]
    result = subprocess.run(
        command,
        cwd=tex_path.parent,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            "Beamer compilation failed.\n"
            f"Command: {' '.join(command)}\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )
    if not SLIDES_PDF_PATH.exists():
        raise RuntimeError("latexmk reported success, but the expected PDF was not created.")
    return f"Compiled PDF successfully with beamer at {beamer_cls_path}."


def write_json(path: Path, payload: dict[str, Any]) -> None:
    ensure_directory(path.parent)
    path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def write_text(path: Path, content: str) -> None:
    ensure_directory(path.parent)
    path.write_text(content, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate the one-section inverse functions prototype deck."
    )
    parser.add_argument(
        "--compile",
        choices=("auto", "never", "require"),
        default="auto",
        help="Compile the generated Beamer deck when prerequisites are available.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    ensure_file_exists(SOURCE_FILE, "chapter source")
    ensure_file_exists(SCHEMA_FILE, "JSON schema")

    source_text = read_text(SOURCE_FILE)
    schema = json.loads(read_text(SCHEMA_FILE))
    deck = build_deck(source_text)
    validate_deck(deck, schema)

    write_json(SLIDE_SPEC_PATH, deck)
    write_text(SLIDES_TEX_PATH, render_beamer_tex(deck))
    write_text(SCRIPT_MD_PATH, render_script_markdown(deck))

    if args.compile == "never":
        print("Generated JSON, Beamer source, and script. PDF compilation was skipped by request.")
        return 0

    compile_message = compile_beamer(SLIDES_TEX_PATH, args.compile)
    print("Generated JSON, Beamer source, and script.")
    print(compile_message)
    return 0


if __name__ == "__main__":
    sys.exit(main())
