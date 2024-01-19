# Tag: Synthesizer, MIDI, Audio
# Type: Plugin, LV2, VST3
# Category: Audio, Synthesizer

%define commit0 9cf668333ebffdb2b2d3d20b76abd433610c2cfc

Name: peaksynth-audio-plugin
Version: 0.0.1
Release: 1%{?dist}
Summary: MIDI controlled synth that uses filter peaks to create tonal spikes in an audio file
License: GPLv3
URL: https://github.com/owennjpr/PeakSynth-Audio-Plugin

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/owennjpr/PeakSynth-Audio-Plugin/archive/%{commit0}.zip#/%{name}-%{commit0}.zip
Source1: JuceBuild.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: JUCE
BuildRequires: fftw-devel
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel

%description
PeakSynth is a mix between a synthesizer and a sampler that instead of oscillators
which sound from scratch, uses IIR filtering to "play" an audio file with midi.
User Midi input is converted into a series of peak filters at frequencies
corresponding to the notes being played. Depending on the character of the audio
file being used, this can lead to lots of interesting outcomes. While this plugin
is intended to be used for the most part with atonal audio like percussion or ambient
noise, (rain sounds, footsteps, wind, etc.) but any kind of audio input can generate
some interesting results. This plugin is early in development and therefore may
have some bugs or issues.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n PeakSynth-Audio-Plugin-%{commit0}

cd PeakSynth
tar xvfz %{SOURCE1}

%build

cd PeakSynth/Builds/LinuxMakefile

%make_build DEPFLAGS=-I/usr/include/JUCE-7.0.7/modules/

%install

install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_libdir}/vst3/

cp -ra PeakSynth/Builds/LinuxMakefile/build/PeakSynth.vst3 %{buildroot}/%{_libdir}/vst3/
cp -ra PeakSynth/Builds/LinuxMakefile/build/PeakSynth.lv2 %{buildroot}/%{_libdir}/lv2/

%files
%doc README.md
%license LICENSE

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Tue Oct 31 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file - 9cf668333ebffdb2b2d3d20b76abd433610c2cfc
