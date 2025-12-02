# Status: active
# Tag: Jack, Alsa, Distortion
# Type: Plugin, Standalone, VST3
# Category: Effect

Name: birdhouse
Version: 0.1.2
Release: 1%{?dist}
Summary: An OSC to Midi Bridge
License: GPL-3.0-or-later
URL: https://github.com/madskjeldgaard/Birdhouse
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./birdhouse-source.sh <TAG>
#        ./birdhouse-source.sh v0.1.2

Source0: Birdhouse.tar.gz
Source1: birdhouse-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: gtk3-devel

Requires: licenses-%{name}

%description
With BirdHouse you can receive OSC messages with a DAW or plugin host and
have them converted to MIDI.

The Birdhouse OSC to MIDI plugin is a simple plugin that listens for OSC messages,
processes their data and sends outputs it as MIDI to allow using it in a DAW or
other plugin host environment. Each instance of Birdhouse is able to process a
stream of OSC messages to a MIDI event type, with a visualization of the stream
and the ability to mute/unmute the output data.

The need for this plugin arose from having to make different projects that rely
on OSC communication to generate notes or affect sound parameters.
Often this was solved with middlewares written in one of the common computer
music languages, with varying levels of success and then passed on to different
Digital Audio Workstations with even more varying levels of success.
The thing is, different software process OSC messages with different priority levels.
This can be annoying in interactive art since we sometimes want to blast software
with values from sensors, other software or from wherever, and be able to expect
pretty consistent results. Birdhouse attempts to solve this.

%package -n license-%{name}
Summary:  License and documentation for %{name}
License:  GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: licenses-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPL-3.0-or-later
Requires: licenses-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n Birdhouse

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/BirdHouse_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra %{__cmake_builddir}/BirdHouse_artefacts/CLAP/* %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/BirdHouse_artefacts/Standalone/* %{buildroot}/%{_bindir}/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md manual/birdhouse-manual.pdf
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Mon Dec 01 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.2-1
- Initial spec file
