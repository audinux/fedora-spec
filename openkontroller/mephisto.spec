# Status: active
# Tag: Editor, Jack
# Type: Plugin, LV2
# Category: Tool, Session Mngmt

Name: lv2-mephisto
Version: 0.18.2
Release: 1%{?dist}
Summary: A JACK patchbay in flow matrix style
URL: https://git.open-music-kontrollers.ch/~hp/mephisto.lv2
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://git.open-music-kontrollers.ch/~hp/mephisto.lv2/archive/%{version}.tar.gz#/mephisto.lv2-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: meson
BuildRequires: cmake
BuildRequires: lv2-devel
BuildRequires: faust-osclib-devel
BuildRequires: fontconfig
BuildRequires: fontconfig-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: glew-devel
BuildRequires: libvterm-devel

%description
A Just-in-time FAUST embedded in an LV2 plugin

%prep
%autosetup -n mephisto.lv2-%{version}

%build

%set_build_flags

%meson -Dlv2libdir=%{_libdir}/lv2/
%meson_build

%install

%meson_install

%files
%doc README.md ChangeLog
%license LICENSES/*
%{_libdir}/lv2/*

%changelog
* Tue Mar 07 2023 Yann Collette <ycollette.nospam@free.fr> - 0.18.2-1
- update to 0.18.2-1

* Fri Apr 15 2022 Yann Collette <ycollette.nospam@free.fr> - 0.18.0-1
- update to 0.18.0-1

* Thu Nov 04 2021 Yann Collette <ycollette.nospam@free.fr> - 0.16.0-1
- inital release
