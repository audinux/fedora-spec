# Tag: Alsa, Jack, Mixer
# Type: Plugin, LV2
# Category: Audio, Tool

Name: balance.lv2
Version: 0.6.10
Release: 1%{?dist}
Summary: Stereo Balance Control
License: GPL-2.0-or-later
URL:     https://github.com/x42/balance.lv2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./x42-source.sh <project> <tag>
# ./x42-source.sh balance.lv2 v0.6.10

Source0: balance.lv2.tar.gz
Source1: x42-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: lv2-devel
BuildRequires: cairo-devel
BuildRequires: pango-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: gnu-free-sans-fonts

Requires: gnu-free-sans-fonts

%description
balance.lv2 is an audio-plugin for stereo balance control with
optional per channel delay.

balance.lv2 facilitates adjusting stereo-microphone recordings
(X-Y, A-B, ORTF). But it also generally useful as
"Input Channel Conditioner". It allows for attenuating the signal
on one of the channels as well as delaying the signals (move away
from the microphone). To round off the feature-set channels can be
swapped or the signal can be downmixed to mono after the delay.

It features a Phase-Correlation meter as well as peak programme
meters according to IEC 60268-18 (5ms integration, 20dB/1.5 sec
fall-off) for input and output signals.

%prep
%autosetup -n %{name}

%build

%set_build_flags
export OPTIMIZATIONS="$CFLAGS"
%make_build PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 fat1_VERSION=%{version} STRIP=true FONTFILE=/usr/share/fonts/gnu-free/FreeSansBold.ttf

%install

%make_install PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 fat1_VERSION=%{version} STRIP=true FONTFILE=/usr/share/fonts/gnu-free/FreeSansBold.ttf

%files
%doc README.md
%license COPYING
%{_libdir}/lv2/*

%changelog
* Thu May 11 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.10-1
- update to 0.6.10-1

* Thu Nov 03 2022 Yann Collette <ycollette.nospam@free.fr> - 0.6.9-1
- Initial spec file
