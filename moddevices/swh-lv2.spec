# Tag: Effect
# Type: LV2, Plugin
# Category: Effect

# Global variables for github repository
%global commit0 810b427069441ee365c819220d1515b2d68d941b
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: swh-lv2
Version: 0.9.%{shortcommit0}
Release: 2%{?dist}
Summary: SWH LV2 set of plugins from portalmod
License: GPL-2.0-or-later
URL: https://github.com/portalmod/swh-lv2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/portalmod/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: fftw-devel
BuildRequires: libxslt

%description
SWH LV2 set of plugins from portalmod

%prep
%autosetup -n %{name}-%{commit0}

%build

%set_build_flags

export CFLAGS="-Wno-implicit-function-declaration $CFLAGS"

%make_build real-clean
%make_build

%install

%make_install INSTALL_PATH=%{buildroot}%{_libdir}/lv2 install-system

%files
%doc README
%license COPYING
%{_libdir}/lv2/*

%changelog
* Thu Oct 22 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9-2
- fix debug build

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9
- update for Fedora 29

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9
- Initial build
