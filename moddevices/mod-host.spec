# Status: active
# Tag: Rack, Jack
# Type: Standalone
# Category: Audio, Effect

%global commit0 f14a230bf48b42035406d2b2dca038efa4d2abca
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

#
# spec file for package mod-host
#
# Copyright (c) 2017 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name: mod-host
Version: 0.10.6.%{shortcommit0}
Release: 10%{?dist}
License: GPL-3.0-or-later
Summary: LV2 host for Jack controllable via socket or command line
URL: https://github.com/moddevices/mod-host
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/moddevices/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz
Source1: %{name}.service
# https://github.com/mod-audio/mod-host/pull/100
Patch0: mod-host-100.patch
# https://github.com/mod-audio/mod-host/pull/101
Patch1: mod-host-101.patch
# https://github.com/mod-audio/mod-host/pull/98 - fix a heap overread on an empty path property
Patch2: mod-host-98.patch
# https://github.com/mod-audio/mod-host/pull/81 - allow runs of spaces between protocol words
Patch3: mod-host-81.patch
# follow-up to https://github.com/mod-audio/mod-host/pull/81 - no leading space on the next word
Patch4: mod-host-81b.patch
# https://github.com/mod-audio/mod-host/pull/82 - add the missing -t short option
Patch5: mod-host-82.patch
# https://github.com/mod-audio/mod-host/pull/104
Patch6: mod-host-104.patch
# https://github.com/mod-audio/mod-host/pull/105
Patch7: mod-host-105.patch
# https://github.com/mod-audio/mod-host/pull/106
Patch8: mod-host-106.patch
# https://github.com/mod-audio/mod-host/pull/107
Patch9: mod-host-107.patch
# https://github.com/mod-audio/mod-host/pull/108
Patch10: mod-host-108.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: python3
BuildRequires: readline-devel
BuildRequires: fftw-devel
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(lilv-0)
BuildRequires: systemd-rpm-macros

%{?systemd_requires}
Requires: lilv
Requires: %{name}-protocol%{?_isa} = %{version}-%{release}

%description
mod-host is an LV2 host for JACK, controllable via socket or command line

Currently the host supports the following LV2 features:
* lv2core
* atom
* event
* buf-size
* midi
* options
* uri-map
* urid
* worker
* presets

mod-host is part of the MOD project (https://mod.audio/).

%package protocol
Summary: mod-host socket protocol library

%description protocol
libmod-host-protocol, the socket server, line protocol and command
dispatch of mod-host, shared by mod-host and other hosts.

%package protocol-devel
Summary: Headers and pkg-config file for the mod-host socket protocol library
Requires: %{name}-protocol%{?_isa} = %{version}-%{release}

%description protocol-devel
Headers, pkg-config file and backend scenarios for libmod-host-protocol,
the socket server, line protocol and command dispatch of mod-host, for
hosts that answer mod-host's protocol with their own plugin backend.

%prep
%autosetup -p1 -n %{name}-%{commit0}

sed -i 's,PREFIX =.*$,PREFIX = %{_prefix},g' Makefile
sed -i 's,MANDIR =.*$,MANDIR = %{_mandir}/man1,g' Makefile
sed -i 's,LDFLAGS += -s,LDFLAGS +=,g' Makefile

%build

%set_build_flags

%make_build
%make_build lib

%install

%make_install LIBDIR=%{_libdir}
%make_install install-lib LIBDIR=%{_libdir}

install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 644 %{SOURCE1} %{buildroot}%{_userunitdir}/%{name}.service

%files
%doc CHANGELOG README.md COPYING
%{_bindir}/mod-host
%{_libdir}/jack/*
%{_mandir}/man1/mod-host.*
%{_unitdir}/%{name}.service
%{_userunitdir}/%{name}.service

%files protocol
%license COPYING
%{_libdir}/libmod-host-protocol.so.0*

%files protocol-devel
%{_libdir}/libmod-host-protocol.so
%{_includedir}/mod-host/
%{_libdir}/pkgconfig/mod-host-protocol.pc
%{_datadir}/mod-host/

%changelog
* Thu Oct 01 2026 Pau Aliagas <linuxnow@gmail.com> - 0.10.6-10
- #101: retry a suffixed client name on any exact-name failure (jack2)

* Wed Sep 30 2026 Pau Aliagas <linuxnow@gmail.com> - 0.10.6-9
- our patches are now the upstream PRs 100, 101 and 104 to 108, one file each;
  PRs 81, 82 and 98 unchanged
- install the protocol library with make install-lib

* Wed Sep 30 2026 Pau Aliagas <linuxnow@gmail.com> - 0.10.6-8
- update PR 103: a backend can answer monitor_output and send output_set

* Wed Sep 30 2026 Pau Aliagas <linuxnow@gmail.com> - 0.10.6-7
- move libmod-host-protocol.so.0 into its own mod-host-protocol subpackage

* Tue Sep 29 2026 Pau Aliagas <linuxnow@gmail.com> - 0.10.6-6
- build the socket, protocol and command dispatch as a shared library,
  libmod-host-protocol.so.0, with its headers and pkg-config file in
  mod-host-protocol-devel

* Fri Sep 25 2026 Pau Aliagas <linuxnow@gmail.com> - 0.10.6-5
- apply the fix from upstream PR 98: a plugin sending an empty path no longer
  makes mod-host read past its buffer
- apply upstream PRs 81 and 82 (riban) and a follow-up to 81: runs of spaces
  between protocol words are accepted, and "-t" runs the self-test

* Tue Sep 22 2026 Pau Aliagas <linuxnow@gmail.com> - 0.10.6-4
- apply upstream PR 101: an optional jack client name on the add command

* Sat Sep 05 2026 Yann Collette <ycollette.nospam@free.fr> - 0.10.6-3
- update to 0.10.6-3 - apply a patch

* Sat Sep 05 2026 Yann Collette <ycollette.nospam@free.fr> - 0.10.6-2
- update to 0.10.6-2 - update to last master

* Tue Jul 27 2021 Yann Collette <ycollette.nospam@free.fr> - 0.10.6-1
- initial spec
