# Status: active
# Tag: Alsa, Jack, Pitch
# Type: Plugin, LV2
# Category: Audio, Tool

Name: fat1.lv2
Version: 0.8.8
Release: 1%{?dist}
Summary: Fons Adriaensen's AT1 -- Autotune LV2 plugin
License: GPL-2.0-or-later
URL: https://github.com/x42/fat1.lv2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./x42-source.sh <project> <tag>
# ./x42-source.sh fat1.lv2 v0.8.8

Source0: fat1.lv2.tar.gz
Source1: x42-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: lv2-devel
BuildRequires: cairo-devel
BuildRequires: pango-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: fftw-devel

%description
Fons Adriaensen's AT1 -- Autotune LV2 plugin

%prep
%autosetup -n %{name}

%build

%set_build_flags
%make_build PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 fat1_VERSION=%{version} STRIP=true

%install

%make_install PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 fat1_VERSION=%{version} STRIP=true

%files
%doc README.md
%license COPYING
%{_bindir}/*
%{_libdir}/lv2/*
%{_datadir}/*

%changelog
* Tue Jun 11 2024 Yann Collette <ycollette.nospam@free.fr> - 0.8.8-1
- update to 0.8.8-1

* Fri Sep 15 2023 Yann Collette <ycollette.nospam@free.fr> - 0.8.7-1
- update to 0.8.7-1

* Sun Jul 02 2023 Yann Collette <ycollette.nospam@free.fr> - 0.8.6-1
- update to 0.8.6-1

* Thu May 11 2023 Yann Collette <ycollette.nospam@free.fr> - 0.8.5-1
- update to 0.8.5-1

* Wed Mar 15 2023 Yann Collette <ycollette.nospam@free.fr> - 0.8.4-1
- update to 0.8.4-1

* Sun Nov 20 2022 Yann Collette <ycollette.nospam@free.fr> - 0.8.3-1
- update to 0.8.3-1

* Thu Oct 06 2022 Yann Collette <ycollette.nospam@free.fr> - 0.8.1-1
- update to 0.8.1-1

* Thu Jan 30 2020 Yann Collette <ycollette.nospam@free.fr> - 0.7.0-1
- Initial spec file
