#!/usr/bin/env python3
"""Extract review-relevant text and risks from one or more DOCX reference letters."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

PLACEHOLDER_PATTERNS = [
    re.compile(r"\[[^\]\n]{1,100}\]"),
    re.compile(r"\{[^\}\n]{1,100}\}"),
    re.compile(r"\b(?:candidate(?:'s)? name|student name|applicant name|program(?:me)? name|"
               r"university name|institution name|referee(?:'s)? name|prof\.?\s*xx)\b", re.I),
    re.compile(r"\b(?:xxx+|tbd|todo|insert here)\b", re.I),
]


def _read_xml(archive: zipfile.ZipFile, name: str) -> ET.Element | None:
    try:
        return ET.fromstring(archive.read(name))
    except KeyError:
        return None


def _paragraph_text(paragraph: ET.Element) -> str:
    parts: list[str] = []

    def visit(node: ET.Element, deleted: bool = False) -> None:
        is_deleted = deleted or node.tag == W + "del"
        if node.tag == W + "t" and not is_deleted:
            parts.append(node.text or "")
        elif node.tag == W + "tab" and not is_deleted:
            parts.append("\t")
        elif node.tag in {W + "br", W + "cr"} and not is_deleted:
            parts.append("\n")
        for child in node:
            visit(child, is_deleted)

    visit(paragraph)
    return "".join(parts).strip()


def _all_paragraphs(root: ET.Element | None) -> list[str]:
    if root is None:
        return []
    return [text for p in root.iter(W + "p") if (text := _paragraph_text(p))]


def _find_placeholders(text: str) -> list[str]:
    found: list[str] = []
    for pattern in PLACEHOLDER_PATTERNS:
        for match in pattern.finditer(text):
            value = match.group(0).strip()
            if value and value not in found:
                found.append(value)
    return found


def extract_docx(path: Path) -> dict:
    with zipfile.ZipFile(path) as archive:
        document = _read_xml(archive, "word/document.xml")
        if document is None:
            raise ValueError("word/document.xml is missing")

        paragraphs = _all_paragraphs(document)
        text = "\n".join(paragraphs)

        headers_and_footers: dict[str, str] = {}
        for name in archive.namelist():
            if re.fullmatch(r"word/(header|footer)\d+\.xml", name):
                entry_text = "\n".join(_all_paragraphs(_read_xml(archive, name)))
                if entry_text:
                    headers_and_footers[name] = entry_text

        comments_root = _read_xml(archive, "word/comments.xml")
        comments: list[dict] = []
        if comments_root is not None:
            for comment in comments_root.iter(W + "comment"):
                comments.append(
                    {
                        "id": comment.attrib.get(W + "id", ""),
                        "author": comment.attrib.get(W + "author", ""),
                        "date": comment.attrib.get(W + "date", ""),
                        "text": "\n".join(_all_paragraphs(comment)),
                    }
                )

        all_visible_text = "\n".join([text, *headers_and_footers.values()])
        placeholders = _find_placeholders(all_visible_text)

        return {
            "path": str(path),
            "word_count": len(re.findall(r"\b[\w'-]+\b", text, flags=re.UNICODE)),
            "paragraph_count": len(paragraphs),
            "insertions": sum(1 for _ in document.iter(W + "ins")),
            "deletions": sum(1 for _ in document.iter(W + "del")),
            "comments": comments,
            "headers_and_footers": headers_and_footers,
            "risk_scan": {
                "placeholders": placeholders,
                "placeholder_count": len(placeholders),
            },
            "text": text,
        }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("documents", nargs="+", type=Path)
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    results = []
    for document in args.documents:
        try:
            results.append(extract_docx(document))
        except Exception as exc:
            results.append({"path": str(document), "error": str(exc)})

    payload = results[0] if len(results) == 1 else results
    json.dump(payload, sys.stdout, ensure_ascii=False, indent=2 if args.pretty else None)
    sys.stdout.write("\n")
    return 1 if any("error" in result for result in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())

