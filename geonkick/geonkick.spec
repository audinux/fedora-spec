# Tag:  Drum, Jack, Alsa
# Type: Plugin, LV2
# Category: Audio, Synthesizer

Name:    geonkick
Version: 3.1.0
Release: 2%{?dist}
Summary: Drum Software Synthesizer
URL:     https://github.com/Geonkick-Synthesizer/geonkick
License: GPL-3.0-only

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/Geonkick-Synthesizer/geonkick/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: lv2-devel
BuildRequires: libsndfile-devel
BuildRequires: rapidjson-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: openssl-devel
BuildRequires: desktop-file-utils

%description
Geonkick is a synthesizer that can synthesize elements of percussion.
The most basic examples are: kick drums, snares, hit-hats, shakers, claps, steaks.

%prep
%autosetup -n %{name}-%{version}

%build

%cmake
%cmake_build

%install

%cmake_install

%files
%doc README.md doc/Geonkick_User_Guide.md
%license LICENSE
%{_bindir}/*
%{_libdir}/lv2/*
%{_datadir}/*

%changelog
* Sat Dec 09 2023 Yann Collette <ycollette.nospam@free.fr> - 3.1.0-2
- Update to 3.1.0-2

* Sun Dec 03 2023 Yann Collette <ycollette.nospam@free.fr> - 3.0.1-2
- Update to 3.0.1-2

* Sat Nov 25 2023 Yann Collette <ycollette.nospam@free.fr> - 3.0.0-2
- Update to 3.0.0-2

* Sat Oct 07 2023 Yann Collette <ycollette.nospam@free.fr> - 2.10.2-2
- Update to 2.10.2-2

* Tue Sep 26 2023 Yann Collette <ycollette.nospam@free.fr> - 2.10.1-2
- Update to 2.10.1-2

* Fri Sep 08 2023 Yann Collette <ycollette.nospam@free.fr> - 2.10.0-2
- Update to 2.10.0-2

* Sun Aug 20 2023 Yann Collette <ycollette.nospam@free.fr> - 2.9.2-2
- Update to 2.9.2-2

* Mon Feb 21 2022 Yann Collette <ycollette.nospam@free.fr> - 2.9.0-2
- Update to 2.9.0-2

* Sun Jan 16 2022 Yann Collette <ycollette.nospam@free.fr> - 2.8.1-2
- Update to 2.8.1-2

* Sat Apr 03 2021 Yann Collette <ycollette.nospam@free.fr> - 2.8.0-2
- Update to 2.8.0-2

* Tue Mar 09 2021 Yann Collette <ycollette.nospam@free.fr> - 2.7.3-2
- Update to 2.7.3-2

* Sun Feb 28 2021 Yann Collette <ycollette.nospam@free.fr> - 2.7.2-2
- Update to 2.7.2-2

* Sun Jan 24 2021 Yann Collette <ycollette.nospam@free.fr> - 2.7.0-2
- Update to 2.7.0-2

* Tue Dec 29 2020 Yann Collette <ycollette.nospam@free.fr> - 2.6.1-2
- Update to 2.6.1-2

* Wed Dec 16 2020 Yann Collette <ycollette.nospam@free.fr> - 2.6.0-2
- Update to 2.6.0-2

* Mon Nov 30 2020 Yann Collette <ycollette.nospam@free.fr> - 2.5.1-2
- Update to 2.5.1-2

* Fri Oct 30 2020 Yann Collette <ycollette.nospam@free.fr> - 2.5.0-2
- Update to 2.5.0-2

* Wed Oct 28 2020 Yann Collette <ycollette.nospam@free.fr> - 2.4.1-2
- Update to 2.4.1-2

* Mon Oct 26 2020 Yann Collette <ycollette.nospam@free.fr> - 2.4.0-2
- Update to 2.4.0-2

* Wed Sep 30 2020 Yann Collette <ycollette.nospam@free.fr> - 2.3.8-2
- Update to 2.3.8-2 - fix for fedora 33

* Tue Sep 22 2020 Yann Collette <ycollette.nospam@free.fr> - 2.3.8-1
- Update to 2.3.8-1

* Tue Aug 18 2020 Yann Collette <ycollette.nospam@free.fr> - 2.3.7-1
- Update to 2.3.7-1

* Thu Aug 13 2020 Yann Collette <ycollette.nospam@free.fr> - 2.3.4-1
- Update to 2.3.4-1

* Mon Jul 27 2020 Yann Collette <ycollette.nospam@free.fr> - 2.3.3-1
- Update to 2.3.3-1

* Sat Jul 25 2020 Yann Collette <ycollette.nospam@free.fr> - 2.3.2-1
- Update to 2.3.2-1

* Fri Jul 24 2020 Yann Collette <ycollette.nospam@free.fr> - 2.3.1-1
- Update to 2.3.1-1

* Fri Jun 12 2020 Yann Collette <ycollette.nospam@free.fr> - 2.2.3-1
- Update to 2.2.3-1

* Thu Jun 11 2020 Yann Collette <ycollette.nospam@free.fr> - 2.2.1-1
- Update to 2.2.1

* Wed May 13 2020 Yann Collette <ycollette.nospam@free.fr> - 2.1.1-1
- Update to 2.1.1

* Sat May 09 2020 Bruno Vernay <brunovern.a@gmail.com> - 2.1.0-1
- Update to 2.1.0, update the URL, add make dependency, add doc

* Fri Apr 17 2020 Yann Collette <ycollette.nospam@free.fr> - 2.0.0-1
- update to 2.0.0

* Sun Apr 5 2020 Yann Collette <ycollette.nospam@free.fr> - 1.10.0-1
- update to 1.10.0

* Sat Dec 28 2019 Yann Collette <ycollette.nospam@free.fr> - 1.9.2-1
- update to 1.9.2

* Mon Oct 7 2019 Yann Collette <ycollette.nospam@free.fr> - 1.9.0-1
- update to 1.9.0

* Sun Aug 11 2019 Yann Collette <ycollette.nospam@free.fr> - 1.8.1-1
- update to 1.8.1

* Fri Aug 9 2019 Yann Collette <ycollette.nospam@free.fr> - 1.8.0-1
- update to 1.8.0

* Wed Jun 5 2019 Yann Collette <ycollette.nospam@free.fr> - 1.6.0-1
- update to 1.6.0

* Thu May 23 2019 Yann Collette <ycollette.nospam@free.fr> - 1.5.3-1
- update to 1.5.3

* Wed May 22 2019 Yann Collette <ycollette.nospam@free.fr> - 1.5.2-1
- update to 1.5.2

* Tue May 21 2019 Yann Collette <ycollette.nospam@free.fr> - 1.5.1-1
- update to 1.5.1

* Mon May 20 2019 Yann Collette <ycollette.nospam@free.fr> - 1.5-1
- initial version of the spec file
