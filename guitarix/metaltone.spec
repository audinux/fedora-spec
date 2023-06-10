# Tag: Guitar, Overdrive
# Type: Plugin, LV2
# Category: Audio, Effect

Name:    lv2-metaltone
Version: 0.1
Release: 1%{?dist}
Summary: Overdrive / Distortion
License: GPL-2.0-or-later
URL:     https://github.com/brummer10/MetalTone

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./brummer10-source.sh MetalTone v0.1

Source0: MetalTone.tar.gz
Source1: brummer10-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: libsigc++20-devel
BuildRequires: vim-common

%description
Overdrive / Distortion

%prep
%autosetup -n MetalTone

%build

%set_build_flags

%make_build STRIP=true

%install 

%make_install INSTALL_DIR=/usr/%{_lib}/lv2 STRIP=true

%files
%doc README.md
%{_libdir}/lv2/*

%changelog
* Mon Sep 21 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial spec file
