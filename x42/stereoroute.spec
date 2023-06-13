# Tag: Alsa, Jack
# Type: Plugin, LV2
# Category: Audio, Tool

Name:    stereoroute.lv2
Version: 0.1.0
Release: 1%{?dist}
Summary: Stereo Routing Plugin
License: GPL-2.0-or-later
URL:     https://github.com/x42/stereoroute.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/x42/stereoroute.lv2/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc make
BuildRequires: lv2-devel

%description
Stereo Routing Plugin

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags
export OPTIMIZATIONS="$CFLAGS"
%make_build PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 fat1_VERSION=%{version} STRIP=true

%install 

%make_install PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 fat1_VERSION=%{version} STRIP=true

%files
%license COPYING
%{_libdir}/lv2/*

%changelog
* Wed May 24 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- Initial spec file
