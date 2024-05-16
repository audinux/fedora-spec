# Tag: Pitch
# Type: LV2
# Category: Plugin, Effect

# Global variables for github repository
%global commit0 efd26e6b02ddf9683ffae00a59ad72b5ab59d585
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: mod-pitchshifter
Version: 0.9.%{shortcommit0}
Release: 3%{?dist}
Summary: mod-pitchshifter LV2 set of plugins from portalmod
License: GPL-2.0-or-later
URL: https://github.com/portalmod/mod-pitchshifter
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/portalmod/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: fftw-devel
BuildRequires: fftw
BuildRequires: python3
BuildRequires: python3-mpmath
BuildRequires: armadillo-devel
BuildRequires: SuperLU-devel

%description
mod-pitchshifter LV2 set of plugins from portalmod

%prep
%autosetup -n %{name}-%{commit0}

sed -i -e "s/-Wl,--strip-all//" Makefile.mk

%build

%set_build_flags

%ifarch aarch64
%make_build INSTALL_PATH=%{_libdir}/lv2 NOOPT=true
%else
%make_build INSTALL_PATH=%{_libdir}/lv2
%endif

%install

%make_install INSTALL_PATH=%{_libdir}/lv2

%files
%doc README.md
%{_libdir}/lv2/*

%changelog
* Thu Nov 24 2022 Yann Collette <ycollette.nospam@free.fr> - 0.9-3
- update to last master

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9
- update for Fedora 29

* Wed Oct 25 2017 Yann Collette <ycollette.nospam@free.fr> - 0.9
- update to latest master version

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9
- Initial build
