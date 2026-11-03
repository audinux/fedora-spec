# SPDX-License-Identifier: GPL-3.0-or-later
# libreac, the Roland REAC protocol library, and libreac-transport, the sockets and threads that
# carry it, from one source and one version. Two libraries, four binary packages.
Name:           libreac
Version:        1.10.0
# THE SONAME'S MAJOR, and it is not decoration. rpm generates this package's
# `provides` (libreac.so.N()(64bit)) and every consumer's runtime `requires`
# from it, so bumping it is what makes a mismatched pair refuse to install
# instead of failing at exec time with `undefined symbol`. It tracks
# LIBREAC_ABI in include/reac/reac.h -- tests/conformance-packaging.sh refuses a copy
# that disagrees with the header, in `make test`, before a package is built.
%global abi 6
# libreac-transport's own soname major. It moves independently of libreac's: the two libraries
# are built from this one source and share a version, not an ABI.
%global tabi 7
Release:        1%{?dist}
Summary:        Roland REAC wire-format core (validate, counter, 24-bit decode/encode, capture)

License:        GPL-3.0-or-later
URL:            https://github.com/FreeREAC/libreac
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
libreac speaks Roland REAC, the protocol between Roland digital consoles and their
stageboxes, so a Linux machine can sit on a REAC network as an equal: hear a
stagebox, enrol it, and read what it is straight from its own frames: its inputs
and outputs, its model, its firmware.

libreac is the REAC protocol library: it recognises a REAC frame (EtherType 0x8819),
reads its sequence counter, detects the sample rate, and decodes and encodes the
24-bit braided audio region in both directions (the 40-channel master broadcast
and the box's upstream return), plus a legacy plain-LE diagnostic path. It also
implements the REAC control plane: control-block layout and checksums, head-amp
records, box identity, and the master/slave establishment state machines, and it
reads frames from a live AF_PACKET capture or an offline pcap.

%package devel
Summary:        Development files for libreac
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and pkg-config for building against libreac.

%package -n libreac-transport
Summary:        The REAC transport layer: sockets, pacer, RT threads, VLAN scan (userspace backend)
Requires:       libreac%{?_isa} >= 1.1.0

%description -n libreac-transport
libreac-transport is the REAC transport layer: AF_PACKET frame RX/TX over a lock-free
ring, a SCHED_FIFO cadence pacer with clock discipline, network interface and VLAN
scanning, segment locking, and slave/master establishment orchestration built on
libreac's protocol state machines. The public API carries no socket type, so an
alternate backend can implement the same shape; the library holds no Linux capability
itself, that belongs to the process that links it.

%package -n libreac-transport-devel
Summary:        Development files for libreac-transport
Requires:       libreac-transport%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(libreac) >= 1.1.0

%description -n libreac-transport-devel
Headers and pkg-config for building against libreac-transport.

%package tests
Summary:        A software REAC stagebox, to test a program that talks to one

%description tests
fake_box answers on the wire the way a REAC stagebox does, so a program that
enrols and plays to a box can be tested without one. It is built from libreac's
own objects and needs no other package. It is installed in
%{_libexecdir}/libreac/tests and is of no use to anyone else.

%prep
%autosetup -n %{name}-%{version}

%build
# Every src/*.c, never a hand-kept list. The list form had drifted twice: it was
# still naming six files after src/reac_ports.c and src/reac_ctrlblk.c landed, so
# the shared object shipped without reac_ports_parse, reac_headamp_base and the
# whole reac_ctrl_*/reac_headamp_* control-block surface, while the -devel package
# happily installed headers declaring them. Nothing failed at build time -- a
# consumer only found out at link.
for f in src/*.c; do
  cc %{optflags} -fPIC -Iinclude -c "$f" -o "$(basename "$f" .c).o"
done
# %%build_ldflags carries the Fedora link flags incl. --build-id, which the
# debuginfo extraction requires (%%optflags already gave the objects -g).
# -lm: reac_encode's float->s24 rounds with lrintf.
#
# --no-undefined IS THE GATE FOR THE PARAGRAPH ABOVE. The glob fixed the drift it
# describes but nothing MEASURED the result, and 0.8.0 shipped the same defect in a new
# shape: reac_macaddr.h declared reac_mac48_unpack, reac_link_state.c called it, and the
# definition was still in reac-pw -- so this link succeeded and every consumer's did not
# (`/usr/lib64/libreac.so: undefined reference`, nine reac-pw targets, in its %%build).
# A shared object is allowed unresolved symbols by default; this refuses them, here,
# where the missing file is.
cc %{build_ldflags} -shared -Wl,-soname,libreac.so.%{abi} -Wl,--no-undefined \
  -o libreac.so.%{version} *.o -lm

# libreac-transport: a second, parallel object family in its own directory, never folded into the
# glob above, or every transport file would join libreac's own soname.
# It links the libreac.so just built, through a development symlink that stays in the build tree.
ln -s libreac.so.%{version} libreac.so
mkdir transport-obj
for f in transport/src/*.c; do
  cc %{optflags} -fPIC -D_GNU_SOURCE -Iinclude -Itransport/src \
     -c "$f" -o transport-obj/"$(basename "$f" .c).o"
done
# --no-undefined is the same gate as above: a symbol the transport calls into libreac that libreac
# lacks fails here, at package build, not at a consumer's exec.
cc %{build_ldflags} -shared -Wl,-soname,libreac-transport.so.%{tabi} -Wl,--no-undefined \
  -o libreac-transport.so.%{version} transport-obj/*.o -L. -lreac -lm -lpthread

# fake_box links the objects of libreac itself, not the shared library, so the package that carries it needs nothing
cc %{optflags} -D_GNU_SOURCE -Iinclude tools/fake_box.c $(ls *.o) %{build_ldflags} -lm -o fake_box

%install
install -Dm0755 libreac.so.%{version} %{buildroot}%{_libdir}/libreac.so.%{version}
ln -s libreac.so.%{version} %{buildroot}%{_libdir}/libreac.so.%{abi}
ln -s libreac.so.%{abi}     %{buildroot}%{_libdir}/libreac.so
# Same rule as %%build: every public header, derived. reac_ctrlblk.h and
# reac_ports.h were missing from the old hand-kept list.
for h in include/reac/*.h; do
  install -Dm0644 "$h" %{buildroot}%{_includedir}/reac/"$(basename "$h")"
done
# The pkg-config files are templates in packaging/, shared with the Debian build.
mkdir -p %{buildroot}%{_libdir}/pkgconfig
sed -e 's|@LIB@|%{_lib}|' -e 's|@VERSION@|%{version}|' packaging/libreac.pc.in \
  > %{buildroot}%{_libdir}/pkgconfig/libreac.pc

# libreac-transport
install -Dm0755 libreac-transport.so.%{version} %{buildroot}%{_libdir}/libreac-transport.so.%{version}
ln -s libreac-transport.so.%{version} %{buildroot}%{_libdir}/libreac-transport.so.%{tabi}
ln -s libreac-transport.so.%{tabi}    %{buildroot}%{_libdir}/libreac-transport.so
for h in include/reac/transport/*.h; do
  install -Dm0644 "$h" %{buildroot}%{_includedir}/reac/transport/"$(basename "$h")"
done
sed -e 's|@LIB@|%{_lib}|' -e 's|@VERSION@|%{version}|' packaging/libreac-transport.pc.in \
  > %{buildroot}%{_libdir}/pkgconfig/libreac-transport.pc

install -Dm0755 fake_box %{buildroot}%{_libexecdir}/libreac/tests/fake_box

%check
# libreac's own suite, against the very objects %%build produced (the Makefile
# finds them up to date and only archives them). Without this the RPM was built
# and shipped without one assertion ever running -- the tests were not even in
# the tarball.
make test

%files
%license LICENSE
%{_libdir}/libreac.so.%{version}
%{_libdir}/libreac.so.%{abi}

%files devel
# The whole directory, so a new public header ships the day it lands instead of
# waiting for someone to remember this list.
%dir %{_includedir}/reac
%{_includedir}/reac/*.h
%{_libdir}/libreac.so
%{_libdir}/pkgconfig/libreac.pc

%files -n libreac-transport
%license LICENSE
%{_libdir}/libreac-transport.so.%{version}
%{_libdir}/libreac-transport.so.%{tabi}

%files -n libreac-transport-devel
%dir %{_includedir}/reac/transport
%{_includedir}/reac/transport/*.h
%{_libdir}/libreac-transport.so
%{_libdir}/pkgconfig/libreac-transport.pc

%files tests
%license LICENSE
%{_libexecdir}/libreac/tests/fake_box

%changelog
* Wed Oct 28 2026 Pau Aliagas <linuxnow@gmail.com> - 1.10.0-1
- The etf qdisc read-back (reac_etf_qdisc_state, reac_etf_qdisc_stats_read)
  has a fuzz harness, fuzz_qdisc, over a fake rtnetlink kernel, with 32
  recorded breakages on 7 checks; it is the witness reac-pw's own copy of the
  reader waited for (#8, R3).
- The dump walker under both reads stops at the bytes recv() returned: it
  compared the remainder as size_t, so an unpadded last message wrapped it and
  the walk ran on into the stale rest of the buffer. Found by the new harness;
  a kernel pads every message, so no rig saw it.

* Tue Oct 27 2026 Pau Aliagas <linuxnow@gmail.com> - 1.9.0-1
- reac_cfg.h declares the pace and role vocabulary libreac-transport used to
  take from reac-pw: enum reac_rate_refuse, enum reac_role_refuse, their
  REAC_*_REFUSE_CODES_INIT tables, the REAC_RATE_BIT_* and REAC_RATE_ALL_BITS
  masks, and REAC_ROLE_STATE_APPLIED / REAC_ROLE_STATE_REESTABLISH_PENDING.
  reac_pacer.h and reac_role_swap.h include it, so libreac builds without a
  reac-pw header, and the vendored copy of reac-pw's two headers is gone (#8).

* Sun Oct 25 2026 Pau Aliagas <linuxnow@gmail.com> - 1.8.0-1
- pcap_source_next skips a record of 0 bytes and goes on; 0 means the end of
  the file and nothing else. It used to return the empty record's length, 0,
  and end the walk on it (#23).
- The fuzz harnesses are Theorem Labs' per-check rewrite: every property check
  names a one-line breakage and the seed that catches it, 393 records on 207
  checks, all proven at this commit by `make fuzz-records`, and a check
  without a record is refused. The headers promise what the checks hold: a
  refused decode or scene build leaves its output untouched; the scene
  trailer, the grant sweep's order and head rows, discovery's observe, age
  and JSON, and the head-amp values are documented (#23).

* Sat Oct 24 2026 Pau Aliagas <linuxnow@gmail.com> - 1.7.3-1
- libreac-tests (RPM and DEB) ships fake_box in /usr/libexec/libreac/tests/fake_box,
  needing only libc and libm, so a consumer's tests install it from the
  channel instead of building libreac from source (#10; serves
  FreeREAC/reac-pw#23).
- fuzz_ctrl's corpus gains the two single-record identity replies (firmware
  CC0016, REAC version CC001A), and fuzz/checks.awk holds every harness
  property check to the seed corpus in `make fuzz-cov` (168 checks; #24,
  issue #22).

* Sat Oct 24 2026 Pau Aliagas <linuxnow@gmail.com> - 1.7.2-1
- A scene replay armed past the end of the head-amp table now arms nothing.
  Its width clamp wrapped for a base of 49 or more and replayed head-amp
  records onto channels 0..47, other boxes' included (#15).
- Every parser of wire bytes has a libFuzzer harness under fuzz/, run under
  ASan and UBSan with a generated seed corpus, a coverage floor and one
  planted mutant per harness; CI fuzzes each for 60 s on every push and pull
  request (#13).

* Thu Oct 08 2026 Pau Aliagas <linuxnow@gmail.com> - 1.7.1-1
- libreac and libreac-transport are now installed from the FreeMixer package
  channel: signed RPMs for Fedora 44 (x86_64, aarch64) and DEBs for Debian
  bookworm and trixie (amd64, arm64). Add the channel once, then install or
  update with dnf or apt. The libraries themselves do not change.
- The Debian packages are libreac6, libreac-dev, libreac-transport7 and
  libreac-transport-dev, named after the sonames they carry. The Fedora
  packages keep their names: libreac, libreac-devel, libreac-transport and
  libreac-transport-devel.

* Wed Oct 07 2026 Pau Aliagas <linuxnow@gmail.com> - 1.7.0-1
- A connected stagebox is described only by what it says on the wire: its
  inputs and outputs from its declaration, its family from its identity page,
  and its name from both (S-1608, S-4000S-3208, S-4000S-1624, S-4000S-4000
  ...). A box whose family has never been captured is named by its widths
  (REAC-0816).
- The built-in model table is now a model catalogue, used only to emulate a
  box and to plan a show offline. It never sizes or names a connected box;
  when the two disagree the box wins and the difference can be reported.
- The S-0808's name, which arrives split across two frames, is now read.
- A box that joins after the console first asked for its identity is asked
  again, once a second, so its firmware and hardware block are no longer left
  empty.
- A stagebox in master mode is recognised from what it announces or the width
  it broadcasts. A 40-channel master that has not announced itself yet is
  waited on instead of being taken for a desk.
- Developers: reac_box_facts.h is new; the catalogue functions are renamed
  (reac_box_catalogue*), reac_box_master_model is gone, and discovery reports
  declared widths. libreac's soname is 6 and libreac-transport's is 7.

* Fri Sep 25 2026 Pau Aliagas <linuxnow@gmail.com> - 1.6.0-1
- A stagebox may declare any even width from 2 to 40 channels in each
  direction, and a 40-channel box is legal. A box that returns 40 channels
  upstream is a box, not a desk.
- A sender that broadcasts is given a bounded time to show whether it is the
  desk or a stagebox, and is treated as a box once that time passes without a
  desk-only message.
- Sample-rate detection measures one stream, so a 48 kHz session heard in both
  directions is no longer read as 96 kHz.
- An identity reply is accepted only when both of its checksums close, and the
  plain-LE diagnostic decode refuses a geometry wider than the frame.
- Developers: reac_cfg.h is the one declaration of the configuration
  vocabulary and reac_code.h the one list of refusal codes. This is a
  source-level change; libreac's soname moves 4 to 5 and libreac-transport's 5
  to 6.

* Tue Sep 22 2026 Pau Aliagas <linuxnow@gmail.com> - 1.5.0-1
- A VLAN trunk names its VLANs by tagging, and the topology tap hears them: a
  VLAN whose stagebox is still cold is discovered as soon as the switch tags
  any frame on it, without transmitting anything.
- Developers: reac_topo_heard_vids() and REAC_TOPO_TAGGED_OTHER are added. No
  existing symbol changes.

* Tue Sep 22 2026 Pau Aliagas <linuxnow@gmail.com> - 1.4.0-1
- The decisions about whether a wire is vacant and when to stop waiting for
  the topology tap are made by the library, through reac_knock.h and
  reac_tapwait.h, instead of by each program that links it. Behaviour is
  unchanged.

* Mon Sep 21 2026 Pau Aliagas <linuxnow@gmail.com> - 1.3.2-1
- A capture no longer hears frames from every network interface on the machine
  for the instant before it is bound to its own. A cold cable could previously
  show a stagebox that was mastering another interface as heard on it.
- The transmit socket is bound to its interface and ignores incoming traffic,
  instead of queueing every REAC frame on the host.

* Fri Sep 11 2026 Pau Aliagas <linuxnow@gmail.com> - 1.0.0-1
- The protocol library as proven on real Roland desks and stageboxes at 44.1,
  48 and 96 kHz.
