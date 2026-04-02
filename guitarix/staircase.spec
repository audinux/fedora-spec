# Status: active
# Tag: Guitar, Distortion
# Type: Plugin, LV2
# Category: Audio, Effect

%define commit0 10faf9848751b7b82af1e472a048e73e4f4d0a22

Name: lv2-staircase
Version: 0.1
Release: 1%{?dist}
Summary: LV2 distortion plugin
License: GPL-2.0-or-later
URL: https://github.com/brummer10/Staircase
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./brummer10-source.sh Staircase 10faf9848751b7b82af1e472a048e73e4f4d0a22

Source0: Staircase.tar.gz
Source1: brummer10-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: libsigc++20-devel
BuildRequires: fftw-devel
BuildRequires: vim-common

%description
Staircase is a lightweight distortion plugin with integrated filtering and real-time spectrum visualization.
It is designed for efficient DSP performance and a clean, responsive UI.

%prep
%autosetup -n Staircase

%build

%set_build_flags

%make_build STRIP=true

%install

%make_install INSTALL_DIR=/usr/%{_lib}/lv2 STRIP=true

%files
%doc README.md
%{_libdir}/lv2/*

%changelog
* Thu Apr 02 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
