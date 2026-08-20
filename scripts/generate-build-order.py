#!/usr/bin/env python3
"""
generate-build-order.py — Generate a topologically sorted SRPM build order.

Reads all *.src.rpm files from a directory, extracts each package's name
and BuildRequires via rpm(8), resolves intra-set dependencies, then outputs
the filenames in an order safe for sequential COPR submission (dependencies
first).

Usage:
    python3 generate-build-order.py [SRPM_DIR] [--output FILE]

    SRPM_DIR  directory containing *.src.rpm files  (default: ./tmp)
    --output  write ordered filenames to FILE instead of stdout

The output is one SRPM filename per line, suitable for use as FILELIST
in rebuild-packages.sh.

Requirements:  rpm  (rpm-build package on Fedora)
"""

import argparse
import subprocess
import sys
from collections import defaultdict, deque
from pathlib import Path


# ---------------------------------------------------------------------------
# RPM helpers
# ---------------------------------------------------------------------------

def _rpm_qp(srpm: Path, *args: str) -> str:
    try:
        return subprocess.check_output(
            ["rpm", "-qp"] + list(args) + [str(srpm)],
            stderr=subprocess.DEVNULL,
        ).decode(errors="replace").strip()
    except subprocess.CalledProcessError:
        return ""


def get_name(srpm: Path) -> str:
    return _rpm_qp(srpm, "--qf", "%{name}")


def get_requires(srpm: Path) -> set:
    raw = _rpm_qp(srpm, "--requires")
    result = set()
    for line in raw.splitlines():
        token = line.strip().split()[0] if line.strip() else ""
        if token:
            result.add(token)
    return result


# ---------------------------------------------------------------------------
# Dependency resolution
# ---------------------------------------------------------------------------

# Suffixes that a package named "foo" commonly provides as sub-packages.
_SUFFIXES = (
    "",
    "-devel",
    "-libs",
    "-static",
    "-common",
    "-data",
    "-doc",
    "-tools",
)


def build_provides_map(names: set) -> dict:
    """Map every token a local package might provide → that package's name."""
    m = {}
    for name in names:
        for suffix in _SUFFIXES:
            m[name + suffix] = name
        # pkgconfig(foo) and cmake(foo) → foo or foo-devel
        m[f"pkgconfig({name})"] = name
        m[f"cmake({name})"] = name
        # Some packages expose perl/python module names like perl(Foo::Bar)
        # which we can't guess without building; skip those.
    return m


def resolve_deps(
    name_to_requires: dict, provides_map: dict
) -> dict:
    """
    Return deps[pkg] = set of local packages that must be built before pkg.
    """
    deps = {name: set() for name in name_to_requires}
    for pkg, reqs in name_to_requires.items():
        for req in reqs:
            # Strip any version constraint ("foo >= 1.0" → "foo")
            token = req.split()[0]
            provider = provides_map.get(token)
            if provider and provider != pkg:
                deps[pkg].add(provider)
    return deps


# ---------------------------------------------------------------------------
# Topological sort (Kahn's algorithm)
# ---------------------------------------------------------------------------

def topo_sort(all_names: set, deps: dict) -> list:
    """
    Return names in build order (dependencies first).
    Appends any cycle members at the end with a warning.
    """
    # in_degree[A] = number of local packages A depends on
    in_degree = {n: len(deps[n]) for n in all_names}

    # rdeps[B] = set of packages that depend on B
    rdeps: dict = defaultdict(set)
    for pkg, dep_set in deps.items():
        for dep in dep_set:
            rdeps[dep].add(pkg)

    # Start with packages that have no local dependencies
    queue = deque(sorted(n for n in all_names if in_degree[n] == 0))
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for dependent in sorted(rdeps[node]):
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)

    # Detect cycles
    remaining = [n for n in all_names if n not in set(order)]
    if remaining:
        print(
            f"WARNING: circular dependency detected among "
            f"{len(remaining)} package(s); appending them at the end:",
            file=sys.stderr,
        )
        for n in sorted(remaining):
            cycle_deps = deps[n] & set(remaining)
            print(f"  {n}  ←→  {', '.join(sorted(cycle_deps))}", file=sys.stderr)
        order.extend(sorted(remaining))

    return order


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(
        description="Generate a topologically sorted COPR build order from src.rpm files"
    )
    ap.add_argument(
        "srpm_dir",
        nargs="?",
        default="tmp",
        help="Directory containing *.src.rpm files (default: tmp)",
    )
    ap.add_argument(
        "--output", "-o",
        default="",
        help="Write result to FILE instead of stdout",
    )
    args = ap.parse_args()

    srpm_dir = Path(args.srpm_dir)
    if not srpm_dir.is_dir():
        sys.exit(f"ERROR: directory not found: {srpm_dir}")

    srpms = sorted(srpm_dir.glob("*.src.rpm"))
    if not srpms:
        sys.exit(f"ERROR: no *.src.rpm files found in {srpm_dir}")

    print(f"Found {len(srpms)} src.rpm files — extracting metadata …", file=sys.stderr)

    # name → srpm path
    name_to_srpm: dict = {}
    # name → set of BuildRequires tokens
    name_to_requires: dict = {}

    for srpm in srpms:
        name = get_name(srpm)
        if not name:
            print(f"  WARNING: could not read name from {srpm.name}", file=sys.stderr)
            continue
        if name in name_to_srpm:
            # Keep the newer one (higher filename sorts last with version ordering)
            existing = name_to_srpm[name]
            print(
                f"  WARNING: duplicate name '{name}': {existing.name} vs {srpm.name}"
                f" — keeping {srpm.name}",
                file=sys.stderr,
            )
        reqs = get_requires(srpm)
        name_to_srpm[name] = srpm
        name_to_requires[name] = reqs

    all_names = set(name_to_srpm.keys())
    print(f"  → {len(all_names)} unique package names", file=sys.stderr)

    provides_map = build_provides_map(all_names)
    deps = resolve_deps(name_to_requires, provides_map)

    # Report intra-set dependencies found
    total_edges = sum(len(d) for d in deps.values())
    print(f"  → {total_edges} intra-set dependency edge(s) found", file=sys.stderr)
    if total_edges:
        for pkg in sorted(deps):
            if deps[pkg]:
                print(
                    f"    {pkg}  ←  {', '.join(sorted(deps[pkg]))}",
                    file=sys.stderr,
                )

    order = topo_sort(all_names, deps)

    lines = [name_to_srpm[name].name for name in order]

    if args.output:
        Path(args.output).write_text("\n".join(lines) + "\n")
        print(f"Wrote {len(lines)} entries to {args.output}", file=sys.stderr)
    else:
        print("\n".join(lines))


if __name__ == "__main__":
    main()
