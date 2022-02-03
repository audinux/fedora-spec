# Global variables for github repository
%global commit0 4461547c300896690eb9dd809f7d0aaf648da11c
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    VL1-emulator
Version: 1.1.0.0
Release: 2%{?dist}
Summary: An emulator of Casio VL-Tone VL1
License: GPLv2+
URL:     https://github.com/linuxmao-org/VL1-emulator

Vendor:       Audinux
Distribution: Audinux

# ./vl1-source.sh <tag>
# ./vl1-source.sh 1.1.0.0

Source0: VL1-emulator.tar.gz
Source1: vl1-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel
BuildRequires: mesa-libGL-devel
BuildRequires: cairo-devel

%description
An emulator of Casio VL-Tone VL1, based on source code by PolyValens

%prep
%autosetup -n %{name}

%build

%set_build_flags

%make_build PREFIX=/usr LIBDIR=%{_lib} SKIP_STRIPPING=true

%install

%make_install PREFIX=/usr LIBDIR=%{_lib} SKIP_STRIPPING=true

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/vl1.lv2
install -m 755 -d %{buildroot}/%{_libdir}/vst

cp bin/vl1 %{buildroot}/%{_bindir}/
cp -r bin/vl1.lv2/* %{buildroot}/%{_libdir}/lv2/vl1.lv2/
cp bin/vl1-vst.so %{buildroot}/%{_libdir}/vst/

%files
%{_bindir}/*
%{_libdir}/lv2/*
%{_libdir}/vst/*

%changelog
* Tue Oct 20 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.0.0-2
- fix debug build

* Thu Jan 16 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.0.0-1
- Initial build
