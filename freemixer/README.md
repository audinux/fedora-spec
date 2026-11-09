# Build order

Dependencies traced from each spec's `BuildRequires`/subpackage `%files`.

## 0. External prerequisites (outside this directory)

- `clap/clap.spec` -> provides `clap-devel`, needed by `omx-clap-host.spec` and `plugin-qualify.spec`
- `moddevices/mod-host.spec` -> provides `mod-host-protocol-devel`, needed by `omx-clap-host.spec`

## 1. No local dependencies

- `libdiginet.spec`
- `libmackie.spec`
- `libreac.spec` (FreeREAC org)
- `omx-contract.spec`

## 2. Depend only on tier 1

- `libsurface.spec` (needs libdiginet + libmackie)
- `reac-pw.spec` (needs libreac)
- `omx-dsp.spec` (needs omx-contract)
- `plugin-hostd-protocol.spec` (needs omx-contract)

## 3. plugin-hostd.spec (first pass)

Build with `rpmbuild --without check -ba plugin-hostd.spec`.

`plugin-hostd.spec` and `omx-clap-host.spec` are mutually dependent by
default: omx-clap-host needs `pkgconfig(plugin-hostd)`, while
plugin-hostd's `%check` (on by default via `%bcond_without check`) needs
`omx-clap-host-tests`/`omx-clap-core-contract`. The spec itself documents
the fix: build plugin-hostd first with `--without check` to bootstrap it
without needing omx-clap-core/omx-clap-host at all.

## 4. omx-clap-host.spec

Repo name is `omx-clap-core` (package name `omx-clap-host`), see tier 0's
`clap-devel` and `mod-host-protocol-devel`, plus the tier-3 bootstrap
`plugin-hostd`, `omx-dsp`, and `omx-contract`.

## 5. plugin-hostd.spec (optional second pass)

Now that `omx-clap-host-tests`/`omx-clap-core-contract` exist, plugin-hostd
can optionally be rebuilt normally (`--with check`, the default) to run its
full test suite. Not required by any downstream consumer - QA only.

## 6. Depend on plugin-hostd + omx-contract

- `omx-panel.spec` (needs omx-contract-data, plugin-hostd-contract)
- `plugin-qualify.spec` (needs plugin-hostd, omx-contract, omx-clap-lv2
  from omx-clap-host, omxdsp from omx-dsp)

## 7. omx-plugins.spec

Needs omx-dsp, omx-contract, omx-clap-host, plugin-hostd, omx-panel, and
plugin-qualify - the most downstream package.

## 8. omx-qualification-records.spec

No local BuildRequires (noarch, data-only, python3 only at build time), but
its subpackage `Requires: plugin-qualify >= 0.17.0` at install time, so it
only makes sense to build/install after plugin-qualify exists.

NOTE: its `URL`/`Source0` point to `FreeMixer/omx-qualification-records`,
which has been renamed to `FreeMixer/plugin-db-qualification` (GitHub still
redirects the old name for now, but the spec should be updated to the new
name/URL).

## Notes on GitHub orgs

- All spec upstream repos exist in their respective orgs (`FreeMixer` for
  most, `FreeREAC` for `libreac.spec`/`reac-pw.spec`) - nothing is actually
  missing, aside from the `omx-qualification-records` rename noted above.
