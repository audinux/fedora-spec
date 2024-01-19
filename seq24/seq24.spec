# Tag: Sequencer, MIDI
# Type: Standalone
# Category: Audio, Sequencer, MIDI

Summary: Real-time midi sequencer
Name: seq24
Version: 0.9.3
Release: 8%{?dist}
License: GPL-2.0-or-later
URL: http://launchpad.net/%{name}

Vendor:       Audinux
Distribution: Audinux

Source: http://launchpad.net/%{name}/trunk/%{version}/+download/seq24-%{version}.tar.bz2
Source1: %{name}.png
Source2: %{name}.desktop

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lash-devel
BuildRequires: gtkmm24-devel
BuildRequires: desktop-file-utils

Requires: hicolor-icon-theme

%description
Seq24 is a real-time midi sequencer. It provides a very simple
interface for editing and playing midi 'loops'.

%prep
%autosetup

%if "%{version}" == "0.9.3"
# Bug in 0.9.3 and 0.9.3 prereleases
# class "mutex" in src/* clashes with "std::mutex" due
# to "using namespace std;". Rename mutex to seq24_mutex.
sed -i \
  -e 's,mutex::,seq24_mutex::,' \
  -e 's,\([ cs]\) mutex,\1 seq24_mutex,' \
  -e 's,::mutex,::seq24_mutex,' \
   src/*.h src/*.cpp
%endif

%build

%configure --enable-jack-session --disable-lash
%make_build

%install

%make_install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -m 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications    \
  %{SOURCE2}

%files
%doc AUTHORS ChangeLog README RTC SEQ24 TODO seq24usr.example
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/man/man1/%{name}.1.gz

%changelog
* Mon Sep 7 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-9
- fixes for Fedora 31

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.3-5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 18 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.9.3-1
- Update to 0.9.3 (final).
- Rename "mutex" to seq24_mutex to work-around symbol clash with std::mutex
  (F24FTBS, RHBZ#1308125).
- Add %%license.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-0.10.r131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-0.9.r131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.3-0.8.r131
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-0.7.r131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-0.6.r131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-0.5.r131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.9.3-0.4.r131
- Only remove vendor on F19+

* Mon Feb 11 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.9.3-0.3.r131
- Remove vendor from desktop-file-install

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-0.2.r131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Feb 18 2012 Brendan Jones <brendan.jones.it@gmail.com> - 0.9.3-0.1.r127
- upstream trunk

* Mon Nov 14 2011 Brendan Jones <brendan.jones.it@gmail.com> - 0.9.2-1
- New upstream version 0.9.2
- Removed obsolete tags and and sections

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 23 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.8.7-17
- Update desktop file according to F-12 FedoraStudio feature
- Update scriptlets

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 28 2008 Matt Domsch <mdomsch@fedoraproject.org> - 0.8.7-14
- remove patch fuzz from gcc43 patch

* Fri Jul 11 2008 Anthony Green <green@redhat.com> 0.8.7-13
- Add buffer overflow fix.

* Fri Jun 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.8.7-12
- Fix license tag
- Fix compile against libsigc++ 2.2

* Mon Mar 03 2008 Anthony Green <green@redhat.com> 0.8.7-11
- Update gcc 4.3 patch.

* Thu Feb 28 2008 Anthony Green <green@redhat.com> 0.8.7-10
- Update for gcc 4.3.

* Tue Oct 09 2007 Anthony Green <green@redhat.com> 0.8.7-8
- Rebuilt for new lash again.

* Mon Oct 08 2007 Anthony Green <green@redhat.com> 0.8.7-7
- Rebuilt for new lash.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.8.7-6
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 26 2006 Anthony Green <green@redhat.com> 0.8.7-5
- Rename "dump" to "seq-dump".
- Simplify description.

* Mon Sep 25 2006 Anthony Green <green@redhat.com> 0.8.7-4
- Fix SOURCE reference.
- Add TODO and seq24usr.example to docs.
- Clean up macro usage.

* Tue Sep 19 2006 Anthony Green <green@redhat.com> 0.8.7-3
- Remove Require(post,postun) for gtk2, as per the packaging
  guidelines.

* Tue Sep 19 2006 Anthony Green <green@redhat.com> 0.8.7-2
- Install the icon in the hicolor tree.
- Require hicolor-icon-theme.
- Add dist tag to Release.
- Fix post/postun scripts and Requires.

* Sat Sep 16 2006 Anthony Green <green@redhat.com> 0.8.7-1
- updated to 0.8.7.
- first Fedora build.
- clean up Requires and BuildRequires.
- move .desktop file to %%{SOURCE2}.
- add stack-smash preventing patch.
- add %%post and %%postun scriptlets.

* Sat May  6 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.8.6-1
- updated to 0.8.6
- added Planet CCRMA categories to desktop file, added icon

* Fri Mar 31 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.8.4-1
- updated to 0.8.4
- added dependency for building on fc5
- add generic bindir file list, includes new "dump" command
- added lash support

* Wed May  4 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.3-1
- updated to 0.6.3

* Tue Mar 22 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.2-1
- updated to 0.6.2

* Fri Jan 21 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.0-1
- updated to 0.6.0, now requires gtkmm2

* Sun Dec 19 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- spec file cleanup

* Sun Aug 29 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.2-1
- updated to 0.5.2

* Thu Jul 29 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.1-1
- updated to 0.5.1

* Wed May  5 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.0-2
- fixed missing defattr in file list

* Wed May  5 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.0-1
- updated to 0.5.0

* Wed Jan 21 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.4-1
- updated to 0.4.4

* Thu Nov 20 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.2-1
- spec file tweaks, add release tags

* Mon May 19 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.2-1
- updated to 0.4.2

* Wed Mar 19 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.1-1
- initial build
