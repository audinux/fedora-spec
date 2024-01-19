# Tag: Alsa, Jack, Compressor
# Type: Plugin, LV2
# Category: Audio, Tool

Name: dpl.lv2
Version: 0.6.6
Release: 1%{?dist}
Summary: Digital Peak Limiter LV2 Plugin
License: GPL-2.0-or-later
URL: https://github.com/x42/dpl.lv2

Vendor:       Audinux
Distribution: Audinux

# ./x42-source.sh <project> <tag>
# ./x42-source.sh dpl.lv2 v0.6.6

Source0: dpl.lv2.tar.gz
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
BuildRequires: pango-devel
BuildRequires: cairo-devel

%description
dpl.lv2 is a look-ahead digital peak limiter intended but not
limited to the final step of mastering or mixing.

%prep
%autosetup -n %{name}

%build

%set_build_flags
export OPTIMIZATIONS="$CFLAGS"
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
* Fri Sep 15 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.6-1
- update to 0.6.6-1

* Thu May 11 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.5-1
- update to 0.6.5-1

* Wed Mar 15 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.4-1
- update to 0.6.4-1

* Sun Nov 20 2022 Yann Collette <ycollette.nospam@free.fr> - 0.6.3-1
- update to 0.6.3-1

* Thu Nov 03 2022 Yann Collette <ycollette.nospam@free.fr> - 0.6.2-1
- Initial spec file
