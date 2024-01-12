# Tag: Audio, Modulaation
# Type: Plugin, LV2
# Category: Audio, Effect

%define commit0 edc2be7fb6b2121a216993a8b4e7f7c114ad8257

Name: lv2-gula-plugins
Version: 0.0.1
Release: 1%{?dist}
Summary: LV2 plugins which is a combination of vibrato and tremelo.
License: GPL-3.0-or-later
URL: https://github.com/steveb/gula-plugins

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/steveb/gula-plugins/archive/%{commit0}.zip#/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: boost-devel

%description
A collection of guitar effect LV2 plugins with MOD Devices user interfaces.

%prep
%autosetup -n gula-plugins-%{commit0}

%build

%set_build_flags
%make_build PREFIX=/usr

%install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -ra lv2/* %{buildroot}/%{_libdir}/lv2/

%files
%doc README.rst
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Fri Jan 20 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial build

