# CLAUDE.md

## Project Overview

Audinux is a Fedora-based repository providing audio production software,
including plugins (LV2, VST3, CLAP), standalone applications, and supporting libraries.

The goal is to provide stable, well-packaged, and reproducible builds
for audio professionals and enthusiasts.

---

## Build Environment

- Target distribution: Fedora (latest stable + rawhide when possible)
- Packaging format: RPM
- Build system: rpmbuild, mock
- Spec files location: per-package directories

### Common tools:
- cmake
- meson
- ninja
- gcc / clang

---

## Packaging Rules

- Follow Fedora Packaging Guidelines strictly
- Do NOT bundle dependencies unless absolutely required
- Prefer system libraries over vendored ones
- Use `%cmake`, `%meson`, `%configure` macros where appropriate
- Always split packages correctly:
  - main package
  - -devel (if applicable)
  - -doc (if applicable)

---

## Audio Plugin Specifics

- Supported formats:
  - LV2 (preferred)
  - VST3
  - CLAP

- Install paths must follow Fedora conventions:
  - LV2: %{_libdir}/lv2
  - VST3: %{_libdir}/vst3
  - CLAP: %{_libdir}/clap

- Never hardcode `/usr/lib` or `/usr/lib64`

---

## Common Pitfalls

- Do not enable unsupported CPU optimizations (e.g. AVX512) by default
- Avoid static linking unless required
- Be careful with real-time audio constraints (no debug flags that break performance)
- Watch for plugins that try to download assets at build time (forbidden)

---

## vcpkg and External Dependencies

- Avoid using vcpkg unless explicitly required
- Prefer Fedora packages
- If vcpkg is used:
  - Document clearly why
  - Ensure reproducibility
  - Avoid network access during build

---

## Testing

- Ensure the package builds in mock
- Check that plugins are correctly discovered by hosts:
  - Carla
  - Ardour
- Validate that no files are installed outside expected directories

---

## Spec File Guidelines

- Keep spec files minimal and readable
- Avoid duplication across packages
- Use macros whenever possible
- Comment non-obvious decisions

---

## Instructions for AI Assistants

When modifying this repository:

- Prefer minimal, incremental changes
- Do NOT introduce new dependencies without justification
- Do NOT change install paths unless required by Fedora policy
- Always ensure RPM builds succeed
- Do NOT break existing packages

When adding a new package:

1. Create a clean spec file
2. Ensure license is correct and included
3. Verify sources are reproducible
4. Test build in mock
5. Ensure plugin is usable in a host

When fixing a package:

- Identify root cause (build system, dependency, patch)
- Avoid quick hacks unless documented
- Prefer upstream fixes when possible

---

## Non-Goals

- This project is NOT a rolling upstream mirror
- Do NOT package unstable or broken software without clear labeling
- Do NOT prioritize bleeding-edge over stability

---

## Maintainer Notes

- Many packages are sensitive to:
  - compiler versions
  - SIMD flags
  - real-time constraints

Be conservative in changes.

If unsure: prefer not changing behavior.

