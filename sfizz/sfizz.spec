Name:    sfizz
Version: 1.2.2
Release: 4%{?dist}
License: BSD-2-Clause
Summary: Sampler plugin and library for SFZ instruments
Url:     https://github.com/sfztools/sfizz

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/sfztools/sfizz/releases/download/%{version}/sfizz-%{version}.tar.gz

Requires: libsndfile

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: libatomic
BuildRequires: libsndfile-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libX11-devel
BuildRequires: freetype-devel
BuildRequires: xcb-util-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: cairo-devel
BuildRequires: pango-devel
BuildRequires: simde-devel
BuildRequires: kiss-fft-devel
BuildRequires: pugixml-devel
BuildRequires: cxxopts-devel
BuildRequires: catch2-devel
BuildRequires: jack-audio-connection-kit-devel

# option_ex(SFIZZ_USE_SYSTEM_GHC_FS   "Use GHC Filesystem libraries preinstalled on system" OFF)

%description
Sfizz is a musical sampler for musicians, and a library for developers.

%package devel
Summary:  Header files for Sfizz
Requires: %{name} = %{version}-%{release}

%description devel
Header files for the Sfizz library.

%prep
%autosetup -n %{name}-%{version}

%build

%cmake -DSFIZZ_JACK=ON \
       -DSFIZZ_USE_SYSTEM_SIMDE=ON \
       -DSFIZZ_USE_SYSTEM_KISS_FFT=ON \
       -DSFIZZ_USE_SYSTEM_PUGIXML=ON \
       -DSFIZZ_USE_SYSTEM_CXXOPTS=ON \
       -DSFIZZ_USE_SYSTEM_CATCH=ON \
       -DSFIZZ_USE_SNDFILE=ON

%cmake_build

%install

%cmake_install

%files
%doc README.md GOVERNANCE.md CONTRIBUTING.md AUTHORS.md
%license LICENSE
%{_bindir}/sfizz_jack
%{_bindir}/sfizz_render
%{_libdir}/libsfizz.so.*
%{_mandir}/*

%files devel
%{_libdir}/libsfizz.so
%{_includedir}/sfizz.h
%{_includedir}/sfizz.hpp
%{_includedir}/sfizz_message.h
%dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/sfizz.pc

%changelog
* Tue Aug 29 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.2-4
- update to 1.2.2-4

* Sat Apr 15 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.1-4
- update to 1.2.1-4

* Sun Jan 16 2022 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-4
- update to 1.2.0-4

* Mon Nov 08 2021 Yann Collette <ycollette.nospam@free.fr> - 1.1.1-4
- update to 1.1.1-4

* Sun Oct 24 2021 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-4
- update to 1.1.0-4

* Mon May 10 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-4
- update to 1.0.0-4 - try to fix dep wrt to pipewire

* Fri Apr 16 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-3
- update to 1.0.0-3

* Sun Oct 25 2020 Yann Collette <ycollette.nospam@free.fr> - 0.5.1-3
- update to 0.5.1-3

* Fri Oct 16 2020 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-3
- update to 0.5.0-3 - fix for fedora 33

* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-3
- update to 0.4.0-3 - fix for fedora 33

* Fri Jul 24 2020 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-2
- update to 0.4.0-2

* Sun Apr 5 2020 Yann Collette <ycollette.nospam@free.fr> - 0.3.2-2
- update to 0.3.2-2

* Sun Mar 15 2020 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-1
- update to 0.3.1

* Sun Feb 2 2020 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- update for Fedora

* Fri Jan 31 2020 Jean Pierre Cimalando <jp-dev@inbox.ru> - 0.2.0-1
- initial release of the spec file
