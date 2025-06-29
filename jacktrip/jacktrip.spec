# Status: active
# Tag: Jack
# Type: Standalone
# Category: Audio, Sampler, Tool

Summary: Multimachine jam sessions over the internet
Name: jacktrip
Version: 2.7.0
Release: 2%{?dist}
License: STK
URL: https://ccrma.stanford.edu/software/jacktrip/
ExclusiveArch: x86_64 aarch64

Vendor:       Planet CCRMA
Distribution: Planet CCRMA

# Usage: ./source-jacktrip.sh <tag>
#        ./source-jacktrip.sh v2.7.0

Source0: jacktrip.tar.gz
Source1: source-jacktrip.sh

BuildRequires: gcc gcc-c++
BuildRequires: meson
BuildRequires: git
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qt5compat-devel
BuildRequires: qt6-qtdeclarative-devel
BuildRequires: qt6-qtnetworkauth-devel
BuildRequires: qt6-qtquickcontrols2-devel
BuildRequires: qt6-qtsvg-devel
BuildRequires: qt6-qtwebsockets-devel
BuildRequires: qt6-qtwebengine-devel
BuildRequires: qt6-qtwebchannel-devel
BuildRequires: qt6-qtshadertools-devel
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: rtaudio-devel
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel
BuildRequires: python3-pyyaml
BuildRequires: python3-jinja2
BuildRequires: help2man
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

%description
JackTrip is a Linux and Mac OS X-based system used for multi-machine
network performance over the Internet. It supports any number of
channels (as many as the computer/network can handle) of
bidirectional, high quality, uncompressed audio signal steaming. You
can use it between any combination of Linux and Mac OS X (i.e., one
end using Linux can connect to the other using Mac OS X).

It is currently being developed and actively tested at CCRMA by the
SoundWIRE group.

%prep
%autosetup -n %{name}

%build

%meson --wrap-mode=default
%meson_build

%install

%meson_install

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/org.jacktrip.JackTrip.desktop

# cleanup

rm -f %{buildroot}/%{_libdir}/libsamplerate.a

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.jacktrip.JackTrip.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.jacktrip.JackTrip.metainfo.xml

%files
%doc README.md
%license LICENSE.md
%{_bindir}/jacktrip
%{_datadir}/icons/hicolor/*
%{_datadir}/applications/*
%{_datadir}/metainfo/*
%{_mandir}/man1/*

%changelog
* Sun Jun 29 2025 Yann Collette <ycollette.nospam@free.fr> - 2.7.0-2
- update to 2.7.0-2

* Wed Apr 23 2025 Yann Collette <ycollette.nospam@free.fr> - 2.6.0-2
- update to 2.6.0-2

* Fri Jan 31 2025 Yann Collette <ycollette.nospam@free.fr> - 2.5.1-2
- update to 2.5.1-2

* Wed Jan 22 2025 Yann Collette <ycollette.nospam@free.fr> - 2.5.0-2
- update to 2.5.0-2

* Sat Sep 28 2024 Yann Collette <ycollette.nospam@free.fr> - 2.4.1-2
- update to 2.4.1-2

* Sat Sep 14 2024 Yann Collette <ycollette.nospam@free.fr> - 2.4.0-2
- update to 2.4.0-2

* Sat Jul 27 2024 Yann Collette <ycollette.nospam@free.fr> - 2.3.1-2
- update to 2.3.1-2

* Thu May 16 2024 Yann Collette <ycollette.nospam@free.fr> - 2.3.0-2
- update to 2.3.0-2

* Mon Apr 01 2024 Yann Collette <ycollette.nospam@free.fr> - 2.2.5-2
- update to 2.2.5-2

* Thu Mar 14 2024 Yann Collette <ycollette.nospam@free.fr> - 2.2.4-2
- update to 2.2.4-2

* Mon Mar 04 2024 Yann Collette <ycollette.nospam@free.fr> - 2.2.3-2
- update to 2.2.3-2

* Sat Feb 10 2024 Yann Collette <ycollette.nospam@free.fr> - 2.2.2-2
- update to 2.2.2-2

* Tue Jan 30 2024 Yann Collette <ycollette.nospam@free.fr> - 2.2.1-2
- update to 2.2.1-2

* Mon Jan 22 2024 Yann Collette <ycollette.nospam@free.fr> - 2.2.0-2
- update to 2.2.0-2

* Sat Sep 02 2023 Yann Collette <ycollette.nospam@free.fr> - 2.0.2-2
- update to 2.0.2-2

* Wed Aug 30 2023 Yann Collette <ycollette.nospam@free.fr> - 2.0.1-2
- update to 2.0.1-2

* Mon Aug 28 2023 Yann Collette <ycollette.nospam@free.fr> - 2.0.0-2
- update to 2.0.0-2

* Fri Aug 04 2023 Yann Collette <ycollette.nospam@free.fr> - 1.10.1-2
- update to 1.10.1-2

* Sat Jun 17 2023 Yann Collette <ycollette.nospam@free.fr> - 1.10.0-2
- update to 1.10.0-2

* Sat May 13 2023 Yann Collette <ycollette.nospam@free.fr> - 1.9.0-2
- update to 1.9.0-2

* Tue Apr 04 2023 Yann Collette <ycollette.nospam@free.fr> - 1.8.1-2
- update to 1.8.1-2

* Sat  Mar 18 2023 Yann Collette <ycollette.nospam@free.fr> - 1.8.0-2
- update to 1.8.0-2

* Sun Feb 12 2023 Yann Collette <ycollette.nospam@free.fr> - 1.7.1-2
- update to 1.7.1-2

* Wed Jan 25 2023 Yann Collette <ycollette.nospam@free.fr> - 1.7.0-2
- update to 1.7.0-2

* Tue Dec 06 2022 Yann Collette <ycollette.nospam@free.fr> - 1.6.8-2
- update to 1.6.8-2

* Fri Dec 02 2022 Yann Collette <ycollette.nospam@free.fr> - 1.6.7-2
- update to 1.6.7-2

* Thu Nov 03 2022 Yann Collette <ycollette.nospam@free.fr> - 1.6.6-2
- update to 1.6.6-2

* Fri Oct 28 2022 Yann Collette <ycollette.nospam@free.fr> - 1.6.5-2
- update to 1.6.5-2

* Sat Aug 13 2022 Yann Collette <ycollette.nospam@free.fr> - 1.6.1-2
- update to 1.6.1-2

* Tue Mar 29 2022 Yann Collette <ycollette.nospam@free.fr> - 1.5.3-2
- update to 1.5.3-2

* Wed Jan 05 2022 Yann Collette <ycollette.nospam@free.fr> - 1.5.0-2
- update to 1.5.0-2

* Sun Dec 19 2021 Yann Collette <ycollette.nospam@free.fr> - 1.4.3-2
- update to 1.4.3-2

* Sat Dec 18 2021 Yann Collette <ycollette.nospam@free.fr> - 1.4.2-2
- update to 1.4.2-2

* Sat Nov 13 2021 Yann Collette <ycollette.nospam@free.fr> - 1.4.1-2
- update to 1.4.1-2

* Sat Nov 06 2021 Yann Collette <ycollette.nospam@free.fr> - 1.4.0-2
- update to 1.4.0-2

* Wed Jul 14 2021 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-2
- update to 1.3.0-2

* Tue Dec 29 2020 Yann Collette <ycollette.nospam@free.fr> - 1.2.2-2
- update to 1.2.2-2

* Thu Nov 05 2020 Yann Collette <ycollette.nospam@free.fr> - 1.2.1-2
- update to 1.2.1-2

* Fri May 1 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-2
- update to 1.1.0-2

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> -
- update for Fedora 29

* Thu Sep 13 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 1.0.5-2
- add patch to fix build on Fedora 17 (gcc4.7)

* Wed Feb 18 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 1.0.5-2
- add patch to activate ports on the server without a client connection

* Wed Feb 18 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 1.0.5-1
- updated to 1.0.5, added patch for gcc44 build on fc11

* Wed Feb 18 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 1.0.4-1
- updated to 1.0.4

* Wed Jan  7 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 1.0.3-1
- updated to 1.0.3, enable build on x86_64

* Tue Oct  7 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 1.0.2-0.1alpha
- updated to latest alpha release (1.0.2-alpha)
- build only on i386 for now

* Wed Jul  9 2008 Arnaud Gomes-do-Vale <Arnaud.Gomes@ircam.fr>
- fix building on CentOS

* Wed Jul  9 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- use qt3-devel when building on fc9
- add patch for building with gcc4.3

* Tue Oct 09 2007 Juan-Pablo Caceres <jcaceres@ccrma.Stanford.EDU> - 0.27-1
- new version 0.27

* Fri Oct 05 2007 Juan-Pablo Caceres <jcaceres@ccrma.Stanford.EDU> - 0.26-1
- new version 0.26, without qwt dependency

* Mon Feb 19 2007 Juan-Pablo Caceres <jcaceres@ccrma.Stanford.EDU> - 0.25-1
- modified names and version

* Thu Jul 20 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 25-1
- initial build.
