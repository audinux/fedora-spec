# Tag: Tracker, Jack, Alsa
# Type: Standalone
# Category: Audio, Sequencer

Name:          milkytracker
Version:       1.03.00
Release:       2%{?dist}
Summary:       Module tracker software for creating music
License:       GPLv3+
URL:           https://github.com/milkytracker/MilkyTracker

Vendor:       Audinux
Distribution: Audinux

Source0:       https://github.com/milkytracker/MilkyTracker/archive/v%{version}.tar.gz#/MilkyTracker-%{version}.tar.gz
Source1:       %{name}.desktop

BuildRequires: gcc gcc-c++
BuildRequires: SDL2-devel
BuildRequires: SDL2-static
BuildRequires: desktop-file-utils
BuildRequires: rtmidi-devel
BuildRequires: zlib-devel
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: cmake

Provides:      bundled(zziplib) = 0.13.47

%description
MilkyTracker is an application for creating music in the .MOD and .XM formats.
Its goal is to be free replacement for the popular Fasttracker II software.

%prep
%autosetup -n MilkyTracker-%{version}

%build

%cmake -DCMAKE_BUILD_TYPE=RELEASE

%cmake_build

%install

%cmake_install

# copy the icon
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp -p resources/pictures/carton.png %{buildroot}%{_datadir}/pixmaps/milkytracker.png

# copy the desktop file
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications/ %{SOURCE1}

%files
%defattr(-,root,root,-)
%doc AUTHORS NEWS README.md ChangeLog.md
%license COPYING
%{_bindir}/milkytracker
%{_datadir}/applications/*
%{_datadir}/pixmaps/milkytracker.png
%{_datadir}/milkytracker/
%{_datadir}/milkytracker/songs/*
%{_datadir}/doc/MilkyTracker/

%changelog
* Thu Dec 10 2020 Yann Collette <ycollette dot nospam at free dot fr> 1.03.00-2
- Update to 1.03.00-2

* Thu Oct 1 2020 Yann Collette <ycollette dot nospam at free dot fr> 1.02.00-2
- Update for Fedora 33

* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free dot fr> 1.02.00
- Update for Fedora 29

* Sun May 13 2018 Yann Collette <ycollette dot nospam at free dot fr> 1.02.00
* Tue Jun 28 2016 Joonas Sarajärvi <muep@iki.fi> - 0.90.86-3
- Rebuilt to make the package available after unretirement

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.86-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 Joonas Sarajärvi <muep@iki.fi> - 0.90.86-1
- Updated to new upstream release
- Use bundled copy of zziplib
- Zip file support was fixed (bz #1270882)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.85-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.90.85-10
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.85-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.85-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.85-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.90.85-6
- Remove the --vendor flag from desktop-file-install https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.85-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 03 2012 Joonas Sarajärvi <muep@iki.fi> - 0.90.85-4
- Fix build error from invalid C++ type conversions

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.85-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.85-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 08 2011 Joonas Sarajärvi <muepsj@gmail.com> - 0.90.85-1
- Update to upstream version 0.90.85
- Redo the build system tweaks to avoid using bundled zziplib
- Fix integer type errors

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.80-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.80-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.80-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri May 30 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.80-3
- Use system-wide zziplib (zlib is not used directly)

* Mon May 26 2008 Joonas Sarajärvi <muepsj@gmail.com> - 0.90.80-2
- Set Source0 to use macros for easier updating.
- Removed the --without-jack configuration option.
- Added -p to the cp command to preserve the timestamp.
- Replaced /usr/share with a macro.
- Added a line to prep to set correct permissions for source files extracted from the tarball.
- Modified a Makefile.am to not compile the included static zlib library.

* Sat May  3 2008 Joonas Sarajärvi <muepsj@gmail.com> - 0.90.80-1
- Initial RPM release.

