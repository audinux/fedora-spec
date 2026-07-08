# Status: active
# Tag: Mixer
# Type: Standalone
# Category: Audio, Tool

Name: LMTR
Version: 0.4.5
Release: 1%{?dist}
Summary: A 16-tracks multitrack recorder for Linux, based on Jack
URL: https://codeberg.org/agrigolo/LMTR
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-or-later

Vendor:       Audinux
Distribution: Audinux

# Usage: ./LMTR-source.sh <TAG>
#        ./LMTR-source.sh v0.4.5

Source0: LMTR.tar.gz
Source1: LMTR-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: qt6-qtbase-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libsndfile-devel
BuildRequires: ladspa-devel
BuildRequires: lv2-devel
BuildRequires: lilv-devel
BuildRequires: suil-devel
BuildRequires: desktop-file-utils


%description
LMTR (shorthand for Linux Multitrack Recorder, and also for Limiter) is a minimalist
studio recorder for musicians who want to capture, mix, and export music without the
complexity of a full DAW.
It gives you sixteen mono tracks, a stereo master bus, sends for each track for
flexible JACK routing, punch-in/out recording, a timeline-locked click track,
per-track LADSPA and LV2 insert slots, and flexible import/export options.

%prep
%autosetup -n %{name}

%build

%set_build_flags
export LDFLAGS="`pkg-config --libs-only-L jack` $LDFLAGS"

%cmake
%cmake_build

%install

%cmake_install

desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/*.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/lmtr.desktop
%{_datadir}/icons/hicolor/128x128/apps/lmtr.png
%{_datadir}/icons/hicolor/16x16/apps/lmtr.png
%{_datadir}/icons/hicolor/256x256/apps/lmtr.png
%{_datadir}/icons/hicolor/32x32/apps/lmtr.png
%{_datadir}/icons/hicolor/48x48/apps/lmtr.png
%{_datadir}/icons/hicolor/512x512/apps/lmtr.png

%changelog
* Tue Jul 07 2026 Yann Collette <ycollette.nospam@free.fr> - 0.4.5-1
- update to 0.4.5-1

* Mon Jul 06 2026 Yann Collette <ycollette.nospam@free.fr> - 0.4.3-1
- Initial spec file
