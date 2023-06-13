# Tag: Alsa, Jack
# Type: Plugin, LV2
# Category: Audio, Tool

Name:    nodelay.lv2
Version: 0.6.3
Release: 1%{?dist}
Summary: audio delay line with latency reporting -- LV2 test & instrumentation tool
License: GPL-2.0-or-later
URL:     https://github.com/x42/nodelay.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/x42/nodelay.lv2/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++ make
BuildRequires: lv2-devel

%description
nodelay is a simple audio delay-line that optionally reports its delay as
latency, in which case the effect should be transparent when used with LV2
hosts that implement latency compensation.

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags
export OPTIMIZATIONS="$CFLAGS"
%make_build PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 STRIP=true

%install 

%make_install PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 STRIP=true

%files
%doc README
%license COPYING
%{_libdir}/lv2/*

%changelog
* Thu May 11 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.3-1
- update to 0.6.3-1

* Sun Nov 20 2022 Yann Collette <ycollette.nospam@free.fr> - 0.6.2-1
- Initial spec file
