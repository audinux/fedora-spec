# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Pau Aliagas <linuxnow@gmail.com>
# the build runs with --nodeps, without systemd-rpm-macros: the unit directory is then the one it defines
%{!?_unitdir:%global _unitdir %{_prefix}/lib/systemd/system}

Name: omx-panel
Version: 0.9.1
Release: 1%{?dist}
License: GPL-3.0-or-later
Summary: Panels for LV2 and CLAP plugins, generated from what each plugin declares
URL: https://github.com/FreeMixer/omx-panel
BuildArch: noarch

Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: sed
BuildRequires: nodejs >= 18
# npm ci fetches typescript (the build) and ajv (the validator, bundled below) from the registry, unless Source0 is
# the vendored tarball (tools/vendored-source.sh), which holds them; the build still runs npm itself
BuildRequires: npm
# %%check reads the installed vocabulary: omx-contract's schema, plugin-hostd's LV2 table, and the param-contract
# unit sheet (omx-contract's OMX_PARAM_CONTRACT_UNITS, from 3.6.0); nothing of omx-plugins, which builds with this package
BuildRequires: omx-contract-data >= 3.6.0
BuildRequires: plugin-hostd-contract >= 0.12.0
# omx-modgui-sync lists the LV2 plugins with lilv and scans one with no descriptor with plugin-hostd-probe
Recommends: python3-lilv
Recommends: plugin-hostd
# %%check runs omx-modgui-sync over a bundle
BuildRequires: python3-lilv
BuildRequires: systemd-rpm-macros

Requires: nodejs >= 18
# the layout reads omx-contract's meanings and plugin-hostd's unit table from the contract directory these install
Requires: omx-contract-data >= 3.6.0
Requires: plugin-hostd-contract >= 0.12.0
# the descriptors of omx-plugins' plugins, for modgui --installed
Recommends: omx-plugins-contract >= 0.15.0
Provides: bundled(nodejs-ajv)

%description
omx-panel makes panels for LV2 and CLAP plugins from what each plugin
declares. It lays a panel out from a plugin's descriptor (sections, controls,
roles, the pages of eight a controller shows), writes a MOD GUI for MOD and
Zynthian in the omx look, imports a plugin's own MOD GUI into a skin package,
and carries the skin package schema, its validator and the directory skin
packages are installed into. The omx-panel command runs each; the tools are
under /usr/share/omx-panel for a build that calls them.

%prep
%autosetup

%build
test -d node_modules || npm ci --no-audit --no-fund
%make_build

%install
%make_install PREFIX=%{_prefix} BINDIR=%{_bindir} DATADIR=%{_datadir} UNITDIR=%{_unitdir} SYSCONFDIR=%{_sysconfdir}

%check
make test

%files
%license LICENSE
%doc README.md docs/
%{_bindir}/omx-panel
%{_bindir}/omx-modgui-sync
%{_bindir}/omx-complement-sync
%{_mandir}/man1/omx-panel.1*
%{_mandir}/man1/omx-modgui-sync.1*
%{_mandir}/man1/omx-complement-sync.1*
# installed, never enabled: no preset names them; `systemctl enable omx-modgui-sync` (omx-complement-sync) is the choice
%{_unitdir}/omx-modgui-sync.service
%{_unitdir}/omx-complement-sync.service
%dir %{_unitdir}/plugin-qualify-sync.service.d/
%{_unitdir}/plugin-qualify-sync.service.d/omx-modgui-sync.conf
%{_unitdir}/plugin-qualify-sync.service.d/omx-complement-sync.conf
%dir %{_sysconfdir}/omx/
%config(noreplace) %{_sysconfdir}/omx/modgui-sync.conf
%{_datadir}/omx-panel/
%dir %{_datadir}/omx/
%dir %{_datadir}/omx/skins/

%changelog
* Tue Nov 03 2026 Pau Aliagas <linuxnow@gmail.com> - 0.9.1-1
- 0.9.0 was tagged but not published: the release proof ran make check without
  the shared private-refs check at hand. Everything 0.9.0 carries is in this
  release; the release workflow now fetches that check before make check.
* Tue Nov 03 2026 Pau Aliagas <linuxnow@gmail.com> - 0.9.0-1
- The MOD GUI test bundle ships with the package, exported as
  @openmixer/omx-panel/fixtures, so a package that tests against it reads it
  from here instead of keeping a copy (#116).
- The commit message and private reference checks run from the shared
  FreeMixer/.github workflow; the local copies are gone (#115).
* Sun Nov 01 2026 Pau Aliagas <linuxnow@gmail.com> - 0.8.1-1
- The param-contract unit codes are read from omx-contract's
  OMX_PARAM_CONTRACT_UNITS sheet (omx-contract-data 3.6.0), no longer from
  omx-plugins-contract's param-units.json, which omx-plugins 0.17.0 drops. The
  omx-contract-data requirement is now >= 3.6.0.
* Sun Nov 01 2026 Pau Aliagas <linuxnow@gmail.com> - 0.8.0-1
- The Easy face: every plugin's handful of controls, from a declared list, else
  its family's roles, else its first controls. omx-panel layout --pages
  --easy-first and omx-panel modgui --easy-first put them first; without the
  option every page and file is as before. omx-modgui-sync turns it on.
- Compare A/B/C/D and an undo ring per processor, as pure functions a host runs:
  @openmixer/omx-panel/compare, and omx-panel compare for other hosts.
* Fri Oct 30 2026 Pau Aliagas <linuxnow@gmail.com> - 0.7.2-1
- omx-panel layout --pages --per-page N cuts each section into pages of at most
  N controls, in the section's order, keeping a declared group that fits a page
  whole and naming each page of a section by the controls it holds; without
  --per-page the pages are the plain cut of eight, as before (#93).

* Thu Oct 29 2026 Pau Aliagas <linuxnow@gmail.com> - 0.7.1-1
- The DEB builds again: v0.7.0 shipped without packages because the release
  lint refused the bundled font as a duplicate of a distribution font, which
  the package carries on purpose so the screenshot bytes are the same on every
  host. CI now builds and lints the DEB on every pull request (#85).
- The screenshot and thumbnail text is set in Inter, the look's own font
  (Inter 4.1, SIL OFL 1.1, its licence beside it), in place of Liberation
  Sans; the fixture images are regenerated (#83).

* Thu Oct 29 2026 Pau Aliagas <linuxnow@gmail.com> - 0.7.0-1
- The MOD GUI screenshot and thumbnail carry text: the plugin title, the
  section labels (one band per section, so per group of a grouped descriptor)
  and each control's name and default with its unit. The text is drawn from a
  font file the look names, Liberation Sans (SIL OFL 1.1, its licence beside
  it), with no host font, so the bytes are the same on every host. --check
  still refuses a stale image (#78).
- A modulation depth in octaves keeps its depth role and is published with its
  unit, so omx-phaser's depth gets a control (omx-plugins#232).
- Two LV2 bundles that would share one complement name are both written, under
  names derived from their paths, instead of both being refused (#72).

* Wed Oct 28 2026 Pau Aliagas <linuxnow@gmail.com> - 0.6.0-1
- The LV2 complement is new: the port groups an LV2 plugin does not declare
  are inferred from what it does declare (designations, shared name or
  symbol prefixes and trailing numbers, units, runs of port index, its own
  MOD GUI) and written into a replacing bundle, so the Zynthian touchscreen
  shows a plugin in sections instead of screens of four. A plugin whose
  grouping is not confident, or whose own groups are complete, is left as
  it is (plugin-hostd#218, G1, G2).
- omx-panel complement writes that bundle, named omx-complement-<bundle>.lv2
  and marked, beside the installed one; the installed files are never
  written. The inference is exported as
  @openmixer/omx-panel/group-infer (plugin-hostd#218, G1, G2).
- omx-complement-sync is a new binary, with omx-complement-sync.service and
  a man page. The unit is installed but not enabled; enabled, a drop-in on
  plugin-qualify-sync.service queues it after each scan, as for
  omx-modgui-sync (plugin-hostd#218, G2).
- A bundle of ours that is no longer wanted is removed, not reported, and
  omx-panel complement --check exits 3 for a stale or out-of-date bundle
  (plugin-hostd#218, G3).
- A generated group node never merges into one already in the bundle: a
  bundle that would collide is refused as group-iri-collision, and two
  bundles that would share one complement name are both refused
  (plugin-hostd#218, G3).
- The Turtle reader keeps an absolute IRI as written, and resolves only a
  relative one (plugin-hostd#218, G2).

* Wed Oct 28 2026 Pau Aliagas <linuxnow@gmail.com> - 0.5.0-1
- A CLAP control whose id is a number is keyed p<id>, so two parameters of
  one name no longer stop the layout; the published keys of scanned CLAP
  plugins change (#27).
- omx-panel modgui adds rdfs:seeAlso <modgui.ttl> to the bundle's
  manifest.ttl when the manifest exists and lacks it, and --check refuses a
  manifest without it (#28).
- A choice control without values is refused by code
  (MODGUI_CHOICE_NO_VALUES) naming the control (#30).
- A descriptor with no control to lay out is refused by code and the refusal
  says why (#31, the omx-panel half).
- A trigger control is left off the MOD GUI face and named on stderr; the
  rest is drawn (#47).
- omx-modgui-sync.service no longer carries WantedBy=plugin-qualify-
  sync.service: a drop-in on plugin-qualify-sync.service starts it after
  each scan when it is enabled, so a scan that begins while a GUI run is
  queued still gets its GUI run (#61).

* Wed Oct 28 2026 Pau Aliagas <linuxnow@gmail.com> - 0.4.3-1
- A control name holding a line break, a return or a tab no longer writes invalid
  Turtle: lilv refused the whole bundle (#51). The DEB of 0.4.2 was not
  published (lintian refused the unit's WantedBy); this is the first DEB with
  omx-modgui-sync's new search rule and the unit that follows plugin-qualify-sync.

* Wed Oct 28 2026 Pau Aliagas <linuxnow@gmail.com> - 0.4.2-1
- omx-modgui-sync reads the LV2 search list as plugin-hostd and plugin-qualify
  do ($LV2_PATH, else plugin-hostd's default), writes its bundles to
  /usr/local/lib/lv2 (~/.lv2 for a user; the folder may hold plugins too, and the
  bundles are named omx-modgui-<name>.lv2), and has --check: it says whether
  mod-host and mod-ui read the folder, and lists the CLAP search list (#44).
- The unit runs after plugin-qualify-sync once enabled, under CPU, memory and
  task limits. The Debian-only apt hook is gone.

* Tue Oct 27 2026 Pau Aliagas <linuxnow@gmail.com> - 0.4.1-1
- The DEB builds on Debian bookworm again: python3-lilv is no build dependency
  (bookworm has none); the omx-modgui-sync tests skip without it. The RPM is
  unchanged (#44).

* Tue Oct 27 2026 Pau Aliagas <linuxnow@gmail.com> - 0.4.0-1
- omx-modgui-sync, moved here from the Zynthian image: gives a generated MOD GUI to
  every LV2 plugin that ships none, into /var/lib/omx/modgui (standard directories,
  set in /etc/omx/modgui-sync.conf). The unit is installed, not enabled. A plugin
  that cannot get a GUI never fails the run (#44).

* Tue Oct 27 2026 Pau Aliagas <linuxnow@gmail.com> - 0.3.4-1
- The unit table is read from the contract data (param-units.json, installed by
  omx-plugins-contract) and not from the C header omx_param_contract.h, which
  only omx-plugins-devel ships: a runtime install lays out a control with a
  unit. omx-plugins-contract >= 0.15.0 is now required. $OMX_PARAM_CONTRACT_H
  is gone (#44).

* Tue Oct 27 2026 Pau Aliagas <linuxnow@gmail.com> - 0.3.3-1
- The MOD GUI's brand is the vendor, else the plugin name, else the file stem; a
  plugin that states no vendor is no longer refused (#44).
- `omx-panel modgui` exits 3, with one line and no stack trace, for a descriptor
  with no visible control (#44).

* Tue Oct 27 2026 Pau Aliagas <linuxnow@gmail.com> - 0.3.2-1
- A reader that stops early (head, grep -q) ends the output quietly: exit 0, no
  stack trace (#42).

* Tue Oct 27 2026 Pau Aliagas <linuxnow@gmail.com> - 0.3.1-1
- `omx-panel descriptors --installed` lists the installed descriptor files, one
  path per line (#37).

* Sun Oct 25 2026 Pau Aliagas <linuxnow@gmail.com> - 0.3.0-1
- The MOD GUI importer reads mod-ui's whole modgui:gui property list, refuses
  MODGUI_PORT_UNKNOWN and MODGUI_IMAGE_NOT_FOUND (ten refusal codes), and reads
  a template reference as mod-ui reads it (#33).

* Sun Oct 25 2026 Pau Aliagas <linuxnow@gmail.com> - 0.2.6-1
- A readout is drawn as a display, never looked up as a control input; 0.2.5
  stopped on a readout. The worked example, with its documents and examples.

* Sun Oct 25 2026 Pau Aliagas <linuxnow@gmail.com> - 0.2.5-1
- A man page for omx-panel; shipped declarations carry no shebang. 0.2.4
  shipped no DEB.

* Sun Oct 25 2026 Pau Aliagas <linuxnow@gmail.com> - 0.2.4-1
- The Debian package no longer carries the vendored modules' dotfiles; 0.2.3
  shipped no DEB.

* Sun Oct 25 2026 Pau Aliagas <linuxnow@gmail.com> - 0.2.3-1
- The Debian package depends on pkgconf, which the vocabulary reader runs;
  0.2.2 shipped no DEB either.

* Sun Oct 25 2026 Pau Aliagas <linuxnow@gmail.com> - 0.2.2-1
- The Debian build depends on node, npm and the dev packages its suite reads;
  0.2.1 shipped no DEB.

* Sun Oct 25 2026 Pau Aliagas <linuxnow@gmail.com> - 0.2.1-1
- The npm package is @openmixer/omx-panel; 0.2.0 named a scope that does not
  exist on the registry and never reached npm.

* Sun Oct 25 2026 Pau Aliagas <linuxnow@gmail.com> - 0.2.0-1
- The panel toolkit: the layout from a descriptor, the MOD GUI generator and
  its images, the omx look, the skin package at schema 1 with its facts, and
  the MOD GUI importer.
* Sat Oct 17 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.0-1
- First package: the skin package schema and the skins directory.
- The package was named omx-skins until 2026-10-25.
