# Tag: Effect
# Type: Plugin, VST3
# Category: Effect, Distortion

Name: gnomedistort2
Version: 1.0.0
Release: 1%{?dist}
Summary: Weird & brutal distortion plugin
License: GPL-3.0-or-later
URL: https://github.com/crowbait/GnomeDistort-2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./gnomedistort-source.sh <TAG>
#        ./gnomedistort-source.sh 5cda11dc5be802ee097cce2c3e34fab8796f1112

Source0: GnomeDistort-2.tar.gz
Source1: gnomedistort-source.sh

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
Brutal multi-band distortion plugin with unique functions:
* Global low- and high-cut filters with variable slopes
* 3 frequency bands (possible ranges: 20-999Hz, 20Hz-20kHz, 1-20kHz)
* Per band:
  * Peak filter with high gain range
  * very high range input gain
  * Unique SMEAR (just try it)
  * "Somewhat tame-ish" to "brutally destructive" waveshaper options
  * Output gain meant for reduction
* Global post-stage waveshaper (same options as in bands)
* Themes!

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n GnomeDistort-2

sed -i -e "s/GnomeDistort 2/GnomeDistort_2/g" CMakeLists.txt

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/GnomeDistort2_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

%files -n vst3-%{name}
%doc README.md
%license LICENSE.md
%{_libdir}/vst3/*

%changelog
* Sat Jul 06 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
