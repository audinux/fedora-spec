# Tag:  Drum, Jack, Alsa, MIDI
# Type: Standalone
# Category: Audio, Sequencer
# GUIToolkit: Qt5
# LastSourceUpdate: 2021

Name:    hydrogen
Version: 1.1.1
Release: 12%{?dist}
Summary: Advanced drum machine for GNU/Linux
URL:     http://www.hydrogen-music.org/
License: GPLv2+

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/hydrogen-music/hydrogen/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: flac-devel 
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: ladspa-devel
BuildRequires: liblrdf-devel
BuildRequires: libsndfile-devel
BuildRequires: libtar-devel
BuildRequires: portaudio-devel
BuildRequires: portmidi-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtxmlpatterns-devel
BuildRequires: qt5-linguist
BuildRequires: libarchive-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: rubberband-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: filesystem

%description
Advanced drum machine for GNU/Linux. The main goal is to bring 
professional yet simple and intuitive pattern-based drum programming.

%prep
%autosetup -n %{name}-%{version}

sed -i -e "s/Sound/X-Sound/g" linux/org.hydrogenmusic.Hydrogen.desktop

%build

%cmake -DWANT_ALSA:BOOL=ON \
       -DWANT_CPPUNIT:BOOL=OFF \
       -DWANT_DEBUG:BOOL=OFF \
       -DWANT_JACK:BOOL=ON \
       -DWANT_JACKSESSION:BOOL=ON \
       -DWANT_LADSPA:BOOL=ON \
       -DWANT_LASH:BOOL=ON \
       -DWANT_LIBARCHIVE:BOOL=ON \
       -DWANT_LRDF:BOOL=OFF \
       -DWANT_NSMSESSION:BOOL=ON \
       -DWANT_OSS:BOOL=OFF \
       -DWANT_PORTAUDIO:BOOL=OFF \
       -DWANT_PORTMIDI:BOOL=OFF \
       -DWANT_PULSEAUDIO:BOOL=ON \
       -DWANT_RUBBERBAND:BOOL=ON \
       -DWANT_SHARED:BOOL=ON \
       -DCMAKE_INSTALL_LIBDIR=%{_lib}

%cmake_build

%install

%cmake_install

# install hydrogen.desktop properly.
desktop-file-install --vendor '' \
        --add-category=X-Drumming \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/org.hydrogenmusic.Hydrogen.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.hydrogenmusic.Hydrogen.desktop

%files
%doc AUTHORS ChangeLog README.txt
%license COPYING*
%{_bindir}/hydrogen
%{_bindir}/h2cli
%{_bindir}/h2player
%{_datadir}/hydrogen/*
%{_datadir}/icons/*
%{_datadir}/applications/*.desktop
%{_datadir}/appdata/*.appdata.xml
%{_libdir}/*.so
%{_datadir}/man/*
%exclude %{_includedir}/%{name}

%changelog
* Mon Dec 06 2021 Yann Collette <ycollette.nospam@free.fr> - 1.1.1-12
- update to 1.1.1-12

* Sun Sep 05 2021 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-12
- update to 1.1.0-12

* Sun Apr 11 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-12
- update to 1.0.2-12

* Tue Oct 20 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-12
- fix debug build

* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-11
- update for Fedora 33

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9.7-11
- update for Fedora 29

* Mon Oct 23 2017 Yann Collette <ycollette.nospam@free.fr> - 0.9.7-11
- Remove scons

* Mon Jun 01 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9.6-11
- Update to version 0.9.6

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.5.1-11
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 11 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.9.5.1-8
- format-security patch

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 12 2013 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.5.1-6
- Fix scons build once again

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 0.9.5.1-5
- Drop desktop vendor tag.

* Sun Jul 22 2012 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.5.1-4
- Use pkg-config to detect cflags for liblrdf since raptor header file location changed

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.1-2
- Rebuilt for c++ ABI breakage

* Sun Feb 19 2012 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.5.1-1
- Update to 0.9.5.1. Drop upstreamed patch.

* Mon Jan 16 2012 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.5-3
- gcc-4.7 compile fixes

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 27 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.5-1
- Update to 0.9.5

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 16 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4.2-3
- Fix data directory. Fixes RHBZ#643622

* Wed Sep 29 2010 jkeating - 0.9.4.2-2
- Rebuilt for gcc bug 634757

* Fri Sep 24 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4.2-1
- Update to 0.9.4.2
- Drop all upstreamed patches

* Sat Apr 10 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4.1-1
- Update to 0.9.4.1
- Build the wasp plugins
- Fixes ladspa plugin path on 64bit systems
- Fixes crash RHBZ#570348

* Sat Feb 13 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-3
- Fix DSO linking RHBZ#564719

* Sat Jan 30 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-2
- Add patch against portmidi-200 on F13+. Fixes RHBZ#555488

* Tue Sep 15 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-1
- Update to 0.9.4

* Sat Aug 22 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-0.7.rc2
- Update to 0.9.4-rc2

* Wed Aug 05 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-0.6.rc1.1
- Update .desktop file

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-0.5.rc1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-0.4.rc1.1
- Rebuild against new lash build on F-12 due to the e2fsprogs split

* Tue Apr 14 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-0.3.rc1.1
- Update to 0.9.4-rc1-1

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-0.2.790svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-0.1.790svn
- Update to 0.9.4-beta3 (uses scons and qt4)

* Fri Apr 04 2008 Lubomir Kundrak <lkundrak@redhat.com> - 0.9.3-13
- QT3 changes by rdieter
- Fix build

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.3-12
- Autorebuild for GCC 4.3

* Thu Jan 03 2008 Lubomir Kundrak <lkundrak@redhat.com> 0.9.3-11
- Previous change was not a good idea
- Adding missing includes to fix build with gcc-4.3

* Sun Oct 14 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.9.3-10
- Remove unneeded dependencies on desktop-file-utils

* Tue Oct 09 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.9.3-9
- Incorporate fixes from #190040, thanks to Hans de Goede
- Removed useless LIBDIR introduced in previous revision
- Fixed desktop file installation
- Call gtk-update-icon-cache only if it is present

* Sun Oct 07 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.9.3-8
- Remove -j from make to fix concurrency problems
- Handle libdir on 64bit platforms correctly
- Rename patches

* Sat Oct 06 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.9.3-7.1
- Fix desktop file
- Fix compatibility with new FLAC
- Fix linking for Build ID use

* Mon Mar 26 2007 Anthony Green <green@redhat.com> 0.9.3-7
- Improve Source0 link.
- Add %%post(un) scriptlets for MimeType update.
- Add update-desktop-database scriptlets.

* Sat Jul 22 2006 Anthony Green <green@redhat.com> 0.9.3-6
- Add hydrogen-null-sample.patch to fix crash.

* Sun Jul 02 2006 Anthony Green <green@redhat.com> 0.9.3-5
- Clean up BuildRequires.
- Configure with --disable-oss-support
- Don't run ldconfig (not needed)
- Remove post/postun scriptlets.

* Sat May 13 2006 Anthony Green <green@redhat.com> 0.9.3-4
- BuildRequire libxml2-devel.
- Remove explicit Requires for some runtime libraries.
- Set QTDIR via /etc/profile.d/qt.sh.
- Update desktop icons and icon cache in post and postun.
- Don't use __rm or __make macros.

* Sat May 13 2006 Anthony Green <green@redhat.com> 0.9.3-3
- Conditionally apply ardour-lib64-ladspa.patch.

* Sat May 13 2006 Anthony Green <green@redhat.com> 0.9.3-2
- Build fixes for x86_64.

* Wed Apr 26 2006 Anthony Green <green@redhat.com> 0.9.3-1
- Created.
