# Status: active
# Tag: Jack, Effect, AI
# Type: Plugin, Standalone, VST3
# Category: Effect, Audio

%global commit0 fdcfaa57b13e7cfdfb28f77ba4112020557b0d35

Name: nam-juce
Version: 0.4.0
Release: 2%{?dist}
Summary: A JUCE implementation of the Neural Amp Modeler Plugin
License: GPL-3.0-or-later
URL: https://github.com/Tr3m/nam-juce
ExclusiveArch: x86_64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./tr3m-source.sh <PROJECT> <TAG>
#        ./tr3m-source.sh nam-juce v0.4.0

Source0: nam-juce.tar.gz
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

%description
A JUCE implementation of Steven Atkinson's NeuralAmpModelerPlugin.

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
%autosetup -n nam-juce

sed -i -e "s/PRODUCT_NAME \"Neural Amp Modeler\"/PRODUCT_NAME \"Neural_Amp_Modeler\"/g" CMakeLists.txt

#add_subdirectory(Modules/NeuralAmpModelerCore/Dependencies/eigen)
#add_subdirectory(Modules/json)

%build

%cmake -DUSE_NATIVE_ARCH=0
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_bindir}/

cp -ra %{__cmake_builddir}/NEURAL_AMP_MODELER_artefacts/Release/Standalone/* %{buildroot}/%{_bindir}/
cp -ra %{__cmake_builddir}/NEURAL_AMP_MODELER_artefacts/Release/VST3/* %{buildroot}/%{_libdir}/vst3/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE.txt

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Mon Aug 25 2025 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-2
- update to 0.4.0-2 - remove unused dep

* Mon Sep 16 2024 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-1
- Initial spec file
