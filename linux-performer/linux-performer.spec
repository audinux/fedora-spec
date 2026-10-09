# Status: active
# Tag: Jack, Alsa, Distortion
# Type: Plugin, Standalone, VST3
# Category: Effect

Name: linux-performer
Version: 0.1.45
Release: 1%{?dist}
Summary: A live-performance plugin host for Linux
License: GPL-2.0-or-later
URL: https://github.com/dguedry/linux-performer
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./linux-performer-source.sh <TAG>
#        ./linux-performer-source.sh v0.1.45

Source0: linux-performer.tar.gz
Source1: linux-performer-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: gtk3-devel
BuildRequires: ladspa-devel
BuildRequires: desktop-file-utils

%description
Performer exists because the live hosts keyboard players rely on -- MainStage, Gig Performer, Cantabile,
Camelot -- have no Linux version. It hosts VST3, LV2 and LADSPA plugins natively, and Windows VST3s
bridged with yabridge work like any other plugin.
- A program per sound, 128 per keyboard, selected by MIDI Program Change while you play. Upper and Lower
  manuals change independently. Group them by kind -- organs, strings, brass -- to find things quickly.
- Splits and layers with per-slot key range, velocity range, velocity curve, transpose, gain and pan.
- Insert effects per instrument and per program.
- MIDI learn for any plugin parameter, with suggested mappings from parameter names and reusable
  per-plugin templates.
- Every plugin in its own process. A plugin that crashes or hangs takes only itself down; the rest of
  the rig plays on.
- Built for low latency: a native PipeWire/JACK client, 128-sample blocks by default, parallel plugin
  loading, and a late-block counter you can watch.
- A global tempo with tap tempo, so tempo-synced delays and arpeggiators have something to sync to.
  Tap it in the toolbar or from a footswitch.
- An on-screen keyboard for building a set without a controller attached.
- Tablet control -- the whole plugin, not a remote control for it. A built-in web app changes programs
  from a music stand, and opens any loaded plugin's own interface on the tablet, laptop or phone: the real
  editor, mirrored and fully interactive, so you can reach a Kontakt library's every page or a B-3X's
  drawbars without walking back to the computer. Nothing to install -- scan the code or type a short one,
  and add it to the home screen if you like.
  Performer can serve its own wifi network when the venue has none.

%prep
%autosetup -n %{name}

%build

%cmake
%cmake_build

%install

%cmake_install

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/performer.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/performer.desktop

%files
%doc README.md docs/*
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/icons/hicolor/16x16/apps/*
%{_datadir}/icons/hicolor/24x24/apps/*
%{_datadir}/icons/hicolor/32x32/apps/*
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/64x64/apps/*
%{_datadir}/icons/hicolor/128x128/apps/*
%{_datadir}/icons/hicolor/256x256/apps/*
%{_datadir}/icons/hicolor/512x512/apps/*

%changelog
* Fri Oct 09 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.45-1
- update to 0.1.45-1

* Wed Oct 07 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.43-1
- update to 0.1.43-1

* Mon Oct 05 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.41-1
- Initial spec file
