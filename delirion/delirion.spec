# Status: active
# Tag: Effect, Chorus
# Type: Plugin, VST3
# Category: Effect

%global commit0 947d5ba328094984c2259e3c1f6772af0ade7f0d

Name: delirion
Version: 1.1.0
Release: 1%{?dist}
Summary: A multiband Doppler-based chorusing/detune effect
License: GPL-3.0-or-later
URL: https://github.com/igorski/delirion
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./delirion-source.sh <TAG>
#        ./delirion-source.sh maste

Source0: delirion.tar.gz
Source1: delirion-source.sh

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
A VST audio plugin that is a multi-band doppler shifter with band
specific distortion and reverberation effects.
The less scientific and more romantic definition is that it makes
any incoming audio sound like remembered in a fever dream.

Delirion was built using the JUCE framework.

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n delirion

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/delirion_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

%files -n vst3-%{name}
%doc README.md
%license LICENSE
%{_libdir}/vst3/*

%changelog
* Sun Oct 12 2025 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- update to 1.1.0-1

* Mon Sep 02 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
