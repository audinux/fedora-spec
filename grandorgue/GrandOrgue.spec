# Tag: Organ
# Type: Standalone
# Category: Audio, Sampler

Name: grandorgue
Version: 3.14.0.0
Release: 7%{?dist}
Summary: A sample based pipe organ simulator.
License: GPL-2.0-or-later
URL: https://github.com/GrandOrgue/grandorgue

Vendor:       Audinux
Distribution: Audinux

# Usage: ./GrandOrgue-source.sh <TAG>
#        ./GrandOrgue-source.sh 3.14.0-0

Source0: grandorgue.tar.gz
Source1: GrandOrgue-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: zlib
BuildRequires: libxslt
BuildRequires: zip
BuildRequires: po4a
BuildRequires: ImageMagick
BuildRequires: docbook-style-xsl
%if 0%{?fedora} <= 38
BuildRequires: wxGTK3-devel
%else
BuildRequires: wxGTK-devel
%endif
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: systemd-devel
BuildRequires: wavpack-devel
BuildRequires: fftw-devel
BuildRequires: SDL2-devel
BuildRequires: zita-convolver-devel
BuildRequires: libudev-devel
BuildRequires: rtaudio-devel
BuildRequires: rtmidi-devel
BuildRequires: portaudio-devel
BuildRequires: yaml-cpp-devel
BuildRequires: desktop-file-utils

%description
GrandOrgue is a sample based pipe organ simulator.

Obsoletes: GrandOrgue >= 0.3.1

%package demo
Summary: GrandOrgue demo sampleset
License: GPL-2.0-or-later
Group: Productivity/Multimedia/Sound/Midi
BuildArch: noarch
Requires: %{name}%{?_isa} = %{version}-%{release}

%description demo
This package contains the demo sampleset for GrandOrgue.

%package resources
Summary: GrandOrgue resource files
License: GPL-2.0-or-later
Group: Productivity/Multimedia/Sound/Midi
BuildArch: noarch

%description resources
This package contains resource files for GrandOrgue.

%prep
%autosetup -n grandorgue

sed -i -e "s/target_link_libraries(GrandOrgue golib)/target_link_libraries(GrandOrgue golib yaml-cpp)/g" src/grandorgue/CMakeLists.txt

%build

%set_build_flags
%cmake \
%if 0%{?fedora} <= 38
       -DwxWidgets_CONFIG_EXECUTABLE:FILEPATH=/usr/bin/wx-config-3.0 \
%else
       -DwxWidgets_CONFIG_EXECUTABLE:FILEPATH=/usr/bin/wx-config-3.2 \
%endif
%if 0%{?fedora} >= 38
       -DCMAKE_CXX_FLAGS="-include cstdint -fPIC $CXXFLAGS" \
%endif
       -DLIBINSTDIR=%{_lib} \
       -DCMAKE_MODULE_PATH=%{_libdir}/cmake/yaml-cpp
%cmake_build

%install

%cmake_install

%find_lang GrandOrgue

# install hydrogen.desktop properly.
desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/GrandOrgue.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/GrandOrgue.desktop

%files -f GrandOrgue.lang
%doc README.md AUTHORS
%license LICENSE
%{_bindir}/*
%{_libdir}/*
%{_datadir}/applications/*
%{_mandir}/man1/*

%files resources
%dir %{_datadir}/GrandOrgue/packages
%dir %{_datadir}/GrandOrgue
%{_datadir}/metainfo/*
%{_datadir}/GrandOrgue/help
%{_datadir}/GrandOrgue/sounds
%{_datadir}/GrandOrgue/perftests
%{_datadir}/mime/packages/*
%{_datadir}/icons/hicolor/*

%files demo
%{_datadir}/GrandOrgue/packages/*.orgue

%changelog
* Fri Jan 12 2024 Yann Collette <ycollette.nospam@free.fr> - 3.14.0.0-7
- update to 3.14.0.0-7

* Mon Jan 08 2024 Yann Collette <ycollette.nospam@free.fr> - 3.13.3.1-7
- update to 3.13.3.1-7

* Thu Nov 23 2023 Yann Collette <ycollette.nospam@free.fr> - 3.13.3.0-7
- update to 3.13.3.0-7

* Sun Nov 19 2023 Yann Collette <ycollette.nospam@free.fr> - 3.13.2.1-7
- update to 3.13.2.1-7

* Mon Nov 06 2023 Yann Collette <ycollette.nospam@free.fr> - 3.13.1.1-7
- update to 3.13.1.1-7

* Thu Oct 12 2023 Yann Collette <ycollette.nospam@free.fr> - 3.13.0.1-7
- update to 3.13.0.1-7

* Wed Aug 16 2023 Yann Collette <ycollette.nospam@free.fr> - 3.13.0.0-7
- update to 3.13.0.0-7

* Tue Aug 15 2023 Yann Collette <ycollette.nospam@free.fr> - 3.12.3.1-7
- update to 3.12.3.1-7

* Sun Jul 23 2023 Yann Collette <ycollette.nospam@free.fr> - 3.12.3-0
- update to 3.12.3-0-7

* Sun Jul 23 2023 Yann Collette <ycollette.nospam@free.fr> - 3.12.2-1
- update to 3.12.2-1-7

* Fri Jun 09 2023 Yann Collette <ycollette.nospam@free.fr> - 3.12.2-0
- update to 3.12.2-0-6

* Tue Jun 06 2023 Yann Collette <ycollette.nospam@free.fr> - 3.12.1-1
- update to 3.12.1-1-6

* Wed May 31 2023 Yann Collette <ycollette.nospam@free.fr> - 3.12.1-0
- update to 3.12.1-0-5

* Fri May 26 2023 Yann Collette <ycollette.nospam@free.fr> - 3.12.0-1
- update to 3.12.0-1-5

* Wed May 10 2023 Yann Collette <ycollette.nospam@free.fr> - 3.11.3-5
- update to 3.11.3-0-5

* Tue May 09 2023 Yann Collette <ycollette.nospam@free.fr> - 3.11.2-5
- update to 3.11.2-1-5

* Mon May 08 2023 Yann Collette <ycollette.nospam@free.fr> - 3.11.2-4
- update to 3.11.2-0-4

* Mon Apr 17 2023 Yann Collette <ycollette.nospam@free.fr> - 3.11.1-4
- update to 3.11.1-1-4

* Thu Mar 02 2023 Yann Collette <ycollette.nospam@free.fr> - 3.10.1-4
- update to github repo / 3.10.1-1-4

* Thu Oct 22 2020 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-4
- fix debug build

* Wed Sep 30 2020 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-3
- fix for fedora 33

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-2
- update to release 2330

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-2
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-2
- update to release 2294

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-1
- update to release 2242

* Mon Jun 01 2015 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-1
- Initial version
