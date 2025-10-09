# Status: active
# Tag: MIDI, Tool
# Type: Standalone, Plugin, VST3
# Category: MIDI, Tool

%global debug_package %{nil}
%global commit0 74c7830f5763bed01e9a7c4955f0d894ee8412f5

Name: midi-monitor
Version: 30072020
Release: 2%{?dist}
Summary: A JUCE-based midi monitor
License: GPL-2.0-or-later
URL: https://github.com/surge-synthesizer/midi-monitor
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# To get the sources, use:
# $ ./source-midi-monitor.sh 74c7830f5763bed01e9a7c4955f0d894ee8412f5

Source0: midi-monitor.tar.gz
Source1: source-midi-monitor.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: rsync
BuildRequires: git
BuildRequires: python3
BuildRequires: alsa-lib-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libcurl-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: pkgconfig(jack)

%description
A JUCE-based midi monitor

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n %{name}

# Fix build of juceaide on f36
sed -i -e "s/\"-DJUCE_BUILD_HELPER_TOOLS=ON\"/\"-DJUCE_BUILD_HELPER_TOOLS=ON\" \"-DCMAKE_CXX_FLAGS='-include utility -fPIC'\"/g" lib/JUCE/extras/Build/juceaide/CMakeLists.txt
#sed -i -e "/OUTPUT_VARIABLE/d" lib/JUCE/extras/Build/juceaide/CMakeLists.txt
#sed -i -e "s/--config Debug/--config Debug --verbose/g" lib/JUCE/extras/Build/juceaide/CMakeLists.txt

%build

%set_build_flags

export CXXFLAGS="-include utility $CXXFLAGS"

%cmake
%cmake_build

%install

export HOME=`pwd`
mkdir .vst3

install -m 755 -d %{buildroot}%{_bindir}/
cp -r %{__cmake_builddir}/midi-monitor_artefacts/Standalone/* %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}%{_libdir}/vst3/MidiMonitor.vst3/
cp -r %{__cmake_builddir}/midi-monitor_artefacts/VST3/MidiMonitor.vst3/* %{buildroot}/%{_libdir}/vst3/MidiMonitor.vst3/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Sat Sep 07 2024 Yann Collette <ycollette.nospam@free.fr> - 30072020-2
- update to last master - 74c7830f5763bed01e9a7c4955f0d894ee8412f5

* Sun Dec 26 2021 Yann Collette <ycollette.nospam@free.fr> - 30072020-1
- Initial spec file
