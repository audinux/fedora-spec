# Tag: Library, Editor
# Type: Standalone, IDE, Language
# Category: Audio, Programming, Graphic

Name: JUCE60
Version: 6.0.8
Release: 5%{?dist}
Summary: JUCE Framework
URL: https://github.com/juce-framework/JUCE
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

# original tarfile can be found here:
Source0: https://github.com/juce-framework/JUCE/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:  juce60-0001-set-default-path.patch

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: dssi-devel
BuildRequires: ladspa-devel
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: python-unversioned-command
BuildRequires: webkit2gtk3-devel
BuildRequires: libcurl-devel

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
export CXXFLAGS="-DJUCER_ENABLE_GPL_MODE -O0 -fPIE -g"
export CFLAGS="-DJUCER_ENABLE_GPL_MODE -O0 -fPIE -g"

cd docs/doxygen
sed -i -e "s/python/python2/g" Makefile

mkdir build
%make_build CONFIG=Release STRIP=true
cd ../../extras

cd AudioPluginHost/Builds/LinuxMakefile/
%make_build CONFIG=Release STRIP=true
cd ../../..

cd BinaryBuilder/Builds/LinuxMakefile/
%make_build CONFIG=Release STRIP=true
cd ../../..

cd Projucer/Builds/LinuxMakefile/
%make_build CONFIG=Release STRIP=true
cd ../../..

cd UnitTestRunner/Builds/LinuxMakefile/
%make_build CONFIG=Release STRIP=true
cd ../../..

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 extras/AudioPluginHost/Builds/LinuxMakefile/build/AudioPluginHost %{buildroot}%{_bindir}/AudioPluginHost60
install -m 755 extras/BinaryBuilder/Builds/LinuxMakefile/build/BinaryBuilder     %{buildroot}%{_bindir}/BinaryBuilder60
install -m 755 extras/Projucer/Builds/LinuxMakefile/build/Projucer               %{buildroot}%{_bindir}/Projucer60
install -m 755 extras/UnitTestRunner/Builds/LinuxMakefile/build/UnitTestRunner   %{buildroot}%{_bindir}/UnitTestRunner60

install -m 755 -d %{buildroot}/%{_usrsrc}/JUCE60/
install -m 755 -d %{buildroot}/%{_usrsrc}/JUCE60/examples/
cp -ra examples/* %{buildroot}/%{_usrsrc}/JUCE60/examples/
install -m 755 -d %{buildroot}/%{_usrsrc}/JUCE60/modules/
cp -ra modules/*  %{buildroot}/%{_usrsrc}/JUCE60/modules/

install -m 755 -d         %{buildroot}/%{_datadir}/JUCE60/doc/
cp -ra docs/doxygen/doc/* %{buildroot}/%{_datadir}/JUCE60/doc/

%files
%doc README.md
%license LICENSE.md
%{_bindir}/*
%{_datadir}/*
%{_usrsrc}/*

%changelog
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
