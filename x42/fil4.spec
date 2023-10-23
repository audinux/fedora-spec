# Tag: Alsa, Jack
# Type: Plugin, LV2
# Category: Audio, Tool

Name:    fil4.lv2
Version: 0.8.8
Release: 1%{?dist}
Summary: 4 Band Parametric EQ
License: GPL-2.0-or-later
URL:     https://github.com/x42/fil4.lv2

Vendor:       Audinux
Distribution: Audinux

# ./x42-source.sh <project> <tag>
# ./x42-source.sh fil4.lv2 v0.8.8

Source0: fil4.lv2.tar.gz
Source1: x42-source.sh

BuildRequires: gcc gcc-c++ make
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: lv2-devel
BuildRequires: cairo-devel
BuildRequires: pango-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: fftw-devel

%description
fil4.lv2 is a 4 band parametric equalizer with additional low+high shelf
filters, Low and High-pass, as well as an optional, custom GUI displaying
the transfer function and realtime signal spectrum or spectrogram.

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
* Fri Sep 15 2023 Yann Collette <ycollette.nospam@free.fr> - 0.8.8-1
- update to 0.8.8-1

* Thu May 11 2023 Yann Collette <ycollette.nospam@free.fr> - 0.8.7-1
- update to 0.8.7-1

* Wed Mar 15 2023 Yann Collette <ycollette.nospam@free.fr> - 0.8.6-1
- update to 0.8.6-1

* Sun Nov 20 2022 Yann Collette <ycollette.nospam@free.fr> - 0.8.5-1
- update to 0.8.5-1

* Tue Nov 01 2022 Yann Collette <ycollette.nospam@free.fr> - 0.4.4-1
- Initial spec file
