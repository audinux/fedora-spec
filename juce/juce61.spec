# Status: active
# Tag: Library, Editor
# Type: Standalone, IDE, Language
# Category: Audio, Programming, Graphic

Name: JUCE61
Version: 6.1.6
Release: 7%{?dist}
Summary: JUCE Framework
URL: https://github.com/juce-framework/JUCE
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

# original tarfile can be found here:
Source0: https://github.com/juce-framework/JUCE/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:  juce61-0001-set-default-path.patch
Patch1:  juce61-0002-fix-curl-API.patch

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: dssi-devel
BuildRequires: ladspa-devel
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: python-unversioned-command
BuildRequires: libcurl-devel
BuildRequires: gtk3-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: mesa-libGL-devel

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

%build

%set_build_flags

#export CXXFLAGS="-DJUCER_ENABLE_GPL_MODE $CXXFLAGS"
#export CFLAGS="-DJUCER_ENABLE_GPL_MODE $CFLAGS"
export CXXFLAGS="`pkg-config --cflags gtk+-3.0` -DJUCE_WEB_BROWSER=0 -DJUCER_ENABLE_GPL_MODE -O0 -fPIE -g -std=c++14 -include utility $CXXFLAGS"
export CFLAGS="`pkg-config --cflags gtk+-3.0` -DJUCE_WEB_BROWSER=0 -DJUCER_ENABLE_GPL_MODE -O0 -fPIE -g $CFLAGS"

cd docs/doxygen

mkdir build
%make_build CONFIG=Release STRIP=true DEPFLAGS="$CXXFLAGS"
cd ../../extras

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
install -m 755 extras/AudioPluginHost/Builds/LinuxMakefile/build/AudioPluginHost %{buildroot}%{_bindir}/AudioPluginHost61
install -m 755 extras/BinaryBuilder/Builds/LinuxMakefile/build/BinaryBuilder     %{buildroot}%{_bindir}/BinaryBuilder61
install -m 755 extras/Projucer/Builds/LinuxMakefile/build/Projucer               %{buildroot}%{_bindir}/Projucer61
install -m 755 extras/UnitTestRunner/Builds/LinuxMakefile/build/UnitTestRunner   %{buildroot}%{_bindir}/UnitTestRunner61

install -m 755 -d %{buildroot}/%{_usrsrc}/JUCE61/
install -m 755 -d %{buildroot}/%{_usrsrc}/JUCE61/examples/
cp -ra examples/* %{buildroot}/%{_usrsrc}/JUCE61/examples/
install -m 755 -d %{buildroot}/%{_usrsrc}/JUCE61/modules/
cp -ra modules/*  %{buildroot}/%{_usrsrc}/JUCE61/modules/

install -m 755 -d         %{buildroot}/%{_datadir}/JUCE61/doc/
cp -ra docs/doxygen/doc/* %{buildroot}/%{_datadir}/JUCE61/doc/

%files
%doc README.md
%license LICENSE.md
%{_bindir}/*
%{_datadir}/*
%{_usrsrc}/*

%changelog
* Tue Sep 16 2025 Yann Collette <ycollette.nospam@free.fr> - 6.1.6-7
- update to 6.1.6-7 - remove unused dep

* Tue Apr 05 2022 Yann Collette <ycollette.nospam@free.fr> - 6.1.6-6
- update to 6.1.6-6 - fix for Fedora 36

* Mon Feb 28 2022 Yann Collette <ycollette.nospam@free.fr> - 6.1.6-5
- update to 6.1.6-5

* Fri Jan 28 2022 Yann Collette <ycollette.nospam@free.fr> - 6.1.5-5
- update to 6.1.5-5

* Mon Dec 20 2021 Yann Collette <ycollette.nospam@free.fr> - 6.1.4-5
- update to 6.1.4-5

* Wed Dec 08 2021 Yann Collette <ycollette.nospam@free.fr> - 6.1.3-5
- update to 6.1.3-5

* Mon Sep 20 2021 Yann Collette <ycollette.nospam@free.fr> - 6.1.2-5
- update to 6.1.2-5

* Fri Sep 10 2021 Yann Collette <ycollette.nospam@free.fr> - 6.1.1-5
- update to 6.1.1-5

* Mon Aug 23 2021 Yann Collette <ycollette.nospam@free.fr> - 6.1.0-5
- update to 6.1.0-5

* Tue Jun 01 2021 Yann Collette <ycollette.nospam@free.fr> - 6.0.8-5
- fix crash at startup

* Sat Apr 03 2021 Yann Collette <ycollette.nospam@free.fr> - 6.0.8-4
- update to 6.0.8-4

* Thu Jan 14 2021 Yann Collette <ycollette.nospam@free.fr> - 6.0.7-4
- update to 6.0.7-4

* Tue Dec 01 2020 Yann Collette <ycollette.nospam@free.fr> - 6.0.5-4
- update to 6.0.5-4

* Sun Oct 25 2020 Yann Collette <ycollette.nospam@free.fr> - 6.0.4-4
- adjust default paths

* Sat Oct 24 2020 Yann Collette <ycollette.nospam@free.fr> - 6.0.4-3
- update to 6.0.4-3

* Sat Oct 24 2020 Yann Collette <ycollette.nospam@free.fr> - 6.0.1-3
- update to 6.0.1-3

* Mon Feb 10 2020 Yann Collette <ycollette.nospam@free.fr> - 5.4.7-3
- update to 5.4.7

* Tue Feb 4 2020 Yann Collette <ycollette.nospam@free.fr> - 5.4.6-3
- update to 5.4.6

* Fri Oct 18 2019 Yann Collette <ycollette.nospam@free.fr> - 5.4.5-3
- update to 5.4.5

* Thu May 2 2019 Yann Collette <ycollette.nospam@free.fr> - 5.4.4-3
- update to 5.4.4

* Thu May 2 2019 Yann Collette <ycollette.nospam@free.fr> - 5.4.3-3
- Fixes for gcc 9

* Fri Feb 22 2019 Yann Collette <ycollette.nospam@free.fr> - 5.4.3-3
- Switch to 5.4.3

* Fri Feb 8 2019 Yann Collette <ycollette.nospam@free.fr> - 5.4.2-3
- Switch to 5.4.2

* Thu Dec 27 2018 Yann Collette <ycollette.nospam@free.fr> - 5.4.1-3
- activate GPL mode

* Wed Nov 21 2018 Yann Collette <ycollette.nospam@free.fr> - 5.4.1-2
- fix compilation flags

* Mon Nov 12 2018 Yann Collette <ycollette.nospam@free.fr> - 5.4.1-1
- initial specfile
