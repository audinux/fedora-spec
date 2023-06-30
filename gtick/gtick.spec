Name: gtick
Version: 0.5.4
Release: 11%{?dist}
License: GPLv3+
Summary: Metronome application
URL: http://www.antcom.de/gtick/

Source0: http://www.antcom.de/gtick/download/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: gtk2-devel
BuildRequires: glib2-devel
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick
BuildRequires: libsndfile-devel >= 1
BuildRequires: pulseaudio-libs-devel

%description
gtick is a small metronome application written for Linux and UN*X supporting
different meters (2/4, 3/4, 4/4) and speeds ranging from 30 to 250 bpm. It
utilizes GTK+ and OSS (ALSA compatible) or Pulseaudio.

%prep
%setup -q

%build
%configure --with-sndfile
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

desktop-file-edit \
    --set-generic-name="Graphical Metronome" \
    --set-key=X-GNOME-FullName --set-value="GTick (Graphical Metronome)" \
    --set-comment="Keep a steady tempo when you play music" \
    --set-key=Exec --set-value=gtick \
    --set-icon=gtick \
    --set-key=StartupNotify --set-value=true \
    %{buildroot}%{_datadir}/applications/gtick.desktop

rm -f %{buildroot}%{_datadir}/icons/hicolor/*/apps/gtick.xpm
rm -f %{buildroot}%{_datadir}/pixmaps/gtick_32x32.xpm

for res in 32 48 64; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${res}x${res}/apps
    convert src/icon${res}x${res}.xpm \
        %{buildroot}%{_datadir}/icons/hicolor/${res}x${res}/apps/gtick.png
done

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING doc/NOTES NEWS README THANKS TODO
%doc %{_mandir}/man1/gtick.1*
%{_bindir}/gtick
%{_datadir}/applications/gtick.desktop
%{_datadir}/appdata/gtick.appdata.xml
%{_datadir}/icons/hicolor/*/apps/gtick.png

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Nils Philippsen <nils@tiptoe.de> - 0.5.4-7
- require gcc for building

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.4-5
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Mar 18 2016 Nils Philippsen <nils@redhat.com> - 0.5.4-1
- version 0.5.4
- change license to GPLv3+ in accordance with the sources
- remove obsolete AOSS wrapper completely
- ship PNG icons built from original XPM files
- edit original desktop file rather than installing our own
- ship appdata file
- clean up packaging

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Nils Philippsen <nils@redhat.com> - 0.5.1-2
- don't wrap in aoss, just use plain pulseaudio from Fedora 19 on
- clean up desktop file

* Thu Feb 28 2013 Nils Philippsen <nils@redhat.com> - 0.5.1-1
- enable external ticking sounds (build with libsndfile)
- don't crash if no valid "other" sound file is chosen
- delete old specfile metadata comments

* Wed Feb 27 2013 Dave Allan <dallan@redhat.com> - 0.5.1-1
- Updated to release 0.5.1.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 10 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.4.2-9
- Modify desktop to use aoss

* Wed Oct 10 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.4.2-8
- Add alsa-oss requires

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.4.2-5
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jun 21 2010 Rangeen Basu Roy Chowdhury <sherry151@fedoraproject.org> - 0.4.2-3
- Updated the .desktop file
- Completed the scriptlets for icon-cache update
- Removed macros
- Removed unnecessary BuildRequires

* Sat Jun 19 2010 Rangeen Basu Roy Chowdhury <sherry151@fedoraproject.org> - 0.4.2-2
- Updated the .desktop file
- Removed gtickpadsp. Gtick runs only with OSS or with OSS emulation from terminal
- Added gtick.png as a source

* Fri Jun 18 2010 Rangeen Basu Roy Chowdhury <sherry151@fedoraproject.org> - 0.4.2-1
- Initial Fedora Package
- Updated to release 0.4.2
- Based on the spec from DAG

* Sun Aug 19 2007 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Updated to release 0.4.1.

* Thu Aug 16 2007 Dag Wieers <dag@wieers.com> - 0.4.0-1
- Updated to release 0.4.0.

* Tue May 08 2007 Dries Verachtert <dries@ulyssis.org> - 0.3.15-1
- Updated to release 0.3.15.

* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.3.14-1
- Updated to release 0.3.14.

* Mon Feb 12 2007 Dries Verachtert <dries@ulyssis.org> - 0.3.13-1
- Updated to release 0.3.13.

* Sat Oct 28 2006 Dag Wieers <dag@wieers.com> - 0.3.12-1
- Updated to release 0.3.12.

* Sat Sep 30 2006 Dag Wieers <dag@wieers.com> - 0.3.11-1
- Updated to release 0.3.11.

* Fri May 19 2006 Dag Wieers <dag@wieers.com> - 0.3.10-1
- Updated to release 0.3.10.

* Sun Mar 19 2006 Dag Wieers <dag@wieers.com> - 0.3.9-1
- Updated to release 0.3.9.

* Tue Mar 07 2006 Dag Wieers <dag@wieers.com> - 0.3.8-1
- Updated to release 0.3.8.

* Wed Nov 30 2005 Dag Wieers <dag@wieers.com> - 0.3.7-1
- Updated to release 0.3.7.

* Sun Feb 06 2005 Dag Wieers <dag@wieers.com> - 0.3.5-1
- Updated to release 0.3.5.

* Wed Jun 16 2004 Dag Wieers <dag@wieers.com> - 0.3.2-1
- Updated to release 0.3.2.

* Fri Apr 30 2004 Dag Wieers <dag@wieers.com> - 0.3.1-1
- Updated to release 0.3.1.

* Wed Mar 03 2004 Dag Wieers <dag@wieers.com> - 0.3.0-0
- Updated to release 0.3.0.

* Mon Jan 26 2004 Dag Wieers <dag@wieers.com> - 0.2.14-0
- Updated to release 0.2.14.

* Mon Dec 29 2003 Dag Wieers <dag@wieers.com> - 0.2.12-0
- Updated to release 0.2.12.

* Mon Dec 15 2003 Dag Wieers <dag@wieers.com> - 0.2.11-0
- Updated to release 0.2.11.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 0.2.8-0
- Updated to release 0.2.8.

* Sat Nov 01 2003 Dag Wieers <dag@wieers.com> - 0.2.7-0
- Updated to release 0.2.7.

* Mon Oct 13 2003 Dag Wieers <dag@wieers.com> - 0.2.6-0
- Updated to release 0.2.6.

* Wed Oct 01 2003 Dag Wieers <dag@wieers.com> - 0.2.5-0
- Updated to release 0.2.5.

* Wed Sep 10 2003 Dag Wieers <dag@wieers.com> - 0.2.4-0
- Updated to release 0.2.4.

* Sat Aug 30 2003 Dag Wieers <dag@wieers.com> - 0.2.3-0
- Updated to release 0.2.3.

* Mon Jul 28 2003 Dag Wieers <dag@wieers.com> - 0.2.2-0
- Updated to release 0.2.2.

* Tue Jun 24 2003 Dag Wieers <dag@wieers.com> - 0.2.1-0
- Initial package. (using DAR)
