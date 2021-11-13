# Tag: Jack
# Type: Standalone
# Category: Audio, Sampler, Tool

Summary: Multimachine jam sessions over the internet
Name:    jacktrip
Version: 1.4.1
Release: 2%{?dist}
License: STK
URL:     https://ccrma.stanford.edu/software/jacktrip/

Vendor:       Planet CCRMA
Distribution: Planet CCRMA

Source0: https://github.com/jacktrip/jacktrip/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: rtaudio-devel
BuildRequires: meson
BuildRequires: help2man
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

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
%autosetup -n %{name}-%{version}

%build

%meson
%meson_build

%install

%meson_install

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/org.jacktrip.JackTrip.desktop

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
