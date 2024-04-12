# Tag: Editor, Audio, MIDI, Sequencer
# Type: Standalone, DSSI, LV2, LADSPA, VST, VST3, CLAP
# Category: DAW, MIDI

Summary: Audio/MIDI multi-track sequencer
Name: qtractor-mao
Version: 0.9.90
Release: 2%{?dist}
License: GPLv2+
URL: http://qtractor.sourceforge.net/

# ./qtractor-source.sh <tag>
# ./qtractor-source.sh qtractor_0_9_90

Source0: qtractor.tar.gz
Source1: qtractor-source.sh

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: dssi-devel
# for plugin GUI support:
BuildRequires: gtk2-devel
BuildRequires: gtkmm2.4-devel
BuildRequires: pkgconfig(jack)
BuildRequires: ladspa-devel
BuildRequires: liblo-devel
BuildRequires: libmad-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: libvorbis-devel
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-linguist
BuildRequires: qt6-qtsvg-devel
BuildRequires: qt6-qttools-devel
BuildRequires: rubberband-devel
BuildRequires: suil-devel
BuildRequires: lilv-devel
BuildRequires: aubio-devel
BuildRequires: desktop-file-utils

Requires: hicolor-icon-theme
Requires: qt6ct

Recommends: (qgnomeplatform-qt6%{?_isa} or plasma-desktop%{?_isa})

Obsoletes: qtractor < 0.9.36-1

%description
Qtractor is an Audio/MIDI multi-track sequencer application written in C++ 
around the Qt4 toolkit using Qt Designer. The initial target platform will be
Linux, where the Jack Audio Connection Kit (JACK) for audio, and the Advanced
Linux Sound Architecture (ALSA) for MIDI, are the main infrastructures to 
evolve as a fairly-featured Linux Desktop Audio Workstation GUI, specially 
dedicated to the personal home-studio.

%prep
%autosetup -n qtractor

sed -i -e "s|\${JACK_LIBDIR}|/usr/lib64/pipewire-0.3/jack/|g" CMakeLists.txt

%build

%cmake -DCONFIG_LV2_EVENT=ON \
       -DCONFIG_QT6=ON 
%cmake_build

%install

%cmake_install
%find_lang qtractor --with-qt

# For ticket #51
desktop-file-edit \
    --set-key="Exec" --set-value="env QT_QPA_PLATFORMTHEME=qt6ct qtractor %f" \
    %{buildroot}/%{_datadir}/applications/org.rncbc.qtractor.desktop

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.rncbc.qtractor.desktop

%files -f qtractor.lang
%doc ChangeLog README
%license LICENSE
%{_datadir}/applications/org.rncbc.qtractor.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/org.rncbc.qtractor.xml
%{_bindir}/qtractor
%{_libdir}/qtractor
%{_datadir}/man/man1/qtractor*
%{_datadir}/man/*/man1/qtractor*
%{_datadir}/metainfo/org.rncbc.qtractor.metainfo.xml
%{_datadir}/qtractor/audio/metro_bar.wav
%{_datadir}/qtractor/audio/metro_beat.wav
%{_datadir}/qtractor/instruments/*
%{_datadir}/qtractor/palette/*

%changelog
* Thu Apr 11 2024 Yann Collette <ycollette.nospam@free.fr> - 0.9.90-2
- update to 0.9.90-2

* Sat Jan 27 2024 Yann Collette <ycollette.nospam@free.fr> - 0.9.39-2
- update to 0.9.39-2 - add QT_QPA_PLATFORMTHEME=qt6ct env var in desktop file

* Sat Jan 20 2024 Yann Collette <ycollette.nospam@free.fr> - 0.9.38-2
- update to 0.9.38-2 - add a missing Requires for non Qt platform

* Wed Jan 03 2024 Yann Collette <ycollette.nospam@free.fr> - 0.9.38-1
- update to 0.9.38-1

* Tue Dec 05 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.37-1
- update to 0.9.37-1

* Fri Dec 01 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.36-1
- update to 0.9.36-1

* Mon Jul 24 2023 Kalev Lember <klember@redhat.com> - 0.9.34-1
- Update to 0.9.34
- Switch to cmake build system
- Drop SSE build conditionals

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 02 2021 Brendan Jones <brendan.jones.it@gmail.com> - 0.9.19-1
- Update to 0.9.19

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 14 2019 Brendan Jones <brendan.jones.it@gmail.com> - 0.9.10-1
- Update to 0.9.10

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 30 2018 Brendan Jones <brendan.jones.it@gmail.com> - 0.9.2-1
- Update to 0.9.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.5-2
- Remove obsolete scriptlets

* Sun Dec 24 2017 Brendan Jones <brendan.jones.it@gmail.com> - 0.8.5-1
- Update to 0.8.5

* Sun Oct 08 2017 Brendan Jones <brendan.jones.it@gmail.com> - 0.8.4-1
- Update to 0.8.4

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 18 2017 Brendan Jones <brendan.jones.it@gmail.com> - 0.8.1-1
- Update to 0.8.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.8.0-1
- Update to 0.8.0
- libmad support back in the main package
- Enabled GTK2 plugin GUI support

* Tue Sep 27 2016 Brendan Jones <brendan.jones.it@gmail.com> - 0.7.9-1
- Update to 0.7.9

* Tue Jun 28 2016 Brendan Jones <brendan.jones.it@gmail.com> - 0.7.8-1
- Update to 0.7.8

* Sat May 07 2016 Brendan Jones <brendan.jones.it@gmail.com> 0.7.7-1
- Update to 0.7.7

* Fri Apr 22 2016 Brendan Jones <brendan.jones.it@gmail.com> 0.7.6-1
- Update to 0.7.6

* Tue Feb 23 2016 Rex Dieter <rdieter@fedoraproject.org> 0.7.4-2
- qtractor: FTBFS in rawhide (#1307974)

* Tue Feb 23 2016 Brendan Jones <brendan.jones.it@gmail.com> 0.7.4-1
- Update to 0.7.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Brendan Jones <brendan.jones.it@gmail.com> 0.7.2-1
- Update to 0.7.2

* Tue Oct 27 2015 Brendan Jones <brendan.jones.it@gmail.com> 0.7.1-1
- Update to 0.7.1

* Mon Jun 29 2015 Brendan Jones <brendan.jones.it@gmail.com> 0.6.7-1
- Update to 0.6.7

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 01 2015 Brendan Jones <brendan.jones.it@gmail.com> 0.6.6-1
- Update to 0.6.6

* Tue Feb 03 2015 Brendan Jones <brendan.jones.it@gmail.com> 0.6.5-1
- Update to 0.6.5

* Tue Nov 25 2014 Brendan Jones <brendan.jones.it@gmail.com> 0.6.4-1
- Update to 0.6.4
- Refactor secondary patch

* Thu Sep 25 2014 Brendan Jones <brendan.jones.it@gmail.com> 0.6.3-1
- Update to 0.6.3

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Rex Dieter <rdieter@fedoraproject.org> 0.6.2-2
- update mime scriptlet, BR: qt4-devel

* Tue Jul 08 2014 Brendan Jones <brendan.jones.it@gmail.com> 0.6.2-1
- Update to 0.6.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Brendan Jones <brendan.jones.it@gmail.com> 0.6.1-1
- Update to 0.6.1

* Fri Mar 28 2014 Brendan Jones <brendan.jones.it@gmail.com> 0.6.0-1
- Update to 0.6.0

* Thu Mar 13 2014 Dan HorĂ¡k <dan[at]danny.cz> - 0.5.12-2
- fix build on non-x86 arches

* Sat Jan 11 2014 Brendan Jones <brendan.jones.it@gmail.com> 0.5.12-1
- Update to 0.5.12

* Mon Oct 07 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.5.11-1
- Update to 0.5.11

* Mon Aug 12 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.5.10-3
- Arm is not supported upstream

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 19 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.5.10-1
- Update to 0.5.10

* Thu Jun 06 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.5.9-1
- Update to 0.5.9

* Sun May 19 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.5.8-2
- Remove no longer required sed on desktop file

* Mon Apr 22 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.5.8-1
- Update to 0.5.8

* Sat Jan 05 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.5.7-1
- Update to 0.5.7

* Thu Oct 04 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.5.6-1
- Update to 0.5.6

* Tue Jun 19 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.5.5-1
- Update to 0.5.5, factor out libmad (thanks to oget)

* Sat Mar 03 2012 Brendan Jones <brendan.jones.it@gmail.com> - 0.5.4-1
- Update to version 0.5.4

* Sun Feb 26 2012 Brendan Jones <brendan.jones.it@gmail.com> - 0.5.3-3
- Provide rpmfusion support, update comments

* Wed Feb 22 2012 Brendan Jones <brendan.jones.it@gmail.com> - 0.5.3-2
- Copied from rpmfusion, add suil, lilv suppport as they replace the deprecated
  slv2
- Remove libmad from build (forbidden license)

* Tue Jan 24 2012 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.5.3-1
- Update to 0.5.3

* Sun Dec 25 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.5.2-1
- Update to 0.5.2

* Thu Nov 03 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.5.1-2
- Rebuild for dist F-16

* Sat Oct 08 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.5.1-1
- Update to 0.5.1

* Sat Jul 30 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.5.0-1
- Update to 0.5.0

* Thu May 26 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4.9-1
- Update to 0.4.9

* Tue Jan 18 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4.8-1
- Update to 0.4.8

* Sat Oct 02 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4.7-1
- Update to 0.4.7

* Sat Aug 21 2010 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.4.6-4
- rebuilt

* Sun Aug 08 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.4.6-3
- Rebuild against new liblo-0.26 on F-14 again

* Tue Jul 20 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.4.6-2
- Rebuild against new liblo-0.26 on F-14

* Sun May 23 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4.6-1
- Update to 0.4.6
- Drop upstreamed .desktop file modifications
- Drop old documentation

* Sun May 16 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4.6-0.1.1568svn1565
- Update to 0.4.6 rc (svn1565)

* Sat Jan 30 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4.5-1
- updated to 0.4.5.

* Fri Oct 23 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4.3-1
- updated to 0.4.3.

* Fri Jun 05 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4.2-1
- updated to 0.4.2.

* Wed May 27 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4.1-4
- Explicitly disable SSE optimizations on non-"%%{ix86} ia64 x86_64" architectures

* Fri May 22 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4.1-3
- preserve timestamps

* Thu May 21 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4.1-2
- ship odt documentation instead of the pdf

* Sat Apr  4 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4.1-1
- updated to 0.4.1.

* Tue Mar 24 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4.0-1
- updated to 0.4.0.

* Fri Feb 20 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.3.0-1
- updated to 0.3.0. SPEC file adapted from PlanetCCRMA.

* Mon Oct  6 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.2.2-1
- updated to 0.2.2

* Tue Sep 23 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.2.1-1
- updated to 0.2.1

* Thu Jun 19 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.3-1
- added patch for gcc43 build on fc9 (from gentoo).

* Fri May  2 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.3-1
-  initial build
- x86_64 build needs an explicit path for the qmake binary to be found
