# Status: active
# Tag: Audio, AI, Amp Simul
# Type: Plugin, LV2
# Category: Audio, Tool

%global commit0 d34a9a66e9ae3a4811e9bcf6df420347e23638b0

Name: lv2-neural-amp-modeler-ui
Version: 0.0.1
Release: 2%{?dist}
Summary: This is a GUI for the Neural Amp Modeler LV2 plugin
License: GPL-2.0-or-later
URL: https://github.com/brummer10/neural-amp-modeler-ui
ExclusiveArch: x86_64 

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./brummer10-source.sh neural-amp-modeler-ui d34a9a66e9ae3a4811e9bcf6df420347e23638b0

Source0: neural-amp-modeler-ui.tar.gz
Source1: brummer10-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: ncurses
BuildRequires: pkgconfig(jack)
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: lv2-devel
BuildRequires: libsigc++20-devel

Requires: lv2-neural-amp-modeler

%description
This is a Gui for the Neural Amp Modeler LV2 plugin by Mike Oliphant

%prep
%autosetup -n neural-amp-modeler-ui

%build

%set_build_flags

%make_build STRIP=true

%install

install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -ra bin/* %{buildroot}%{_libdir}/lv2/

%files
%doc README.md
%{_libdir}/lv2/*

%changelog
* Tue May 13 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to 0.0.1-2 - d34a9a66e9ae3a4811e9bcf6df420347e23638b0

* Tue Feb 20 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
