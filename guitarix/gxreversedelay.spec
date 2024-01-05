# Tag: Delay
# Type: Plugin, LV2
# Category: Audio, Effect

# Global variables for github repository
%global commit0 b34579b58726257bdbc05bd885b4dc308eefa5d8
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: lv2-GxReverseDelay
Version: 0.1.%{shortcommit0}
Release: 2%{?dist}
Summary: Digital reverse delay LV2 plugin
License: GPL-2.0-or-later
URL: https://github.com/brummer10/GxReverseDelay.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/brummer10/GxReverseDelay.lv2/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:  gxreversedelay-0001-cleanup-flags.patch

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: python
BuildRequires: gtk2-devel
BuildRequires: glib2-devel

%description
Digital reverse delay LV2 plugin.

%prep
%autosetup -p1 -n GxReverseDelay.lv2-%{commit0}

%build

%set_build_flags

%make_build INSTALL_DIR=%{buildroot}%{_libdir}/lv2 STRIP=true

%install

%make_install INSTALL_DIR=%{buildroot}%{_libdir}/lv2 STRIP=true

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/gx_reversedelay.lv2/*

%changelog
* Sat Nov 28 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1-2
- upstream fix for build on F32 and F33

* Sat Nov 28 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial build
