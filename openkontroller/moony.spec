# Tag: Tool, Devel
# Type: Plugin, LV2
# Category: MIDI, Plugin, Programming

Name: moony.lv2
Version: 0.40.0
Release: 2%{?dist}
Summary: Realtime Lua as programmable glue in LV2
URL: https://git.open-music-kontrollers.ch/~hp/moony.lv2
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://git.open-music-kontrollers.ch/~hp/moony.lv2/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: sratom-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: flex
BuildRequires: meson

%description
An investigative LV2 plugin bundle

%prep
%autosetup -n %{name}-%{commit0}

%build

%set_build_flags

%meson -Dlv2libdir=%{_lib}/lv2
%meson_build

%install

%meson_install

%files
%doc README.md ChangeLog
%license COPYING
%{_libdir}/lv2/*

%changelog
* Mon Nov 01 2021 Yann Collette <ycollette.nospam@free.fr> - 0.40.0-2
- update to 0.40.0-2

* Sat Jan 16 2021 Yann Collette <ycollette.nospam@free.fr> - 0.36.0-2
- update to 0.36.0-2

* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.34.0-2
- fix debug build

* Sat Jul 18 2020 Yann Collette <ycollette.nospam@free.fr> - 0.34.0-1
- Initial spec file
