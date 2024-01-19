# Tag: Audio, Effect, Pitch
# Type: Plugin, LV2
# Category: Audio, Effect

Name: repitch.lv2
Version: 0.2.3
Release: 1%{?dist}
Summary: Counterbalance pitch when vari-speeding
License: GPL-2.0-or-later
URL: https://github.com/x42/repitch.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/x42/repitch.lv2/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequiers: make
BuildRequires: git
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
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
* Thu May 11 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2.3-1
- update to 0.2.3-1

* Sun Nov 20 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2.2-1
- update to 0.2.2-1

* Tue Nov 01 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2.1-1
- Initial spec file
