# Status: active
# Tag: Effect, Chorus
# Type: Plugin, VST3
# Category: Effect

%global commit0 ea49b7599fd96cc7a831ffc6081aadeca435ff7d

Name: delirion
Version: 0.0.1
Release: 1%{?dist}
Summary: A multiband Doppler-based chorusing/detune effect
License: GPL-3.0-or-later
URL: https://github.com/igorski/delirion
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./delirion-source.sh <TAG>
#        ./delirion-source.sh master

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
BuildRequires: webkit2gtk3-devel

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
* Mon Sep 02 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
