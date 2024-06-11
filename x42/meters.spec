# Tag: Alsa, Jack, Analyzer, Graphic
# Type: Plugin, LV2, Standalone
# Category: Audio, Tool

Name: meters.lv2
Version: 0.9.26
Release: 1%{?dist}
Summary: collection of LV2 plugins for audio-level metering
License: GPL-2.0-or-later
URL: https://github.com/x42/meters.lv2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./x42-source.sh <project> <tag>
# ./x42-source.sh meters.lv2 v0.9.26

Source0: meters.lv2.tar.gz
Source1: x42-source.sh

BuildRequires: gcc gcc-c++ make
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
meters.lv2 is a collection of audio-level meters with GUI in LV2 plugin format.

It includes needle style meters (mono and stereo variants)
 - IEC 60268-10 Type I / DIN
 - IEC 60268-10 Type I / Nordic
 - IEC 60268-10 Type IIa / BBC
 - IEC 60268-10 Type IIb / EBU
 - IEC 60268-17 / VU

Stereo & Mono variants of bar-graph meters:
 - 30 Band 1/3 octave spectrum analyzer IEC 61260
 - Digital True-Peak Meter (4x Oversampling), Type II rise-time, 13.3dB/s falloff.
 - True-Peak (4x Oversampling) + RMS (600ms integration time) combined with numeric readout
 - K-12, K-14, K-20 / RMS type K-Meters according to the K-system introduced by Bob Katz
 - DR-14 (crest factor / loudness range measurement method)

and the following stereo plugins:
 - EBU R128 Meter with Histogram and History
 - Stereo Phase Correlation Meter (Needle Display)
 - BBC Mid/Side M-6 (Needle Display)
 - Goniometer (Stereo Phase Scope)
 - Phase/Frequency Wheel
 - Stereo/Frequency Monitor

as well as a mono:
 - Signal Distribution Histogram
 - Bitmeter

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
* Tue Jun 11 2024 Yann Collette <ycollette.nospam@free.fr> - 0.9.26-1
- update to 0.9.26-1

* Thu May 11 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.25-1
- update to 0.9.25-1

* Wed Mar 15 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.24-1
- update to 0.9.24-1

* Thu Nov 03 2022 Yann Collette <ycollette.nospam@free.fr> - 0.9.23-1
- Initial spec file
