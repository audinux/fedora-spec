# Tag: Reverb
# Type: Plugin, LV2
# Category: Audio, Effect

%define _lto_cflags %{nil}

Name:    dragonfly-reverb
Version: 3.2.5
Release: 3%{?dist}
Summary: DragonFly reverberation plugin
License: GPLv2+
URL:     https://github.com/michaelwillis/dragonfly-reverb/

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./dragonfly-source.sh 3.2.5

Source0: dragonfly-reverb.tar.gz
Source1: dragonfly-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel

%description
A free hall-style reverb based on freeverb3 algorithms

%prep
%autosetup -n %{name}

%build

%make_build SKIP_STRIPPING=true CFLAGS="%optflags" CXXFLAGS="%optflags"

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/DragonflyHallReverb.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/DragonflyRoomReverb.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/DragonflyEarlyReflections.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/DragonflyPlateReverb.lv2
install -m 755 -d %{buildroot}/%{_libdir}/vst
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps

cp bin/DragonflyHallReverb       %{buildroot}/%{_bindir}/
cp bin/DragonflyRoomReverb       %{buildroot}/%{_bindir}/
cp bin/DragonflyEarlyReflections %{buildroot}/%{_bindir}/
cp bin/DragonflyPlateReverb      %{buildroot}/%{_bindir}/

cp -r bin/DragonflyHallReverb.lv2/*       %{buildroot}/%{_libdir}/lv2/DragonflyHallReverb.lv2/
cp -r bin/DragonflyRoomReverb.lv2/*       %{buildroot}/%{_libdir}/lv2/DragonflyRoomReverb.lv2/
cp -r bin/DragonflyEarlyReflections.lv2/* %{buildroot}/%{_libdir}/lv2/DragonflyEarlyReflections.lv2/
cp -r bin/DragonflyPlateReverb.lv2/*      %{buildroot}/%{_libdir}/lv2/DragonflyPlateReverb.lv2/

cp bin/DragonflyHallReverb-vst.so       %{buildroot}/%{_libdir}/vst/
cp bin/DragonflyRoomReverb-vst.so       %{buildroot}/%{_libdir}/vst/
cp bin/DragonflyEarlyReflections-vst.so %{buildroot}/%{_libdir}/vst/
cp bin/DragonflyPlateReverb-vst.so      %{buildroot}/%{_libdir}/vst/

cp dragonfly-early-screenshot.png %{buildroot}/%{_datadir}/pixmaps/
cp dragonfly-hall-screenshot.png  %{buildroot}/%{_datadir}/pixmaps/
cp dragonfly-plate-screenshot.png %{buildroot}/%{_datadir}/pixmaps/
cp dragonfly-room-screenshot.png  %{buildroot}/%{_datadir}/pixmaps/

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_libdir}/lv2/*
%{_libdir}/vst/*
%{_datadir}/pixmaps/*

%changelog
* Fri Mar 5 2021 Yann Collette <ycollette.nospam@free.fr> - 3.2.5-3
- update to 3.2.5-3

* Thu Mar 4 2021 Yann Collette <ycollette.nospam@free.fr> - 3.2.4-3
- update to 3.2.4-3

* Thu Dec 8 2020 Yann Collette <ycollette.nospam@free.fr> - 3.2.3-3
- update to 3.2.3-3

* Sat Oct 3 2020 Yann Collette <ycollette.nospam@free.fr> - 3.2.1-3
- update to 3.2.1-3 - fix for fedora 33

* Fri Aug 28 2020 Yann Collette <ycollette.nospam@free.fr> - 3.2.1-2
- update to 3.2.1-2

* Tue Jun 30 2020 Yann Collette <ycollette.nospam@free.fr> - 3.2.0-2
- update to 3.2.0-2

* Sun Jun 28 2020 Yann Collette <ycollette.nospam@free.fr> - 3.1.2-2
- update to 3.1.2-2

* Sun Jun 14 2020 Yann Collette <ycollette.nospam@free.fr> - 3.1.1-2
- update to 3.1.1-2 - fix missing presets

* Wed Jun 10 2020 Yann Collette <ycollette.nospam@free.fr> - 3.1.1-1
- update to 3.1.1-1

* Sun Mar 1 2020 Yann Collette <ycollette.nospam@free.fr> - 3.0.0-1
- update to 3.0.0

* Mon Jun 24 2019 Yann Collette <ycollette.nospam@free.fr> - 2.0.0-1
- update to 2.0.0

* Sun Jan 20 2019 Yann Collette <ycollette.nospam@free.fr> - 1.1.4-1
- update to 1.1.4

* Thu Jan 3 2019 Yann Collette <ycollette.nospam@free.fr> - 1.1.2-1
- update to 1.1.2

* Tue Nov 13 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- update to 1.0.0

* Fri Oct 26 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9.5-1
- update to 0.9.5

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9.3-1
- update for Fedora 29
- update to 0.9.3

* Fri Oct 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9.2-1
- Initial build
