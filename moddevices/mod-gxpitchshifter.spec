# Tag: Effect, Pitch
# Type: Plugin, LV2
# Category: Effect

Name: mod-gxpitchshifter
Version: 1.0.3
Release: 1%{?dist}
Summary: Guitarix compatible mod-pitchshifter LV2 set of plugins from portalmod
License: GPL-2.0-or-later
URL: https://github.com/ycollet/mod-pitchshifter
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ycollet/mod-pitchshifter/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: python3
BuildRequires: lv2-devel
BuildRequires: fftw-devel
BuildRequires: fftw
BuildRequires: python3-mpmath
BuildRequires: armadillo-devel
BuildRequires: SuperLU-devel

%description
Guitarix compatible mod-pitchshifter LV2 set of plugins from portalmod

%prep
%autosetup -n %{name}-%{version}

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
* Thu Nov 24 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0.3-1
- update to 1.0.3-1

* Mon Nov 23 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-1
- update to 1.0.2-1

* Sun Nov 22 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-1
- update to 1.0.1-1

* Thu Nov 12 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial build
