from __future__ import annotations

import re


_VARIABLE_A_CONTEXTS = [
    # x-language: these nearly always refer to the point/variable a.
    re.compile(r"\b(x\s+(?:approaches|equals|near|is\s+close\s+to|is\s+within\s+delta\s+of)\s+)a\b", re.IGNORECASE),
    re.compile(r"\b(x\s+minus\s+)a\b", re.IGNORECASE),
    re.compile(r"\b(distance\s+between\s+x\s+and\s+)a\b", re.IGNORECASE),
    re.compile(r"\b(distance\s+from\s+x\s+to\s+)a\b", re.IGNORECASE),
    re.compile(r"\b((?:close|closer|close\s+enough)\s+to\s+)a\b", re.IGNORECASE),
    re.compile(r"\b((?:near|around)\s+)a\b", re.IGNORECASE),
    # Limit/continuity language: "at a" and "of a" are variable-a contexts when preceded by
    # mathematical nouns. This avoids changing article uses such as "at a point".
    re.compile(r"\b((?:defined|continuous|continuity|limit|value)\s+at\s+)a\b", re.IGNORECASE),
    re.compile(r"\b((?:neighborhood|neighbourhood|strip|window|radius|distance)\s+(?:around|of|from)\s+)a\b", re.IGNORECASE),
    re.compile(r"\b((?:within|outside)\s+delta\s+of\s+)a\b", re.IGNORECASE),
    re.compile(r"\b((?:f|g|h|value|limit)\s+of\s+)a\b", re.IGNORECASE),
    # Bare "at/to/of a" is only rewritten when it is sentence-final or followed by punctuation.
    re.compile(r"\b(at\s+)a(?=\s*[,.;:!?)]|$)", re.IGNORECASE),
    re.compile(r"\b(to\s+)a(?=\s*[,.;:!?)]|$)", re.IGNORECASE),
    re.compile(r"\b(of\s+)a(?=\s*[,.;:!?)]|$)", re.IGNORECASE),
]

_FUNCTION_LETTER_NAMES = {
    "f": "eff",
    "g": "gee",
    "h": "aitch",
}

_FUNCTION_LETTER_FOLLOW_CONTEXT = re.compile(
    r"\b(?P<letter>[fgh])(?=\s+(?:of|inverse|is|has|becomes|equals|maps|sends|takes|returns)\b)"
)
_FUNCTION_LETTER_PRECEDE_CONTEXT = re.compile(
    r"\b(?P<context>(?:of|for|with|apply|applying|domain\s+of|range\s+of|algebra\s+of|outputs?\s+of|inputs?\s+of)\s+)"
    r"(?P<letter>[fgh])\b"
)

_UPPERCASE_MATH_LETTER_NAMES = {
    "L": "ell",
    "M": "em",
    "N": "en",
}

_UPPERCASE_MATH_LETTER = re.compile(r"\b(?P<letter>[LMN])\b")

_VARIABLE_C_CONTEXTS = [
    re.compile(r"\b((?:y\s+equals|equals|level|value|constant)\s+)c\b", re.IGNORECASE),
]

_VARIABLE_A_TTS = "ayyy"


def _replace_function_letter(match: re.Match[str]) -> str:
    letter = match.group("letter")
    return _FUNCTION_LETTER_NAMES.get(letter, letter)


def _replace_function_letter_after_context(match: re.Match[str]) -> str:
    letter = match.group("letter")
    return f"{match.group('context')}{_FUNCTION_LETTER_NAMES.get(letter, letter)}"


def _replace_uppercase_math_letter(match: re.Match[str]) -> str:
    letter = match.group("letter")
    return _UPPERCASE_MATH_LETTER_NAMES.get(letter, letter)


def normalize_tts_pronunciation(text: str) -> str:
    """Normalize narration text for TTS pronunciation without changing visual math.

    The main practical fixes are context-sensitive single-letter variables. English TTS
    models often pronounce a bare lowercase "a" as the article, but in limit notation it
    should be the letter name. The patterns below are intentionally context-limited so
    normal article uses like "a function" or "a theorem" stay untouched.
    """

    normalized = re.sub(r"\s+", " ", text).strip()
    for pattern in _VARIABLE_A_CONTEXTS:
        normalized = pattern.sub(lambda match: f"{match.group(1)}{_VARIABLE_A_TTS}", normalized)
    normalized = _FUNCTION_LETTER_FOLLOW_CONTEXT.sub(_replace_function_letter, normalized)
    normalized = _FUNCTION_LETTER_PRECEDE_CONTEXT.sub(_replace_function_letter_after_context, normalized)
    normalized = _UPPERCASE_MATH_LETTER.sub(_replace_uppercase_math_letter, normalized)
    for pattern in _VARIABLE_C_CONTEXTS:
        normalized = pattern.sub(lambda match: f"{match.group(1)}C", normalized)
    return normalized
