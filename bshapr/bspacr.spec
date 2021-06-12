%define _lto_cflags %{nil}

# Tag: Jack
# Type: Plugin, LV2
# Category: Audio, Effect

Summary: No loss LV2 sound effect plugin
Name:    lv2-BSpacr
Version: 1.2.0
Release: 1%{?dist}
License: GPL
URL:     https://github.com/sjaehn/BSpacr

Source0: https://github.com/sjaehn/BSpacr/archive/refs/tags/%{version}.tar.gz#/BSpacr-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel

%description
No loss LV2 sound effect plugin

%prep
%autosetup -n BSpacr-%{version}

%build

%make_build PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC"

%install

%make_install PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC"

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Thu Apr 01 2021 Yann Collette <ycollette dot nospam at free.fr> 1.2.0-1
- initial release 
