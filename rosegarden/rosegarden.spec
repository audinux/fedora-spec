# Tag: Editor, Audio, Sequencer
# Type: Standalone
# Category: Audio, Sequencer, DAW

%global major 24.06

Name: rosegarden4
Version: %{major}
Release: 4%{?dist}
Summary: MIDI, audio and notation editor
License: GPLv2+
URL: https://www.rosegardenmusic.com/
ExclusiveArch: x86_64 aarch64

Source0: https://sourceforge.net/projects/rosegarden/files/rosegarden/%{major}/rosegarden-%{major}.tar.xz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: dssi-devel
BuildRequires: fftw-devel
BuildRequires: fontpackages-devel
BuildRequires: pkgconfig(jack)
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-qtx11extras-devel
BuildRequires: ladspa-devel
BuildRequires: liblo-devel
BuildRequires: liblrdf-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: lirc-devel
BuildRequires: zlib-devel
BuildRequires: lilv-devel
BuildRequires: lv2-devel
BuildRequires: gtk2-devel
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

# Use lilypond feta fonts
Requires: lilypond-emmentaler-fonts
Provides: rosegarden = %{version}-%{release}

%description
Rosegarden is a professional audio and MIDI sequencer, score editor, and
general purpose music composition and editing environment.

Rosegarden is an easy to learn, attractive application, ideal for composers,
musicians, music students, and small studio or home recording environments.

%prep
%autosetup -n rosegarden-%{version}

# Fix permissions:
chmod 644 src/gui/widgets/BaseTextFloat.*

%build

%cmake
%cmake_build

%install

%cmake_install

# Update the screenshot shown in the software center
#
# NOTE: It would be *awesome* if this file was pushed upstream.
#
# See http://people.freedesktop.org/~hughsient/appdata/#screenshots for more details.
#
appstream-util replace-screenshots %{buildroot}%{_datadir}/metainfo/rosegarden.appdata.xml \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/rosegarden/a.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/rosegarden/b.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/rosegarden/c.png

desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --delete-original \
  --remove-category X-SuSE-Sequencer \
  --remove-category X-Red-Hat-Base \
  %{buildroot}%{_datadir}/applications/com.rosegardenmusic.rosegarden.desktop

%files
%doc AUTHORS CONTRIBUTING README.md
%license COPYING
%{_bindir}/rosegarden
%{_datadir}/applications/*rosegarden.desktop
%{_datadir}/icons/hicolor/*/mimetypes/application-x-rosegarden-*.png
%{_datadir}/icons/hicolor/*/apps/rosegarden.png
%{_datadir}/mime/packages/rosegarden.xml
%{_datadir}/metainfo/rosegarden.appdata.xml

%changelog
* Thu Jun 06 2024 Yann Collette <ycollette.nospam@free.fr> - 24.06-4
- update to 24.06-4: add missing requirements

* Wed Jun 05 2024 Yann Collette <ycollette.nospam@free.fr> - 24.06-1
- update to 24.06-1

* Wed Dec 06 2023 Yann Collette <ycollette.nospam@free.fr> - 23.12-1
- update to 23.12-1

* Wed Jun 07 2023 Yann Collette <ycollette.nospam@free.fr> - 23.06-1
- update to 23.06-1

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 21.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun May 22 2022 Guido Aulisi <guido.aulisi@gmail.com> - 21.12-1
- Update to 21.12

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.06.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 29 2021 Guido Aulisi <guido.aulisi@gmail.com> - 21.06.1-1
- Update to 21.06.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 10 14:12:40 CET 2020 Guido Aulisi <guido.aulisi@gmail.com> - 20.12-1
- Update to 20.12

* Thu Aug 06 2020 Guido Aulisi <guido.aulisi@gmail.com> - 20.06-1
- Update to 20.06
- FTBFS in Fedora rawhide/f33

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.12-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 18 2020 Guido Aulisi <guido.aulisi@gmail.com> - 19.12-1
- Update to 19.12
- Some spec cleanup

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 17.12-4
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 17.12-2
- Remove obsolete scriptlets

* Sun Dec 24 2017 Brendan Jones <brendan.jones.it@gmail.com> - 17.12-1
- Update to 17.12

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Apr 25 2016 Brendan Jones <brendan.jones.it@gmail.com> 16.02-2
- Ensure we are in the right directory
- Correct changelog

* Sun Apr 24 2016 Brendan Jones <brendan.jones.it@gmail.com> 16.02-1
- Update to 16.02

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 23 2015 Brendan Jones <brendan.jones.it@gmail.com> - 15.10-1
- Update to 15.10

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Brendan Jones <brendan.jones.it@gmail.com> 14.12-1
- Update to 14.12

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 14.02-6
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 14.02-5
- Use better AppData screenshots

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Rex Dieter <rdieter@fedoraproject.org> 14.02-3
- add mime scriptlet

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 04 2014 Brendan Jones <brendan.jones.it@gmail.com> -1
- Update to 14.02

* Tue Nov 05 2013 Brendan Jones <brendan.jones.it@gmail.com> 13.10-1
- Update to 13.10

* Mon Sep 30 2013 Brendan Jones <brendan.jones.it@gmail.com> 13.06-2
- Add appdata file
- Clean up changelog

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Brendan Jones <brendan.jones.it@gmail.com> 13.04-1
- Update to 13.04

* Wed Feb 13 2013 Brendan Jones <brendan.jones.it@gmail.com> 12.12.25-4
- Reinstate vendor for < 19

* Mon Feb 11 2013 Brendan Jones <brendan.jones.it@gmail.com> 12.12.25-3
- Correct sources

* Mon Feb 11 2013 Brendan Jones <brendan.jones.it@gmail.com> 12.12.25-2
- Remove desktop vendor
- Remove plugin path patch

* Thu Jan 10 2013 Brendan Jones <brendan.jones.it@gmail.com> 12.12.25-1
- Update to 12.12.25

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 10 2012 Brendan Jones <brendan.jones.it@gmail.com> - 12.04-1
- New upstream 12.04
- rmove gcc patch accepted upstream

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.11.42-2
- Rebuilt for c++ ABI breakage

* Tue Jan 17 2012 Brendan Jones <brendan.jones.it@gmail.com> - 11.11.42-1
- Patch for GCC 4.7 FTB
- New upstream 11.11.42

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.11.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 27 2011 Brendan Jones <brendan.jones.it@gmail.com> - 11.11.11-1
- Update to 11.11 and README
- Update spec to current guidelines

* Sun May 15 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 11.06-1
- Update to 11.06

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 03 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 11.02-1
- Update to 11.02

* Sat Nov 06 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 10.10-1
- Update to 10.10

* Tue Jul 20 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 10.04.2-2
- Rebuild against new liblo
- Fix the license file issue

* Sun May 09 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 10.04.2-1
- Update to 10.04.2
- Drop upstreamed qt-4.7 patch

* Thu Apr 22 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 10.04-1
- Update to 10.04
- BR qt-devel instead of kdelibs-devel
- Add release notes to %%doc
- Patch for build against qt-4.7

* Thu Feb 18 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 10.02.1-1
- Update to 10.02.1 (Qt4 version)

* Sat Feb 13 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.7.3-6
- Fix DSO linking RHBZ#564747

* Wed Nov 25 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.7.3-5
- Font subpackages are noarch
- Rebuild needed (something broke the ABI?)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 07 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.7.3-3
- The software makes use of kdialog. Thus we re-add Requires: kdebase.

* Sat Mar 07 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.7.3-2
- Add Requires: perl-XML-Twig. RHBZ#468919
- Fix the lilypondview script. RHBZ#464046
- Separate fonts to their own subpackages RHBZ#477450

* Fri Mar 06 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.7.3-1
- New upstream version.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Apr 02 2008 Rex Dieter <rdieter@fedoraproject.org> -  1.6.1-2
- fix rawhide build (#434424)
- drop: Requires: kdebase3 (don't want a hard dep here)
- drop scriptlet deps (undesirable)
- fix 64bit platform %%if

* Wed Feb 13 2008 Callum Lerwick <seg@haxxed.com> - 1.6.1-1
- New upstream version.

* Wed Dec 12 2007 Callum Lerwick <seg@haxxed.com> - 1.6.0-1
- New upstream version.
- Patch cmakelists to use our optflags. (bz330631)

* Wed May 02 2007 Callum Lerwick <seg@haxxed.com> - 1.5.1-1
- New upstream version.

* Tue Feb 13 2007 Callum Lerwick <seg@haxxed.com> - 1.5.0-1
- New upstream version.

* Sat Nov 11 2006 Callum Lerwick <seg@haxxed.com> - 1.4.0-1
- New upstream version.

* Tue Sep 05 2006 Callum Lerwick <seg@haxxed.com> - 1.2.3-5
- Bump for FC6 mass rebuild.

* Sun Jul 23 2006 Callum Lerwick <seg@haxxed.com> - 1.2.3-4
- Add dependency on kdebase so help works.

* Sun Jul 16 2006 Callum Lerwick <seg@haxxed.com> - 1.2.3-3
- Look for DSSI plugins in the correct place on x86_64.
- Add gettext BR.

* Sat Jun 17 2006 Callum Lerwick <seg@haxxed.com> - 1.2.3-2
- Removed which from Buildrequires, mock needing it is confirmed to be a bug.
- Use find_lang macro.
- Look for ladspa plugins in the correct place on x86_64.
- Build against liblo, jack, dssi, lirc.
- Salvage the upstream desktop file, rather than using our own.

* Sat Apr 15 2006 Callum Lerwick <seg@haxxed.com> - 1.2.3-1
- Initial packaging for Extras.
