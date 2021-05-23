# Global variables for github repository
%global commit0 f1c3f4b94ea04a991c201bbe6a19336471b5f37e
%global gittag0 v0.1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    lv2-GxMatchEQ
Version: 0.1.%{shortcommit0}
Release: 2%{?dist}
Summary: Matching Equalizer to apply EQ curve from on source to a other source
License: GPLv2+
URL:     https://github.com/brummer10/GxMatchEQ.lv2

Source0: https://github.com/brummer10/GxMatchEQ.lv2/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: python
BuildRequires: gtk2-devel
BuildRequires: glib2-devel

%description
Matching Equalizer to apply EQ curve from on source to a other source.

%prep
%autosetup -n GxMatchEQ.lv2-%{commit0}

%build

%set_build_flags

%make_build INSTALL_DIR=%{buildroot}%{_libdir}/lv2 STRIP=true

%install 

make INSTALL_DIR=%{buildroot}%{_libdir}/lv2 STRIP=true install

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/gx_matcheq.lv2/*

%changelog
* Tue Oct 20 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1-2
- fix debug build

* Fri May 22 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial build
