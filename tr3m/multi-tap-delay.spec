# Status: active
# Tag: Jack, Effect, Compressor, Delay
# Type: Plugin, Standalone, VST3
# Category: Effect, Audio

%global commit0 7d85a107621aa62dcbaf763a9ec327a1c17139d8

Name: multi-tap-delay
Version: 0.0.1
Release: 1%{?dist}
Summary: A digital delay VST plugin that utilizes four delay lines to create a rhythmic pattern with the repeats
License: GPL-3.0-or-later
URL: https://github.com/Tr3m/multi-tap-delay
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./tr3m-source.sh <PROJECT> <TAG>
#        ./tr3m-source.sh multi-tap-delay master

Source0: multi-tap-delay.tar.gz
Source1: tr3m-source.sh

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
BuildRequires: soundtouch-devel
BuildRequires: JUCE7

%description
A Multi-Tap delay audio plug-in that utilizes four delay lines to create a rhythmic pattern with the repeats.

%package -n license-%{name}
Summary: License and documentations for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentations for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n multi-tap-delay

sed -i -e "s/PRODUCT_NAME \"Multi-Tap Delay\"/PRODUCT_NAME \"Multi_Tap_Delay\"/g" CMakeLists.txt
sed -i -e "s/add_subdirectory(modules\/soundtouch)/#add_subdirectory(modules\/soundtouch)/g" CMakeLists.txt

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_bindir}/

cp -ra %{__cmake_builddir}/multi_tap_delay_artefacts/Release/Standalone/* %{buildroot}/%{_bindir}/
cp -ra %{__cmake_builddir}/multi_tap_delay_artefacts/Release/VST3/* %{buildroot}/%{_libdir}/vst3/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE.txt

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Mon Sep 16 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
