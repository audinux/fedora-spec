# Tag: Rack, Jack
# Type: Standalone
# Category: Audio, Effect

# Global variables for github repository
%global commit0 9e17878aff58ef2e3aecc74fc94a817d96b92d1f
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
Release: 1%{?dist}
License: GPL-3.0
Summary: LV2 host for Jack controllable via socket or command line
Url: https://github.com/moddevices/mod-host

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/moddevices/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz
Source1: %{name}.service

%{?systemd_requires}
BuildRequires: gcc
BuildRequires: make
BuildRequires: python3
BuildRequires: readline-devel
BuildRequires: fftw-devel
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(lilv-0)
BuildRequires: systemd-rpm-macros

Requires: lilv

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

mod-host is part of the MOD project (http://moddevices.com).

%prep
%autosetup -n %{name}-%{commit0}

sed -i 's,PREFIX =.*$,PREFIX = %{_prefix},g' Makefile
sed -i 's,MANDIR =.*$,MANDIR = %{_mandir}/man1,g' Makefile
sed -i 's,LDFLAGS += -s,LDFLAGS +=,g' Makefile
sed -i 's,python,python3,g' utils/txt2cvar.py

%build

%set_build_flags
%make_build

%install
%make_install

install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 644 %{SOURCE1} %{buildroot}%{_userunitdir}/%{name}.service

%files
%doc CHANGELOG README.md COPYING
%{_bindir}/mod-host
%{_libdir}/jack/*
%{_mandir}/man1/mod-host.*
%{_unitdir}/%{name}.service
%{_userunitdir}/%{name}.service

%changelog
* Tue Jul 27 2021 Yann Collette <ycollette.nospam@free.fr> - 0.10.6-1
- initial spec
