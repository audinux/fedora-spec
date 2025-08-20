# Status: active
# Tag: Jack, Loop
# Type: Standalone
# Category: Audio, Sequencer

Name: lv2-loop192
Version: 0.1.0
Release: 1%{?dist}
Summary: minimal live MIDI looper
License: GPL-3.0
URL: https://github.com/jean-emmanuel/loop192
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/jean-emmanuel/loop192/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: liblo-devel
BuildRequires: gtkmm30-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: desktop-file-utils

%description
Looper plugin for LV2, specifically for the Mod Devices pedal board.

%prep
%autosetup -n loop192-%{version}

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
* Tue Aug 19 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- update to 0.1.0-1

* Sun Oct 30 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial development
