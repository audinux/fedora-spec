Summary: Software Synthesizer
Name:    amsynth
Version: 1.12.4
Release: 3%{?dist}
License: GPL
URL:     https://github.com/amsynth/amsynth

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/amsynth/amsynth/archive/release-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: gtkmm24-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsndfile-devel
BuildRequires: dssi-devel
BuildRequires: liblo-devel
BuildRequires: lash-devel
BuildRequires: lv2-devel
BuildRequires: pandoc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gettext-devel
BuildRequires: intltool

%description
amSynth is a software synthesizer, taking inspiration from the
original synths and latest digital ones, while keeping an intuitive
interface.

%package -n lv2-amsynth
Summary: amsynth lv2 plugin

%description -n lv2-amsynth
Amsynth LV2 plugin

%package -n vst-amsynth
Summary: amsynth vst plugin

%description -n vst-amsynth
Amsynth VST plugin

%package -n dssi-amsynth
Summary: amsynth DSSI plugin

%description -n dssi-amsynth
Amsynth DSSI plugin

%prep
%autosetup -n %{name}-release-%{version}

sed -i -e "s/AX_CXX_COMPILE_STDCXX_11/#AX_CXX_COMPILE_STDCXX_11/g" configure.ac

%build

./autogen.sh
export CXXFLAGS="-fPIC -std=c++11"
%configure
%make_build

%install

%make_install

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc AUTHORS ChangeLog INSTALL NEWS README
%license COPYING
%{_bindir}/amsynth
%{_datadir}/amsynth/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/amsynth.png
%{_datadir}/icons/hicolor/scalable/apps/amsynth.svg
%{_datadir}/locale/*
%{_datadir}/appdata/*
%{_mandir}/*

%files -n dssi-amsynth
%{_libdir}/dssi/*

%files -n lv2-amsynth
%{_libdir}/lv2/*

%files -n vst-amsynth
%{_libdir}/vst/*

%changelog
* Sat Jan 08 2022 Yann Collette <ycollette dot nospam at free.fr> 1.12.4-3
- update to 1.12.4-3

* Sat Jan 01 2022 Yann Collette <ycollette dot nospam at free.fr> 1.12.3-3
- update to 1.12.3-3

* Fri Nov 05 2021 Yann Collette <ycollette dot nospam at free.fr> 1.12.2-3
- update to 1.12.2-3 - install desktop file

* Sat Nov 21 2020 Yann Collette <ycollette dot nospam at free.fr> 1.12.2-2
- update to 1.12.2-2

* Sat Nov 14 2020 Yann Collette <ycollette dot nospam at free.fr> 1.12.1-2
- update to 1.12.1-2

* Mon Nov 09 2020 Yann Collette <ycollette dot nospam at free.fr> 1.12.0-2
- update to 1.12.0-2

* Sun Sep 20 2020 Yann Collette <ycollette dot nospam at free.fr> 1.11.0-2
- update to 1.11.0-2

* Sat May 9 2020 Yann Collette <ycollette dot nospam at free.fr> 1.10.0-1
- update to 1.10.0-1

* Sun Apr 14 2019 Yann Collette <ycollette dot nospam at free.fr> 1.9.0-1
- update to 1.9.0-1

* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free.fr> 1.8.0-1
- update for Fedora 29

* Tue Oct 24 2017 Yann Collette <ycollette dot nospam at free.fr> 1.8.0-1
- update to 1.8.0-1

* Thu Jun 04 2015 Yann Collette <ycollette dot nospam at free.fr> 1.5.1-1
- updated to 1.5.1-1
- added a DSSI package
- added a LV2 package

* Mon Aug 06 2012 Martin Tarenskeen <m.tarenskeen at zonnet.nl> 1.3.1-1
- updated to 1.3.1
- removed old patches (now fixed upstream)
- small patch to include unistd.h in Config.cc
- dssi version included

* Tue Jan  2 2007 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.2.0-1
- updated to 1.2.0, fixed install target for skeleton files (they
  install in /usr/share instead of /usr/share/amsynth)

* Fri Nov 24 2006 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.1.0-0.4.cvs
- spec file tweaks, use separate desktop file

* Thu Aug 24 2006 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.1.0-0.3.cvs
- wrong group (typo: Application instead of Applications, thanks to jos
  for the tip)

* Fri Jul 14 2006 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.1.0-0.2.cvs
- added explicit gtkmm24 requires for gtkmm24, keeping the previous version
  allows amsynth to install but it does not run

* Mon Jun 19 2006 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.1.0-0.2.cvs
- added Planet CCRMA categories to desktop file

* Wed Jan 25 2006 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.1.0-0.1.cvs
- updated to 1.1.0, uses gtkmm2
- needs a cvs snapshot and a patch for the gtkmm include and signal.h include

* Fri Feb 18 2005 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.0.0-3
- do not install main executable suid root

* Fri Dec 24 2004 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.0.0-2
- use rpm optimization flags

* Mon Dec 20 2004 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 
- spec file cleanup

* Sat May  8 2004 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 
- added proper buildrequires

* Tue Mar  2 2004 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.0.0-1
- bumped epoch to 1 to transition from 1.0rc4 to 1.0.0 (darn...)

* Sun Feb 29 2004 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.0.0-1
- updated to 1.0.0

* Wed Nov 12 2003 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.0rc4-1
- added release tags, spec file tweaks
- added patch1 with defines for using old alsa API

* Sat Jul 26 2003 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.0rc4-1
- updated t0 1.0rc4

* Wed Apr  2 2003 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.0rc2-2
- rebuild for jack 0.66.3, added explicit requires for it

* Mon Jan 27 2003 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.0rc2-1
- added patch to make it compile on 7.3

* Sun Jan 26 2003 Fernando Lopez-Lezcano <nando at ccrma.stanford.edu> 1.0rc2-1
- Initial build.
