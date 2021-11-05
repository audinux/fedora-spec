Name:    mephisto
Version: 0.16.0
Release: 1%{?dist}
Summary: A JACK patchbay in flow matrix style
URL:     https://github.com/OpenMusicKontrollers/mephisto.lv2
License: GPLv2+

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/OpenMusicKontrollers/mephisto.lv2/archive/refs/tags/%{version}.tar.gz#/mephisto.lv2-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: faust-osclib-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: glew-devel
BuildRequires: meson
BuildRequires: cmake

%description
A Just-in-time FAUST embedded in an LV2 plugin

%prep
%autosetup -n mephisto.lv2-%{version}

%build

%set_build_flags

%meson
%meson_build 

%install

%meson_install

%files
%doc README.md ChangeLog
%license COPYING
%{_bindir}/*
%{_datadir}/*

%changelog
* Thu Nov 04 2021 Yann Collette <ycollette.nospam@free.fr> - 0.16.0-1
- inital release
