# Global variables for github repository
%global commit0 e672d5feb9d631798e3d56eb96e8958c3d2c6821
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    mod-distortion
Version: 0.9.%{shortcommit0}
Release: 2%{?dist}
Summary: mod-distortion LV2 set of plugins from portalmod
License: GPL-2.0-or-later
URL:     https://github.com/portalmod/mod-distortion

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/portalmod/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel

%description
mod-distortion LV2 set of plugins from portalmod

%prep
%autosetup -n %{name}-%{commit0}

%build
%make_build INSTALL_PATH=%{buildroot}%{_libdir}/lv2

%install 
%make_install INSTALL_PATH=%{buildroot}%{_libdir}/lv2

%files
%{_libdir}/lv2/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9-2
- update for Fedora 29

* Sun May 13 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9-2
- fix f27 / f28 build

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9-1
- Initial build
