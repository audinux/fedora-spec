# Tag: Effect, Graphic
# Type: LV2, Plugin
# Category: Plugin, Graphic

# Global variables for github repository
%global commit0 a1e043cb5886fb61d193fd97ec49b280e63f1a5e
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

#
# spec file for package mod-ui
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

Name: mod-ui
Version: 0.99.8.%{shortcommit0}
Release: 2%{?dist}
License: GPL-3.0
Summary: Web-based interface for the MOD
URL: https://github.com/moddevices/mod-ui
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/moddevices/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: python3-devel
BuildRequires: python3
BuildRequires: python3-setuptools
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(lilv-0)

Requires: lilv
Requires: python3
Requires: python3-pillow
Requires: python3-pyserial
Requires: python3-tornado

%description
This is the UI for the MOD software. It is a webserver that delivers an HTML5
interface and communicates with mod-host. It also communicates with the MOD
hardware, but does not depend on it to run.

%prep
%autosetup -n %{name}-%{commit0}

sed -i '/LDFLAGS +=/d' utils/Makefile
sed -i '/CFLAGS += -Wall/d' utils/Makefile
sed -i '/CXXFLAGS += -Wall/d' utils/Makefile

%build

%install

%set_build_flags
export CXXFLAGS="-fPIC $CXXFLAGS"
export CFLAGS="-fPIC $CFLAGS"

python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%doc CHANGELOG README.rst LICENSE
%{_bindir}/mod-ui
%{python3_sitelib}/mod/
%{python3_sitelib}/mod-*.egg-info/
%{python3_sitelib}/modtools/
%dir %{_datadir}/mod
%{_datadir}/mod/*

%changelog
* Tue Mar 19 2024 Yann Collette <ycollette.nospam@free.fr> - 0.99.8-2
- update to last master

* Tue Jul 27 2021 Yann Collette <ycollette.nospam@free.fr> - 0.99.8-1
- initial spec
