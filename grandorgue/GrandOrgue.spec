# Tag: Organ
# Type: Standalone
# Category: Audio, Sampler

Name:    grandorgue
Version: 3.10.1
Release: 4%{?dist}
Summary: A sample based pipe organ simulator.
License: GPLv2+
URL:     https://github.com/GrandOrgue/grandorgue

Vendor:       Audinux
Distribution: Audinux

# Usage: ./GrandOrgue-source.sh <TAG>
# ./GrandOrgue-source.sh v3.10.1-1

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
BuildRequires: wxGTK3-devel
BuildRequires: jack-audio-connection-kit-devel
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

%build

%cmake -DwxWidgets_CONFIG_EXECUTABLE:FILEPATH=/usr/bin/wx-config-3.0 \
       -DLIBINSTDIR=%{_lib}

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
