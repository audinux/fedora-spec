# Tag: Jack, Editor, Analyzer
# Type: Standalone
# Category: Tool, Audio

Name: jamin
Summary: JACK Audio Connection Kit (JACK) Audio Mastering interface
Version: 0.98.9
Release: 2%{?dist}
License: GPL-2.0-or-later
URL: http://jamin.sourceforge.net

Vendor:       Audinux
Distribution: Audinux

Source0: https://salsa.debian.org/multimedia-team/jamin/-/archive/upstream/0.98.9_git20170111_199091_repack1/jamin-upstream-0.98.9_git20170111_199091_repack1.tar.gz#/%{name}-%{version}.tar.gz
Patch0: 1003_add_dynamic_linking.patch
Patch1: 1004_install_correct_dir.patch
Patch2: 1005_desktop_file.patch
Patch3: add-potfiles.patch
Patch4: fix_typos.patch
Patch5: jamin-gcc10.patch
Patch6: jamin-spectrum.patch
Patch7: NEWS.patch

BuildRequires: gcc make
BuildRequires: autoconf
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: libtool
BuildRequires: fftw-devel
BuildRequires: gtk3-devel
BuildRequires: pkgconfig(jack)
BuildRequires: ladspa-devel
BuildRequires: liblo-devel
BuildRequires: libxml2-devel
BuildRequires: perl-XML-Parser
BuildRequires: desktop-file-utils

Requires:      ladspa-swh-plugins
# Add ladspa-foo (not packaged anymore) as a Requires

%description
JAMin is the JACK Audio Connection Kit (JACK) Audio Mastering interface. JAMin
is designed to perform professional audio mastering of any number of input
streams. It uses LADSPA for its backend DSP work, specifically the swh plugins.

%prep
%autosetup -p1 -n jamin-upstream-0.98.9_git20170111_199091_repack1

%build

NOCONFIGURE=indeed ./autogen.sh
%configure
%make_build

%install

%make_install

# move icon to the proper freedesktop location
install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
mv %{buildroot}%{_datadir}/icons/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=JAMin
Name[cz]=JAMin
Name[fr]=JAMin
Name[ru]=JAMin
GenericName=Jack Audio Mastering
Comment=JACK Audio Mastering interface
Comment[cz]=JACK Audio Mastering interface
Comment[fr]=Interface de masterisation JACK Audio
Comment[ru]=JAMin -- приложение для мастеринга звука
Keywords=audio;sound;mastering;ladspa
Exec=jamin
Icon=jamin
MimeType=application/x-jamin;
StartupNotify=true
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

# Kill .la file(s)
rm -f %{buildroot}%{_libdir}/ladspa/*.la

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS ChangeLog TODO
%license COPYING
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_mandir}/man1/%{name}*
%{_libdir}/ladspa/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/mime/packages/%{name}.xml

%changelog
* Thu Mar 02 2023 Yann Collette <ycollette.nospam@free.fr> - 0.98.9-2
- fix desktop file

* Wed Mar 01 2023 Yann Collette <ycollette.nospam@free.fr> - 0.98.9-1
- update to last debian package + patches

* Wed Oct 14 2020 Yann Collette <ycollette.nospam@free.fr> - 0.97.16-21.20201014cvs
- update for fedora 33

* Sat Feb 01 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.97.16-21.20111031cvs
- Fix FTBFS with GCC 10
- Some spec cleanup

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.16-20.20111031cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.16-19.20111031cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.16-18.20111031cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.16-17.20111031cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.16-16.20111031cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.97.16-15.20111031cvs
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.16-14.20111031cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.16-13.20111031cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.16-12.20111031cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.16-11.20111031cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97.16-10.20111031cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 0.97.16-9.20111031cvs
- update mime scriptlet

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97.16-8.20111031cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97.16-7.20111031cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97.16-6.20111031cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97.16-5.20111031cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97.16-4.20111031cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97.16-3.20111031cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 5 2011 Brendan Jones <brendan.jones.it@gmail.com> - 0.97.16-2.20111031cvs
- Rebuild for libpng 1.5

* Mon Oct 31 2011 Brendan Jones <brendan.jones.it@gmail.com> - 0.97.16-1.20111031cvs
- Update to latest svn revision

* Tue Jul 20 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.95.0-9.20100210cvs
* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.0-10.20100210cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 20 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.95.0-9.20100210cvs
- Rebuild against new liblo

* Wed Feb 10 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.95.0-8.20100210cvs
- Update to the latest cvs
- Fix DSO-linking failure

* Wed Aug 05 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.95.0-7
- Update .desktop file

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 07 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.95.0-5
- Suppress double ./configure (in autogen.sh)
- Clean up unnecessary BR's
- Minor SPEC file update for macro consistency
- Update description

* Fri Mar 06 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.95.0-4
- Respin for Fedora (SPEC file borrowed from PlanetCCRMA)

* Tue Nov 25 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- run autogen.sh for fc10

* Wed Nov 14 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- updated desktop categories

* Wed Dec  6 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.95.0-3
- spec file tweaks
- move icon to proper freedesktop location, add post/postun scripts
- add patch for ladspa plugin directory, added autoconf & friends build
  requirement (borrowed from SuSE source package)
- add patch for default plugin search directory in x86_64 (it is hardwired
  in the plugin.c file)

* Mon May  6 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.95.0-2
- added Planet CCRMA categories

* Wed May  4 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.95.0-1
- updated to 0.95.0, fixed file list, added icon to desktop entry

* Tue Dec 21 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- spec file cleanup

* Mon Aug  9 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.17-0.cvs.1
- switched to jamin cvs, the 0.9.0 version does not work with the
  newer versions of liblo

* Mon Aug  9 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.0-1
- udpated to final 0.9.0 release
- added liblo requirement, fixed file list

* Fri Jul 30 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.0-0.beta10.1
- updated to the latest beta tarball (0.8.0 does not work with the
  newest swh-plugins)

* Sat May  8 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- added proper buildrequires

* Mon Jan 12 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.8.0-1
- updated to 0.8.0 (first stable release)

* Mon Dec 15 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.0-0.cvs.1
- initial build.
- added menu entry
