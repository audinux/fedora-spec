# Status: active
# Tag: Mixer
# Type: Plugin, LV2
# Category: Audio

Name: xmixer
Version: 0.0.1
Release: 1%{?dist}
Summary: A simple 4 in 1 Mixer
License: GPL-2.0-or-later
URL: https://github.com/brummer10/XMixer.lv2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./brummer10-source.sh XMixer.lv2 main

Source0: XMixer.lv2.tar.gz
Source1: brummer10-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: lilv-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: libsigc++20-devel
BuildRequires: vim-common

%description
A simple 4 in 1 Mixer

%prep
%autosetup -n XMixer.lv2

%build

%set_build_flags

export CXXFLAGS="-std=c++11 -fPIC -I/usr/include/cairo $CXXFLAGS"
%make_build STRIP=true

%install

%make_install INSTALL_DIR=/usr/%{_lib}/lv2 STRIP=true

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Sun May 23 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
