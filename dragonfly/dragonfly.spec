# Tag: Reverb
# Type: Plugin, LV2
# Category: Audio, Effect

%define _lto_cflags %{nil}

Name:    dragonfly-reverb
Version: 3.2.10
Release: 3%{?dist}
Summary: DragonFly reverberation plugin
License: GPLv2+
URL:     https://github.com/michaelwillis/dragonfly-reverb/

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./dragonfly-source.sh 3.2.10

Source0: dragonfly-reverb.tar.gz
Source1: dragonfly-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel
BuildRequires: desktop-file-utils

%description
A free hall-style reverb based on freeverb3 algorithms

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst-%{name}
VST2 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n clap-%{name}
CLAP version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n %{name}

%build

%make_build SKIP_STRIPPING=true CFLAGS="%optflags" CXXFLAGS="%optflags"

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/lv2
install -m 755 -d %{buildroot}/%{_libdir}/vst
install -m 755 -d %{buildroot}/%{_libdir}/vst3
install -m 755 -d %{buildroot}/%{_libdir}/clap
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps

cp bin/DragonflyHallReverb       %{buildroot}/%{_bindir}/
cp bin/DragonflyRoomReverb       %{buildroot}/%{_bindir}/
cp bin/DragonflyEarlyReflections %{buildroot}/%{_bindir}/
cp bin/DragonflyPlateReverb      %{buildroot}/%{_bindir}/

cp -r bin/*.lv2 %{buildroot}/%{_libdir}/lv2/
cp -r bin/*.vst3 %{buildroot}/%{_libdir}/vst3/
cp bin/*-vst.so %{buildroot}/%{_libdir}/vst/
cp bin/*.clap %{buildroot}/%{_libdir}/clap/

cp dragonfly-early-screenshot.png %{buildroot}/%{_datadir}/pixmaps/
cp dragonfly-hall-screenshot.png  %{buildroot}/%{_datadir}/pixmaps/
cp dragonfly-plate-screenshot.png %{buildroot}/%{_datadir}/pixmaps/
cp dragonfly-room-screenshot.png  %{buildroot}/%{_datadir}/pixmaps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}-hall-reverb.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=DragonflyHallReverb
Exec=DragonflyHallReverb
Icon=dragonfly-hall-screenshot
Comment=DragonFly Hall Reverb
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/%{name}-plate-reverb.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=DragonflyPlateReverb
Exec=DragonflyPlateReverb
Icon=dragonfly-plate-screenshot
Comment=DragonFly Plate Reverb
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/%{name}-room-reverb.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=DragonflyRoomReverb
Exec=DragonflyRoomReverb
Icon=dragonfly-room-screenshot
Comment=DragonFly Room Reverb
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/%{name}-early-reflections-reverb.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=DragonflyEarlyReflectionsReverb
Exec=DragonflyEarlyReflectionsReverb
Icon=dragonfly-early-screenshot
Comment=DragonFly Early Reflections Reverb
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-early-reflections-reverb.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-hall-reverb.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-room-reverb.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-plate-reverb.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n clap-%{name}
%{_libdir}/clap/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Sun Apr 23 2023 Yann Collette <ycollette.nospam@free.fr> - 3.2.10-3
- update to 3.2.10-3

* Tue Apr 04 2023 Yann Collette <ycollette.nospam@free.fr> - 3.2.9-3
- update to 3.2.9-3

* Thu Dec 29 2022 Yann Collette <ycollette.nospam@free.fr> - 3.2.8-3
- update to 3.2.8-3

* Mon Sep 26 2022 Yann Collette <ycollette.nospam@free.fr> - 3.2.7-3
- update to 3.2.7-3

* Sun Apr 3 2022 Yann Collette <ycollette.nospam@free.fr> - 3.2.6-3
- update to 3.2.6-3

* Fri Mar 5 2021 Yann Collette <ycollette.nospam@free.fr> - 3.2.5-3
- update to 3.2.5-3

* Thu Mar 4 2021 Yann Collette <ycollette.nospam@free.fr> - 3.2.4-3
- update to 3.2.4-3

* Tue Dec 8 2020 Yann Collette <ycollette.nospam@free.fr> - 3.2.3-3
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
