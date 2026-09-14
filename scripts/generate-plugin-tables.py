#!/usr/bin/env python3
"""
generate-plugin-tables.py — Generate markdown and ODT tables of audio plugins.

Reads every *.spec file under REPO_DIR, extracts header metadata
(# Category, # Type) and RPM fields (Name, URL, Summary), then writes
three tables:

  1. Synthesizers   — packages whose Category contains "Synthesizer"
  2. Effects        — packages whose Category contains "Effect"
  3. All plugins    — synths + effects, with detected plugin formats

Usage:
    python3 scripts/generate-plugin-tables.py [REPO_DIR] [options]

    REPO_DIR       root of the fedora-spec repository  (default: current dir)
    --output-md    write markdown to FILE  (default: plugin-catalogue.md)
    --output-odt   write ODT to FILE       (default: plugin-catalogue.odt)
    --no-md        skip markdown output
    --no-odt       skip ODT output

ODT output requires the odfpy package  (pip install odfpy).
"""

import argparse
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Plugin format keywords recognised in the "# Type:" header line.
FORMAT_KEYWORDS = {
    "LV2":        "LV2",
    "VST3":       "VST3",
    "VST":        "VST",
    "CLAP":       "CLAP",
    "YSFX":       "YSFX",
    "Standalone": "STANDALONE",
    "STANDALONE": "STANDALONE",
    "VAMP":       "VAMP",
    "LADSPA":     "LADSPA",
    "DSSI":       "DSSI",
    "NYQUIST":    "NYQUIST",
    "GSTREAMER":  "GSTREAMER",
    "MODGUI":     "MODGUI",
}

# ---------------------------------------------------------------------------
# Spec parsing
# ---------------------------------------------------------------------------

def parse_spec(path: Path) -> dict | None:
    name = url = summary = ""
    categories: list[str] = []
    types: list[str] = []

    try:
        text = path.read_text(errors="replace")
    except OSError:
        return None

    for line in text.splitlines():
        s = line.strip()
        if s.startswith("# Category:"):
            categories = [c.strip() for c in s[len("# Category:"):].strip().split(",")]
        elif s.startswith("# Type:"):
            types = [t.strip() for t in s[len("# Type:"):].strip().split(",")]
        elif s.startswith("Name:") and not name:
            val = s[len("Name:"):].strip()
            if not val.startswith("%"):
                name = val
        elif s.startswith("URL:") and not url:
            url = s[len("URL:"):].strip()
        elif s.startswith("Summary:") and not summary:
            summary = s[len("Summary:"):].strip()

    if not name:
        return None

    is_synth  = "Synthesizer" in categories
    is_effect = "Effect" in categories
    if not (is_synth or is_effect):
        return None

    seen: set[str] = set()
    formats: list[str] = []
    for tok in types:
        label = FORMAT_KEYWORDS.get(tok)
        if label and label not in seen:
            formats.append(label)
            seen.add(label)

    return {
        "name":      name,
        "url":       url,
        "summary":   summary,
        "is_synth":  is_synth,
        "is_effect": is_effect,
        "formats":   formats,
    }


# ---------------------------------------------------------------------------
# Markdown output
# ---------------------------------------------------------------------------

def _md_link(pkg: dict) -> str:
    return f"[{pkg['name']}]({pkg['url']})" if pkg["url"] else pkg["name"]


def _md_description_table(packages: list[dict]) -> str:
    rows = ["| Package | Description |", "| --- | --- |"]
    for pkg in packages:
        rows.append(f"| {_md_link(pkg)} | {pkg['summary']} |")
    return "\n".join(rows)


def _md_format_table(packages: list[dict]) -> str:
    rows = ["| Package | Plugin formats |", "| --- | --- |"]
    for pkg in packages:
        fmts = " / ".join(pkg["formats"]) if pkg["formats"] else "—"
        rows.append(f"| {_md_link(pkg)} | {fmts} |")
    return "\n".join(rows)


def write_markdown(synths, effects, all_pkgs, path: Path) -> None:
    lines = [
        "# Audinux Plugin Catalogue",
        "",
        "## Synthesizers",
        "",
        _md_description_table(synths),
        "",
        "## Effects",
        "",
        _md_description_table(effects),
        "",
        "## All plugins — format index",
        "",
        _md_format_table(all_pkgs),
        "",
    ]
    path.write_text("\n".join(lines))
    print(f"Markdown written to {path}", file=sys.stderr)


# ---------------------------------------------------------------------------
# ODT output
# ---------------------------------------------------------------------------

def write_odt(synths, effects, all_pkgs, path: Path) -> None:
    try:
        from odf.opendocument import OpenDocumentText
        from odf.style import (
            Style, TextProperties, ParagraphProperties,
            TableColumnProperties, TableProperties,
        )
        from odf.text import H, P, A, Span
        from odf.table import Table, TableColumn, TableRow, TableCell
    except ImportError:
        print(
            "ERROR: odfpy not installed. Run: pip install odfpy",
            file=sys.stderr,
        )
        return

    doc = OpenDocumentText()

    # --- Styles -----------------------------------------------------------

    # Heading 1
    h1_style = Style(name="Heading1", family="paragraph")
    h1_style.addElement(ParagraphProperties(breakbefore="auto"))
    h1_style.addElement(TextProperties(fontsize="18pt", fontweight="bold"))
    doc.styles.addElement(h1_style)

    # Heading 2
    h2_style = Style(name="Heading2", family="paragraph")
    h2_style.addElement(TextProperties(fontsize="14pt", fontweight="bold"))
    doc.styles.addElement(h2_style)

    # Table header cell
    th_style = Style(name="TableHeader", family="table-cell")
    th_style.addElement(TextProperties(fontweight="bold"))
    doc.styles.addElement(th_style)

    # Normal paragraph
    p_style = Style(name="NormalPara", family="paragraph")
    doc.styles.addElement(p_style)

    # Hyperlink character style
    link_style = Style(name="Internet_Link", family="text")
    link_style.addElement(TextProperties(color="#000080", textunderlinestyle="solid"))
    doc.styles.addElement(link_style)

    # Table style
    tbl_style = Style(name="PluginTable", family="table")
    tbl_style.addElement(TableProperties(width="17cm", align="margins"))
    doc.automaticstyles.addElement(tbl_style)

    # Column styles
    col_name_style = Style(name="ColName", family="table-column")
    col_name_style.addElement(TableColumnProperties(columnwidth="5cm"))
    doc.automaticstyles.addElement(col_name_style)

    col_desc_style = Style(name="ColDesc", family="table-column")
    col_desc_style.addElement(TableColumnProperties(columnwidth="12cm"))
    doc.automaticstyles.addElement(col_desc_style)

    col_fmt_style = Style(name="ColFmt", family="table-column")
    col_fmt_style.addElement(TableColumnProperties(columnwidth="12cm"))
    doc.automaticstyles.addElement(col_fmt_style)

    # -----------------------------------------------------------------

    def make_para(text: str, style_name: str = "NormalPara") -> P:
        p = P(stylename=style_name)
        p.addText(text)
        return p

    def make_heading(text: str, level: int) -> H:
        sname = "Heading1" if level == 1 else "Heading2"
        h = H(outlinelevel=level, stylename=sname)
        h.addText(text)
        return h

    def cell(content_para) -> TableCell:
        tc = TableCell()
        tc.addElement(content_para)
        return tc

    def header_cell(text: str) -> TableCell:
        tc = TableCell(stylename="TableHeader")
        p = P(stylename="NormalPara")
        sp = Span(stylename="TableHeader")
        sp.addText(text)
        p.addElement(sp)
        tc.addElement(p)
        return tc

    def pkg_cell(pkg: dict) -> TableCell:
        """Cell with a hyperlink to the package URL."""
        tc = TableCell()
        p = P(stylename="NormalPara")
        if pkg["url"]:
            a = A(type="simple", href=pkg["url"], stylename="Internet_Link")
            a.addText(pkg["name"])
            p.addElement(a)
        else:
            p.addText(pkg["name"])
        tc.addElement(p)
        return tc

    def add_description_table(section_packages: list[dict]) -> None:
        tbl = Table(stylename="PluginTable")
        tbl.addElement(TableColumn(stylename="ColName"))
        tbl.addElement(TableColumn(stylename="ColDesc"))
        # header row
        hr = TableRow()
        hr.addElement(header_cell("Package"))
        hr.addElement(header_cell("Description"))
        tbl.addElement(hr)
        for pkg in section_packages:
            row = TableRow()
            row.addElement(pkg_cell(pkg))
            row.addElement(cell(make_para(pkg["summary"])))
            tbl.addElement(row)
        doc.text.addElement(tbl)

    def add_format_table(section_packages: list[dict]) -> None:
        tbl = Table(stylename="PluginTable")
        tbl.addElement(TableColumn(stylename="ColName"))
        tbl.addElement(TableColumn(stylename="ColFmt"))
        # header row
        hr = TableRow()
        hr.addElement(header_cell("Package"))
        hr.addElement(header_cell("Plugin formats"))
        tbl.addElement(hr)
        for pkg in section_packages:
            fmts = " / ".join(pkg["formats"]) if pkg["formats"] else "—"
            row = TableRow()
            row.addElement(pkg_cell(pkg))
            row.addElement(cell(make_para(fmts)))
            tbl.addElement(row)
        doc.text.addElement(tbl)

    # --- Document body ------------------------------------------------

    doc.text.addElement(make_heading("Audinux Plugin Catalogue", 1))

    doc.text.addElement(make_heading("Synthesizers", 2))
    add_description_table(synths)

    doc.text.addElement(P())  # blank line between tables

    doc.text.addElement(make_heading("Effects", 2))
    add_description_table(effects)

    doc.text.addElement(P())

    doc.text.addElement(make_heading("All plugins — format index", 2))
    add_format_table(all_pkgs)

    doc.save(str(path))
    print(f"ODT written to {path}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(
        description="Generate markdown and ODT plugin tables from Audinux spec files"
    )
    ap.add_argument(
        "repo_dir",
        nargs="?",
        default=".",
        help="Root of the fedora-spec repository (default: current directory)",
    )
    ap.add_argument(
        "--output-md",
        default="plugin-catalogue.md",
        metavar="FILE",
        help="Write markdown to FILE (default: plugin-catalogue.md)",
    )
    ap.add_argument(
        "--output-odt",
        default="plugin-catalogue.odt",
        metavar="FILE",
        help="Write ODT to FILE (default: plugin-catalogue.odt)",
    )
    ap.add_argument("--no-md",  action="store_true", help="Skip markdown output")
    ap.add_argument("--no-odt", action="store_true", help="Skip ODT output")
    args = ap.parse_args()

    repo = Path(args.repo_dir)
    if not repo.is_dir():
        sys.exit(f"ERROR: directory not found: {repo}")

    specs = sorted(repo.rglob("*.spec"))
    if not specs:
        sys.exit(f"ERROR: no *.spec files found under {repo}")

    print(f"Scanning {len(specs)} spec files …", file=sys.stderr)

    packages = []
    for spec in specs:
        pkg = parse_spec(spec)
        if pkg:
            packages.append(pkg)

    packages.sort(key=lambda p: p["name"].casefold())

    synths  = [p for p in packages if p["is_synth"]]
    effects = [p for p in packages if p["is_effect"]]
    all_pkgs = sorted(
        {p["name"]: p for p in packages}.values(),
        key=lambda p: p["name"].casefold(),
    )

    print(
        f"  → {len(all_pkgs)} unique packages "
        f"({len(synths)} synth entries, {len(effects)} effect entries)",
        file=sys.stderr,
    )

    if not args.no_md:
        write_markdown(synths, effects, all_pkgs, Path(args.output_md))

    if not args.no_odt:
        write_odt(synths, effects, all_pkgs, Path(args.output_odt))


if __name__ == "__main__":
    main()
