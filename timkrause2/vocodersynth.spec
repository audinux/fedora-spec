# Status: active
# Tag: Vocoder
# Type: Plugin, LV2
# Category: Audio, Synthesizer, Effect

%global commit0 02017873c8fc8b2b741857a493e5ba6b24708806

Name: vocodersynth
Version: 0.0.1
Release: 1%{?dist}
Summary: Linear Predictive Coding based vocoder, voice controlled and midi controlled impulse generators.
License: GPL-3.0-or-later
URL: https://github.com/TimKrause2/VocoderSynth
ExclusiveArch: x86_64

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./timkrause2-source.sh <project> <tag>
# ./timkrause2-source.sh VocoderSynth main

Source0: VocoderSynth.tar.gz
Source1: timkrause2-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: ncurses
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: libsigc++20-devel

%description
VocoderSynth LV2 plugin is a Linear Predictive Coding based vocoder
with 3 selectable inputs: raw audio, a voice controlled impulse and
noise generator and a MIDI controlled synth of impulse generators.

%prep
%autosetup -n VocoderSynth

%build

%set_build_flags

%make_build STRIP=true

%install

%make_install STRIP=true

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -ra VocoderSynth.lv2 %{buildroot}/%{_libdir}/lv2/

%files
%doc README.md
%license COPYING
%{_libdir}/lv2/*

%changelog
* Fri Dec 05 2025 Yann Collette <ycollette.nospam@free.fr> - 0.6.0-1
- Initial spec file
