# Tag: Jack, Alsa
# Type: Plugin, Application, LV2
# Category: Audio, Synthetizer

%global commit0 abdedd527e6e1cf86636f0f1e8a3e75b06ed166a
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    helm
Version: 1.0.0.%{shortcommit0}
Release: 5%{?dist}
Summary: A LV2 / Standalone polyphonic synth with lots of modulation
License: GPLv2+
URL:     https://github.com/mtytel/helm

Source0: https://github.com/mtytel/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1: helm.appdata.xml

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: mesa-libGL-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: freetype-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: libappstream-glib

%description
A free polyphonic synth with lots of modulation.
Features:
* 32 voice polyphony
* Interactive visual interface
* Powerful modulation system with live visual feedback
* Dual oscillators with cross modulation and up to 15 unison oscillators each
* Sub oscillator with shuffle waveshaping
* Oscillator feedback and saturation for waveshaping
* 12 different waveforms
* Blending between 12 or 24dB low/band/high pass filter
* Low/Band/High Shelf filters
* 2 monophonic and 1 polyphonic LFO
* Step sequencer
* Lots of modulation sources including polyphonic aftertouch
* Simple arpeggiator
* Effects: Formant filter, stutter, delay, distortion, reverb

%prep
%autosetup -n %{name}-%{commit0}

# For Fedora 29
%if 0%{?fedora} >= 29
  sed -i -e "114,125d" JUCE/modules/juce_graphics/colour/juce_PixelFormats.h
%endif

sed -i "s/\/lib\//\/lib64\//g" Makefile

%build

%set_build_flags
%make_build STRIP=true standalone lv2

%install

%make_install STRIP=true standalone lv2

# install appdata file
install -Dp -m 644 %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files
%doc changelog README.md
%license COPYING
%{_bindir}/*
%{_libdir}/lv2/*
%{_libdir}/lxvst/*
%{_datadir}/helm/*
%{_datadir}/doc/helm/*
%{_mandir}/man1/helm.1.gz
%{_datadir}/applications/helm.desktop
%{_datadir}/icons/hicolor/*
%{_metainfodir}/%{name}.appdata.xml

%changelog
* Sat May 22 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta-5
- update spec

* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta-4
- fix debug build

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta-3
- update for Fedora 29

* Sat Aug 11 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta-3
- update to abdedd527e6e1cf86636f0f1e8a3e75b06ed166a

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta-2
- update to 756e767e4d20e77836f45b4ba016ea547d7cf474 

* Mon Oct 23 2017 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta-1
- update to latest master

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta
- Initial build
