# Status: active
# Tag: Tracker, Jack, Alsa
# Type: Standalone
# Category: Audio, Sequencer

Summary: Music tracker for the Yamaha YM2608 sound chip
Name:    BambooTracker
Version: 0.6.5
Release: 1%{?dist}
License: GPL
URL:     https://github.com/rerrahkr/BambooTracker
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# To get the sources: ./bambootracker_source.sh <TAG>
#                     ./bambootracker_source.sh v0.6.5

Source0: BambooTracker.tar.gz
Source1: bambootracker_source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libsndfile-devel
BuildRequires: rtaudio-devel
BuildRequires: rtmidi-devel
BuildRequires: qt6-qtmultimedia-devel
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qttools-devel
BuildRequires: qt6-qt5compat-devel
BuildRequires: desktop-file-utils

%description
Music tracker for the Yamaha YM2608 (OPNA) sound chip which was used in NEC PC-8801/9801 series computers.

%prep
%autosetup -n %{name}

sed -i -e "s/set(CMAKE_C_FLAGS \"-O3 -Wall\")/set(CMAKE_C_FLAGS \"-O3 -Wall \${CMAKE_C_FLAGS}\")/g" submodules/emu2149/src/CMakeLists.txt

%build

%set_build_flags
export CXXFLAGS="-include cstdint $CXXFLAGS"

%cmake -DSYSTEM_RTAUDIO=ON \
       -DSYSTEM_RTMIDI=ON \
       -DWARNINGS_ARE_ERRORS=OFF \
       -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install

%cmake_install

desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc CHANGELOG.md IMPORTANT.md LICENSE README.md README_ja.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/BambooTracker/demos/*
%{_datadir}/BambooTracker/lang/*
%{_datadir}/BambooTracker/skins/*
%{_datadir}/doc/BambooTracker/licenses/*
%{_datadir}/doc/BambooTracker/specs/*
%{_datadir}/icons/hicolor/16x16/*
%{_datadir}/icons/hicolor/32x32/*
%{_datadir}/icons/hicolor/64x64/*
%{_datadir}/icons/hicolor/128x128/*
%{_datadir}/icons/hicolor/256x256/*
%{_datadir}/man/*
%{_datadir}/mime/*

%changelog
* Sat Mar 08 2025 Yann Collette <ycollette.nospam@free.fr> - 0.6.5-1
- update to version 0.6.5-1

* Tue Sep 24 2024 Yann Collette <ycollette.nospam@free.fr> - 0.6.4-1
- update to version 0.6.4-1

* Sat Sep 02 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.3-1
- update to version 0.6.3-1

* Wed Aug 02 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.2-1
- update to version 0.6.2-1

* Sun Feb 05 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.1-1
- update to version 0.6.1-1

* Mon Sep 26 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5.3-1
- update to version 0.5.3-1

* Wed Aug 24 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5.2-1
- update to version 0.5.2-1

* Sun Jul 24 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5.1-1
- update to version 0.5.1-1

* Tue Aug 03 2021 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-1
- update to version 0.5.0-1

* Thu Feb 11 2021 Yann Collette <ycollette.nospam@free.fr> - 0.4.6-1
- update to version 0.4.6-1

* Fri Nov 06 2020 Yann Collette <ycollette.nospam@free.fr> - 0.4.5-1
- update to version 0.4.5-1

* Sun Aug 23 2020 Yann Collette <ycollette.nospam@free.fr> - 0.4.4-1
- update to version 0.4.4-1

* Sun Jun 28 2020 Yann Collette <ycollette.nospam@free.fr> - 0.4.3-1
- update to version 0.4.3-1

* Sun May 10 2020 Yann Collette <ycollette.nospam@free.fr> - 0.4.2-1
- update to version 0.4.2-1

* Sat Apr 25 2020 Yann Collette <ycollette.nospam@free.fr> - 0.4.1-1
- update to version 0.4.1-1

* Thu Apr 2 2020 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-1
- update to version 0.4.0-1

* Sun Feb 23 2020 Yann Collette <ycollette.nospam@free.fr> - 0.3.5-1
- update to version 0.3.5-1

* Wed Jan 29 2020 Yann Collette <ycollette dot nospam at free.fr> 0.3.4-1
- Update to version 0.3.4

* Wed Dec 18 2019 Yann Collette <ycollette dot nospam at free.fr> 0.3.3-1
- Update to version 0.3.3

* Sun Dec 15 2019 Yann Collette <ycollette dot nospam at free.fr> 0.3.2-1
- Update to version 0.3.2

* Sat Nov 30 2019 Yann Collette <ycollette dot nospam at free.fr> 0.3.1-1
- Update to version 0.3.1

* Fri Nov 1 2019 Yann Collette <ycollette dot nospam at free.fr> 0.3.0-1
- Update to version 0.3.0

* Tue Sep 17 2019 Yann Collette <ycollette dot nospam at free.fr> 0.2.4-1
- Update to version 0.2.4

* Sun Sep 1 2019 Yann Collette <ycollette dot nospam at free.fr> 0.2.3-1
- Update to version 0.2.3

* Thu Jun 27 2019 Yann Collette <ycollette dot nospam at free.fr> 0.2.2-1
- Update to version 0.2.2

* Mon Jun 17 2019 Yann Collette <ycollette dot nospam at free.fr> 0.2.1-1
- Update to version 0.2.1

* Thu May 30 2019 Yann Collette <ycollette dot nospam at free.fr> 0.2.0-1
- Initial release of spec file
