# Tag: Jack
# Type: Standalone
# Category: Audio, Tool

Summary: Allows control over JACK transport via Midi
Name: jackctlmmc
Version: 4
Release: 22%{?dist}
License: GPL-2.0-only
URL: https://sourceforge.net/projects/%{name}
ExclusiveArch: x86_64 aarch64

Source0: https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: qt-devel
BuildRequires: pkgconfig(jack)
BuildRequires: desktop-file-utils

%description
A small application that allows the user to control JACK transport via Midi
Machine Control (MMC) commands. MMC is a common protocol sent by hard disk
recorders and midi control pads to let other devices or programs know where you
are in a track.

%package -n qjackmmc
License: GPL-2.0-or-later
Summary: Qt application that controls JACK transport via Midi

%description -n qjackmmc
QJackMMC is a Qt based program that can connect to a device or program that
emits MIDI Machine Control (MMC) and allow it to drive JACK transport, which in
turn can control other programs. QJackMMC is the Qt version of jackctlmmc.

%prep

%autosetup -n %{name}

# Fix encoding issues
for file in  AUTHORS README NEWS VERSION TODO gpl.txt; do
   sed 's|\r||' $file > $file.tmp
   iconv -f ISO-8859-1 -t UTF8 $file.tmp > $file.tmp2
   touch -r $file $file.tmp2
   mv -f $file.tmp2 $file
done

%build
%configure --enable-gui=yes --enable-cli=yes
%make_build

%install
%make_install

desktop-file-install                                       \
   --add-category="Midi"                                   \
   --add-category="X-Alsa"                                 \
   --add-category="X-Jack"                                 \
   --remove-category="MIDI"                                \
   --remove-category="ALSA"                                \
   --remove-category="JACK"                                \
   --dir=%{buildroot}%{_datadir}/applications              \
      %{buildroot}/%{_datadir}/applications/qjackmmc.desktop

%files
%doc AUTHORS README NEWS VERSION TODO
%license gpl.txt
%{_bindir}/%{name}

%files -n qjackmmc
%license gpl.txt
%{_bindir}/qjackmmc
%{_datadir}/applications/qjackmmc.desktop
%{_datadir}/pixmaps/qjackmmc.png

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4-10
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild


* Sat Aug 06 2011 Brendan Jones <brendan.jones.it@gmail.com> 4-3
- add License to sub-package

* Mon May 30 2011 Brendan Jones <brendan.jones.it@gmail.com> 4-2
- invalidate installed desktop file, removing sed statements

* Mon May 30 2011 Brendan Jones <brendan.jones.it@gmail.com> 4-1
- initial build

