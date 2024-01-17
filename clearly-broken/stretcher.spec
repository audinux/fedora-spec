# Tag: Effect
# Type: Plugin, LV2, VST3
# Category: Audio, Effect

%global commit0 c7dc69b207e0fc44789450f1d2d121b9a887ddf1

Name: stretcher
Version: 0.0.1
Release: 1%{?dist}
Summary: an audio time stretcher plugin using Rubberband
License: GPL-2.0-only
URL: https://github.com/clearly-broken-software/Stretcher

# Usage: ./clearly-broken-source.sh <PROJECT> <TAG>
#        ./clearly-broken-source.sh Stretcher c7dc69b207e0fc44789450f1d2d121b9a887ddf1

Source0: Stretcher.tar.gz
Source1: clearly-broken-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: mesa-libGL-devel
BuildRequires: libsndfile-devel
BuildRequires: rubberband-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libX11-devel
BuildRequires: lv2-devel

%description
An audio time stretcher plugin using Rubberband.

%package -n vst-%{name}
Summary:  VST version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst-%{name}
VST version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n Stretcher

%build
%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/Stretcher.lv2/
install -m 755 -d %{buildroot}/%{_libdir}/vst/

install -m 755 -p %{__cmake_builddir}/bin/Stretcher %{buildroot}%{_bindir}/
install -m 755 -p %{__cmake_builddir}/bin/Stretcher-vst2.so %{buildroot}%{_libdir}/vst/
cp -ra %{__cmake_builddir}/bin/Stretcher.lv2/* %{buildroot}%{_libdir}/lv2/Stretcher.lv2/

%files
%doc readme.md
%{_bindir}/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Tue Aug 02 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- initial spec file
