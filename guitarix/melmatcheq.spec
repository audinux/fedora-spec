# Tag: Analyzer, Amp Simul, Equalizer
# Type: LV2, Plugin
# Caterory: Effect, Tool

Name: lv2-MelMatchEQ
Version: 0.1
Release: 1%{?dist}
Summary: MelMatchEQ is a profiling EQ using a 26 step Mel Frequency Band
License: GPL-2.0-or-later
URL: https://github.com/brummer10/MelMatchEQ.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/brummer10/MelMatchEQ.lv2/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: gtk2-devel
BuildRequires: glib2-devel

%description
MelMatchEQ is a profiling EQ in LV2 plugin format, using a 26-step Mel Frequency Band.
It can analyse the spectral profile of two sound sources and calculate the required EQ
settings, which, when applied to the second sound source, makes its profile in the Mel
spectrum match that of the first.

%prep
%autosetup -n MelMatchEQ.lv2-%{version}

sed -i -e "s/INSTALL_DIR =/INSTALL_DIR ?=/g" Makefile

%build

%set_build_flags

%make_build INSTALL_DIR=%{_libdir}/lv2 STRIP=true

%install

%make_install INSTALL_DIR=%{_libdir}/lv2 STRIP=true

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Mon Jan 01 2024 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial build
