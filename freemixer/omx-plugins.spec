# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Pau Aliagas <linuxnow@gmail.com>
Name: omx-plugins
Version: 0.17.0
Release: 1%{?dist}
License: GPL-3.0-or-later
Summary: The OpenMixer console's delay, drive, EQ, channel strip, keyed gate and effects, as plugins for your DAW
URL: https://github.com/FreeMixer/omx-plugins

Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconf-pkg-config
# The releases this tree builds against: a floor each (no ceiling), once here and
# the same in debian/control (tools/deps-check.sh). The Makefile and tools/gen.mjs read them from here.
BuildRequires: omx-dsp-devel >= 0.28.0
BuildRequires: omx-contract-devel >= 3.7.1
BuildRequires: omx-clap-core-devel >= 0.14.0
# plugin-hostd's format tables, which the generators read backwards (tools/format-tables.mjs)
BuildRequires: plugin-hostd-devel >= 0.15.2
# the omx-contract command, first packaged in 2.15.0: the generators read the contract directory through it
# (3.3.0: the directory and its schema are omx-contract-data's, the definitions each owner's -contract package's)
BuildRequires: omx-contract >= 3.7.1
# the panel layout and the MOD GUI are omx-panel's, from a descriptor and the declared panel (tools/omx-panel.mjs)
BuildRequires: omx-panel >= 0.2.0
# omx-panel recommends omx-plugins-devel: an older one installed beside this build puts its release's contract
# package where make test reads this one's (tools/test/contract-dir-check.sh), so a build installs none
BuildConflicts: omx-plugins-devel < %{version}
BuildRequires: clap-devel
BuildRequires: lv2-devel
# %%check: the generators and checks are Node scripts; the hosts that load the built plugins
BuildRequires: nodejs
# make selftest copies the tree with tar
BuildRequires: tar
BuildRequires: diffutils
BuildRequires: lilv
BuildRequires: lilv-devel
BuildRequires: sord
BuildRequires: omx-clap-host
# %%check: make round-trip scans the built faces back with plugin-hostd-probe describe
BuildRequires: plugin-hostd >= 0.15.2
# %%install: our own plugins' pins are known at build time (tools/gen-pins.sh); %%check then holds the
# shipped pins.d file to the shipped binaries' hashes (tools/pins-check.sh)
BuildRequires: plugin-qualify >= 0.9.0
# the shipped .clap is the stripped one (find-debuginfo runs after %%install), so its pin is measured
# again once the buildroot is stripped: a pin taken at %%install names bytes the package never ships
%define __spec_install_post \
    %{?__debug_package:%{__debug_install_post}}\
    %{__arch_install_post}\
    %{__os_install_post}\
    %{__make} -s install-pins DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir} CLAPDIR=/usr/lib/clap\
%{nil}

# The name a user installs: both formats.
Requires: %{name}-clap%{?_isa} = %{version}-%{release}
Requires: %{name}-lv2%{?_isa} = %{version}-%{release}
# each plugin's descriptor, which a host and the console read at run time
Requires: %{name}-contract = %{version}-%{release}
# the first plugin-hostd release that reads pins.d (plugin-hostd issue #42): a floor only, no ceiling
Recommends: plugin-hostd >= 0.5.0

%description
Take the sound of the OpenMixer console into your DAW or onto your own rig:
delay, drive, the channel EQ as an 8-band EQ, a 16-band EQ or a 32-band EQ, a
31-band graphic EQ, the full channel strip and the keyed gate with its sidechain
input, and the console's effects: chorus, flanger, phaser, tremolo, rotary
speaker, reverb, pitch shifter, transient shaper, de-esser, sub-octaver, plosive tamer, clipper, upward compressor, bus compressor, loudness leveler, spectral balancer, spring reverb, limiter, compressor
with its sidechain key, multiband compressor and dynamic EQ. They come
as CLAP plugins for Bitwig, REAPER and Carla, and as LV2 plugins for Ardour,
Carla, MOD and Zynthian. Each one runs the same DSP as the console, so a track sounds the same
in a session as it does on the desk, sample for sample. Every plugin comes in
both formats with the same controls, MOD GUI included.

This package installs both formats; omx-plugins-clap and omx-plugins-lv2
install one each. It also carries the factory presets of every plugin, as
files in %{_datadir}/omx/presets.

%package clap
Summary: OpenMixer delay, drive, EQ, strip, gate and effects as CLAP plugins

%description clap
The OpenMixer console's delay, drive, 8-, 16- and 32-band EQ, 31-band graphic
EQ, channel strip, keyed gate and effects (chorus, flanger, phaser, tremolo,
rotary speaker, reverb, pitch shifter, transient shaper, de-esser, sub-octaver, plosive tamer, clipper, upward compressor, bus compressor, loudness leveler, spectral balancer, spring reverb, limiter, compressor) as
CLAP plugins, installed in /usr/lib/clap where Bitwig, REAPER,
Carla and other CLAP hosts find them. They run the console's own DSP, so they
sound like the desk.

%package lv2
Summary: OpenMixer delay, drive, EQ, strip, gate and effects as LV2 plugins
Requires: lv2

%description lv2
The OpenMixer console's delay, drive, 8-, 16- and 32-band EQ, 31-band graphic
EQ, channel strip, keyed gate and effects (chorus, flanger, phaser, tremolo,
rotary speaker, reverb, pitch shifter, transient shaper, de-esser, sub-octaver, plosive tamer, clipper, upward compressor, bus compressor, loudness leveler, spectral balancer, spring reverb, limiter, compressor) as
LV2 plugins, installed in %{_libdir}/lv2 where Ardour, Carla, MOD
and Zynthian find them, with a MOD GUI where the plugin has one. They run the
console's own DSP, so they sound like the desk.

%package test
Summary: The OpenMixer test instruments, for host tests and plugin measurement

%description test
The test instruments the OpenMixer console's own proofs play: a sine voice, a
pool voice, a note echo and a transport probe, as CLAP plugins. They are installed in
%{_libexecdir}/omx-plugins/test, outside every CLAP search path, so no host
lists them; a test or the plugin qualifier opens them there by path. Install
this package on a console to measure the linked test instruments' cost on its
own machine.

%package devel
Summary: Headers and static library of the OpenMixer plugins, for projects that build on them
Requires: omx-dsp-devel >= 0.28.0
# the generated parameter headers include omx-contract's C renders, and omxplugins.pc requires omx-contract
Requires: omx-contract-devel >= 3.7.1
Requires: %{name}-contract = %{version}-%{release}
Requires: clap-devel

%description devel
The headers other projects include to use the OpenMixer plugins' parameters and
instance code, such as omx_delay_core.h and each plugin's generated
parameter header, installed in %{_includedir}/omx-plugins, and
libomxplugins.a (pkg-config omxplugins): every plugin's CLAP face in one
static library, with the table of their entries in omx_clap_static.h, for a
host that runs the plugins in its own process without loading .clap files.

%package contract
Summary: The OpenMixer plugins' descriptors in omx-contract's contract directory
BuildArch: noarch
# the contract directory, its schema and its reader's own package
Requires: omx-contract-data >= 3.7.1
# the files lived in omx-plugins-devel before this package
Conflicts: %{name}-devel < %{version}-%{release}

%description contract
Each OpenMixer plugin's descriptor, its parameters in omx-contract's words,
and the manifest naming this release, as files in omx-contract's contract
directory, for any program that reads them at run time: a host, the console's
panels and the omx-contract command.

%prep
%autosetup

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir} CLAPDIR=/usr/lib/clap
%{__make} install-devel DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir}
%{__make} install-test DESTDIR=%{buildroot} PREFIX=%{_prefix} TESTCLAPDIR=%{_libexecdir}/omx-plugins/test

%check
# a CI build host holds the channel's omx-plugins-contract before 0.17.0, whose units sheet omx-contract 3.6.0 now
# declares: tools/ci-stale-units.sh drops it there (only under CI, never on a user's system), until 0.17.0 is out
[ -z "${CI:-}${GITHUB_ACTIONS:-}" ] || [ "$(id -u)" != 0 ] || tools/ci-stale-units.sh
%make_build test
# the shipped pins.d file still names the shipped binaries' own hashes (sabotage: a changed binary goes red)
tools/pins-check.sh %{buildroot}%{_datadir}/plugin-hostd/pins.d/omx-plugins.pins %{buildroot}/usr/lib/clap

%files
%license LICENSE
%doc README.md
# the factory presets of every plugin, read only data the console's preset library lists (presets/)
%{_datadir}/omx/presets/
# our own plugins' pins, known at build time (plugin-hostd issue #42's pins.d, a floor-only Recommends above);
# the directory is plugin-hostd's, co-owned here so the package stands on its own at %%files time
%dir %{_datadir}/plugin-hostd/pins.d
%{_datadir}/plugin-hostd/pins.d/omx-plugins.pins

%files clap
%license LICENSE
%doc README.md
%dir /usr/lib/clap
# BEGIN GENERATED clap-files: tools/gen.mjs, one line per shipped plugin
/usr/lib/clap/omx-balancer.clap
/usr/lib/clap/omx-chorus.clap
/usr/lib/clap/omx-clipper.clap
/usr/lib/clap/omx-comp.clap
/usr/lib/clap/omx-deesser.clap
/usr/lib/clap/omx-delay.clap
/usr/lib/clap/omx-drive.clap
/usr/lib/clap/omx-dyneq.clap
/usr/lib/clap/omx-eq8.clap
/usr/lib/clap/omx-eq16.clap
/usr/lib/clap/omx-eq32.clap
/usr/lib/clap/omx-flanger.clap
/usr/lib/clap/omx-geq.clap
/usr/lib/clap/omx-glue.clap
/usr/lib/clap/omx-keyed-gate.clap
/usr/lib/clap/omx-limiter.clap
/usr/lib/clap/omx-loudlevel.clap
/usr/lib/clap/omx-multiband.clap
/usr/lib/clap/omx-phaser.clap
/usr/lib/clap/omx-pitch.clap
/usr/lib/clap/omx-plosive.clap
/usr/lib/clap/omx-reverb.clap
/usr/lib/clap/omx-rotary.clap
/usr/lib/clap/omx-spring.clap
/usr/lib/clap/omx-strip.clap
/usr/lib/clap/omx-suboct.clap
/usr/lib/clap/omx-transient.clap
/usr/lib/clap/omx-tremolo.clap
/usr/lib/clap/omx-upward.clap
# END GENERATED clap-files

%files test
%license LICENSE
%dir %{_libexecdir}/omx-plugins
%dir %{_libexecdir}/omx-plugins/test
# BEGIN GENERATED clap-test-files: tools/gen.mjs, one line per test plugin
%{_libexecdir}/omx-plugins/test/omx-test-note-echo.clap
%{_libexecdir}/omx-plugins/test/omx-test-pool-voice.clap
%{_libexecdir}/omx-plugins/test/omx-test-sine-voice.clap
%{_libexecdir}/omx-plugins/test/omx-test-transport-probe.clap
# END GENERATED clap-test-files

%files devel
%license LICENSE
%{_includedir}/omx-plugins/
%{_libdir}/libomxplugins.a
%{_libdir}/pkgconfig/omxplugins.pc

%files contract
%license LICENSE
# each plugin's descriptor and the manifest, in omx-contract's contract directory (the directory itself is omx-contract-data's)
%{_datadir}/omx-contract/contract.d/3/omx-plugins/

%files lv2
%license LICENSE
%doc README.md
# BEGIN GENERATED lv2-files: tools/gen.mjs, one line per shipped plugin
%{_libdir}/lv2/omx-balancer.lv2/
%{_libdir}/lv2/omx-chorus.lv2/
%{_libdir}/lv2/omx-clipper.lv2/
%{_libdir}/lv2/omx-comp.lv2/
%{_libdir}/lv2/omx-deesser.lv2/
%{_libdir}/lv2/omx-delay.lv2/
%{_libdir}/lv2/omx-drive.lv2/
%{_libdir}/lv2/omx-dyneq.lv2/
%{_libdir}/lv2/omx-eq8.lv2/
%{_libdir}/lv2/omx-eq16.lv2/
%{_libdir}/lv2/omx-eq32.lv2/
%{_libdir}/lv2/omx-flanger.lv2/
%{_libdir}/lv2/omx-geq.lv2/
%{_libdir}/lv2/omx-glue.lv2/
%{_libdir}/lv2/omx-keyed-gate.lv2/
%{_libdir}/lv2/omx-limiter.lv2/
%{_libdir}/lv2/omx-loudlevel.lv2/
%{_libdir}/lv2/omx-multiband.lv2/
%{_libdir}/lv2/omx-phaser.lv2/
%{_libdir}/lv2/omx-pitch.lv2/
%{_libdir}/lv2/omx-plosive.lv2/
%{_libdir}/lv2/omx-reverb.lv2/
%{_libdir}/lv2/omx-rotary.lv2/
%{_libdir}/lv2/omx-spring.lv2/
%{_libdir}/lv2/omx-strip.lv2/
%{_libdir}/lv2/omx-suboct.lv2/
%{_libdir}/lv2/omx-transient.lv2/
%{_libdir}/lv2/omx-tremolo.lv2/
%{_libdir}/lv2/omx-upward.lv2/
# END GENERATED lv2-files

%changelog
* Sat Oct 31 2026 Pau Aliagas <linuxnow@gmail.com> - 0.17.0-1
- omx-dyneq, the six-band dynamic EQ, and omx-multiband, the multiband
  compressor of two to five bands, from omx-dsp 0.26.0's kernels (#179).
- omx-comp takes a key: a sidechain port, the key and duck sections and
  the compKey meter (#179).
- The EQs' and the multiband's band centres, the deesser, drive and
  phaser frequencies and every integer frequency are authored
  logarithmic, as their LV2 faces state; a Hz travel from 0 is not (#276).
- omx-geq declares the fader for its 31 bands (#231).
- The panels are regenerated against omx-panel 0.7.1: the MOD GUI text in
  Inter and the phaser's depth published (#232).
- DEB builds install python3 in CI and read the version without make's
  directory lines (#278).
- omx-test-pool-voice, a test instrument that renders its voices as
  clap.thread-pool tasks (installed by omx-plugins-test only).
- omx-suboct (sub-octaver), omx-plosive (plosive tamer), omx-clipper,
  omx-upward (upward compressor), omx-glue (bus compressor), omx-loudlevel
  (loudness leveler), omx-balancer (spectral balancer) and omx-spring
  (spring reverb), each with its factory presets.
- omx-delay takes up to four read taps of its one line: the number of taps
  and, for each, its time, gain and pan.
- The unit codes come from omx-contract 3.6.0 (omx_param_units.h); the copy in
  omx-plugins-contract is gone, and the build floors are omx-dsp 0.28.0,
  omx-contract 3.6.0 and plugin-hostd 0.15.2.

* Thu Oct 29 2026 Pau Aliagas <linuxnow@gmail.com> - 0.16.0-1
- The EQs carry one parameter group per band on eq8, eq16 and eq32, so a
  touchscreen shows one band per screen (#257).
- The generated headers, LV2 files and descriptors carry the release
  version, taken from the Makefile VERSION (#260).
- The parameter reference of every plugin is generated from the
  declarations and checked.
- The generated doap:maintainer states foaf:homepage, and the manifests
  list modgui.ttl first, so omx-panel 0.5.0's check finds it (#244).
- The panel layout and the MOD GUI are omx-panel's: this repository hands
  it a descriptor and a declared panel, and a build needs omx-panel >=
  0.2.0 (#233).
- The commit-message check runs under the ai-trace-check action and in
  its own named job.

* Wed Oct 28 2026 Pau Aliagas <linuxnow@gmail.com> - 0.15.1-1
- The sixty band-Q controls of eq8, eq16, eq32 and strip link
  EQ_NOTCH_Q_RANGE, the range their travel states (0.3..116), so the travel
  each descriptor states is what its link resolves to. The generator is fixed
  and a check holds every one of the sixty to it (#252).

* Tue Oct 27 2026 Pau Aliagas <linuxnow@gmail.com> - 0.15.0-1
- The plugins' descriptors ship in a noarch package, omx-plugins-contract, in omx-contract's contract
  directory beside a MANIFEST.json naming the release; omx-plugins and the devel package require it.
  The omx-contract floor is 3.4.0.
- The parameter units are a sheet, contract/param-units.json, in that directory, and the unit enum in
  omx_param_contract.h is generated from it.
- The factory kernels' calls follow omx-dsp 0.26.0 (floor 0.26.0): comp, delay, gate and reverb pass its
  new resolve arguments, and a declaration holds a face argument at its kernel's named default.
- The omx-clap-core floor is 0.14.0, the first tag that carries what 0.13.0 was meant to.
- preset-probe refuses a staged location longer than its buffer instead of truncating it; the
  round-trip scan entry for stepped-to-log parameters holds through plugin-hostd 0.12.0.

* Thu Oct 22 2026 Pau Aliagas <linuxnow@gmail.com> - 0.14.0-1
- Our own plugins' pins are known at build time, so they ship with the package instead of being
  recorded by plugin-hostd on first use (plugin-hostd issue #42, pins.d): plugin-qualify --pins runs
  over the plugins the build just installed and the result is packaged as
  /usr/share/plugin-hostd/pins.d/omx-plugins.pins (RPM and DEB), replaced with the binaries in the
  same transaction and removed with the package (tools/gen-pins.sh).
- The package recommends plugin-hostd >= 0.5.0, the first release that reads pins.d: a floor only, no
  ceiling; it co-owns the pins.d directory.
- %%check (RPM) and dh_auto_install (DEB) hold the shipped pins to the shipped binaries' own hashes:
  a plugin's binary changed after its pin was written goes red (tools/pins-check.sh).
- The shipped pin is measured after the package is stripped, so it names the bytes the package ships:
  find-debuginfo (RPM) and dh_strip (DEB) run before make install-pins.
- The new subpackage omx-plugins-test (RPM and DEB) carries the test instruments, a sine voice, a note
  echo and a transport probe, in %%{_libexecdir}/omx-plugins/test, outside every CLAP search path; make
  install-test installs them, make install never does. tools/package-lists-check.sh (make
  package-lists, in make test) refuses a built plugin that no package lists.
- CI runs clap-validator on every built CLAP plugin (tools/clap-validate.sh) and keeps the JSON
  reports; its state-* tests are required (tools/clap-validate-required.mjs), the others are reported.
- Every plugin's CLAP state round trips exactly: a loaded state asks the host to rescan the values, the
  state carries the host's bypass (older states still load), a state that names no parameter is refused
  and a plugin's worst-case state fits the loader. clap-probe state, in every plugin's make test,
  checks it.
- The factory presets, the JSON files in presets/, are offered in every host: CLAP preset-discovery
  (clap.preset-discovery-factory, files in /usr/share/omx/presets/<clap id>/) and clap.preset-load,
  which applies a preset's parameters and asks the host to rescan the values, and a presets.ttl in each
  LV2 bundle with one pset:Preset per file. make test lists and loads them through CLAP discovery,
  preset-load and lilv (FreeMixer/omx-plugins issue #214).
- omx-eq8, omx-eq16, omx-eq32 and omx-strip install their descriptors too: tools/gen.mjs renders the
  descriptor of a base of variants and of a chain, so the contract directory holds all nineteen and
  MANIFEST.json lists them; their CLAP faces state the parameter modules and their LV2 faces the
  designations, as every described plugin's do (tools/test/contract-dir-check.sh requires the four).
- The round-trip ledger records the seven EQ frequency ports that are authored stepped and scan
  back as log, against plugin-hostd issue #147.
- Every plugin declares its resource hints (omx-contract 3.1.0): threads-spawned 0, streams-from-disk
  false and opens-sockets false, served by the CLAP face as org.openmixer.resource-hints.draft/0 and stated
  by the LV2 face as omxres: properties, both from the one declaration. The footprints and the activate
  time stay undeclared until a measurement backs them. Builds against omx-contract >= 3.1.0.
- The Zynthian tarball is repacked from the trixie arm64 DEBs, for ZynthianOS Vangelis (Debian
  trixie); Oram (bookworm) gets no upstream updates. The bundle check refuses a glibc symbol above
  trixie's 2.41 and a library a bare trixie lacks (tools/zynthian-bundle.sh, FreeMixer/omx-plugins
  issue #225).

* Wed Oct 21 2026 Pau Aliagas <linuxnow@gmail.com> - 0.13.0-1
- The descriptors install under contract.d/3, in omx-contract 3.0.0's words:
  CLAP's open features and the LV2 class in the extension bag, the one-line
  description in plugin.doc, a ratio's unit ratio.
- The generators read plugin-hostd's format tables backwards: the LV2 faces
  state 57 lv2:designation param: terms and the ratio unit
  urn:openmixer:unit#ratio, the CLAP faces each parameter's module.
- make round-trip, in make test, replaces make face-descriptor: every described
  plugin's faces are built, scanned back with plugin-hostd-probe describe and
  compared with the authored descriptor word by word.
- Builds against omx-contract >= 3.0.0, plugin-hostd-devel >= 0.7.0 and
  omx-clap-core-devel >= 0.13.0.

* Tue Oct 20 2026 Pau Aliagas <linuxnow@gmail.com> - 0.12.0-1
- Each plugin's descriptor is installed byte for byte in omx-contract's contract
  directory, as contract.d/2/omx-plugins/plugins/<name>.json, with a
  MANIFEST.json that lists every file with its sha256 and this version.
  omx-plugins-devel carries them and needs omx-contract-devel 2.16.0 or newer,
  which owns the directory.
- The spec builds with diffutils, which the new check uses to compare the
  installed descriptors with the sources.

* Sun Oct 18 2026 Pau Aliagas <linuxnow@gmail.com> - 0.11.0-1
- Factory presets: 120 presets for the 19 plugins, installed with the
  omx-plugins package as files in /usr/share/omx/presets, one directory per
  plugin. The catalogue presets are checked against their measured figures
  through the DSP.
- omx-plugins-devel also installs the test plugins' generated declaration
  headers, which hold the constants and CLAP id a test predicts from.
- The compressor and de-esser level meters read their level through omx-dsp's
  omx_meter_level_db instead of a copy of their own. The readings are bit for
  bit the same.
- Builds against omx-dsp >= 0.24.0 and omx-contract >= 2.16.0.
- The oracles take their sample rates from omx-contract's
  OMX_ORACLE_FULL_RATES_* names.
- The strip's cross-check declares the low-pass above 0.6 of Nyquist as a
  known gap and checks the rest.
- The parameter, panel, CLAP extension and port group checks each have
  sabotage tests that must fail on a broken face.
- A parallel make no longer races on the EQ default probe: each build makes
  its own copy and moves it into place.

* Sat Oct 17 2026 Pau Aliagas <linuxnow@gmail.com> - 0.10.0-1
- Every plugin over one kernel is described in omx-contract's own words: a
  descriptor file per plugin carries its identity, its controls with their
  symbols, names, groups, meanings and the definitions their travels are
  read from, its ports and its latency, and the declaration keeps only what
  the descriptor has no word for.
- The built CLAP and LV2 faces are scanned as a host scans any plugin, and
  must state exactly what the descriptor says.
- The panel description is laid out from a descriptor, so any plugin, ours
  or a scanned one, gets a panel; a LUFS or dBu level takes the threshold
  and ceiling roles.
- omx transient is no longer drawn under the compressor's family: a declared
  family needs the meanings it stands on.
- Builds against omx-contract >= 2.15.0 and omx-dsp >= 0.22.0, which ships
  the kernels' definitions; the build reads them from the contract directory
  through the omx-contract command.

* Fri Oct 16 2026 Pau Aliagas <linuxnow@gmail.com> - 0.9.0-1
- Every meter is coherent: the plugins publish their meters through a ring
  of three copies, so a host never reads values from two different blocks.
- omx comp reports its gain reduction and its input and output levels, and
  the de-esser its input and output levels.
- omx pitch declares its units: semitones and cents are whole steps that a
  host shows as semitones and cents, and the mix as a percent.
- The plugins use the meters header omx-clap-core installs instead of a
  copy of their own.
- The first release that waits for plugin-qualify: every plugin is measured
  for real-time safety and must be rated suitable before any package is
  built, and the verdicts are kept with the release run.

* Thu Oct 15 2026 Pau Aliagas <linuxnow@gmail.com> - 0.8.0-1
- Library dependencies are a floor only, no ceiling: omx-dsp >= 0.18.0
  (the first release the plugins build and pass make test against; 0.17.0
  does not link) and omx-contract >= 2.11.0. tools/deps-check.sh fails on
  any upper bound.
- The parameter-contract header names the LUFS unit (OMX_CLAP_UNIT_LUFS,
  0x103), which openmixer's MAIN loudness target travels in.

* Wed Oct 14 2026 Pau Aliagas <linuxnow@gmail.com> - 0.7.0-1
- Built against omx-dsp 0.18.0 (at least 0.18.0, below 0.19) and omx-
  contract 2.11.0 (at least 2.11.0, below 2.12). No pins file: the
  packaging declares both ranges and the build reads them from there.
- The manuals read every range, default and limit from the plugins'
  parameters, which come from omx-contract, so a travel moved in the
  contract moves the manual with it.

* Tue Oct 13 2026 Pau Aliagas <linuxnow@gmail.com> - 0.6.0-1
- Built against omx-dsp 0.13.0 and omx-contract 2.6.0, the pair the channel
  installs.
- omx comp takes the compressor's detector topology: Feedforward hears the
  input, Feedback the compressor's own output. omx strip keeps its
  parameters and runs its compressor feed-forward.
* Tue Oct 13 2026 Pau Aliagas <linuxnow@gmail.com> - 0.5.1-1
- omx deesser reports its gain reduction: the CLAP face serves the kernel's
  gain reduction per block through clap.meters/1, and its oracle holds that
  meter to the kernel at every rate.
- A plugin declares its meters in its declaration; the generator serves them
  through clap.meters/1 and checks them in the oracle.
* Mon Oct 12 2026 Pau Aliagas <linuxnow@gmail.com> - 0.5.0-1
- The faces follow omx-dsp 0.6.0, the oldest release they build against now.
- omx pitch reports its latency at full mix: its shortest delay plus half its
  window, 883 frames at 44.1 kHz, and 0 below 100 %, where the dry signal is
  on time. The CLAP face takes a new latency at its next activation and asks
  the host for that restart when the mix crosses 100 %; the LV2 latency port
  follows the mix.
- Every face serves its panel description, read from its declaration.
- The CLAP faces carry the extensions their declaration names: the parameter
  contract, remote-control pages and each placement's defaults.
- Each plugin declares its panel once; the console's sections and graphs are
  part of it.
- The panels use one widget vocabulary, the console's names.
- The LV2 faces group their ports, one group per panel section.
- The MOD GUI look is generated from its design tokens.
- The declarations' comments are in plain words.
* Sun Oct 11 2026 Pau Aliagas <linuxnow@gmail.com> - 0.4.0-1
- **libomxplugins**: one static library with a table of every plugin's CLAP
  entry, so a host links the plugins in-process without dlopen. The devel
  package ships `libomxplugins.a`, `omx-plugins/omx_clap_static.h` and
  `omxplugins.pc`; `omx_clap_static_find(id)` returns a plugin's entry and
  `omx_clap_static_entry` is one entry whose factory lists them all.
* Sat Oct 10 2026 Pau Aliagas <linuxnow@gmail.com> - 0.3.0-1
- New plugin, **omx comp** (CLAP and LV2): the console's compressor.
  Threshold, ratio and knee set how hard it holds the level down, attack and
  release how fast, with make-up gain and a dry/wet mix; Kind picks the RMS
  detector (compressor) or the peak detector (limiter), and detector
  oversampling can run the control path at 4x.
- **omx strip** is now built from its declaration, as a chain of the console's
  own stages: input trim, high- and low-pass filters, gate, four-band EQ and
  compressor, each with its own on/off switch, in the console's order or any
  other.
- **omx strip: sessions saved with 0.2.0 do not load as they were.** Its
  parameter list changed: the new Input and Filters switches come first, so
  every later parameter moved; Order now picks among the 120 orders of five
  stages (0 is still the console's order); the gate gains knee start and end,
  hold and hysteresis; the RMS switch is replaced by Kind (compressor, RMS
  detector, or limiter, peak), and a fresh strip now starts as a compressor
  where 0.2.0 started with the peak detector; the compressor gains mix and
  detector oversampling. At the settings 0.2.0 had, the strip sounds the same,
  sample for sample.
- Builds against omx-dsp 0.5.2 and omx-contract 2.3.0, the releases with the
  input trim.

* Thu Oct 08 2026 Pau Aliagas <linuxnow@gmail.com> - 0.2.0-1
- New plugin, **omx keyed-gate** (CLAP and LV2): the console's keyed gate, its
  detector fed by a sidechain key the host routes to it, or by the signal
  itself. It takes over the keyed gate bundle the OpenMixer console shipped,
  with the same LV2 URI, ports and defaults.
- New plugins, **omx eq16** and **omx eq32** (CLAP and LV2): the console's
  channel EQ as a 16-band EQ and a 32-band EQ, the same bands, pass filters
  and DSP as omx eq8. Stereo, zero latency; every band starts off, so a
  freshly loaded instance passes the signal untouched.
- Every LV2 plugin shows its controls as the console's bundles did:
  frequencies on a logarithmic travel in hertz, gains in dB, times,
  percentages and octaves in their units, the latency in frames, and the EQ
  band types and filter slopes as named choices instead of bare numbers.
- New package **omx-plugins-devel** (RPM) and **omx-plugins-dev** (DEB): the
  headers other projects include, such as omx_delay_instance.h and each
  plugin's generated parameter header, so they stop copying them.
- Every parameter's travel, default and choices now come from the OpenMixer
  contract (omx-contract 1.3.0), not from numbers typed in each plugin, so a
  plugin and the console cannot disagree about a range. A fresh EQ (eq8, eq16,
  eq32) now starts with its bands where the console's one rule puts them: four
  bands at 100, 400, 2000 and 8000 Hz, any other count spread evenly and
  snapped to preferred frequencies, a low shelf first, a high shelf last and
  bells between. Every band still starts off, so a freshly loaded instance
  passes the signal untouched.
- The CLAP plugins now install to /usr/lib/clap on every distribution, the
  path the CLAP standard gives for Linux. The Fedora packages used
  /usr/lib64/clap before.
- Builds against omx-dsp 0.2.0 and omx-contract 1.3.0; CI runs on GitHub's
  ubuntu-latest runners.

* Wed Oct 07 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.0-1
- First package: the OpenMixer console's delay, drive, 8-band EQ and channel
  strip, each as a CLAP and an LV2 plugin, running the same DSP as the console
  (omx-dsp 0.1.4).
