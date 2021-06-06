Summary: An audio stream chopping LV2 plugin
Name:    lv2-BChoppr
Version: 1.10.8
Release: 2%{?dist}
License: GPL
URL:     https://github.com/sjaehn/BChoppr

Source0: https://github.com/sjaehn/BChoppr/archive/%{version}.tar.gz#/BChoppr-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel

%description
BChoppr cuts the audio input stream into a repeated sequence of up to 16 chops.
Each chop can be leveled up or down (gating). BChoppr is the successor of BSlizr

%prep
%autosetup -n BChoppr-%{version}

%build

%make_build PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -include stdexcept -std=c++11 -fvisibility=hidden -fPIC"

%install

%make_install PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} CXXFLAGS="%{build_cxxflags} -include stdexcept -std=c++11 -fvisibility=hidden -fPIC"

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Sun Jun 06 2021 Yann Collette <ycollette dot nospam at free.fr> 1.10.8-2
- updata to 1.10.8-2

* Sun Apr 18 2021 Yann Collette <ycollette dot nospam at free.fr> 1.10.6-2
- updata to 1.10.6-2

* Thu Feb 11 2021 Yann Collette <ycollette dot nospam at free.fr> 1.10.4-2
- updata to 1.10.4-2

* Fri Jan 29 2021 Yann Collette <ycollette dot nospam at free.fr> 1.10.2-2
- updata to 1.10.2-2

* Mon Jan 11 2021 Yann Collette <ycollette dot nospam at free.fr> 1.10.0-2
- updata to 1.10.0-2

* Thu Aug 27 2020 Yann Collette <ycollette dot nospam at free.fr> 1.8.0-2
- updata to 1.8.0-2

* Thu Jun 25 2020 Yann Collette <ycollette dot nospam at free.fr> 1.6.4-2
- updata to 1.6.4

* Fri Apr 24 2020 Yann Collette <ycollette dot nospam at free.fr> 1.4.0-2
- fix for Fedora 32

* Thu Apr 2 2020 Yann Collette <ycollette dot nospam at free.fr> 1.4.0-1
- initial release 
