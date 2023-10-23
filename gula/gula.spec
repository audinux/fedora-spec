Name: gula
Version: 0.1
Release: 1%{?dist}
Summary: An LV2 plugin which is a combination of vibrato and tremelo.
License: GPL3
URL: https://github.com/steveb/gula-plugins

Source0: https://github.com/steveb/gula-plugins/archive/refs/heads/master.zip#/gula-master.zip

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: boost-devel

%description
A collection of guitar effect LV2 plugins with MOD Devices user interfaces.

%prep
%autosetup -n gula-plugins-master

sed -i -e "/SSE_CFLAGS =/d" src/Makefile
sed -i -e "/CXXFLAGS +=/,/LDFLAGS +=/d" src/Makefile

%build

%set_build_flags

%make_build

%install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -ra lv2/* %{buildroot}/%{_libdir}/lv2/

%files
%doc README.rst
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Thu May 12 2022 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- initial version of the spec
