# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Pau Aliagas <linuxnow@gmail.com>
Name: plugin-qualify
Version:        0.18.5
Release: 1%{?dist}
License: GPL-3.0-or-later
Summary: Find out whether an audio plugin is safe to run in a live mixing console
URL: https://github.com/FreeMixer/plugin-qualify

Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: nodejs >= 18
BuildRequires: npm
# the CLAP prober, the LV2 measurer and their interposer: the CLAP headers and lilv from Fedora,
# pin.h from plugin-hostd-devel, the declared sample rates from omx-contract-devel, the LV2 host
# features from omx-clap-lv2-devel (a static archive: nothing of it is needed at run time)
BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconfig
BuildRequires: pkgconfig(clap)
BuildRequires: pkgconfig(lilv-0)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(plugin-hostd) >= 0.15.3
BuildRequires: pkgconfig(omx-contract) >= 3.4.0
BuildRequires: pkgconfig(omx-clap-lv2) >= 0.26.2
BuildRequires: pkgconfig(omxdsp) >= 0.21.0
BuildRequires: systemd-rpm-macros

Requires: nodejs >= 18
Requires: python3
# the measurer and the LV2 host probe link lilv, and the descriptors read it through python3-lilv
Requires: lilv-libs
Requires: python3-lilv
# the scanned descriptors are held to omx-contract's schema before they are written (tools/descriptors.py)
Requires: python3-jsonschema
# plugin-hostd-probe, the runner every CLAP plugin is measured through; --pin-files, which the sync takes its pins from, first released in 0.15.0
# 0.15.3: the memory footprint in the probe output, without which every host with a budget reads unmeasured (#114)
Requires: plugin-hostd >= 0.15.3
Recommends: mod-host
# omx-clap-scan, which lists the plugins in a .clap before each is qualified; from 0.23.0 its rows carry the
# remote-control pages (remote_controls), which the descriptors keep
Requires: omx-clap-host >= 0.23.0
# the hosting codes' TypeScript modules, which the shipped tools/gen-hosting-codes.mjs reads through
# tools/clap-core-tsdir.mjs (the CLI's codes are generated at build time, src/hosting-codes.generated.ts):
# /usr/share/omx-clap-core/ts, in the runtime package omx-clap-core from 0.17.0 on; the host above brings the same version
# 0.25.1: the hosting.memory.* codes (#114); 0.26.2: the guarded plugin call and hosting.stability.callee-saved-clobbered
Requires: omx-clap-core >= 0.26.2
%{?systemd_requires}

# The JavaScript and Python are scripts run by their interpreters, never compiled modules.
%global __requires_exclude_from ^%{_prefix}/lib/node_modules/.*$
# the interposer is preloaded by path, never linked: it provides no library to other packages
%global __provides_exclude_from ^%{_libexecdir}/%{name}/.*$

%description
A plugin that glitches on stage is worse than one you never installed.
plugin-qualify takes an LV2 or CLAP plugin and tells you whether it can be
trusted inside a real-time audio engine: it scans the plugin, measures its
latency and CPU cost at the sample rates and buffer sizes you play at, runs it
under a real host with memory checking, and gives one plain verdict. Anything
it could not measure is never a pass. Use it to vet a plugin before a gig, to
curate a plugin collection, or to judge the same plugin against the rules of
different hosts.

%prep
%autosetup

%build
%make_build -C native

%install
packaging/build.sh %{buildroot} %{_prefix}/lib
%make_install -C native LIBEXECDIR=%{_libexecdir}/%{name}
install -d %{buildroot}%{_unitdir} %{buildroot}%{_presetdir} %{buildroot}%{_systemdgeneratordir}
install -m 0755 packaging/systemd/plugin-qualify-sync-generator %{buildroot}%{_systemdgeneratordir}/
install -m 0644 packaging/systemd/plugin-qualify-sync.service packaging/systemd/plugin-qualify-sync.timer \
  packaging/systemd/plugin-qualify-sync.path %{buildroot}%{_unitdir}/
install -m 0644 packaging/systemd/80-plugin-qualify.preset %{buildroot}%{_presetdir}/
install -D -m 0644 packaging/systemd/plugin-qualify.tmpfiles.conf %{buildroot}%{_tmpfilesdir}/plugin-qualify.conf
install -m 0755 packaging/trigger-scan.sh %{buildroot}%{_libexecdir}/%{name}/trigger-scan

# the preset enables the timer and the path unit; nothing here runs a sweep: the timer fires at the next boot,
# and the path unit, armed once the transaction is over, waits for a minute of quiet before its first run
%post
systemd-tmpfiles --create %{_tmpfilesdir}/plugin-qualify.conf >/dev/null 2>&1 || :
%systemd_post plugin-qualify-sync.timer plugin-qualify-sync.path

%posttrans
if [ -d /run/systemd/system ] && systemctl -q is-enabled plugin-qualify-sync.path 2>/dev/null; then
  systemctl start plugin-qualify-sync.path >/dev/null 2>&1 || :
fi
# an upgrade: the pins on disk get the files this plugin-hostd collects, measuring nothing (plugin-qualify#239)
if [ -s /var/lib/omx/qualify-sync.json ]; then
  %{_bindir}/plugin-qualify-sync --system --refresh-pins --no-wait >/dev/null 2>&1 || :
fi

# a plugin package installed, upgraded or removed in a standard folder: one scan per transaction
%transfiletriggerin -- /usr/lib/lv2 /usr/lib64/lv2 /usr/local/lib/lv2 /usr/lib/clap /usr/lib64/clap
%{_libexecdir}/%{name}/trigger-scan

%transfiletriggerpostun -- /usr/lib/lv2 /usr/lib64/lv2 /usr/local/lib/lv2 /usr/lib/clap /usr/lib64/clap
%{_libexecdir}/%{name}/trigger-scan

%preun
%systemd_preun plugin-qualify-sync.timer plugin-qualify-sync.path plugin-qualify-sync.service

%postun
%systemd_postun plugin-qualify-sync.timer plugin-qualify-sync.path plugin-qualify-sync.service

%files
%license LICENSE
%doc README.md
%{_bindir}/plugin-qualify
%{_bindir}/plugin-qualify-sync
%{_bindir}/plugin-qualify-records-package
%{_mandir}/man1/plugin-qualify.1*
%{_mandir}/man1/plugin-qualify-sync.1*
%{_mandir}/man1/plugin-qualify-records-package.1*
%dir %{_sysconfdir}/omx
%config(noreplace) %{_sysconfdir}/omx/qualify.conf
%{_unitdir}/plugin-qualify-sync.service
%{_unitdir}/plugin-qualify-sync.timer
%{_unitdir}/plugin-qualify-sync.path
%{_systemdgeneratordir}/plugin-qualify-sync-generator
%{_presetdir}/80-plugin-qualify.preset
%{_tmpfilesdir}/plugin-qualify.conf
%{_prefix}/lib/node_modules/@openmixer/
%{_libexecdir}/%{name}/

%changelog
* Sun Nov 01 2026 Pau Aliagas <linuxnow@gmail.com> - 0.18.5-1
- Each rate is measured on an instance of its own. Reactivating one instance at
  another rate crashed LSP's probes; the CLAP crashes rerun on a Raspberry Pi 5
  went from 56 to 1.
- A record says how the probe ended and its load, and the sync prints its counts
  per plugin.
- A private JACK server stops on its TERM. A TERM to the shell's process group
  left jackd running, so every stop ended in a KILL that left the server's row in
  JACK's registry. Once the eight rows were taken, every adapter run failed. The
  rows of our own dead servers are freed before a start.
- lv2_measure connects every port before it activates a plugin, as every host
  does. Plugins that read a port in activate (swh's IIR filters) no longer crash
  it.
- lv2_measure names Qt's offscreen platform when there is no display, so a Qt
  plugin instantiates instead of aborting (samplv1, drumkv1).

* Sat Oct 31 2026 Pau Aliagas <linuxnow@gmail.com> - 0.18.4-1
- The isolated step no longer refuses instruments as silent: its notes start after
  the MIDI links are made, and each third of the window adds one more, held. A
  silent refusal says how many MIDI inputs were linked.
- A silent refusal from the tool before this is run again by the next
  --isolated-only. One that heard the notes is not.
- The held note test plays 30 keys from 36, each held, read from before the first,
  in the adapter pass and the isolated step, so a drum kit that maps only some
  keys is not read as silent. A silent-under-note from one key is run again by
  --adapter-only.

* Sat Oct 31 2026 Pau Aliagas <linuxnow@gmail.com> - 0.18.3-1
- The isolated step runs for every plugin of a pass: a private jackd is now
  reaped when it ends, so the next plugin's server can start. On a Raspberry
  Pi 5 only the first of 152 steps had run.
- A step that could not run is run again by the next --isolated-only and
  replaced in the record.
- plugin-qualify-sync.service gives the plugins a HOME, /var/lib/omx/qualify-home.
  Without one Surge XT is silent under jalv and the LV2 adapter and its CLAP
  answers -503, and a sync from the unit judged it by that.

* Sat Oct 31 2026 Pau Aliagas <linuxnow@gmail.com> - 0.18.2-1
- An lv2:InstrumentPlugin is played one held note in its run under the LV2
  adapter, its output read at its JACK ports by jack_peak: a silent one
  reads unknown, omx-clap-host.silent-under-note, not qualified and not
  refused (#266).
- An LV2 file named by a percent-encoded IRI gets a pin, so Surge XT,
  Pianoteq 9 and six others can have a record; this needs plugin-hostd
  0.15.4 (#267, plugin-hostd#239).
- Each cost figure prints the scheduling policy it was timed under (#214).
- verdict=isolated means the plugin was seen running alone: a plugin rated
  conditional, or one that crashed or hung in the probe, takes an isolated
  step in the same pass, on a private JACK server under a plugin-hostd of
  its own, with a sine through it for 3 seconds. Every record carries the
  steps that judged it, and a new record missing a step is refused (#249).
- A record from before the steps keeps its word and owes the step, listed in
  qualify-owed.json; --isolated-only runs only that step (#249).

* Sat Oct 31 2026 Pau Aliagas <linuxnow@gmail.com> - 0.18.1-1
- --rejudge derives every record's verdicts, tiers and pin word again from the figures it holds, under this version's rules, measuring nothing: an RT violation is conditional and isolated, and the record says when the figures were measured and by which runner. An LV2 record with no adapter run reads unknown and owes that run, listed in qualify-owed.json. A second run changes nothing.
- --memory-only takes only the footprint of each plugin at 48000/128 and 48000/256, through the probe runner under the usual limits, and merges it into its record, leaving every other figure as it was. A leak needs a soak and is reported as not measured.
- An LV2 plugin's run under the adapter also decides its verdict on the Raspberry Pi boards.
- --adapter-only runs each LV2 plugin only under omx-clap-host's LV2 adapter, at 48000/128 and 48000/256 on private JACK servers, and merges the block with the host versions into its record, leaving every other figure as it was. A crash or a timeout is a recorded outcome; a pass cut short resumes. --rejudge then clears the list of owed runs and gives those records their real verdicts.
- An RT-unsafe plugin is offered on the isolated tier: tiers.offeredOn holds isolated for a conditional verdict, with runsAlone on the tier.

* Fri Oct 30 2026 Pau Aliagas <linuxnow@gmail.com> - 0.18.0-1
- Qualification measures and judges memory: the footprint of an instance, its growth over a soak and a hard limit, read against each host's budget as hosting.memory.* verdicts (#114). Needs plugin-hostd 0.15.3 and omx-clap-core 0.25.1.
- An allocation, lock or syscall while an instrument is played rates conditional, isolated in the pin like the same violation in the run; it is no longer refused. A process error under notes is still unsuitable (#196).
- The hosting codes are omx-clap-core's, regenerated from 0.25.1 (#146).

* Fri Oct 30 2026 Pau Aliagas <linuxnow@gmail.com> - 0.17.5-1
- Every sync starts by bringing each pin's files up to the ones plugin-hostd --pin-files names, measuring nothing; --refresh-pins does only that, and the package upgrade runs it. A pin written before 0.17.3 no longer leaves an LV2 with presets refused with -509 until it is qualified again (#239).

* Fri Oct 30 2026 Pau Aliagas <linuxnow@gmail.com> - 0.17.4-1
- A package transaction no longer runs a qualification sweep when systemd is not running (an image build took 95 minutes in it): the trigger leaves qualify-pending in /var/lib/omx and the next plugin-qualify-sync run scans and clears it; PLUGIN_QUALIFY_SYNC_INLINE=1 keeps the inline run (#237).

* Thu Oct 29 2026 Pau Aliagas <linuxnow@gmail.com> - 0.17.3-1
- The sync takes a pin's files from plugin-hostd --pin-files, preset files included (#228); records carry the LV2 adapter's admission (#223) and the latency object on every cell (#201); the mod-host probe uses the device's LV2_PATH (#224); the sync takes a lock (#222); published descriptors are readable by the console (#221). Needs plugin-hostd 0.15.0.

* Thu Oct 29 2026 Pau Aliagas <linuxnow@gmail.com> - 0.17.2-1
- The sync writes CLAP descriptors one plugin per run with its own timeout, keys CLAP targets by file, and removes the records of a plugin's other bytes (#218, #219).

* Thu Oct 29 2026 Pau Aliagas <linuxnow@gmail.com> - 0.17.1-1
- The Debian release build installs python3 for the changelog step; no code change.
* Thu Oct 29 2026 Pau Aliagas <linuxnow@gmail.com> - 0.17.0-1
- The distributed records layer: the sync reads the records a device ships before it measures, and takes a plugin
  only on a binary checksum match; plugin-qualify-records-package builds the Debian package of a device's
  qualification records (#195).
- The measurement grid covers every declared host rate and quantum, for LV2 as for CLAP, with the runs merged into
  one probe output and a bounded memory: a run past the bound is probe.oom (#193).
- A record cell without latency figures says why, by the contract's reason code (#201).
- The commit-message check is named for what it checks.
* Wed Oct 28 2026 Pau Aliagas <linuxnow@gmail.com> - 0.16.1-1
- The sync service names the interpreter first in ExecStart: executed as a script it stayed in systemd's own
  SELinux domain on Fedora, with no executable memory for V8 and no /tmp, and died at start (#188).
* Wed Oct 28 2026 Pau Aliagas <linuxnow@gmail.com> - 0.16.0-1
- A package transaction in a plugin folder scans once: debian triggers and rpm file triggers on the standard
  LV2 and CLAP folders (#169).
- The path unit names the standard folders; the settings file adds the rest (#170).
- The sync service carries its own limits (#171).
- A plugin that is gone leaves no record, descriptor or pin behind (#172).
- python3-lilv is a dependency of the deb on every suite that carries it (#175).
- tools/install-roundtrip.sh runs the after-install scan on a clean image (#173).
- The schema-floor refusal code and the id-hash prefix for descriptors.py are declared (#179, first step of
  #142).
- CI: the commit-message check is the ai-trace-check action (#156).

* Tue Oct 27 2026 Pau Aliagas <linuxnow@gmail.com> - 0.15.1-1
- The scan golden is omx-clap-host 0.23.0's: its rows carry remote_controls (the plugin's remote-control
  pages, [] for a plugin with none), and a test asserts the pages fake.clap's passthrough plugin declares.
  The live-scan test failed against 0.23.0 on the stale golden, which stopped the npm publish of 0.15.0.
- Floors: omx-clap-host >= 0.23.0, omx-clap-core >= 0.23.0.
* Tue Oct 27 2026 Pau Aliagas <linuxnow@gmail.com> - 0.15.0-1
- plugin-qualify-sync (new): qualifies every installed CLAP and LV2 plugin once, and again when
  its files change, as a systemd service started after boot and when a plugin is installed;
  it writes the pin file and the qualification records, and a plugin that crashes or
  hangs is recorded as such. tools/mod-host-admit.mjs ships with its dist (#154).
- An LV2 record carries the latency and the cost measured at the run's rate, and names the
  figures a run could not take, so an LV2 plugin can be live (#163).
- plugin-qualify adjust --history: the second verdict is decided from plugin-hostd's running
  history, demoting or promoting on cost alone and never lifting a refusal, and --pins
  writes it (#158).
- mod-host admission sends add and remove only, with no activate (#159); mod-host and jalv
  verdicts are measured by running the plugin, and the record holds the console's two
  tiers (#152).
- --all covers the LV2 bundles on the LV2 path as it covers CLAP; a bundle is a directory
  holding manifest.ttl (#66, #152).
- The --no-host-sweep flag, which nothing read, is removed.
- Floors: omx-contract >= 3.4.0.
* Sat Oct 24 2026 Pau Aliagas <linuxnow@gmail.com> - 0.14.1-1
- descriptors.py reads its scan argument intermixed with the options: on
  Python 3.11 and 3.12.3 (Debian bookworm, Ubuntu noble) `clap --descriptor-dir
  DIR -` was refused as an unrecognized argument, which also failed the 0.14.0
  npm publish (#144).
* Sat Oct 24 2026 Pau Aliagas <linuxnow@gmail.com> - 0.14.0-1
- The scanners write a scanned descriptor per plugin into descriptor_dir
  ($XDG_STATE_HOME/omx/descriptors), named <id>@<version>-<sha256 first 12>.json,
  validated against omx-contract's descriptor schema and written atomically;
  clap-qualify --json also prints the binary hash, port types, note dialects and
  the latency extension (#140). The package requires python3-jsonschema.
- Audit of plugin-qualify against omx-clap-core's compat tables, with
  audit-overlap.sh and its CI self-test (#124).
* Thu Oct 22 2026 Pau Aliagas <linuxnow@gmail.com> - 0.13.1-1
- HOSTING_CODE is build-time data (src/hosting-codes.generated.ts, written by
  tools/gen-hosting-codes.mjs from omx-clap-core's tables): no browser-reachable
  module imports a node: module, so a browser bundle of the public subpaths
  builds again (#134)

* Wed Oct 21 2026 Pau Aliagas <linuxnow@gmail.com> - 0.13.0-1
- The hosting codes are read from omx-clap-core's installed TypeScript
  module instead of omx-contract (the contract split moved
  data/hosting/*.json there): HOSTING_CODE is omx-clap-core's tables now,
  found at pkg-config --variable=tsdir omx-clap-core, the fetched checkout,
  or /usr/share/omx-clap-core/ts (OMX_CLAP_CORE_TSDIR overrides)
- Two writes stop, as omx-clap-core 0.13.0 did: a topology past the
  auxiliary limit is hosting.topology.too-many-ports instead of the retired
  extra-inputs-fed-silence, and a CLAP's feature list is no longer judged
  (the "not an audio effect" refusal is dropped)
- omx-clap-host is now a hard dependency (the TypeScript module above is
  read at import), not merely recommended. Floors: omx-contract >= 3.0.0,
  omx-clap-lv2 >= 0.13.0
* Tue Oct 20 2026 Pau Aliagas <linuxnow@gmail.com> - 0.12.0-1
- The cost of an instrument is measured with notes held, at every rate (the
  voices are part of the figure).
- lv2_measure plays an LV2 instrument through its MIDI input, so an instrument
  is measured sounding, not silent.
- The full classifier reads the note sweep, and an instrument's latency comes
  from a note instead of from an impulse it never sounds on.
* Sun Oct 18 2026 Pau Aliagas <linuxnow@gmail.com> - 0.11.0-1
- The default rates and quanta of a qualification now come from omx-contract
  instead of a copy kept here
- A worker interface whose work or work_response is NULL is refused, and the
  refusal is reported as hosting.worker.nonconforming
- The LV2 measurer resolves a relative LV2_PATH entry before lilv reads it
- CI installs the LV2 scanner and two LV2 plugin packages, so the scanner
  tests run instead of being skipped
- The LV2 measurer and the host probe take their dB readings from omx-dsp's
  omx_lin_to_db_d instead of a hand-written 20 * log10, and need omx-dsp
  0.21.0 or later to build. A NaN level in the host probe stays NaN and fails
  its claim instead of reading as silence
- Plugins are measured through the probe runner, CLAP and LV2 alike, and
  judged from its output. Each judgment is written as a qualification record
  beside a byte copy of the probe output it judged. plugin-qualify now
  requires plugin-hostd 0.4.0

* Fri Oct 16 2026 Pau Aliagas <linuxnow@gmail.com> - 0.10.1-1
- The npm package can be published again. The publish workflow now installs
  plugin-hostd the way the CI workflow does, from one shared action, so the
  package that failed to publish with 0.10.0 goes out with this release
- A check refuses private citations in the repository, and the text that
  held some now states the facts instead

* Fri Oct 16 2026 Pau Aliagas <linuxnow@gmail.com> - 0.10.0-1
- The latency check reads a plugin's delay where its impulse response
  really arrives, the first frame at or above 1/1000 of the peak, instead of
  the first sample above silence. A plugin whose fractional delay leaks a
  tiny value one frame early (a pitch shifter, for instance) was refused by
  one frame although it declared its true latency; an LV2 or CLAP plugin
  that declares a delay is now measured correctly
- plugin-qualify now installs lv2_host_probe beside the measurer. It loads
  an LV2 plugin through lilv and drives it as a host does, so a console that
  exports a plugin can test it with the installed tool. The setting
  OMX_LV2_HOST_PROBE names it, and it exits 2 when the plugin is not in the
  bundle
- The repository no longer carries the old copy of the measurer kept for
  openmixer, nor the test that compared against it

* Thu Oct 15 2026 Pau Aliagas <linuxnow@gmail.com> - 0.9.0-1
- The LV2 measurer takes its host features and options from the shared LV2
  feature provider in omx-clap-core, so a plugin that asks for options,
  bounded block length or a worker is measured with the same features the
  console's host gives it.
- --all now walks the CLAP search path as well as the LV2 path. An unreadable
  CLAP directory is a named scan refusal, and LV2 bundles on the path are
  reported instead of skipped.
- --pins writes one pin and its verdict per qualified plugin in the pin_set
  line plugin-hostd reads from its pin_file.
- Dependencies are floors only (omx-clap-lv2 >= 0.8.0, omx-dsp >= 0.18.0,
  omx-contract), with no ceiling.

* Tue Oct 13 2026 Pau Aliagas <linuxnow@gmail.com> - 0.8.0-1
- With no setting, the native tools are looked for in the checkout's own
  native/build first, then where the package installs them, so make -C native
  in a checkout is never shadowed by an older installed prober.
- A prober or the measurer and the interposer it runs under come from one
  place, the first that holds either; a place holding only one of them is
  refused instead of pairing it with the other from elsewhere.

* Tue Oct 13 2026 Pau Aliagas <linuxnow@gmail.com> - 0.7.0-1
- clap-qualify pins a symlinked .clap under the name it was handed, the name
  the console adds and plugin-hostd checks, with the target's bytes.
- A CLAP plugin with more parameters than the host accepts (2048,
  omx-clap-core's cap) reads unpinnable instead of getting a pin the host
  refuses at add.
- A parameter layout that cannot be read says why: a get_info failure, or
  memory running out while reading or hashing the layout.

* Tue Oct 13 2026 Pau Aliagas <linuxnow@gmail.com> - 0.6.0-1
- The package carries the LV2 measurer taken in from openmixer, lv2_measure,
  in /usr/libexec/plugin-qualify beside the CLAP prober. It prints what
  openmixer's copy prints, the plugin's integrity pin included, plus what
  its host now does.
- The measuring host is faithful: it runs a plugin's worker between blocks,
  sends patch:Set to patch:writable parameters, bounds the soak's control
  sweep (OMX_SWEEP_DB, OMX_SWEEP_RATIO), keeps a plugin's stdout out of its
  record, and says what it did in a "host" object.
- benchmark.py runs the plugin's worker between blocks instead of dropping
  its jobs; the cost record carries the worker's counts.
- extractJsonRecord, soakTimeoutSeconds and the soak sweep declarations are
  exported.
- A soak failure measured at the console's rate rates the plugin unsuitable
  at that rate (hosting.stability.soak-failed-at-rate). A rate the supervisor
  cut short reads timedOut, never died.
- The cost gate refuses a reading missing a field it judges
  (hosting.cost.fields-missing); COST_FIELDS, coreFraction and
  classifierCostFromDocument are exported.
- lv2-measure.mjs measures the hosting dimensions (stability, rtSafety,
  features) through it, one process per plugin under the interposer;
  --plugins names the plugins without a scan.
- The command looks for the measurer by its setting (OMX_LV2_MEASURE), then
  where the package installs it, then in the checkout's native/build.

* Tue Oct 13 2026 Pau Aliagas <linuxnow@gmail.com> - 0.5.1-1
- The package carries the CLAP prober and its interposer, in
  /usr/libexec/plugin-qualify, so an installed plugin-qualify qualifies CLAP
  plugins and prints their integrity pin with nothing set. The package is now
  built per architecture.
- The command looks for the prober by its setting, then where the package
  installs it, then in the checkout's native/build.
- omx-clap-host, which brings omx-clap-scan, is recommended.

* Mon Oct 12 2026 Pau Aliagas <linuxnow@gmail.com> - 0.5.0-1
- The CLAP prober and the measurement interchange (v1.3) carry each plugin's
  integrity pin: the SHA-256 of the files the host loads and the omx-layout/1
  fingerprint, computed through plugin-hostd 0.1.4's pin.h.
* Mon Oct 12 2026 Pau Aliagas <linuxnow@gmail.com> - 0.4.1-1
- The npm release builds the native tools before it tests, so this version
  reaches npm; 0.4.0 carries the same code and was never published there.

* Mon Oct 12 2026 Pau Aliagas <linuxnow@gmail.com> - 0.4.0-1
- Each refusal the CLAP host core can answer with now carries a one-line
  description (CLAP_CORE_REFUSAL_DESCRIPTIONS), so a console can show what a
  refused plugin did wrong in plain words.

* Mon Oct 12 2026 Pau Aliagas <linuxnow@gmail.com> - 0.3.0-1
- plugin-qualify now checks CLAP plugins directly. It loads each .clap file
  without a display, runs it at every sample rate and sweeps every parameter
  while watching for anything unsafe on the audio thread, then writes a
  verdict for that exact binary and console. A plugin that has changed since
  it was checked is never trusted on the old verdict.
- The verdict follows the extensions the chosen host profile really offers:
  asking for a profile with no CLAP support now reads as unknown instead of
  borrowing the OpenMixer console's answer.
- The CLAP scan keeps parameter value names, the plugin's modules and its
  remote-control pages, so a console can show named choices and the plugin's
  own control pages.

* Sun Oct 11 2026 Pau Aliagas <linuxnow@gmail.com> - 0.2.1-1
- The GitHub release carries the npm tarball openmixer-plugin-qualify-0.2.1.tgz,
  dist/ built in.

* Sun Oct 11 2026 Pau Aliagas <linuxnow@gmail.com> - 0.2.0-1
- New hosting code `hosting.output.non-finite`: the refusal the
  libomx-clap-core CLAP host gives a plugin whose output goes non-finite.
- `CLAP_CORE_REFUSALS` lists the refusals libomx-clap-core returns from
  open, activate and the timed open, each by the hosting code it answers
  with.
- `ScalingNoteCode` types the words `latency.scalingNote` may carry, and a
  test keeps `benchmark.py`'s scaling notes equal to the declared list.
- The CLAP host extensions list is documented as the mirror of the header
  libomx-clap-core's host object offers.

* Thu Oct 08 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.1-1
- plugin-qualify installs from the FreeMixer package channel: `dnf install
  plugin-qualify` on Fedora, `apt install plugin-qualify` on Debian bookworm
  and trixie (Raspberry Pi OS included).
- The npm package is now `@openmixer/plugin-qualify`, published to npm with
  provenance. The `@freemixer/plugin-qualify` name was never published;
  install the new one with `npm install @openmixer/plugin-qualify`.
- The package no longer carries Python bytecode caches.

* Wed Oct 07 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.0-1
- First release as a package of its own.
- The scan, the offline latency and cost measurement and the mod-host hosting
  sweep.
- The fail-closed hosting verdict, judged against a host profile
  (`openmixer-console`, `jalv`, `mod-host`, or your own file).
- The `lv2-plugin-measurements` document and its reader, and the
  `plugin-qualify` command.
- The package builds itself when installed from git and ships its fixtures.
