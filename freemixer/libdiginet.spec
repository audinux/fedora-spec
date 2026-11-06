# SPDX-License-Identifier: GPL-3.0-or-later
# libdiginet, the protocol of the Digidesign Control|24 and ProControl surfaces, and
# libdiginet-transport, the wire under it, from one source and one version; diginet-tools
# carries diginet-probe and diginet-packet-helper.
Name:           libdiginet
Version:        0.1.9
# The sonames' majors. rpm derives this package's provides and every consumer's requires from
# them. They copy DIGINET_ABI and DIGINET_TRANSPORT_ABI of include/diginet/diginet.h, and
# tests/conformance-packaging.sh (in make test) refuses a copy that disagrees.
%global abi 0
%global tabi 0
Release:        1%{?dist}
Summary:        Drive a Digidesign Control|24 or ProControl surface from Linux

License:        GPL-3.0-or-later
URL:            https://github.com/FreeMixer/libdiginet
Source0:        https://github.com/FreeMixer/libdiginet/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  git-core
BuildRequires:  pkgconf-pkg-config

%description
libdiginet speaks DigiNet, the raw Ethernet protocol of the Digidesign Control|24 and
ProControl control surfaces, so a Linux mixer or DAW can drive one again: motor faders and
their touch, V-Pots and their LED rings, every key and lamp, scribble strips, meters, the
counter and the jog wheel.

This package holds two shared libraries. libdiginet is the protocol: the frame grammar,
encoders and decoders for every control, and one personality per desk; it refuses to encode
the desk's memory-writing message family. libdiginet-transport is the wire: the packet
socket, discovery, the online handshake, acknowledgements, a keepalive that ACKs never
starve, retransmit, back-off, latest-wins coalescing and display pacing. It never wakes a
desk another host is using.

%package devel
Summary:        Development files for libdiginet and libdiginet-transport
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers, pkg-config files (libdiginet, libdiginet-transport) and the Kaitai Struct grammar of
the protocol, diginet.ksy, for building programs that drive a Control|24 or ProControl; and
libdiginet-emu, a static desk emulator with its headers and pkg-config file, for testing them
without a desk.

%package -n diginet-tools
Summary:        diginet-probe and diginet-packet-helper for a Control|24 or ProControl
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n diginet-tools
diginet-probe wakes a Control|24 or ProControl cabled to a network interface, moves a fader,
lights a lamp, writes a scribble strip, logs and decodes every key, touch and turn, and ends
with a summary of what the desk answered. It is installed with the one capability it needs
to open a packet socket, cap_net_raw.

diginet-packet-helper opens the packet socket that hears a desk on every network interface and
hands it to the program that started it, so that program needs no capability. It is installed
with cap_net_raw and nothing else.

%prep
%autosetup -n %{name}-%{version}

%build
%make_build CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}" shared

%install
# not %%make_install: it names the `install` target (the static archives) as well
make DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir} INCDIR=%{_includedir} \
  BINDIR=%{_bindir} DATADIR=%{_datadir} MANDIR=%{_mandir} install-shared

#%check
#make CFLAGS="%{optflags}" test

%files
%license LICENSE
%doc README.md
%{_libdir}/libdiginet.so.%{version}
%{_libdir}/libdiginet.so.%{abi}
%{_libdir}/libdiginet-transport.so.%{version}
%{_libdir}/libdiginet-transport.so.%{tabi}

%files devel
%doc BUILDING.md docs/protocol.md
%dir %{_includedir}/diginet
%dir %{_includedir}/diginet/transport
%dir %{_includedir}/diginet/testsupport
%{_includedir}/diginet/*.h
%{_includedir}/diginet/transport/*.h
%{_includedir}/diginet/testsupport/*.h
%{_libdir}/libdiginet-emu.a
%{_libdir}/libdiginet.so
%{_libdir}/libdiginet-transport.so
%{_libdir}/pkgconfig/libdiginet.pc
%{_libdir}/pkgconfig/libdiginet-transport.pc
%{_libdir}/pkgconfig/libdiginet-emu.pc
%dir %{_datadir}/diginet
%{_datadir}/diginet/diginet.ksy

%files -n diginet-tools
%doc docs/probe.md
%caps(cap_net_raw=ep) %{_bindir}/diginet-probe
%caps(cap_net_raw=ep) %{_bindir}/diginet-packet-helper
%{_mandir}/man1/diginet-probe.1*
%{_mandir}/man1/diginet-packet-helper.1*

%changelog
* Thu Nov 05 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.9-1
- update to 0.1.9-1

* Tue Nov 03 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.7-1
- libdiginet-emu: the desk emulator, its pump and the network-namespace helper
  are installed as test support (a static archive, include/diginet/testsupport
  and libdiginet-emu.pc), in libdiginet-devel, so consumers build their tests
  against it instead of carrying copies (#59).

* Sun Nov 01 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.6-1
- A desk that ACKed its e2 has 10 s to show its e1, since it does so at its
  next announce, up to 9.4 s apart on a Control|24. The 3 s stays for the
  a0. Such a desk no longer counts towards DESK_DEAF (#56).
- Five fuzz checks hold to what their comments say (#55).

* Sat Oct 31 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.5-1
- diginet_sysex_encode() refuses a len within 4 of SIZE_MAX with
  DIGINET_E_SPACE. Such a len wrapped the space check, and the encoder read
  past the payload. Only a caller passing such a len reaches it: every
  encoder in the library passes at most 10 bytes and no decode or transport
  path calls it, so no desk frame can (#53).
- docs/protocol.md says what the Control|24 captures show: desk frames that
  batch moves of one fader, the desk's counter step, the v of the version in
  the announce, the desk's own 0x70 messages, and stale bytes at or above
  0x80 in the padding (#52).
- The transport fuzz harness runs its model in the order poll hands the
  frames over, holds poll's result, and holds the session deadline to when
  the session next has work, an e2 owed to a Control|24's e0 included
  (#51, from Sami Jawhar).

* Fri Oct 30 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.4-1
- A desk that vanishes, unplugged or powered off, sends no e0 and stops
  ACKing: a host frame it leaves unACKed through every retry ends the
  session (DIGINET_R_ACK_LOST), about 0.6 s with the defaults, instead of
  the session reading online until offline_ms (25 s) of silence. A desk's
  e0 after a reboot still ends it with DIGINET_R_DESK_OFFLINE (#45).
- A Control|24 is online on the a0 for its e2 again: a freshly booted desk
  enters its session only after the host has sent in it, and its e0 before
  its first e1 gets another e2. That e2 opens a new session on the desk,
  which blanks its scribbles, so the first e1 naming this host is ONLINE
  again (DIGINET_R_RENEWED) and the host shows everything again. A host
  restarted while the desk holds its session is online on the a0 for the e2
  the desk's e1 wakes, that e1 being the proof (#48).

* Fri Oct 30 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.3-1
- A Control|24 in session announces only e1 naming its host, as a ProControl
  does, and an e0 means it is out of session: it is online on the a0 for an
  e2 and an e1 naming this host, and after a reboot its e0 ends the session,
  which the next wake takes again, so a host repaints on that state change.
  Every e2 carries send counter 0, the only counter on which a Control|24
  takes a session. The a0-alone online path and the session lost on an
  unACKed host frame, which no desk reaches, are gone (#41).
- A desk moved between two interfaces of one host is re-taken at once: an
  e1 naming any MAC of this host is this host's session, not another host's;
  the mux gives each session the host's other MACs from the io's host_macs
  (diginet_host_macs() on the packet socket) (#40).

* Fri Oct 30 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.2-1
- A Control|24 is online on the a0 that answers our e2: it announces its
  session in e0 after a boot and in e1 once its front panel is used, so the
  session ends on an e0 only after an e1 named this host, and otherwise on a
  host frame it stops ACKing (#30).
- A restarted host re-takes its own session at the desk's next announce
  instead of waiting about 30 s for the desk to time out (#33).
- One packet socket hears every interface, including interfaces added later;
  diginet-packet-helper opens it with cap_net_raw and hands it to an
  unprivileged caller over a Unix socket; the desk mux runs a session per desk
  with appeared and gone notices; a desk that announces but lets three wakes
  in a row time out is reported as DIGINET_N_DESK_DEAF; diginet-probe --any
  drives it (#35).
- docs/protocol.md carries what a Control|24 (firmware 1.08) measured on
  2026-10-29: the ring, the meter, the counter, the scribble addresses, the
  strip keys, the jog wheel, the motor set-point, a new session blanking the
  desk, and a burst taken whole (#29).
- The fuzz harnesses meet the OSS Verify build contract: every property
  carries mutant records met on their own seeds, sabotage patches, and a
  harness for the desk mux (#27, #35).

* Sat Oct 24 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.1-1
- A failed send in diginet_session_wake() no longer overwrites the data
  frame in flight: the wake is built aside and only becomes the in-flight
  frame once it has gone out, so a retransmit still carries the data (#22).
- Two coalesced commands can no longer spell the F0 13 xx 70 sequence that
  made the whole frame undeliverable: the body is checked as each command
  joins it and a pair that would collide goes out in two frames (#23).
- Fuzz harnesses for the frame, the command grammar, the codecs and the
  session, with coverage floors held in CI and a mutant per property; the
  seeds are generated and the committed corpus is checked against them (#21).
* Mon Oct 19 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.0-1
- First release: a C library for the Ethernet protocol of the Digidesign
  Control|24 and ProControl surfaces. Not yet tried on a desk.
- libdiginet: the frame grammar (protocol/diginet.ksy, installed with the
  development package), parsing and building of frames with the header
  sum, and the desk's announce.
- Encoders and decoders for the motor faders and their touch sense,
  buttons and lamps, V-Pots and the jog wheel, the V-Pot LED rings,
  meters, the automation and counter-mode LEDs, the scribble strips and
  the eight-digit counter, with one personality each for the Control|24
  and the ProControl.
- The system message family that writes the desk's own memory
  (F0 13 xx 70) is refused by the encoders, the body check and the frame
  builder.
- libdiginet-transport: the packet socket and one host's session with a
  desk: discovery, wake, ACKs, one frame in flight with retransmission,
  back-off after a desk retry, a keepalive on its own clock, a queue
  where a newer value replaces a queued one, pacing of display writes,
  and no wake while the desk is in another host's session.
- diginet-tools: diginet-probe, a first test on a real desk (wake it,
  move a fader, light a lamp, write a scribble strip, log every press),
  installed with cap_net_raw, and its manual page.
