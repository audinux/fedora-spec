# Tag: Tool, Devel
# Type: Plugin, LV2
# Category: Tool, Plugin

Name: tracker.lv2
Version: 0.1.1
Release: 1%{?dist}
Summary: A simple tracker for LV2 events
URL: https://git.open-music-kontrollers.ch/~hp/tracker.lv2
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

# current commit: a20e9434ea61f8aacbb302aea2d011f57e9705f6
# git clone --recursive https://git.open-music-kontrollers.ch/~hp/tracker.lv2
# cd tracker.lv2
# git checkout a20e9434ea61f8aacbb302aea2d011f57e9705f6
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz tracker.lv2.tar.gz tracker.lv2/*
# rm -rf tracker.lv2

Source0: tracker.lv2.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: meson
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: fontconfig-devel
BuildRequires: sord

%description
A simple tracker for LV2 events

%prep
%autosetup -n %{name}

%build

%set_build_flags

%meson -Dlv2libdir=%{_lib}/lv2
%meson_build

%install
%meson_install

%files
%doc README.md
%license COPYING
%{_libdir}/lv2/*

%changelog
* Sat Jan 16 2021 Yann Collette <ycollette.nospam@free.fr> - 0.1.1-1
- update to last master

* Sat Nov 28 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- Initial build
