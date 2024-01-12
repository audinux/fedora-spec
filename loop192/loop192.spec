# Tag: Jack, Loop
# Type: Standalone
# Category: Audio, Sequencer

%global commit0 91f97ca022ad91a26ca2afd16b698bc88c4bd0f4

Name: lv2-loop192
Version: 0.0.1
Release: 1%{?dist}
Summary: minimal live MIDI looper
License: GPL-3.0
URL: https://github.com/jean-emmanuel/loop192

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/jean-emmanuel/loop192/archive/%{commit0}.zip#/%{name}-%{commit0}.zip

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: liblo-devel
BuildRequires: gtkmm30-devel
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: desktop-file-utils

%description
Looper plugin for LV2, specifically for the Mod Devices pedal board.

%prep
%autosetup -n loop192-%{commit0}

%build

%set_build_flags
%make_build PREFIX=/usr

%Install

%make_install PREFIX=/usr

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/loop192.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/loop192.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_mandir}/*

%changelog
* Sun Oct 30 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial development
