# Status: active
# Tag: Drum
# Type: Plugin, VST3
# Category: Audio, Sequencer

Name: drumgroovepro
Version: 0.9.6
Release: 1%{?dist}
Summary: A free, open-source MIDI drum groove sequencer
License: GPL-3.0-or-later
URL: https://github.com/InToEtherion/DrumGroovePro
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./drumgroovepro-source.sh <TAG>
#        ./drumgroovepro-source.sh v0.9.6

Source0: DrumGroovePro.tar.gz
Source1: drumgroovepro-source.sh

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
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel

%description
A VST3 plugin for browsing, arranging, and exporting MIDI drum grooves
with drum library remapping and multi-track timeline capabilities.
DrumGroovePro MIDI drum groove workstation designed for producers, composers, and drummers.
It provides an intuitive interface for browsing your MIDI groove library, dissecting patterns
into individual drum parts (kick, snare, hi-hat, etc.), and arranging them on a multi-track
timeline with per-track BPM control.

Perfect for:
* Quickly auditioning drum grooves at different tempos
* Building complex drum arrangements from individual parts
* Converting grooves between different drum libraries (Superior Drummer, Addictive Drums, EZdrummer, etc.)
* Exporting complete drum arrangements as MIDI files
* Creating custom drum patterns by mixing and matching parts

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n DrumGroovePro

sed -i -e "s|../JUCE juce_build|JUCE juce_build|g" CMakeLists.txt

%build

%set_build_flags
export LDFLAGS="`pkg-config --libs-only-L jack` $LDFLAGS"

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/lib/VST3/* %{buildroot}/%{_libdir}/vst3/

%files -n vst3-%{name}
%doc README.md
%license LICENSE
%{_libdir}/vst3/*

%changelog
* Tue Nov 11 2025 Yann Collette <ycollette.nospam@free.fr> - 0.9.5-1
- Initial spec file
