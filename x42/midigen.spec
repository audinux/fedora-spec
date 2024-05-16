# Tag: MIDI, Tool
# Type: Plugin, LV2
# Category: MIDI, Tool

Name: midigen.lv2
Version: 0.4.2
Release: 1%{?dist}
Summary: LV2 MIDI Test Sequence Generator
License: GPL-2.0-or-later
URL: https://github.com/x42/midigen.lv2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/x42/midigen.lv2/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: lv2-devel

%description
midigen.lv2 is simple test-sequence generator.

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags
export OPTIMIZATIONS="$CFLAGS"
%make_build PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 fat1_VERSION=%{version} STRIP=true

%install

%make_install PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 fat1_VERSION=%{version} STRIP=true

%files
%doc README.md
%license COPYING
%{_libdir}/lv2/*

%changelog
* Wed May 24 2023 Yann Collette <ycollette.nospam@free.fr> - 0.4.2-1
- Initial spec file
