# Tag: Library, Editor
# Type: Standalone, IDE, Language
# Category: Audio, Programming, Graphic

Name:    JUCE
Version: 7.0.5
Release: 9%{?dist}
Summary: JUCE Framework
URL:     https://github.com/juce-framework/JUCE
License: GPLv2+

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/juce-framework/JUCE/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: juce_Projucer.desktop
Source2: juce_Projucer.1

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: lv2-devel
BuildRequires: dssi-devel
BuildRequires: ladspa-devel
BuildRequires: alsa-lib-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: libcurl-devel
BuildRequires: freetype-devel
BuildRequires: python-unversioned-command
BuildRequires: desktop-file-utils

%description
JUCE is an open-source cross-platform C++ application framework for creating high quality
desktop and mobile applications, including VST, VST3, AU, AUv3, AAX and LV2 audio plug-ins
and plug-in hosts. JUCE can be easily integrated with existing projects via CMake, or can
be used as a project generation tool via the [Projucer](https://juce.com/discover/projucer),
which supports exporting projects for Xcode (macOS and iOS), Visual Studio, Android Studio,
Code::Blocks and Linux Makefiles as well as containing a source code editor.

%prep
%autosetup -p1 -n %{name}-%{version}

%build

cd docs/doxygen
make
cd ../..

%cmake -DJUCE_BUILD_EXTRAS=ON -DJUCE_BUILD_EXAMPLES=OFF -DJUCE_INSTALL_DESTINATION="%{_lib}/cmake/JUCE-%{version}"
%cmake_build

%install

%cmake_install

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/512x512/
install -m 644 examples/Assets/juce_icon.png %{buildroot}/%{_datadir}/icons/hicolor/512x512/

install -m 755 -d %{buildroot}/%{_mandir}/man1/
install -m 644 %{SOURCE2} %{buildroot}/%{_mandir}/man1/

install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/

install -m 755 %{__cmake_builddir}/extras/AudioPluginHost/AudioPluginHost_artefacts/AudioPluginHost %{buildroot}/%{_bindir}
install -m 755 %{__cmake_builddir}/extras/NetworkGraphicsDemo/NetworkGraphicsDemo_artefacts/NetworkGraphicsDemo %{buildroot}/%{_bindir}
install -m 755 %{__cmake_builddir}/extras/BinaryBuilder/BinaryBuilder_artefacts/BinaryBuilder %{buildroot}/%{_bindir}
install -m 755 %{__cmake_builddir}/extras/Projucer/Projucer_artefacts/Projucer %{buildroot}/%{_bindir}
install -m 755 %{__cmake_builddir}/extras/AudioPerformanceTest/AudioPerformanceTest_artefacts/AudioPerformanceTest %{buildroot}/%{_bindir}
install -m 755 %{__cmake_builddir}/extras/UnitTestRunner/UnitTestRunner_artefacts/UnitTestRunner %{buildroot}/%{_bindir}

install -m 755 -d %{buildroot}/%{_datadir}/JUCE-%{version}/doc/
cp -ra docs/doxygen/doc/ %{buildroot}/%{_datadir}/JUCE-%{version}/doc/

desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/*.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.md
%license LICENSE.md 
%{_bindir}/*
%{_datadir}/*
%{_libdir}/cmake/*
%{_includedir}/*

%changelog
* Thu Jan 26 2023 Yann Collette <ycollette.nospam@free.fr> - 7.0.5-9
- update to 7.0.5-9

* Fri Jan 06 2023 Yann Collette <ycollette.nospam@free.fr> - 7.0.4-9
- update to 7.0.4-9

* Tue Nov 29 2022 Yann Collette <ycollette.nospam@free.fr> - 7.0.3-9
- update to 7.0.3-9

* Tue Aug 23 2022 Yann Collette <ycollette.nospam@free.fr> - 7.0.2-9
- add patch for default font selection (thanks to jpcima).

* Tue Aug 16 2022 Yann Collette <ycollette.nospam@free.fr> - 7.0.2-8
- remove patch

* Tue Aug 16 2022 Yann Collette <ycollette.nospam@free.fr> - 7.0.2-7
- use cmake to build juce

* Mon Aug 15 2022 Yann Collette <ycollette.nospam@free.fr> - 7.0.2-6
- update to 7.0.2-6

* Mon Jul 04 2022 Yann Collette <ycollette.nospam@free.fr> - 7.0.1-6
- update to 7.0.1-6

* Thu Jun 23 2022 Yann Collette <ycollette.nospam@free.fr> - 7.0.0-6
- update to 7.0.0-6

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
