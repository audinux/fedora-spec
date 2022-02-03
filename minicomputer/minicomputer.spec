# Tag: Jack, Alsa
# Type: Plugin, LV2
# Category: Audio, Synthesizer
# GUIToolkit: Fltk

Name:    minicomputer
Summary: Standalone Linux software synthesizer
Version: 1.4
Release: 2%{?dist}
License: GPL
URL:     https://minicomputer.sourceforge.net/

Vendor:       Audinux
Distribution: Audinux

Source0: https://sourceforge.net/projects/minicomputer/files/minicomputer/version%20%{version}/MinicomputerV%{version}.tar.gz
Source1: minicomputer-SConstruct
Source2: https://github.com/jeremysalwen/Minicomputer-LV2/archive/master.zip#/minicomputer-lv2.zip

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel
BuildRequires: lv2-devel
BuildRequires: fltk-devel
BuildRequires: scons
BuildRequires: unzip

%description
Minicomputer is a standalone Linux software synthesizer for creating experimental electronic sounds as its often
used in but not limited to Industrial music, IDM, EBM, Glitch, sound design and minimal electronic.
It is monophonic but can produce up to 8 different sounds at the same time.
It uses Jack as realtime audio infrastructure and can be controlled via Midi.

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPLv2+

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -cn %{name}-%{version}

cp %{SOURCE1} SConstruct
sed -i -e "/unistd/a#include<unistd.h>" editor/Memory.h

unzip %{SOURCE2}
sed -i -e "s|usr/lib/lv2|usr/%{_lib}/lv2|g" Minicomputer-LV2-master/src/Makefile
sed -i -e "s|TTLS = minicomputer|TTLS = minicomputer.ttl|g" Minicomputer-LV2-master/src/Makefile
sed -i -e "19i #include <pthread.h>" Minicomputer-LV2-master/src/minicomputer.c

%build

%set_build_flags
scons DESTDIR="%{buildroot}" Prefix=/usr

cd Minicomputer-LV2-master/src
%make_build

%install

cd Minicomputer-LV2-master/src
%make_install
cd ../..

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/doc/
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/presets/
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/

cp minicomputerManual.pdf %{buildroot}/%{_datadir}/%{name}/doc/
cp minicomputer.xpm       %{buildroot}/%{_datadir}/pixmaps/
cp minicomputer           %{buildroot}/%{_bindir}/
cp minicomputerCPU        %{buildroot}/%{_bindir}/
cp -r factoryPresets/*    %{buildroot}/%{_datadir}/%{name}/presets/

%files
%doc README
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/*

%files -n lv2-%{name}
%doc Minicomputer-LV2-master/README Minicomputer-LV2-master/CHANGES
%license Minicomputer-LV2-master/COPYING
%{_libdir}/lv2/*

%changelog
* Sat Oct 31 2020 Yann Collette <ycollette.nospam@free.fr> - 1.4-2
- add LV2 package from anoter repo

* Wed Oct 28 2020 Yann Collette <ycollette.nospam@free.fr> - 1.4-1
- initial release
