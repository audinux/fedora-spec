# Global variables for github repository
%global commit0 f7e34e37d376e18ec097fa42957c9ecb42d50b9f
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    ossia-score
Version: 3.0.1
Release: 1%{?dist}
Summary: ossia score is a sequencer for audio-visual artists, designed to create interactive shows
URL:     https://github.com/OSSIA/score
License: CeCILL License v2

Vendor:       Audinux
Distribution: Audinux

# ./ossia-source.sh <tag>
# ./ossia-source.sh v3.0.1

Source0: https://gitlab.com/OSSIA/score/-/archive/v%{version}/score-v%{version}.tar.gz
Source1: ossia-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: boost-devel
BuildRequires: zlib-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-private-devel
BuildRequires: qt5-qtbase-gui
BuildRequires: qt5-qtwebsockets-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qttools
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtserialport-devel
BuildRequires: qt5-qtquickcontrols2-devel
BuildRequires: ffmpeg-devel
BuildRequires: portmidi-devel
BuildRequires: portaudio-devel
BuildRequires: lilv-devel
BuildRequires: suil-devel
BuildRequires: avahi-compat-libdns_sd-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: unzip

%description
ossia score is a sequencer for audio-visual artists, designed to create interactive shows

%prep
%setup -qn score-v%{version}

sed -i -e "s/BOOST_MINOR 70/BOOST_MINOR 69/g" 3rdparty/libossia/cmake/OssiaDeps.cmake

%build

%cmake -DCMAKE_BUILD_TYPE=RELEASE \
       -DSCORE_CONFIGURATION=static-release \
       -DCMAKE_AR=/usr/bin/gcc-ar \
       -DCMAKE_RANLIB=/usr/bin/gcc-ranlib \
       -DPORTAUDIO_ONLY_DYNAMIC=1

%cmake_build

%install

%cmake_install

# Cleanup
rm -rf %{buildroot}/usr/lib/*.a
rm -rf %{buildroot}/usr/lib/cmake/
rm -rf %{buildroot}/%{_libdir}/*.a
rm -rf %{buildroot}/%{_includedir}/
rm -rf %{buildroot}/%{_datadir}/

%files
%doc INSTALL.md README.md AUTHORS
%license LICENSE.txt
%{_bindir}/*

%changelog
* Sun Jan 16 2022 Yann Collette <ycollette.nospam@free.fr> - 3.0.1-2
- update to version 3.0.1

* Sun Oct 25 2020 Yann Collette <ycollette.nospam@free.fr> - 2.5.2-2
- fix debug build

* Wed Oct 23 2019 Yann Collette <ycollette.nospam@free.fr> - 2.5.2-1
- initial version of the spec file
