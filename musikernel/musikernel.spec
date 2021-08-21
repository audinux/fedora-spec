%define __provides_exclude_from ^%{_usr}/lib/musikernel2/.*$
%global __python %{__python3}

Name:    musikernel2
Version: 16.05.1

Release: 1%{?dist}
Summary: Digital audio workstations, instrument and effect plugins

License: GPLv3
URL:     https://github.com/j3ffhubb/musikernel/
Source0: https://github.com/j3ffhubb/musikernel/archive/musikernel2-16.05.1.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: liblo-devel
BuildRequires: libsndfile-devel
BuildRequires: ftw-devel
BuildRequires: portmidi-devel
BuildRequires: portaudio-devel
BuildRequires: python3-devel
BuildRequires: python3-Cython
BuildRequires: liblo-devel
BuildRequires: vorbis-tools
BuildRequires: gettext

Requires: python3-qt5
Requires: rubberband
Requires: python3-numpy
Requires: python3-mido
Requires: python3-mutagen
Requires: python3-psutil
Requires: python3-pyyaml
Requires: lame
Requires: rubberband
Requires: vorbis-tools

# Missing
# pymarshal
# wavefile

%description
MusiKernel is digital audio workstations (DAWs), instrument and effect plugins

%prep
%autosetup

%build
cd src
%make_build 

%install
cd src
export DONT_STRIP=1
%make_install

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_libdir}/*
