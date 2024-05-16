# Tag: Audio, Tool
# Type: Plugin, LV2
# Category: Audio, Tool

%define commit0 23152a8bf6dcdf2496df0d696dfd4c1a61f67e54

Name: lv2-cv-to-cc
Version: 0.1
Release: 1%{?dist}
Summary: convert LV2 CV to MIDI CC
License: GPL-2.0-or-later
URL: https://github.com/polyeffects/cv_to_cc.lv2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/polyeffects/cv_to_cc.lv2/archive/%{commit0}.zip#/%{name}-%{commit0}.zip

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: lv2-devel

%description
converts LV2 CV v/oct to MIDI notes

%prep
%autosetup -n cv_to_cc.lv2-%{commit0}

%build

%set_build_flags

%make_build STRIP=true

%install

%make_install PREFIX=/usr LV2DIR=%{_libdir}/lv2 STRIP=true

%files
%doc README.md
%{_libdir}/lv2/*

%changelog
* Sat Oct 14 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial development
