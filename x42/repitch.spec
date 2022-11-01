# Tag: Alsa, Jack
# Type: Plugin, LV2
# Category: Audio, Tool

Name:    repitch.lv2
Version: 0.2.1
Release: 1%{?dist}
Summary: Counterbalance pitch when vari-speeding
License: GPLv2+
URL:     https://github.com/x42/repitch.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/x42/repitch.lv2/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++ make
BuildRequires: git
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: lv2-devel
BuildRequires: rubberband-devel

%description
Counterbalance pitch when vari-speeding

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags
export OPTIMIZATIONS="$CFLAGS"
%make_build PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 STRIP=true

%install 

%make_install PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 STRIP=true

%files
%license COPYING
%{_libdir}/lv2/*

%changelog
* Tue Nov 01 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2.1-1
- Initial spec file
