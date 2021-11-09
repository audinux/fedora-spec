Name:    jamin
Summary: JACK Audio Connection Kit (JACK) Audio Mastering interface
Version: 0.97.16
Release: 21.20201014cvs%{?dist}
License: GPLv2+
URL:     http://jamin.sourceforge.net

Source0: %{name}-%{version}-20201014cvs.tar.bz2
# To fetch the sources:
Source1: %{name}-snapshot.sh
# Fix DSO-linking failure
# http://sourceforge.net/tracker/?func=detail&aid=2948900&group_id=78441&atid=553292
Patch0:  %{name}-linking.patch
# Spectrum views enhancement & small eq fixes
# http://sourceforge.net/tracker/?func=detail&aid=1902205&group_id=78441&atid=553292
Patch1:  %{name}-spectrum.patch
# Fix FTBFS with GCC 10
Patch2:  %{name}-gcc10.patch

BuildRequires: gcc make
BuildRequires: desktop-file-utils
BuildRequires: fftw-devel
BuildRequires: gettext
BuildRequires: gtk2-devel
BuildRequires: intltool
BuildRequires: jack-audio-connection-kit-devel 
BuildRequires: ladspa-devel
BuildRequires: liblo-devel
BuildRequires: libtool
BuildRequires: libxml2-devel 
BuildRequires: perl-XML-Parser 

Requires:      ladspa-swh-plugins

%description
JAMin is the JACK Audio Connection Kit (JACK) Audio Mastering interface. JAMin
is designed to perform professional audio mastering of any number of input
streams. It uses LADSPA for its backend DSP work, specifically the swh plugins.

%prep
%autosetup -p 1

# .desktop file fixes:
# Add GenericName
sed -i 's|\(GenericName=\)|\1Jack Audio Mastering|' data/%{name}.desktop.in

# Remove extension from the icon (as required by freedesktop.org)
sed -i 's|\.svg||' data/%{name}.desktop.in

%build

NOCONFIGURE=indeed ./autogen.sh
%configure
%make_build

%install

%make_install

# move icon to the proper freedesktop location
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
mv %{buildroot}%{_datadir}/icons/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

# desktop file categories
BASE="Audio"
XTRA="X-Multitrack X-DigitalProcessing X-Jack"

%{__mkdir} -p %{buildroot}%{_datadir}/applications
desktop-file-install                            \
  --dir %{buildroot}%{_datadir}/applications    \
  `for c in ${BASE} ${XTRA} ; do echo "--add-category $c " ; done` \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

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
