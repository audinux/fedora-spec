%global debug_package %{nil}

# Tag: Jack, MIDI, Sfz, Sf2, Sf3, OSC
# Type: Standalone
# Category: Audio, Tool

Name:    Carla
Version: 2.2.0
Release: 6%{?dist}
Summary: A rack manager JACK
License: GPLv2+
URL:     https://github.com/falkTX/Carla

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/falkTX/Carla/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: carla-change-lib.sh
Source2: carla-change-py.sh

BuildRequires: gcc gcc-c++ make
BuildRequires: python-qt5-devel
BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: gtk2-devel
BuildRequires: gtk3-devel
BuildRequires: qt-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: fluidsynth-devel
BuildRequires: fftw-devel
BuildRequires: mxml-devel
BuildRequires: zlib-devel
BuildRequires: mesa-libGL-devel
BuildRequires: non-ntk-fluid
BuildRequires: non-ntk-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: linuxsampler-devel

Requires(pre): python3-qt5

%description
A fully-featured audio plugin host, with support for many audio drivers and plugin formats.
- LADSPA, DSSI, LV2 and VST2, VST3 and AU plugin formats
- SF2/3 and SFZ sound banks
- Internal audio and midi file player
- Automation of plugin parameters via MIDI CC
- Remote control over OSC
- Rack and Patchbay processing modes, plus Single and Multi-Client if using JACK
- Native audio drivers (ALSA, DirectSound, CoreAudio, etc) and JACK


%prep
%autosetup -n %{name}-%{version}

%ifarch x86_64 amd64
%{SOURCE1}
%endif
%{SOURCE2}

%build
%make_build PREFIX=/usr LIBDIR=%{_libdir}

%install 
%make_install PREFIX=/usr LIBDIR=%{_libdir}

# Create a vst directory
install -m 755 -d %{buildroot}/%{_libdir}/vst/

%files
%{_bindir}/*
%{_includedir}/carla/*
%{_libdir}/carla/*
%{_libdir}/lv2/*
%{_libdir}/pkgconfig/*
%{_libdir}/vst/
%{_datadir}/applications/*
%{_datadir}/carla/*
%{_datadir}/icons/*
%{_datadir}/mime/*

%changelog
* Sun Oct 25 2020 Yann Collette <ycollette.nospam@free.fr> - 2.2.0-6
- update to 2.2.0-6

* Thu Apr 16 2020 Yann Collette <ycollette.nospam@free.fr> - 2.1.0-6
- update to 2.1.0-6

* Sat Mar 30 2019 Yann Collette <ycollette.nospam@free.fr> - 2.0.0-6
- update to 2.0.0-6

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 2.0.0beta-5
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 2.0.0beta-5
- update to latest master

* Tue May 1 2018 Yann Collette <ycollette.nospam@free.fr> - 2.0.0beta-4
- version 4
- update default folders
- update to master

* Wed Nov 22 2017 Yann Collette <ycollette.nospam@free.fr> - 2.0.0beta
- add a missing requires

* Mon Oct 23 2017 Yann Collette <ycollette.nospam@free.fr> - 2.0.0beta
- update to latest master

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 2.0.0beta
- Initial build
