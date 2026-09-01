#!/usr/bin/env python3
"""
generate_monthly_report.py — automated Audinux monthly ODT report generator.

Queries the git log for the target month and extracts metadata directly from
spec files to produce a ready-to-review ODT report.

Usage:
    python3 generate_monthly_report.py [--year YEAR] [--month MONTH] [--output FILE]

Defaults to the previous calendar month.
Requires: odfpy  (pip install odfpy)
"""

import argparse
import calendar
import datetime
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

try:
    from odf.opendocument import OpenDocumentText
    from odf.style import Style, TextProperties, ParagraphProperties
    from odf.text import P, H
    from odf import dc
except ImportError:
    sys.exit("odfpy not installed.  Run: pip install odfpy")

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

MONTH_NAMES = [
    "", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]


# ── Git helpers ────────────────────────────────────────────────────────────────

def month_bounds(year: int, month: int) -> tuple:
    """Return (after, before) strings suitable for git --after / --before.

    git --after=DATE is exclusive (shows commits *after* that date), so we
    pass the last day of the previous month and the first day of the next month
    to capture exactly the target month.
    """
    first = datetime.date(year, month, 1)
    last_day = calendar.monthrange(year, month)[1]
    last = datetime.date(year, month, last_day)
    return (first - datetime.timedelta(days=1)).isoformat(), \
           (last  + datetime.timedelta(days=1)).isoformat()


def _git(*args: str) -> str:
    result = subprocess.run(
        ["git"] + list(args),
        cwd=REPO_ROOT, capture_output=True, text=True
    )
    return result.stdout.strip()


def added_specs(after: str, before: str) -> list:
    """Spec files first committed (A) in the date range."""
    out = _git("log", "--diff-filter=A", "--name-only", "--format=",
               f"--after={after}", f"--before={before}")
    return sorted({
        REPO_ROOT / f for f in out.splitlines()
        if f.endswith(".spec") and (REPO_ROOT / f).exists()
    })


def modified_specs(after: str, before: str, exclude: set) -> list:
    """Spec files modified (M) in the date range, excluding newly-added ones."""
    out = _git("log", "--diff-filter=M", "--name-only", "--format=",
               f"--after={after}", f"--before={before}")
    return sorted({
        REPO_ROOT / f for f in out.splitlines()
        if f.endswith(".spec")
        and (REPO_ROOT / f).exists()
        and (REPO_ROOT / f) not in exclude
    })


def all_commits(after: str, before: str) -> list:
    """All commit one-liners in the date range, newest first."""
    out = _git("log", "--oneline", f"--after={after}", f"--before={before}")
    return [line for line in out.splitlines() if line]


# ── Spec parser ────────────────────────────────────────────────────────────────

_MACRO_RE = re.compile(r'%\{(\w+)\}|%(\w+)')


def _resolve(text: str, defs: dict) -> str:
    """Best-effort substitution of simple %{name} / %name macros."""
    for _ in range(5):
        text = _MACRO_RE.sub(lambda m: defs.get(m.group(1) or m.group(2), m.group(0)), text)
    return text


def parse_spec(path: Path) -> dict:
    """Extract key metadata from a spec file."""
    try:
        text = path.read_text(errors="replace")
    except OSError:
        return {"name": path.stem, "path": path}

    # Collect %global / %define macros for lightweight expansion
    defs = {
        m.group(1): m.group(2).strip()
        for m in re.finditer(r'^%(?:global|define)\s+(\w+)\s+(.+)$', text, re.MULTILINE)
    }

    def field(name: str) -> str:
        m = re.search(rf'^{name}:\s*(.+)$', text, re.MULTILINE)
        return _resolve(m.group(1).strip(), defs) if m else ""

    # Header comment tags (audinux-specific)
    tag = cat = typ = ""
    for line in text.splitlines():
        if   line.startswith("# Tag:"):      tag = line.split(":", 1)[1].strip()
        elif line.startswith("# Category:"): cat = line.split(":", 1)[1].strip()
        elif line.startswith("# Type:"):     typ = line.split(":", 1)[1].strip()

    # First paragraph of %description (up to 3 non-empty lines)
    desc = ""
    m = re.search(r'%description[^\n]*\n(.*?)(?=\n%|\Z)', text, re.DOTALL)
    if m:
        lines = [l.strip() for l in m.group(1).splitlines() if l.strip()]
        desc = " ".join(lines[:3])

    return {
        "name":        field("Name"),
        "version":     field("Version"),
        "url":         field("URL"),
        "summary":     field("Summary"),
        "tag":         tag,
        "category":    cat,
        "type":        typ,
        "description": desc,
        "path":        path,
    }


# ── ODT builder ────────────────────────────────────────────────────────────────

def _add_style(doc, name, family, tp=None, pp=None):
    s = Style(name=name, family=family)
    if tp: s.addElement(TextProperties(**tp))
    if pp: s.addElement(ParagraphProperties(**pp))
    doc.styles.addElement(s)


def build_odt(year: int, month: int,
              new_pkgs: list, updated_pkgs: list,
              commits: list) -> OpenDocumentText:
    doc = OpenDocumentText()
    month_name = MONTH_NAMES[month]
    today = datetime.date.today().isoformat()

    _add_style(doc, "Title",      "paragraph",
               tp=dict(fontsize="24pt", fontweight="bold", color="#1F497D"),
               pp=dict(marginbottom="0.3cm", margintop="0.5cm"))
    _add_style(doc, "Heading1",   "paragraph",
               tp=dict(fontsize="16pt", fontweight="bold", color="#2E74B5"),
               pp=dict(margintop="0.6cm", marginbottom="0.2cm"))
    _add_style(doc, "Heading2",   "paragraph",
               tp=dict(fontsize="13pt", fontweight="bold", color="#404040"),
               pp=dict(margintop="0.4cm", marginbottom="0.15cm"))
    _add_style(doc, "Body",       "paragraph",
               tp=dict(fontsize="11pt"),
               pp=dict(marginbottom="0.15cm"))
    _add_style(doc, "PkgName",    "paragraph",
               tp=dict(fontsize="12pt", fontweight="bold", color="#1F497D"),
               pp=dict(margintop="0.3cm", marginbottom="0.05cm"))
    _add_style(doc, "URL_style",  "paragraph",
               tp=dict(fontsize="10pt", color="#0563C1"),
               pp=dict(marginbottom="0.1cm"))
    _add_style(doc, "UpdateItem", "paragraph",
               tp=dict(fontsize="10pt"),
               pp=dict(marginleft="0.5cm", marginbottom="0.05cm"))
    _add_style(doc, "CommitItem", "paragraph",
               tp=dict(fontsize="9pt", fontfamily="Courier New"),
               pp=dict(marginleft="0.5cm", marginbottom="0.05cm"))

    doc.meta.addElement(dc.Title(text=f"Audinux — Monthly Report {month_name} {year}"))
    doc.meta.addElement(dc.Creator(text="Yann Collette"))
    doc.meta.addElement(dc.Date(text=today))

    def p(text, style="Body"):
        el = P(stylename=style)
        el.addText(text)
        doc.text.addElement(el)

    def h(text, level=1):
        el = H(outlinelevel=level, stylename=f"Heading{level}")
        el.addText(text)
        doc.text.addElement(el)

    # ── Title ──────────────────────────────────────────────────────────────────
    p("Audinux — Monthly Report", style="Title")
    p(f"{month_name} {year}  |  Maintainer: Yann Collette", style="Body")
    p("")

    # ── 1. Summary ─────────────────────────────────────────────────────────────
    h("1. Summary")
    p(
        f"During {month_name} {year}, the Audinux repository saw the following activity: "
        f"{len(new_pkgs)} new package(s) were introduced and {len(updated_pkgs)} package(s) "
        f"were updated. [Edit this paragraph to add highlights.]"
    )
    p("")

    # ── 2. New packages, grouped by # Category: header ────────────────────────
    h("2. New Packages Added")
    p(
        f"The following {len(new_pkgs)} package(s) were introduced for the first time "
        f"in {month_name} {year}."
    )
    p("")

    if new_pkgs:
        groups = defaultdict(list)
        for pkg in new_pkgs:
            # Use first token of Category, fall back to Type, then "Other"
            cat = pkg.get("category") or pkg.get("type") or "Other"
            groups[cat.split(",")[0].strip()].append(pkg)

        for cat_name in sorted(groups):
            h(cat_name, level=2)
            for pkg in groups[cat_name]:
                p(f"● {pkg['name']}", style="PkgName")
                desc = pkg.get("description") or pkg.get("summary") or "(no description available)"
                p(desc, style="Body")
                if pkg.get("url"):
                    p(f"URL: {pkg['url']}", style="URL_style")
                p("")
    else:
        p("No new packages this month.", style="Body")
    p("")

    # ── 3. Package updates ─────────────────────────────────────────────────────
    h("3. Package Updates")
    p(f"{len(updated_pkgs)} package(s) were updated during {month_name} {year}.")
    p("")
    h("3.1  Updated Package List", level=2)
    if updated_pkgs:
        for pkg in sorted(updated_pkgs, key=lambda x: x.get("name", "").lower()):
            ver = pkg.get("version") or "?"
            p(f"  • {pkg['name']:<35s}→  {ver}", style="UpdateItem")
    else:
        p("No updates this month.", style="Body")
    p("")

    # ── 4. Other notable work (raw commit log) ─────────────────────────────────
    h("4. Other Notable Work")
    p(
        "Raw commit log for the month — edit to keep only the highlights "
        "and rewrite as prose if needed."
    )
    p("")
    for commit in commits[:50]:
        p(f"  {commit}", style="CommitItem")
    if len(commits) > 50:
        p(f"  … and {len(commits) - 50} more commits.", style="CommitItem")
    p("")

    # ── Footer ─────────────────────────────────────────────────────────────────
    p("")
    p("─" * 60, style="Body")
    p(
        f"Generated: {today}  |  Audinux Fedora Repository  |  Maintainer: Yann Collette",
        style="Body"
    )

    return doc


# ── Entry point ────────────────────────────────────────────────────────────────

def main():
    today = datetime.date.today()
    last_month = (today.replace(day=1) - datetime.timedelta(days=1))

    ap = argparse.ArgumentParser(
        description="Generate an Audinux monthly ODT report from git history"
    )
    ap.add_argument("--year",   type=int, default=last_month.year,
                    help="Report year  (default: last month's year)")
    ap.add_argument("--month",  type=int, default=last_month.month,
                    help="Report month 1-12  (default: last month)")
    ap.add_argument("--output", default="",
                    help="Output .odt path  (default: scripts/monthly-doc/audinux-<month><year>-report.odt)")
    args = ap.parse_args()

    year, month = args.year, args.month
    if not 1 <= month <= 12:
        sys.exit("--month must be between 1 and 12")

    month_name = MONTH_NAMES[month].lower()
    out_path = args.output or str(
        REPO_ROOT / "scripts" / "monthly-doc" / f"audinux-{month_name}{year}-report.odt"
    )

    after, before = month_bounds(year, month)
    print(f"Scanning git log for {MONTH_NAMES[month]} {year}  ({after} → {before})")

    added   = added_specs(after, before)
    modified = modified_specs(after, before, set(added))
    commits  = all_commits(after, before)

    print(f"  New spec files:     {len(added)}")
    print(f"  Updated spec files: {len(modified)}")
    print(f"  Total commits:      {len(commits)}")

    new_pkgs     = [parse_spec(p) for p in added]
    updated_pkgs = [parse_spec(p) for p in modified]

    doc = build_odt(year, month, new_pkgs, updated_pkgs, commits)
    doc.save(out_path)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
