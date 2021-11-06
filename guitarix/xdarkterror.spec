# Tag: Guitar, Amp Simul
# Type: Plugin, LV2
# Category: Audio, Effect

Name:    xdarkterror
Version: 0.0.1
Release: 1%{?dist}
Summary: Valve amplifier simulation
License: GPLv2+
URL:     https://github.com/brummer10/XDarkTerror.lv2

Vendor:       Audinux
Distribution: Audinux

# git clone https://github.com/brummer10/XDarkTerror.lv2
# cd XDarkTerror.lv2
# #git checkout v1.5
# git submodule init
# git submodule update
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz XDarkTerror.lv2.tar.gz XDarkTerror.lv2/*
# rm -rf XDarkTerror.lv2

Source0: XDarkTerror.lv2.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: libsigc++20-devel

%description
Valve amplifier simulation

%prep
%autosetup -n XDarkTerror.lv2

%build

%set_build_flags

%make_build STRIP=true

%install 

%make_install INSTALL_DIR=/usr/%{_lib}/lv2 STRIP=true

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Mon Sep 21 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file - master / aac27f8bb8b1ad2095b84cf5d693fd167ab0ab04
