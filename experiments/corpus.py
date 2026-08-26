"""Paper text + chunking shared by every Stage 1 arm. Throwaway harness code."""
from __future__ import annotations
import re, xml.etree.ElementTree as ET
from pathlib import Path
from atlas_chat.services import _jats_parser as J

PAPERS = {
    "gopee2024": "PMC11578897",
    "suo2022": "PMC7612819",
}
XML_DIR = Path(__file__).parent / "papers"


def _drop_bibr(node):
    """Remove inline citation xrefs, keeping their tail text."""
    for parent in node.iter():
        for child in list(parent):
            if child.tag == "xref" and child.get("ref-type") == "bibr":
                tail = child.tail or ""
                idx = list(parent).index(child)
                parent.remove(child)
                if idx == 0:
                    parent.text = (parent.text or "") + tail
                else:
                    prev = list(parent)[idx - 1]
                    prev.tail = (prev.tail or "") + tail


_NON_PROSE = ("fig", "table-wrap", "supplementary-material", "boxed-text", "disp-formula")


def _drop_non_prose(node):
    """Remove figure/table captions. They sit *inside* body <p> elements in this JATS, so
    itertext() would otherwise splice legend text onto the end of prose paragraphs."""
    for parent in node.iter():
        for child in list(parent):
            if child.tag in _NON_PROSE:
                tail = child.tail or ""
                idx = list(parent).index(child)
                parent.remove(child)
                if idx == 0:
                    parent.text = (parent.text or "") + tail
                else:
                    list(parent)[idx - 1].tail = (list(parent)[idx - 1].tail or "") + tail


def paragraphs(name: str) -> list[tuple[str, str]]:
    """[(section_title, paragraph_text)] in document order, citations stripped.

    Walks the whole body, not just <sec> subtrees — some papers (Suo) put main-text
    paragraphs directly under <body>.
    """
    xml = (XML_DIR / f"{name}.xml").read_text()
    root = ET.fromstring(J._clean_xml(xml))
    J._strip_namespace_from_tree(root)
    _drop_bibr(root)
    _drop_non_prose(root)
    out: list[tuple[str, str]] = []

    def walk(node, title):
        for child in node:
            if child.tag == "sec":
                walk(child, (child.findtext("title") or title or "").strip())
            elif child.tag == "p":
                txt = re.sub(r"\s+", " ", "".join(child.itertext())).strip()
                if len(txt) > 40:
                    out.append((title, txt))
            elif child.tag not in ("title", "ref-list"):
                walk(child, title)

    walk(root.find(".//body"), "")
    return out


def chunks(name: str, target_chars: int = 1000) -> list[dict]:
    """Document-order chunks. Paragraphs packed to ~target_chars, never split mid-paragraph
    unless the paragraph itself exceeds the target."""
    out = []
    for title, txt in paragraphs(name):
        if len(txt) <= target_chars:
            pieces = [txt]
        else:
            pieces, cur = [], ""
            for sent in re.split(r"(?<=[.!?])\s+", txt):
                if len(cur) + len(sent) > target_chars and cur:
                    pieces.append(cur.strip()); cur = ""
                cur += sent + " "
            if cur.strip():
                pieces.append(cur.strip())
        for piece in pieces:
            out.append({"i": len(out), "section": title, "text": piece,
                        "n_chars": len(piece), "n_tokens": max(1, len(piece) // 4)})
    return out
