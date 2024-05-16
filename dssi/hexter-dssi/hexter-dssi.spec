# Tag: Synthesizer
# Type: Plugin, DSSI
# Category: Audio, Synthesizer, Plugin

%global srcname0 hexter

Summary: DSSI software synthesizer plugin emulating DX7
Name: hexter-dssi
Version: 1.1.0
Release: 4%{?dist}
URL: http://smbolton.com/hexter.html
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Source0: https://github.com/smbolton/%{srcname0}/archive/version_%{version}/%{srcname0}-version_%{version}.tar.gz
Source1: hexter.desktop
Source2: hexter.png
Patch0: Fixed-Segfault-on-startup.patch

BuildRequires: gcc
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: dssi-devel
BuildRequires: gtk2-devel
BuildRequires: liblo-devel
BuildRequires: ncurses-devel
BuildRequires: chrpath
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: make

Requires: dssi

%description
hexter is a software synthesizer that models the sound generation of a Yamaha
DX7 synthesizer. It can easily load most DX7 patch bank files, accept patch
editing commands via MIDI sys-ex messages (ALSA systems only), and recreate the
sound of the DX7 with greater accuracy than any previous open-source emulation
(that the author is aware of....)

hexter operates as a plugin for the Disposable Soft Synth Interface (DSSI).
DSSI is a plugin API for software instruments (soft synths) with user
interfaces, permitting them to be hosted in-process by audio applications.

%prep
%setup -q -n %{srcname0}-version_%{version}
%patch0 -p1

%build
export LDFLAGS="-lm"
./autogen.sh
%configure --with-gnu-ld
make %{?_smp_mflags}
(cd extra; gcc $CFLAGS -o tx_edit tx_edit.c -lcurses -lasound -lm)

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir -p $RPM_BUILD_ROOT%{_bindir}
ln -s jack-dssi-host $RPM_BUILD_ROOT%{_bindir}/hexter
install -m 755 extra/tx_edit $RPM_BUILD_ROOT%{_bindir}/tx_edit

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install                              \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
  %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/36x36/apps
install -pm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/36x36/apps/hexter.png

%files
%doc AUTHORS ChangeLog COPYING README.rst TODO
%{_bindir}/hexter
%{_bindir}/tx_edit
%{_datadir}/hexter/
%{_datadir}/applications/hexter.desktop
%{_datadir}/icons/hicolor/36x36/apps/hexter.png
%{_libdir}/dssi/*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 17 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.1.0-2
- Fix for GUI still not working

* Mon Mar 16 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.1.0-1
- New upstream release as of 2018-03-18

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-11
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 01 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.0.0-1
- New upstream release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.6.2-6
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 20 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.6.2-4
- Rebuild against new liblo

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 30 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.6.2-2
- Add a .desktop file

* Fri May 29 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.6.2-1
- Update to 0.6.2

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 31 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.6.1-3
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.6.1-2
- Autorebuild for GCC 4.3

* Sun Apr 15 2007 Anthony Green <green@redhat.com> 0.6.1-1
- Upgrade sources.

* Sun Dec 17 2006 Anthony Green <green@redhat.com> 0.5.9-8
- Fix typo in tx_edit install line.

* Sat Dec 16 2006 Anthony Green <green@redhat.com> 0.5.9-7
- Build and install tx_edit.
- Add relevant BuildRequires.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.5.9-6
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 Anthony Green <green@redhat.com> 0.5.9-5
- Fix release tag.

* Mon Sep 18 2006 Anthony Green <green@redhat.com> 0.5.9-4.1
- Rebuild.

* Wed Jul 12 2006 Anthony Green <green@redhat.com> 0.5.9-4
- Update Source0 link.
- Don't use %%makeinstall.  It's broken (?)
- Mention DX7 in Summary.

* Sun Jun  4 2006 Anthony Green <green@redhat.com> 0.5.9-3
- Remove useless post and postun scripts.
- Tweak hexter jack-dssi-host symlink.

* Thu May 18 2006 Anthony Green <green@redhat.com> 0.5.9-2
- Clean up Requires & BuildRequires.
- Don't use %%{__rm} & %%{__make}.
- Use %%makeinstall.
- Add hexter symlink.

* Tue Apr 25 2006 Anthony Green <green@redhat.com> 0.5.9-1
- Created.

