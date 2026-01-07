# Status: active
# Tag: Jack, Alsa
# Type: Plugin, Standalone, LV2
# Category: Audio, Synthesizer

Name: qmidiarp
Summary: An arpeggiator, sequencer and MIDI LFO for ALSA
Version: 0.7.3
Release: 21%{?dist}
License: GPL-2.0-or-later
URL: https://sourceforge.net/projects/qmidiarp 
Source0: https://downloads.sourceforge.net/qmidiarp/files/%{name}-%{version}.tar.bz2

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-linguist
BuildRequires: liblo-devel
BuildRequires: pkgconfig(jack)
BuildRequires: lv2-devel
BuildRequires: desktop-file-utils

Requires: hicolor-icon-theme

%description
QMidiArp is a MIDI phrase generator and controller LFO for the ALSA sequencer. 
It can run multiple synchronized arpeggiators, LFOs and step sequencers. 
QMidiArp has been growing since June 2009 on top of Matthias Nagorni's original 
arp idea.  

%package -n lv2-qmidiarp 
Summary: LV2 plugins of the QMidiArp MIDI arpeggiator, sequencer and LFO

%description -n lv2-qmidiarp
lv2-qmidiarp contains LV2 versions of the QMidiArp's LFO, ARP and sequencer

%prep

%autosetup 

# Fix encoding issues
for file in ChangeLog AUTHORS README COPYING NEWS; do
   sed 's|\r||' $file > $file.tmp
   iconv -f ISO-8859-1 -t UTF8 $file.tmp > $file.tmp2
   touch -r $file $file.tmp2
   mv -f $file.tmp2 $file
done

%build

%set_build_flags
export LDFLAGS="`pkg-config --libs-only-L jack` $LDFLAGS"

%configure --enable-nsm 
%make_build

%install

%make_install

%files 
%doc AUTHORS ChangeLog README NEWS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/de/man1/%{name}.1.*
%{_mandir}/fr/man1/%{name}.1.*
%{_mandir}/man1/%{name}.1.*
%{_datadir}/metainfo/%{name}*

%files -n lv2-qmidiarp
%{_libdir}/lv2/qmidiarp*

%changelog
* Tue Jan 06 2026 Yann Collette <ycollette.nospam@free.fr> - 0.7.3-21
- update to 0.7.3-21

* Wed Dec 31 2025 Yann Collette <ycollette.nospam@free.fr> - 0.7.2-21
- update to 0.7.2-21

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav SuchÃ½ <msuchy@redhat.com> - 0.6.5-19
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.5-3
- Remove obsolete scriptlets

* Mon Dec 25 2017 Brendan Jones <brendan.jones.it@gmail.com> - 0.6.5-2
- Use qt5-devel

* Sun Dec 24 2017 Brendan Jones <brendan.jones.it@gmail.com> - 0.6.5-1
- Update to 0.6.5

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 20 2015 Brendan Jones <brendan.jones.it@gmail.com> 0.6.3-1
- Update to 0.6.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Sep 25 2014 Brendan Jones <brendan.jones.it@gmail.com> 0.6.1-1
- Update to 0.6.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 13 2014 Brendan Jones <brendan.jones.it@gmail.com> 0.6.0-2
- Add missing BR

* Mon Jan 13 2014 Brendan Jones <brendan.jones.it@gmail.com> 0.6.0-1
- add LV2 plugins
- update to 0.6.0

* Wed Dec 04 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.5.3-1
- Update to 0.5.3

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 22 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.5.2-2
- Enable nsm support

* Wed May 22 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.5.2-1
- New upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.5.1-1
- New upstream release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 25 2012 Brendan Jones <brendan DOT jones DOT it AT gmail DOT com> 0.5.0-1
- Updated to 0.5.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 24 2011 Brendan Jones <brendan DOT jones DOT it AT gmail DOT com> 0.4.4-2
- Upstream issued new tarball without release bump

* Sat Dec 24 2011 Brendan Jones <brendan DOT jones DOT it AT gmail DOT com> 0.4.4-1
- Updated to 0.4.4
- Removed fsf patch

* Sun Nov 20 2011 Brendan Jones <brendan DOT jones DOT it AT gmail DOT com> 0.4.3-1
- Updated to 0.4.3
- patch fsf address

* Sun Jul 10 2011 Brendan Jones <brendan DOT jones DOT it AT gmail DOT com> 0.4.2-1
- Updated to 0.4.2

* Mon May 30 2011 Brendan Jones <brendan DOT jones DOT it AT gmail DOT com> 0.4.1-1
- Updated to 0.4.1

* Thu Feb 24 2011 Brendan Jones <brendan DOT jones DOT it AT gmail DOT com> 0.3.9-6
- corrected use of name macro 

* Thu Feb 24 2011 Brendan Jones <brendan DOT jones DOT it AT gmail DOT com> 0.3.9-5
- corrected use of name macro 

* Tue Feb 22 2011 Brendan Jones <brendan DOT jones DOT it AT gmail DOT com> 0.3.9-4
- additional spacing in SPEC file

* Wed Feb 16 2011 Brendan Jones <brendan DOT jones DOT it AT gmail DOT com> 0.3.9-3
- correct icon cache directory

* Wed Feb 16 2011 Brendan Jones <brendan DOT jones DOT it AT gmail DOT com> 0.3.9-2
- correct sourceforge URL, mime database update and other minor corrections

* Mon Feb 07 2011 Brendan Jones <brendan DOT jones DOT it AT gmail DOT com> 0.3.9-1
- initial build 

