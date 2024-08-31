# Status: active
# Tag: Alsa, Jack, Effect, Compressor
# Type: Standalone, Plugin, LV2
# Category: Audio, Tool

Name: darc.lv2
Version: 0.7.0
Release: 1%{?dist}
Summary: Dynamic Audio Range Compressor
License: GPL-2.0-or-later
URL: https://github.com/x42/darc.lv2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./x42-source.sh <project> <tag>
# ./x42-source.sh darc.lv2 v0.7.0

Source0: darc.lv2.tar.gz
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
darc.lv2 is a general purpose audio signal compressor.

The compression gain is controlled by threshold and ratio only:
Makeup gain is automatically set to retain equal loudness at -10 dBFS/RMS
with a soft knee. This maintains perceived loudness over a wide range of
thresholds and ratio settings.

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
* Tue Jun 11 2024 Yann Collette <ycollette.nospam@free.fr> - 0.7.0-1
- update to 0.7.0-1

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
