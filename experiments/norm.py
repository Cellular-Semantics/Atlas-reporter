"""Shared normalisation for span matching. Throwaway test harness code."""
from __future__ import annotations
import re, unicodedata

_REF = re.compile(r"\[\d+(?:\s*[,–—-]\s*\d+)*\]")
_DASH = re.compile(r"[‐‑‒–—―−]")

def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = _DASH.sub("-", s)
    s = _REF.sub("", s)                      # inline citation markers
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()

def contains(haystack: str, needle: str) -> bool:
    return norm(needle) in norm(haystack)


_LETTERS = re.compile(r"[^a-z ]+")

def norm_loc(s: str) -> str:
    """Locator normalisation: letters only. Used to decide whether a gold span is present
    in a chunk, uniformly across arms — ASTA renders superscript refs as loose digits,
    our JATS walk drops them, so digits cannot be compared fairly. Spans are long enough
    (>60 chars) that dropping digits does not create collisions."""
    s = norm(s)
    s = _LETTERS.sub(" ", s)
    return re.sub(r"\s+", " ", s).strip()

def contains_loc(haystack: str, needle: str) -> bool:
    return norm_loc(needle) in norm_loc(haystack)
