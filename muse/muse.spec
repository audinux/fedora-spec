# Status: active
# Tag: Editor, Audio, MIDI, Sequencer
# Type: Standalone
# Category: DAW, MIDI

%global majorver 4.2
# No need to provide & require internal libraries
%global _privatelibs libmuse_.*[.]so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$
%undefine _strict_symbol_defs_build
%undefine _ld_as_needed
%undefine _lto_cflags

Name:  muse
Summary: Midi/Audio Music Sequencer
# Epoch is set to 1 for PlanetCCRMA compatibility.
# See: https://fedoraproject.org/wiki/AudioCreation
Epoch: 1
Version: %{majorver}.1
Release: 10%{?dist}
License: LicenseRef-Callaway-Public-Domain AND GPL-2.0-only AND GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL: https://muse-sequencer.github.io/

# original freeverb plugin was public domain
# givertcap (not built) is GPLv2
# The rest, including the core of muse is distributed under GPLv2+
# Automatically converted from old format: Public Domain and GPLv2 and GPLv2+ and LGPLv2+ - review is highly recommended.

Source0: https://github.com/muse-sequencer/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(dssi)
BuildRequires: pkgconfig(fluidsynth)
BuildRequires: pkgconfig(jack)
BuildRequires: ladspa-devel
BuildRequires: pkgconfig(libinstpatch-1.0)
BuildRequires: pkgconfig(liblo)
BuildRequires: pkgconfig(lrdf)
BuildRequires: pkgconfig(lilv-0)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(python3)
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qttools-static
BuildRequires: pkgconfig(rtaudio)
BuildRequires: pkgconfig(rubberband)
BuildRequires: pkgconfig(gtkmm-2.4)
BuildRequires: libatomic
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Requires: hicolor-icon-theme

%description
MusE is a MIDI/Audio sequencer with recording and editing capabilities. It can
perform audio effects like chorus/flanger in real-time via LASH and it supports
JACK and ALSA interfaces. MusE aims to be a complete multitrack virtual studio
for Linux.

%prep
%autosetup -p1 -n %{name}-%{version}

# Fix Python shebangs
sed -i -e 's|/usr/bin/env python3|%{__python3}|' -e 's|/usr/bin/python$|%{__python3}|' share/scripts/* utils/*

%build

export CMAKE_CXX_FLAGS="-D_GNU_SOURCE"

%cmake -DMusE_DOC_DIR=%{_pkgdocdir}/ \
       -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build -- mplugins
%cmake_build

%install

%cmake_install

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.muse_sequencer.Muse.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/io.github.muse_sequencer.Muse.appdata.xml

%files
%license COPYING
%{_pkgdocdir}
%{_bindir}/%{name}*
%{_bindir}/grepmidi
%{_libdir}/%{name}-%{majorver}*/
%{_datadir}/%{name}-%{majorver}*/
%{_datadir}/applications/io.github.muse_sequencer.Muse.desktop 
%{_datadir}/icons/hicolor/*/apps/muse.png
%{_mandir}/man1/grepmidi*
%{_mandir}/man1/%{name}*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/metainfo/io.github.muse_sequencer.Muse.appdata.xml

%changelog
* Tue Apr 28 2026 Yann Collette <ycollette.nospam@free.fr> - 1:4.2.1-10
- update to 1:4.2.1-10 - fix build for Audinux

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jun 12 2025 Python Maint <python-maint@redhat.com> - 1:4.2.1-8
- Rebuilt for Python 3.14

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 09 2025 Michel Lind <salimma@fedoraproject.org> - 1:4.2.1-6
- Rebuilt for rubberband 4

* Fri Oct 18 2024 Richard Shaw <hobbes1069@gmail.com> - 1:4.2.1-5
- Rebuild for new rtaudio.

* Mon Sep 02 2024 Miroslav SuchÃ½ <msuchy@redhat.com> - 1:4.2.1-4
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Python Maint <python-maint@redhat.com> - 1:4.2.1-2
- Rebuilt for Python 3.13

* Tue Jun 04 2024 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1:4.2.1-1
- Update version

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1:4.0.0-6
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 03 2021 Neal Gompa <ngompa13@gmail.com> - 1:4.0.0-1
- Rebase to MuSE 4.0

* Thu Jun 17 2021 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1:3.0.2-16
- Rebuild for fluidsynth-2.2.1

* Sat Apr 17 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1:3.0.2-15
- Rebuild for libinstpatch 1.1.6
- Find gtkmm using pkg_check_modules() so we have the correct compiler and
  linker flags for its recursive dependencies, such as atkmm. This is a
  temporary workaround for FTBFS RHBZ#1923460, which is caused by RHBZ#1944935
  in cmake.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 03 2020 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1:3.0.2-13
- Fixes FTBFS RHBZ#1864180
- Backport Qt include fixes patch for newer Qt
- Switch to using cmake RPM macros on build and install

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1:3.0.2-10
- Rebuild against fluidsynth2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 10 2019 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot] com> - 1:3.0.2-7
- Fixed more python shebangs

* Mon Feb 11 2019 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot] com> - 1:3.0.2-6
- Versioned Python shebangs
- Converted some Python2 scripts to Python3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 28 2018 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot] com> - 1:3.0.2-3
- Fix FTBFS RHBZ#1583068

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot] com> - 1:3.0.2-1
- Update to 3.0.2

* Tue Jan 23 2018 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot] com> - 1:3.0.1-1
- Update to 3.0.1
- Remove obsolete scriptlets
- Add appdata file from upstream trunk
- Update the provides filtering

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:3.0-2
- Remove obsolete scriptlets

* Sun Jan 07 2018 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot] com> - 1:3.0-1
- Update to 3.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1:2.2.1-6
- Rebuild due to bug in RPM (RHBZ #1468476)

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Mon Feb 13 2017 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1:2.2.1-4
- gcc7 fix

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 07 2016 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1:2.2.1-2
- gcc6 fix

* Fri Feb 05 2016 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1:2.2.1-1
- MusE-2.2.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1:2.1.2-7
- Rebuilt for GCC 5 C++11 ABI change

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 2.1.2-6
- add mime scriptlet

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1:2.1.2-3
- Unversioned docdir https://fedoraproject.org/wiki/Changes/UnversionedDocdirs

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 30 2013 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1:2.1.2-1
- MusE-2.1.2

* Sat Feb 16 2013 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1:2.1.1-1
- MusE-2.1.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jan 19 2013 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1:2.1-1
- MusE-2.1

* Sat Aug 25 2012 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1:2.0.1-1
- MusE-2.0.1

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 01 2012 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1:2.0-2
- Add requires filter

* Sun Jul 01 2012 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1:2.0-1
- MusE-2.0 final!

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0-0.8.rc2
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1:2.0-0.7.rc2
- Update to MusE-2.0-rc2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0-0.6.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 14 2011 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1:2.0-0.5.rc1
- Update to MusE-2.0-rc1

* Sat Jun 18 2011 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1:2.0-0.4.beta2
- Update to MusE-2.0-beta2

* Tue Feb 08 2011 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1:2.0-0.3.alpha
- Fix build failure against gcc-4.6

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0-0.2.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 26 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1:2.0-0.1.alpha
- Update to 2.0alpha
- Removed provides filtering according to the new guidelines.

* Mon Sep 27 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1:1.1-1
- Update to 1.1

* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 1:1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jul 20 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1:1.0.1-4
- Rebuild against new liblo-0.26

* Sun Jul 18 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1:1.0.1-3
- Add AudioVideo to .desktop file categories RHBZ#614718

* Wed Apr 07 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1:1.0.1-2
- Correct synti path on 64bit systems
- Remove the -fno-var-tracking-assignments workaround
- Rebuild needed on F-13 to pick up the proper soname deps. RHBZ#566419

* Sat Jan 30 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1:1.0.1-1
- Update to 1.0.1
- Drop upstreamed patches

* Thu Dec 24 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1:1.0-1
- Update to 1.0

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-0.7.rc3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1:1.0-0.7.rc3
- Bugfix: muse doesn't start properly on x86_64 on F-11+. Backport glibc-2.10 patch from trunk
- Remove BR: e2fsprogs-devel

* Sat Jun 20 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1:1.0-0.6.rc3
- Update to 1.0rc3

* Wed May 13 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1:1.0-0.5.rc2
- Update to 1.0rc2

* Mon Feb 23 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1:1.0-0.4.rc1
- Updated icon cache scriptlets according to the new guidlines

* Mon Feb 23 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1:1.0-0.3.rc1
- Handle the Provides list within the SPEC file
- Add gcc-4.4 patch
- Fix size_t warnings
- Explain the various licenses

* Sun Feb 08 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1:1.0-0.2.rc1
- Use AutoProv=no instead of AutoReqProv=no

* Sat Feb 07 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1:1.0-0.1.rc1
- New upstream release with many bugfixes.
- Remove the patches that are committed upstream.

* Fri Jan 30 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1:0.9-3
- PlanetCCRMA's SPEC revised for Fedora submission

* Tue Jul 15 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1:0.9-2
- updated qt3-devel build dependency for fc9
- added patch for gcc4.3 build on fc9

* Fri Feb  1 2008 Arnaud Gomes-do-Vale <Arnaud.Gomes@ircam.fr>
- built on CentOS

* Sat Nov 17 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9-2
- added patch from Debian to avoid using internal lash api calls that
  are not there in last 0.5.3

* Tue Oct  9 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9-1
- updated to 0.9
- adjusted desktop categories

* Thu Dec 21 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.8.1a-2
- spec file tweaks, build on fc6
- make sure LADSPA plugins are searched in the right lib directory
  for all architectures

* Fri May  5 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- added icon and Planet CCRMA categories

* Tue Mar 28 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.8.1a-1
- updated to 0.8.1a

* Mon Jan 23 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.7.2-0.1.pre5
- updated to 0.7.2-pre5

* Sun Nov 20 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- the internal libraries appear in the provides list and conflict with
  old names, for example the obsolete "fluid" package name as now
  included in pd-fluid, so disable automatic provide generation. 

* Fri Nov 18 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.7.2-0.1.pre3
- update to 0.7.2pre3
- build with lash (name change from ladcca)
- added readline-devel (needed by lash)
- delete --enable-rtcap option to configure

* Sat Jun 25 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- do not create givertcap package anymore, fc4 mach is confused by
  the version and it is not needed anymore

* Mon Jan 24 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.7.1-1
- updated to 0.7.1
- needs libsamplerate
- added --enable-ladcca configure flag (has to be explicitly enabled)

* Fri Dec 31 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- spec file cleanup

* Sun Sep 26 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- use qt33 package for fc1 and below

* Wed Jul 21 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.7.0-1
- updated to 0.7.0

* Thu May 20 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- added dsssl build requirement

* Thu May  6 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.7.0-0.pre2.1
- updated to 0.7.0 pre2
- needs qt > 3.2
- --disable-suid-install does not work, change default to "no"

* Wed Jan  7 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.3-1
- updated to 0.6.3

* Wed Nov 19 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.2-1
- added alsa patch for old api

* Fri Nov 14 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.2-1
- spec file tweaks
- fix dssslver for 9 and fc1

* Thu Nov  6 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.2-1
- updated to 0.6.2
- softsynth and jack patches not needed any more

* Sun Sep 14 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.1-2
- applied Takashi's patch for softsynth hangs (patch2)
- fixed build with jack 0.80.0, updated version requirement
- added release tags
- added separate release number for givertcap

* Sat Jul 26 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.1-1
- updated to 0.6.1

* Tue May 20 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.0-1
- updated to 0.6.0 final
- added atomic.h borrowed from kernel 2.4.20 (otherwise it does not
  find atomic_inc)
- added instruments directory and files to files list
- added explicit dependency to qt version 

* Fri Apr  4 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.0pre8-1
- updated to 0.6.0pre8

* Wed Apr  2 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.0pre7-2
- rebuild for jack 0.66.3, added explicit requires for it

* Fri Mar 21 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.0pre7-1
- updated to 0.6.0pre7
- changed default qt in 7.3 to 3.0.5, dsss version to 1.76 in 7.3/8.0
- added node.h patch for 7.2/7.3

* Thu Dec  5 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.0pre5-1
- updated to 0.6.0pre5

* Thu Nov 14 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.0pre3-1
- added patch to fix jack port names
- signals patch no longer needed

* Mon Oct 21 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.0pre2-2
- added patch so that signals are not intercepted, that hungs muse
  on startup under rh 8.0's thread libraries
- disabled qttest, otherwise you have to build while logged in as root
  in the console
- added proper menu entries

* Mon Oct 21 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.0pre2-1
- updated to 0.6.0pre2, enabled jack support

* Mon Jun 24 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.3-1
- updated to 0.5.3b
- enabled rtcaps, added givertcap package
- updated doc file list
- added make -j for smp builds

* Fri Apr 19 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.2-1
- updated to 0.5.2, needs qt 3.0.3 (from rawhide)

* Wed Nov 28 2001 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.14-1
- updated to 0.4.14, adjusted file list

* Tue Nov 27 2001 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- updated to 0.4.16 (added qt3 rpms)
- patch1: remove su's
- patch2: configuration, 3 and 4 suggested patches on the muse list
- cannot make 0.4.16 compile...

* Thu Aug 23 2001 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.8-1
- adapted suse's srpm to redhat

* Fri May 11 2001 - <<tiwai@suse.de>>
- fixed build.
* Wed May 09 2001 - <tiwai@suse.de>
- updated to muse-0.3.19.
* Wed Apr 11 2001 - <tiwai@suse.de>
- updated to muse-0.3.16.
* Wed Apr 04 2001 - <tiwai@suse.de>
- updated to muse-0.3.15.
* Tue Mar 20 2001 - <tiwai@suse.de>
- fixed neededforbuild.
* Fri Mar 16 2001 - <tiwai@suse.de>
- updated to muse-0.3.12.
* Mon Mar 12 2001 - <tiwai@suse.de>
- updated to muse-0.3.11.
* Wed Mar 07 2001 - ro@suse.de
- changed neededforbuild <mesadev> to <mesa-devel>
* Wed Mar 07 2001 - <tiwai@suse.de>
- Updated to muse-0.3.10.
* Mon Feb 26 2001 - <tiwai@suse.de>
- Updated to muse-0.3.9.
* Mon Feb 12 2001 - <tiwai@suse.de>
- Updated to muse-0.3.7.
* Fri Feb 09 2001 - <tiwai@suse.de>
- Updated to muse-0.3.6.
* Tue Jan 30 2001 - <tiwai@suse.de>
- Updated to muse-0.3.5.
* Fri Dec 01 2000 - ro@suse.de
- added liblcms to neededforbuild
* Thu Nov 23 2000 - <tiwai@suse.de>
- Updated to muse-0.2.12.
* Fri Nov 17 2000 - <tiwai@suse.de>
- Updated to muse-0.2.10.
* Fri Nov 17 2000 - ro@suse.de
- fixed neededforbuild: += libmng-devel
* Wed Nov 08 2000 - <tiwai@suse.de>
- Updated to muse-0.2.7.
- Fixed to compile.
* Mon Nov 06 2000 - ro@suse.de
- fixed to compile (include spinlock before mc146818rtc)
* Fri Nov 03 2000 - <tiwai@suse.de>
- Updated to muse-0.2.6.
- Fixed spec file for long package-name support.
- Excluded plug-ins from provide list.
* Mon Oct 09 2000 - <tiwai@suse.de>
- Added libmng to neededforbuild
* Fri Oct 06 2000 - <tiwai@suse.de>
- Updated to muse-0.2.4
* Wed Sep 27 2000 - <tiwai@suse.de>
- Fixed compile for alpha and ppc.
* Tue Sep 26 2000 - <tiwai@suse.de>
- Update to 0.2.3
* Mon Aug 28 2000 - <tiwai@suse.de>
- Update to 0.2.1.
- Disable translations (due to change of qt-2.2).
* Wed Aug 02 2000 - <tiwai@suse.de> 
- Initial version: 0.1.10.  No manual document is included.
