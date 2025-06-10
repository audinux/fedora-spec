# Status: active
# Tag: Synthesizer
# Type: Plugin, VST3, Standalone
# Category: Synthesizer

Name: boris-granular-station
Version: 0.0.1
Release: 1%{?dist}
Summary: A live-input granular plugin
License: GPL-2.0-or-later
URL: https://github.com/glesdora/boris-granular-station
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./boris-granular-station-source.sh <tag>
#        ./boris-granular-station-source.sh master

Source0: boris-granular-station.tar.gz
Source1: boris-granular-station-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: rsync
BuildRequires: git
BuildRequires: python3
BuildRequires: alsa-lib-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel
BuildRequires: freetype-devel
BuildRequires: libcurl-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel
BuildRequires: pkgconfig(jack)
BuildRequires: desktop-file-utils

%description
BORIS Granular Station is a lightweight real-time granulator for live audio input.
It lets you zoom in on the details of sound and explore its temporal dimension as it flows.
BORIS is fast and precise: it's always sample-accurate and adds no extra latency to your FX chain.
Features:
- Granulize incoming audio in real time, with latency minimized based on grain length and pitch shift (often 0 samps!)
- Use the interactive pad on the waveform to set the grain position (x-axis) and its random drift (y-axis)
- Shift the pitch of the grains with a resolution of 1/4th of a semitone
- Use the custom envelope control to smoothly morph between different shapes
- Freeze the incoming audio at any time
- Play with feedback, but be warned: since the granuator output can vary drastically, results may be unpredictable :)

%package -n license-%{name}
Summary:  License and documentation for %{name}
License:  GPL-2.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n boris-granular-station

sed -i -e "s|PRODUCT_NAME \"Boris Granular Station\"|PRODUCT_NAME \"Boris_Granular_Station\"|g" App.cmake

%build

%set_build_flags

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/BorisGranularPlugin_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/BorisGranularStation_artefacts/Boris_Granular_Station  %{buildroot}/%{_bindir}/

%files
%{_bindir}/*

%files -n license-%{name}
%doc readme.md

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Mon Jun 09 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
