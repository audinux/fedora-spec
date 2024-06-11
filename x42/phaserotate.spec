# Tag: Audio, Effect
# Type: Plugin, LV2, Standalone
# Category: Audio, Effect

Name: phaserotate.lv2
Version: 0.6.6
Release: 1%{?dist}
Summary: Phase Rotation LV2 plugin
License: GPL-2.0-or-later
URL: https://github.com/x42/phaserotate.lv2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./x42-source.sh <project> <tag>
# ./x42-source.sh phaserotate.lv2 v0.6.6

Source0: phaserotate.lv2.tar.gz
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
phaserotate.lv2 is an audio phase rotation plugin

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
* Tue Jun 11 2024 Yann Collette <ycollette.nospam@free.fr> - 0.6.6-1
- update to 0.6.6-1

* Fri Sep 15 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.5-1
- update to 0.6.5-1

* Thu May 11 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.4-1
- update to 0.6.4-1

* Wed Mar 15 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.3-1
- update to 0.6.3-1

* Sun Nov 20 2022 Yann Collette <ycollette.nospam@free.fr> - 0.6.2-1
- update to 0.6.2-1

* Wed Nov 02 2022 Yann Collette <ycollette.nospam@free.fr> - 0.6.1-1
- Initial spec file
