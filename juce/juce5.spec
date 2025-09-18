# Status: active
# Tag: Library, Editor
# Type: Standalone, IDE, Language
# Category: Audio, Programming, Graphic

Name: JUCE5
Version: 5.4.7
Release: 3%{?dist}
Summary: JUCE Framework version 5
URL: https://github.com/juce-framework/JUCE
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

# original tarfile can be found here:
Source0: https://github.com/juce-framework/JUCE/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:  juce5-0001-set-default-path.patch
Patch1:  juce5-0002-fix-curl-API.patch

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: dssi-devel
BuildRequires: ladspa-devel
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: python3
BuildRequires: libcurl-devel
BuildRequires: gtk3-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: mesa-libGL-devel
BuildRequires: webkit2gtk4.1-devel

%description
JUCE is an open-source cross-platform C++ application framework used for rapidly
developing high quality desktop and mobile applications, including VST, AU (and AUv3),
RTAS and AAX audio plug-ins. JUCE can be easily integrated with existing projects or can
be used as a project generation tool via the [Projucer](https://juce.com/discover/projucer),
which supports exporting projects for Xcode (macOS and iOS), Visual Studio, Android Studio,
Code::Blocks, CLion and Linux Makefiles as well as containing a source code editor and
live-coding engine which can be used for rapid prototyping.

%prep
%autosetup -p1 -n JUCE-%{version}

sed -i -e "s/python/python3/g" doxygen/Makefile

find extras -name Makefile -exec sed -i -e "s/webkit2gtk-4.0/webkit2gtk-4.1/g" {} \; -print

%build

%set_build_flags

export CXXFLAGS="-DJUCER_ENABLE_GPL_MODE -O0 -fPIE -g -include array $CXXFLAGS"
export CFLAGS="-DJUCER_ENABLE_GPL_MODE -O0 -fPIE -g $CFLAGS"

cd doxygen
mkdir build
%make_build CONFIG=Release STRIP=true DEPFLAGS="$CXXFLAGS"
cd ../extras

cd AudioPluginHost/Builds/LinuxMakefile/
%make_build CONFIG=Release STRIP=true DEPFLAGS="$CXXFLAGS"
cd ../../..

cd BinaryBuilder/Builds/LinuxMakefile/
%make_build CONFIG=Release STRIP=true DEPFLAGS="$CXXFLAGS"
cd ../../..

cd Projucer/Builds/LinuxMakefile/
%make_build CONFIG=Release STRIP=true DEPFLAGS="$CXXFLAGS"
cd ../../..

cd UnitTestRunner/Builds/LinuxMakefile/
%make_build CONFIG=Release STRIP=true DEPFLAGS="$CXXFLAGS"
cd ../../..

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 extras/AudioPluginHost/Builds/LinuxMakefile/build/AudioPluginHost %{buildroot}%{_bindir}/AudioPluginHost5
install -m 755 extras/BinaryBuilder/Builds/LinuxMakefile/build/BinaryBuilder     %{buildroot}%{_bindir}/BinaryBuilder5
install -m 755 extras/Projucer/Builds/LinuxMakefile/build/Projucer               %{buildroot}%{_bindir}/Projucer5
install -m 755 extras/UnitTestRunner/Builds/LinuxMakefile/build/UnitTestRunner   %{buildroot}%{_bindir}/UnitTestRunner5

install -m 755 -d %{buildroot}/%{_usrsrc}/JUCE5/
install -m 755 -d %{buildroot}/%{_usrsrc}/JUCE5/examples/
cp -ra examples/* %{buildroot}/%{_usrsrc}/JUCE5/examples/
install -m 755 -d %{buildroot}/%{_usrsrc}/JUCE5/modules/
cp -ra modules/*  %{buildroot}/%{_usrsrc}/JUCE5/modules/

install -m 755 -d    %{buildroot}/%{_datadir}/JUCE5/doc/
cp -ra doxygen/doc/* %{buildroot}/%{_datadir}/JUCE5/doc/

%files
%doc README.md
%license LICENSE.md
%{_bindir}/*
%{_datadir}/*
%{_usrsrc}/*

%changelog
* Wed Sep 17 2025 Yann Collette <ycollette.nospam@free.fr> - 5.4.7-3
- update to 5.4.7-3 - remove unused dep

* Tue Jun 01 2021 Yann Collette <ycollette.nospam@free.fr> - 5.4.7-2
- fix crash at startup

* Sun Mar 21 2021 Yann Collette <ycollette.nospam@free.fr> - 5.4.7-1
- initial spec - update to 5.4.7
