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
    re.compile(r"【[^】\n]{1,100}】"),
    re.compile(r"［[^］\n]{1,100}］"),
    re.compile(r"\b(?:candidate(?:'s)? name|student name|applicant name|program(?:me)? name|"
               r"university name|institution name|referee(?:'s)? name|prof\.?\s*xx)\b", re.I),
    re.compile(r"\b(?:xxx+|tbd|todo|insert here)\b", re.I),
    re.compile(r"(?:申请人姓名|学生姓名|推荐人姓名|学校名称|项目名称|申请项目|姓名待填|某某同学)"),
    re.compile(r"(?<![A-Za-z])X{2,}(?![A-Za-z])", re.I),
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
    matches: list[tuple[int, int, str]] = []
    for pattern in PLACEHOLDER_PATTERNS:
        for match in pattern.finditer(text):
            value = match.group(0).strip()
            if value:
                matches.append((match.start(), match.end(), value))

    # Prefer the widest match at a position so bracketed placeholders are not
    # counted again by a narrower phrase pattern inside the same span.
    matches.sort(key=lambda item: (item[0], -(item[1] - item[0])))
    selected: list[tuple[int, int, str]] = []
    for start, end, value in matches:
        if any(outer_start <= start and end <= outer_end for outer_start, outer_end, _ in selected):
            continue
        if value not in {existing for _, _, existing in selected}:
            selected.append((start, end, value))
    return [value for _, _, value in selected]


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
            "latin_word_count": len(
                re.findall(r"[A-Za-z0-9]+(?:['-][A-Za-z0-9]+)*", text)
            ),
            "cjk_character_count": len(
                re.findall(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]", text)
            ),
            "character_count_excluding_whitespace": len(re.sub(r"\s", "", text)),
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

