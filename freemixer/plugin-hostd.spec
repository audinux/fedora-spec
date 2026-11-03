%bcond_without check

Name: plugin-hostd
Version: 0.16.0
Release: 1%{?dist}
License: GPL-3.0-or-later
Summary: Run LV2 and CLAP plugins in a live rig without one crash taking down the show
URL: https://github.com/FreeMixer/plugin-hostd

Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: diffutils
BuildRequires: python3
# the protocol library and the declared protocol: <plugin-hostd/protocol.h> and the headers it includes, the protocol's
# JSON and mod-host's. 0.2.0 is the first that holds them (they were this tree's before); a floor only
BuildRequires: plugin-hostd-protocol-devel >= 0.2.0
# the probe runner's default rates, the protocol's parameter scales and the probe output's shared words are read from
# omx-contract's C headers, and the format tables are items of its schema 3 (3.4.0 the first that renders a reply
# code's resp, which plugin_hostd_vocabulary.h is checked against); a floor only
BuildRequires: omx-contract-devel >= 3.4.0
# the protocol library, ports on 127.0.0.1 unless told otherwise (socket_set_bind_address()); the daemon is built
# against the declared protocol of 0.2.0; a floor only
Requires: plugin-hostd-protocol%{?_isa} >= 0.2.0
# omx-clap-core is a build dependency of the check stage only: the CLAP worker and the fixtures the real-worker
# tests drive. A build with `--without check` needs nothing of omx-clap-core, so plugin-hostd and omx-clap-core
# do not build-depend on each other. A floor only: the lowest release with what the tests need (omx-clap-core 0.21,
# the first whose omx-clap-host runs a chain's members in one client in the declared order, and whose tests package
# ships fault-14.clap and jack_identity; 0.25 for param_info answered from clap.params when a plugin has no contract)
%if %{with check}
BuildRequires: omx-clap-host-tests >= 0.25.0
# the reader that holds the committed render of data/ (make check-rendered)
BuildRequires: omx-contract >= 3.4.0
# the daemon's verbs (plugin-hostd-protocol's package of the contract directory) and the shared verbs and the
# reply.host.* codes they refer to (make test-verbs-declared)
BuildRequires: plugin-hostd-protocol-contract >= 0.2.0
BuildRequires: omx-clap-core-contract >= 0.26.2
%endif
# the format tables, which readers read at run time
Requires: %{name}-contract = %{version}-%{release}

# the workers: a format whose worker is not installed refuses its adds (-503), the other format is unaffected
Recommends: mod-host
Recommends: omx-clap-host >= 0.26.2

%description
plugin-hostd keeps your effects and instruments running when one of them
misbehaves. It gives a controller one mod-host socket and starts each plugin, or
each named group of plugins, in a worker process of its own: mod-host for LV2,
omx-clap-host for CLAP. If a plugin crashes, only its worker goes down and the
daemon brings it back. Audio never passes through the daemon, so it adds no
latency: every worker is a JACK client.

%package devel
Summary: Talk to plugin-hostd from your own controller without retyping its protocol
BuildArch: noarch
Requires: %{name}-contract = %{version}-%{release}
# the declared protocol, <plugin-hostd/protocol.h>, which plugin-hostd.pc requires; a floor only
Requires: plugin-hostd-protocol-devel >= 0.2.0

%description devel
The pin header, the words of the grouping planner and the running history,
and the schemas of the probe output and of a preset file. The protocol a
controller speaks (the verbs, error codes, feedback events and settings) is
declared in plugin-hostd-protocol-devel, which this package requires:
pkg-config plugin-hostd gives the flags for both.

%package contract
Summary: plugin-hostd's format tables, for programs that read them at run time
BuildArch: noarch
# the daemon's verbs are plugin-hostd-protocol's package of the contract directory since 0.2.0 (they were this
# package's before): a reader of this package reads that one too; a floor only
Requires: plugin-hostd-protocol-contract >= 0.2.0
Requires: omx-clap-core-contract >= 0.26.2
# the tables live in omx-contract's contract directory and are read against its schema: 3.2.0 is the first whose
# source field takes an index (omx_clap_panel_display.meter_ids[0]), so an older one never sits beside a table it
# refuses; a floor only
Requires: omx-contract >= 3.2.0

%description contract
plugin-hostd's package of omx-contract's contract directory: the format tables
a scan maps a CLAP or LV2 plugin through (formats/clap.json, formats/lv2.json),
the keys of the
running history (history.json) and the reasons a plan gives for a plugin it
leaves alone (grouping.json), under
share/omx-contract/contract.d/3/plugin-hostd. A program that reads them at run
time requires this package, never the development one.

%package tests
Summary: A stand-in plugin worker to test a program that drives plugin-hostd
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
A small worker that speaks the same protocol as mod-host and omx-clap-host and
can be made to die on cue, so a program that talks to plugin-hostd can be
tested against a real daemon without a plugin, a JACK server or any audio.
Run it with -L to print the layout it reports. It is installed in
%{_libexecdir}/plugin-hostd/tests, away from the directories programs run
from.

%prep
%autosetup

sed -i 's,LDFLAGS += -s,LDFLAGS +=,g' Makefile

%build

%set_build_flags

# PREFIX at the build too: the probe compiles in where its lock preload is installed
%make_build PREFIX=%{_prefix}
%make_build PREFIX=%{_prefix} tests/fake-host

%install

%make_install PREFIX=%{_prefix}
# the format tables, as the package plugin-hostd of omx-contract's contract directory (docs/formats.md)
%make_build install-contract DESTDIR=%{buildroot} PREFIX=%{_prefix}

# the verb table is checked against mod-host's README, which a build does not have
%check
%if %{with check}
make test-daemon check-generated check-rendered
%endif

%files
%license COPYING
%doc README.md
%{_bindir}/plugin-hostd
%{_bindir}/plugin-hostd-probe
# the probe's lock preload, which the runner preloads into the measured child
%dir %{_libexecdir}/plugin-hostd
%{_libexecdir}/plugin-hostd/probe-lock.so
%{_mandir}/man1/plugin-hostd.1*
%{_mandir}/man1/plugin-hostd-probe.1*
# the read-only pins of packages: a package that ships pins co-owns it with %dir
%dir %{_datadir}/plugin-hostd/pins.d

%files tests
%license COPYING
%{_libexecdir}/plugin-hostd/tests/fake-host
%{_libexecdir}/plugin-hostd/tests/lib/protocol.sh
%{_libexecdir}/plugin-hostd/tests/lib/plugin_hostd_client.py

%files devel
%license COPYING
%{_includedir}/plugin-hostd/plugin_hostd_vocabulary.h
%{_includedir}/plugin-hostd/pin.h
%{_datadir}/pkgconfig/plugin-hostd.pc
%{_datadir}/plugin-hostd/probe-output.schema.json
%{_datadir}/plugin-hostd/preset.schema.json

%files contract
%license COPYING
%{_datadir}/omx-contract/contract.d/3/plugin-hostd/

%changelog
* Tue Nov 03 2026 Pau Aliagas <linuxnow@gmail.com> - 0.16.0-1
- The protocol is plugin-hostd-protocol's (0.2.0 or later): protocol.h, the search
  lists, the verb tables and the JSON of the protocol and of mod-host's are read from
  the installed library, and this tree keeps no copy. plugin-hostd requires
  plugin-hostd-protocol, plugin-hostd-devel requires plugin-hostd-protocol-devel, and
  the JSON documents move to /usr/share/plugin-hostd-protocol/.
- preset_show <instance> <key> goes to the worker that holds the instance alone, and
  preset_show <uri> is answered as mod-host answers it, by the LV2 worker; a key or
  uri in quotes that holds a space is told apart by the words the worker reads.
- The shared checks of commit messages and private references run from
  FreeMixer/.github, and no copy of them is kept here.

* Mon Nov 02 2026 Pau Aliagas <linuxnow@gmail.com> - 0.15.9-1
- A worker that says abi_clobber (omx-clap-host 0.26.2: a plugin returned from a call
  with a callee-saved register changed) has that plugin quarantined: the history keeps
  it alone from then on, and when it shares its worker or sits in a chain it moves to a
  worker of its own with its state saved; the other members stay where they run (#366).
- The packages require omx-clap-core-contract 0.26.2 and recommend omx-clap-host 0.26.2.

* Sun Nov 01 2026 Pau Aliagas <linuxnow@gmail.com> - 0.15.8-1
- A chain that does not form within chain_form_timeout_ms (10 s) says why, once:
  chain_stalled <chain> <member> <step> <code>, the member, the step and the
  refusal code that held it (#365).
- add <uri> <instance> chain:<chain> adds the plugin into that chain's worker,
  at its end, with no worker of its own and no move. A plugin the chain cannot
  take (a width its head does not take, a format pinned to a world of its own)
  is refused with -501 and nothing is left, so the controller adds it own
  (#348, #357).
- A member after a chain's first is expected into the chain (chain_expect,
  omx-clap-host 0.26.0): it joins the walk with no JACK client of its own. A
  worker that does not answer chain_expect gets the add and the order line as
  before (#358). On a Pi 5, 24 plugins add in 435 ms grouped, against 749 ms
  under mod-host.
- A repeat lookup of a plugin's bundle reads its one manifest instead of
  walking the LV2 path, and its qualification records are read again only when
  they change: a later own add of an LV2 plugin on a Pi drops from about 69 ms
  to 59, and from 91 to 59 for one found late in the walk (#359).

* Sat Oct 31 2026 Pau Aliagas <linuxnow@gmail.com> - 0.15.7-1
- chain answers the worker's refusal. A worker that will not run the members
  as one (a member whose width differs from the head's, mono after stereo)
  made chain answer resp 0 and list every member as running, while each kept a
  client of its own. chain now answers -501, the refused chain ends as
  chain_clear ends it with each member in a worker of its own, and the
  chain_refused event carries the worker's code (#342, #343).

* Sat Oct 31 2026 Pau Aliagas <linuxnow@gmail.com> - 0.15.6-1
- formats/clap.json asks for contract schema 3.2.0, and the rendered headers
  follow omx-contract 3.5 (#350). 0.15.5 could not build its x86_64 RPM against
  omx-contract 3.5, so its RPMs were not published; this release carries what
  0.15.5 says for them.

* Sat Oct 31 2026 Pau Aliagas <linuxnow@gmail.com> - 0.15.5-1
- mod-host-protocol 0.10.6.f14a230-11.3 or newer is required. The workers this
  daemon starts, mod-host and omx-clap-host, listen on 127.0.0.1 with it, and
  are not reached from another machine whatever bind_address says (#333).
- The daemon gives the library its address and no longer replaces bind(). A
  daemon that cannot listen on either port still does not start (#333).
- An LV2 plugin's bundle is the one that holds its binary, not a GUI bundle
  that names it. fil4 and x42 dpl no longer answer -101 where a generated GUI
  bundle is listed first (#339).
- The probe test passes on a host with no memory lock limit (#340).

* Sat Oct 31 2026 Pau Aliagas <linuxnow@gmail.com> - 0.15.4-1
- An LV2 file named by a percent-encoded IRI, Surge XT's libSurge%20XT.so,
  is pinned as written and opened decoded (#329, #239).
- The worker of a CLAP row is given the decoded path, one quoted word: a
  CLAP file with a space in its name is added and replayed (#329, #240).
- A manifest that names its plugin by a prefixed name is found (#324): mda
  Piano no longer answers -509.
- Probe output 1.4: an instrument's cost at each count of notes held,
  voiceCurve (#326).
- The daemon listens on 127.0.0.1 unless told otherwise (#330). A controller
  on another machine needs --bind-address or bind_address.
- docs/zynthian: the digital proofs on the Pi 5, with what failed (#325).

* Fri Oct 30 2026 Pau Aliagas <linuxnow@gmail.com> - 0.15.3-1
- probe: the memory limit is memory.max of a cgroup the measured child runs
  in, and hitting it is probe.memory-limit; a machine that gives none falls
  back to RLIMIT_DATA and says why (plugin-qualify#114).
- probe output 1.3: a grid point carries the child's memory footprint.
- estimate answers RAM: what the workers hold now, what the members would
  add with what they share counted once, the host's ram_budget_mb, and how
  many members have no figure.
- probe: the measured child drops every capability and its bounding set
  (#253).
- A CLAP file whose name holds whitespace is addressed by its percent-
  encoded path (#240).

* Fri Oct 30 2026 Pau Aliagas <linuxnow@gmail.com> - 0.15.2-1
- describe: a travel with both lv2:integer and pprops:logarithmic is log, in
  either order (#142, #307).

* Fri Oct 30 2026 Pau Aliagas <linuxnow@gmail.com> - 0.15.1-1
- Remote pages and param_info read an LV2 bundle's ports (#152, #294).
- describe reads an LV2 port group's path through pg:subGroupOf (#223, #296).
- A percent-encoded LV2 IRI matches its qualification record (#239, #298).
- The Zynthian tools and the bench read worker_list with its pool field (#236, #285).
- describe: an LV2 toggle stays a toggle whatever order the dump lists its
  port's records in (#305).

* Thu Oct 29 2026 Pau Aliagas <linuxnow@gmail.com> - 0.15.0-1
- A pin line takes pool=cores|off; a CLAP or lv2-clap worker for a plugin
  whose pin says pool=cores starts with --thread-pool=on, in a worker of its
  own. worker_list records gain the pool after the core (#236, #280).
- The pin files are read again when they change, and on pin_reload or
  pin_changed, without a restart (#255, #268).
- plugin-hostd --pin-files <uri> prints the files a pin of a plugin holds,
  from the same collector an add checks (#278).
- The plugin search lists are written once and complete for a Zynthian Pi
  (#212, #281).
- Test and CI fixes: the solo-crash count (#271, #279), the Zynthian chain
  round trip plays again when its taps show no peak (#246, #264), and the
  probe's cap grant path runs under CAP_SYS_NICE (#265).

* Thu Oct 29 2026 Pau Aliagas <linuxnow@gmail.com> - 0.14.0-1
- estimate <rate> <quantum> <uri> ... answers what a chain of these plugins
  would cost at that rate and quantum, from the qualification records (#224).
- The setting placement pins each chain's worker to the audio core with the
  least load and the daemon to the reserved cores; worker_list and plan
  records gain the core, before the place in a worker_list record (#226).
- The Zynthian chain tools and docs, the wire protocol document generated and
  checked, the pages site, and the benchmarks, trade-offs, image, stress and
  instruments docs are in main (#228, #230, #229).
- The history and plan verbs answer -901 when there is no memory (#174); the
  planner reads the history (#208); plugin-hostd-contract requires
  omx-contract 3.2.0 (#165).
- The probe measures a plugin's cost on a SCHED_FIFO thread at the highest
  priority the sandbox allows, with user-namespace capability detection and
  a PREFIX-correct lock preload path (#225).

* Tue Oct 27 2026 Pau Aliagas <linuxnow@gmail.com> - 0.13.1-1
- The daemon reads the xruns line a worker writes (omx-clap-core 0.23.0,
  now the floor) and adds a window to xrun_windows_solo or
  xrun_windows_grouped of every member of the worker when the count rose
  in it; the first count of a worker is its baseline (#187).

* Tue Oct 27 2026 Pau Aliagas <linuxnow@gmail.com> - 0.13.0-1
- A configured state_root that does not exist is made at start, as the
  directories below it already were; an add no longer answers -503 over a
  missing directory (#180).
- plugin-hostd-tests ships one protocol client for shell and Python tests,
  lib/protocol.sh and lib/plugin_hostd_client.py, and the harness and the
  verbs test use it (#177).
- bench/: a harness that runs the same plugins under omx-clap-host, under
  plugin-hostd, under mod-host and under jalv, and writes omx-bench/1
  documents; plan and pool modes, xruns, latency, stress and repeats with
  their spread (#188).
- history_get and history_clear: what each plugin did on this machine, kept
  per plugin, binary and host class: the worker's CPU time and Pss read
  from /proc into windows, and its deaths. Settings history_file,
  history_window_s, history_save_s and host_class (#184).
- plan, plan_get and plan_clear: the grouping planner, a pure function over
  the pins and the history that gathers the members of a strip, applies the
  segments as chains (chain places are chain:<n>.<k>) and keeps the ones
  that did not change. The reason codes are declared in data/grouping.json
  and the plan_reason event says why a plan changed. Settings grouping
  (off by default), group_max, group_cost_max, group_rate and
  group_quantum (#185).
- The probe runner copies lv2_measure's latency and cost into the LV2 grid
  point (#200).
- README: grouped workers against one process per plugin, measured.
- CI: superseded pull request runs are cancelled, package and fuzz runs a
  pull request cannot change are skipped, and build and test has 60
  minutes (#198).
- plugin_hostd_vocabulary.h is rendered by omx-contract 3.4.0, which writes
  a reply code's number as an OMX_..._RESP define; the build needs
  omx-contract-devel 3.4.0 or newer and its check stage the omx-contract
  command.

* Mon Oct 26 2026 Pau Aliagas <linuxnow@gmail.com> - 0.12.0-1
- The verbs the daemon adds are declared in its package of omx-contract's
  contract directory, verbs.json beside the format tables: each verb's
  format, reply, refusal codes and what plugin-hostd, omx-clap-host and
  mod-host owe it. The C names come from plugin_hostd_host_verbs.h, which
  protocol.h includes, and plugin_hostd_vocabulary.h names the codes (#131).
- New noarch package plugin-hostd-contract: the contract directory's files,
  share/omx-contract/contract.d/3/plugin-hostd (MANIFEST.json,
  formats/clap.json, formats/lv2.json, verbs.json), which programs read at
  run time. plugin-hostd and plugin-hostd-devel require it; the files leave
  plugin-hostd-devel.
- The build needs omx-contract-devel 3.3.0 or newer, the first schema with
  the verbs kind, and its check stage the omx-contract command.
- A test holds the declared verbs to the daemon on its socket: replies,
  codes, the verbs it answers itself, and the shapes both hosts answer.

* Mon Oct 26 2026 Pau Aliagas <linuxnow@gmail.com> - 0.11.0-1
- chain_get <chain> reads a chain back: its worker, its members in the
  declared order and the members its worker runs now. A quarantined member
  is declared and not running; a chain no chain declared answers -522.
- A chain declared again while its worker is up keeps that worker: a new
  member joins it with its add, the order, its own checkpoint and its
  connections, a move sends the order alone, and no other member restarts
  or loses a value set after its checkpoint. A member left out goes to a
  worker of its own, and an LV2 joiner forms the chain again.
- CLAP members and LV2 members of the adapter row (lv2_worker omx-clap-host)
  form one chain in one omx-clap-host instead of answering -521; LV2 on
  mod-host with CLAP still answers -521.
- omx-clap-host 0.21.0 or newer is recommended, and the tests need
  omx-clap-host-tests 0.21.0 or newer: the first release whose worker runs
  such a chain.
- The fuzz harnesses check each word of a command, every broadcast verb's
  argument count, a reply against the call that answered it and that the
  relay loses no byte a worker wrote; make fuzz-records proves every check
  aborts on its own seed. The daemon does not change with them.
* Sun Oct 25 2026 Pau Aliagas <linuxnow@gmail.com> - 0.10.0-1
- panel_get <uri> answers the path of the panel the plugin publishes, filed
  by the scan of its add; docs/panel.md tells a renderer how to draw it.
- describe reads the six panel scopes of omx-clap-scan 0.20.0's dump as
  drops, so the add of a plugin scanned by omx-clap-core 0.20.0 no longer
  answers -531.
- plugin-hostd-probe panel prints the panel object the scan filed.
- Only a null panel means a plugin has no layout; every other code is a
  failure to show, and a new scan scope or field needs its format row first.
* Sat Oct 24 2026 Pau Aliagas <linuxnow@gmail.com> - 0.9.2-1
- worker_list, supervisor_reset and quit answer -902 to a word past
  their grammar instead of acting on it: worker_list x no longer lists,
  supervisor_reset all x no longer resets, and quit now no longer stops
  the daemon.
- A tab at the end of a command is trimmed like a space: a command
  ending in a carriage return and a tab no longer reaches the worker with
  both.
- The end of a held gesture longer than 1024 bytes reaches the controller
  whole, with its end word; before, it was cut short and the control stayed
  held.
- The build needs mod-host's protocol headers of mod-host-protocol-devel
  0.10.6.f14a230-11 or newer (libmod-host-protocol-dev 0.1.0-5 or newer), the
  first with param_info, remote_pages and track_info.
- Fuzz harnesses for the command parser and the reply stream (#144).

* Sat Oct 24 2026 Pau Aliagas <linuxnow@gmail.com> - 0.9.1-1
- The preset schema, protocol/preset.schema.json, is installed in
  /usr/share/plugin-hostd with the two other schemas, in the development
  package, and named in the man page and the README; a test holds the
  installed set (#145).

* Sat Oct 24 2026 Pau Aliagas <linuxnow@gmail.com> - 0.9.0-1
- The preset verbs preset_list, preset_load, preset_save and preset_show
  are relayed by the daemon and the worker's answer comes back. The preset
  file is org.openmixer.preset/1 (parameters) or /2 (with the state body),
  checked against protocol/preset.schema.json; the daemon refuses an
  unreadable or malformed file itself. Codes -523 to -527 name the
  refusals (#131).
- midi_learn, midi_map, midi_unmap, cv_map and cv_unmap are optional again
  on the clap-worker and zynthian profiles: the host answers them only as
  the mechanism, they are policy of the surfaces (#131).
- New keys descriptor_dir and qualification_dir, beside state_root. After
  an add is answered, a plugin with no descriptor is scanned by
  plugin-hostd-probe describe, selected by the probe key, and written once
  as <id>@<version>-<sha12>.json. The add never waits for the scan (#140).
- New verb descriptor_get answers the path of that file. Codes -528 to
  -531 name a directory that cannot be written, no descriptor, a scan still
  running and a scan that wrote nothing. The man page has a DIRECTORIES
  section (#140).

* Thu Oct 22 2026 Pau Aliagas <linuxnow@gmail.com> - 0.8.0-1
- The chain floor is 1, chain_members_min in the declared constants: a
  chain of one is valid, so one isolated plugin is a chain like any
  other (#131).
- The host verb table: 69 rows, a level per host profile (lv2-worker,
  clap-worker, console, zynthian), in protocol.h, rendered into
  protocol/plugin-hostd.json and the README, checked by
  tests/verb_table.py. midi_learn, midi_map, midi_unmap, cv_map and
  cv_unmap are required of the CLAP worker and of Zynthian (decided
  2026-10-22) (#131).
- An LV2 chain under require_pins states its requirement: the chain's
  worker needs a world narrowed to the union of its members' bundles,
  so each member's LV2 pin still holds (#131).
- lv2_worker defaults to auto: the lv2-clap adapter row first, mod-host
  for the plugins it refuses and when the adapter's worker is not
  installed (#101).

* Tue Oct 20 2026 Pau Aliagas <linuxnow@gmail.com> - 0.7.0-1
- New verbs chain <chain> <instance> <instance> ... and chain_clear: the
  instances, in order, run in one worker, and a worker that runs chains
  (omx-clap-host) is told the order. A member that crashes the worker is
  quarantined to a worker of its own and the chain goes on without it,
  announced by chain_formed. Codes -518 to -522 name the refusals (#101).
- New verb plugin-hostd-probe describe clap:<path>#<id> | lv2:<uri>: it
  writes what a plugin states about itself as a scanned descriptor
  (omx-contract 3). It runs omx-clap-scan --fields on the plugin under the
  runner's limits and reads each field through the format's table; a field
  the table has no row for is refused.
- The format tables PLUGIN_HOSTD_CLAP_MAP and PLUGIN_HOSTD_LV2_MAP: every
  CLAP and LV2 term of omx-contract and every field a scan reads, each
  mapped to a descriptor word, carried in the descriptor's extensions or
  dropped by the decision it names. plugin-hostd-devel ships them in
  omx-contract's contract directory (3/plugin-hostd/formats/), and make
  install-contract installs them.
- The build requires omx-contract-devel >= 3.0.0 (libomx-contract-dev
  >= 3.0.0 on Debian).

* Tue Oct 20 2026 Pau Aliagas <linuxnow@gmail.com> - 0.6.0-1
- The probe runner passes --probe-notes and --hold to the CLAP prober and
  carries what it measures: the cost with voices, the LV2 note sweep and the
  note-onset latency.
- The CLAP prober runs under the interposer beside it, and its child counts
  only under the interposer it finds. A preload the runner was started with is
  dropped for the measured child, named in run.tools.droppedPreload, and put
  back after the child; a bare --child is found as execvp finds it.
- The daemon finds a worker's ready line anywhere in its log, not in the first
  4 KB: a second worker no longer answers 503 when LV2_PATH holds many entries
  that are no bundle.
- The CI runs mod-host, so the LV2 worker path is proven there, and a runner
  that refuses unshare fails build-and-test and the JACK job, with a guard
  that holds it.
* Mon Oct 19 2026 Pau Aliagas <linuxnow@gmail.com> - 0.5.0-1
- plugin-hostd-probe runs LV2 plugins too: `run lv2:<uri>` measures a
  plugin through plugin-qualify's lv2_measure, the pin pass and then the
  measurement, each a child under the same limits and wall clock. The
  bundle's files become the document's binary. A plugin of which nothing
  can be pinned exits 2 with no document, and stderr starts with its
  outcome code (probe.unpinnable).
- A pin whose verdict is refused refuses the add with the new code
  PIN_REFUSED (-516), after the files are checked against the pin; an
  instance whose pin turns refused is refused at its next replay.
- Packages ship pins: the new key pins_dir (default
  /usr/share/plugin-hostd/pins.d, which the packages own) names a
  directory whose *.pins files the daemon reads at start, in name order,
  as a read-only layer under the host's pins. A refused pin there always
  holds, and pin_set and pin_accept of its plugin answer -516; any other
  package pin gives way to a host pin of the same plugin.
- New code NOTE_QUEUE_FULL (-517): the worker had no room for a note_on,
  note_off or all_notes_off before its next block, and nothing of the line
  was kept. The daemon passes it to the controller.
- Under lv2_worker auto, a plugin the LV2 adapter refused gets a worker of
  its own unless the add names a placement, so a plugin that aborts on
  mod-host no longer takes a pool's other instances with it. An add whose
  worker dies on it also sends instance_verb_dropped, which names it.
- A worker whose feedback the relay cannot follow is not started: the add
  answers -503. With no memory the relay closes a worker's socket instead
  of leaving it unread, and its poll set no longer crashes the daemon. A
  failed realloc no longer loses the relay's gesture table or the LV2
  adapter's refusal and pick tables: only the one entry is dropped.
- A worker_env nice the daemon cannot apply is logged on stderr; the reply
  stays resp 0.
- The probe runner's default rates and the protocol's parameter scales are
  read from omx-contract's C header (ORACLE_FLOOR_RATES, PARAM_SCALES), so
  the build now requires omx-contract-devel >= 2.16.0 (libomx-contract-dev
  >= 2.16.0 on Debian). Nothing is linked.
- plugin-hostd-tests requires plugin-hostd of the same build, and CI
  checks it. The packaging check refuses any ceiling on
  omx-clap-host-tests ('<=', '=' or '<').
- The own-host page gains an LV2 block run through omx-clap-host, and CI
  measures the audio through the plugin on Debian bookworm and trixie. The
  LV2 adapter tests' refusal arms use a fixture the adapter still refuses.

* Sun Oct 18 2026 Pau Aliagas <linuxnow@gmail.com> - 0.4.0-1
- New tool plugin-hostd-probe: it starts a program that loads a plugin
  (clap-qualify by default) under limits of CPU time, memory, open files,
  file size and real-time priority, kills the whole process tree on the
  deadline, and writes the facts of the run as a JSON document. Its manual
  page is installed, and plugin-hostd-devel ships the document's schema in
  /usr/share/plugin-hostd/probe-output.schema.json.
- Notes: the instance verbs note_input, note_on, note_off and
  all_notes_off pass notes to a worker that takes them; an effect answers
  -513, and an LV2 instance on mod-host answers -514 (play it through its
  JACK MIDI port).
- The tempo and transport (set_bpm, set_bpb, transport, transport_sync) are
  kept by the daemon and handed to every worker when it starts or restarts.
- Presets: preset_list and preset_get list an instance's presets by the key
  preset_load takes; an LV2 instance on mod-host answers -515.
- The events param_gesture and remote_page_suggest are relayed. When a
  worker dies or an instance is removed in the middle of a gesture, the
  daemon sends the gesture's end itself.
- Under lv2_worker auto, a plugin the adapter refused is asked again after
  lv2_worker_set, pin_set, pin_accept or pin_clear.
- param_info on a CLAP instance passes the worker's answer through; -511
  (no checked unit and scale) is documented.
- mod-host-protocol 0.10.6.f14a230-11.1 or newer is required: older builds
  hang on a command of exactly the socket's buffer size and run only the
  first of several commands that arrive in one read.
- A worker line too long to relay is now dropped whole; before, its tail
  reached the controller as a line of its own.
- Numbers are refused when written as -0, so zero has a single spelling.
- The package builds without omx-clap-core; omx-clap-host-tests is needed
  only to run the tests.

* Fri Oct 16 2026 Pau Aliagas <linuxnow@gmail.com> - 0.3.0-1
- You choose which program runs LV2 plugins: mod-host, omx-clap-host or auto
  (the setting lv2_worker, changed with the lv2_worker_set command). A host
  that cannot take LV2 plugins now answers with a new error (-512) and the
  daemon announces the refusal with the lv2_adapter_refused event.
- omx-clap-host 0.9.0 or newer is recommended: older versions do not load LV2
  plugins, so with the default auto choice everything would run on mod-host.
- A new page explains how to use plugin-hostd in your own host.
- Fixed a build failure of programs that include pin.h with gcc -O3 -Werror.

* Thu Oct 15 2026 Pau Aliagas <linuxnow@gmail.com> - 0.2.1-1
- New package plugin-hostd-tests ships the fake worker (fake-host) in
  /usr/libexec/plugin-hostd/tests/, so the CI of other repositories can run
  the pin-file test for real.

* Thu Oct 15 2026 Pau Aliagas <linuxnow@gmail.com> - 0.2.0-1
- Pins are learned on first use: the first time a plugin is added its pin is
  recorded in a pin store, and a later change of the plugin or its layout is
  announced instead of passing silently.
- pin_file names the pin store; saves are fsync'd so a crash never loses a
  pin, and a corrupt or overlong store line is refused rather than trusted.
- One format table holds a row per plugin format: the pins and the
  supervisor read the row, so a new format needs no changes elsewhere, and
  the protocol names capabilities instead of formats.
- The packages require omx-clap-host-tests as a floor only, with no ceiling.

* Thu Oct 15 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.7-1
- The build needs omx-clap-core 0.7.
- The packages require omx-clap-host-tests >= 0.7.0 and below 0.8 for the
  tests.

* Thu Oct 15 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.6-1
- The CLAP worker and its test fixtures now come from the installed
  omx-clap-core packages (omx-clap-host and omx-clap-host-tests) instead of a
  pinned checkout. There are no pins anywhere in the build.
- The packages require omx-clap-host-tests >= 0.6.0 and below 0.7 for the
  tests.

* Wed Oct 14 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.5-1
- The README gains a Status section drawn from the CI jobs, and spells out
  the apt lines for Debian and Ubuntu.
- The project keeps no changelog file: the git history is the changelog.

* Thu Oct 08 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.4-1
- When a plugin worker cannot get its network ports because another process
  took them first, the daemon now starts it again on fresh ports, up to three
  tries, instead of giving up. This fixes the occasional "-503" when adding a
  plugin.
- The JACK test now also runs on JACK2's jackd, and the continuous checks use
  pinned versions of the tools they build with.

* Thu Oct 08 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.3-1
- mod-host's own command vocabulary now ships as a JSON file,
  /usr/share/plugin-hostd/mod-host.json, beside protocol.json, so a controller
  that is not written in C can read both from the installed package.
- The package descriptions now say what plugin-hostd does for you: it keeps
  your effects and instruments running when one plugin crashes.

* Thu Oct 01 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.2-1
- Messages the plugin workers send back, such as meter and state feedback, now
  reach the controller.
- New commands to ask about a plugin: track_info, remote_pages,
  remote_page_get and param_info.

* Wed Sep 30 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.1-1
- A controller can pin the exact binary and layout of a plugin before adding
  it (pin_set, pin_clear, pin_expect), so a plugin that changed on disk is
  refused instead of loaded.
- Every command is now read from one declaration, so the daemon and its header
  cannot disagree.
- A pinned LV2 plugin gets a worker of its own, an add whose pin_expect goes
  unanswered fails, and a refused replay is announced.

* Wed Sep 30 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.0-1
- First package.
