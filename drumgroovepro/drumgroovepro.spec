# Status: active
# Tag: Drum
# Type: Plugin, VST3
# Category: Audio, Sequencer

Name: drumgroovepro
Version: 0.9.9
Release: 1%{?dist}
Summary: A free, open-source MIDI drum groove sequencer
License: GPL-3.0-or-later
URL: https://github.com/InToEtherion/DrumGroovePro
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./drumgroovepro-source.sh <TAG>
#        ./drumgroovepro-source.sh V0.9.9

Source0: DrumGroovePro.tar.gz
Source1: drumgroovepro-source.sh
Patch0: drumgroovepro-0001-remove-cmake-flags.patch

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

Requires: license-%{name}

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

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -p1 -n DrumGroovePro

sed -i -e "s|../JUCE juce_build|JUCE juce_build|g" CMakeLists.txt

%build

export HOME=`pwd`

%set_build_flags
export LDFLAGS="`pkg-config --libs-only-L jack` $LDFLAGS"

%cmake
%cmake_build

%install

export HOME=`pwd`

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra .vst3/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/DrumGroovePro_artefacts/Standalone/* %{buildroot}/%{_bindir}/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Fri Nov 28 2025 Yann Collette <ycollette.nospam@free.fr> - 0.9.9-1
- update to 0.9.9-1

* Fri Nov 21 2025 Yann Collette <ycollette.nospam@free.fr> - 0.9.8-1
- update to 0.9.8-1

* Sun Nov 16 2025 Yann Collette <ycollette.nospam@free.fr> - 0.9.7-1
- update to 0.9.7-1

* Tue Nov 11 2025 Yann Collette <ycollette.nospam@free.fr> - 0.9.5-1
- Initial spec file
