# Status: active
# Tag: Drum
# Type: Plugin, VST3
# Category: Audio, Sequencer

Name: drumcraker
Version: 1.2.2
Release: 1%{?dist}
Summary: Free drum sampler VST3 plugin optimized for Linux and PipeWire, fully compatible with DrumGizmo drum kits
License: MIT
URL: https://github.com/Wamphyre/DrumCraker
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./drumcraker-source.sh <TAG>
#        ./drumcraker-source.sh v1.2.2

Source0: DrumCraker.tar.gz
Source1: drumcraker-source.sh

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
DrumCraker is a free drum sampler VST3 plugin optimized for Linux and PipeWire,
fully compatible with DrumGizmo drum kits. Designed for low-latency performance
and realistic drum sound reproduction.

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: MIT
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n DrumCraker

sed -i -e "/CMAKE_CXX_FLAGS_RELEASE/d" CMakeLists.txt

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/

cp -ra %{__cmake_builddir}/DrumCrakerVST_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

mkdir -p %{buildroot}/%{_libdir}/vst3/DrumCraker.vst3/Contents/Resources/
cp assets/background.png %{buildroot}/%{_libdir}/vst3/DrumCraker.vst3/Contents/Resources/

%files -n vst3-%{name}
%doc README.md
%license LICENSE
%{_libdir}/vst3/*

%changelog
* Sun Nov 30 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.2-1
- update to 1.2.2-1

* Sun Nov 16 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.1-1
- update to 1.2.1-1

* Wed Nov 12 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-1
- Initial spec file
