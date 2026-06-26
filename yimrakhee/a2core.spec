# Status: active
# Tag: Audio, AI, Amp Simul
# Type: Plugin, LV2, MODGUI
# Category: Audio, Tool

%global commit0 47b7846c8783738841e2bb0f87474073b3261bcc

Name: a2core
Version: 0.0.1
Release: 1%{?dist}
Summary: A lightweight, minimal LV2 plugin for running Neural Amp Modeler (NAM) models
License: MIT
URL: https://codeberg.org/yimrakhee/a2core.lv2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./a2core-source.sh <TAG>
#        ./a2core-source.sh main

Source0: a2core.lv2.tar.gz
Source1: a2core-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: eigen3-devel
BuildRequires: json-devel
BuildRequires: lv2-devel

%description
A collection of LV2 plugins including delay, tube distortion, compressor,
LPF, HPF, phaser, reverb, and utilities, all featuring GUIs.

%prep
%autosetup -n a2core.lv2

%build

export HOME=`pwd`
mkdir -p .lv2

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -ra .lv2/* %{buildroot}/%{_libdir}/lv2/

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Thu Jun 18 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- first version of the spec
