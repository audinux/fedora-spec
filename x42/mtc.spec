# Status: active
# Tag: Video, Tool
# Type: Plugin, LV2
# Category: Tool

Name: mtc.lv2
Version: 0.2.3
Release: 1%{?dist}
Summary: MTC Generator LV2 Plugin
License: GPL-2.0-or-later
URL: https://github.com/x42/mtc.lv2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/x42/mtc.lv2/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel

%description
MTC Generator LV2 Plugin

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags
export OPTIMIZATIONS="$CFLAGS"
%make_build PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 STRIP=true

%install

%make_install PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 STRIP=true

%files
%doc README.md
%license COPYING
%{_libdir}/lv2/*

%changelog
* Thu May 11 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2.3-1
- update to 0.2.3-1

* Tue Nov 01 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2.2-1
- Initial spec file
