
# Tag: Mixer, Alsa, Jack
# Type: Plugin, LV2
# Category: Audio, Tool

Name:    matrixmixer.lv2
Version: 0.4.2
Release: 2%{?dist}
Summary: A LV2 matrix mixer
License: GPLv2+
URL:     https://github.com/x42/matrixmixer.lv2

Vendor:       Audinux
Distribution: Audinux

# ./matrixmixer-source.sh <tag>
# ./matrixmixer-source.sh v0.4.2

Source0: matrixmixer.lv2.tar.gz
Source1: matrixmixer-source.sh

BuildRequires: gcc gcc-c++ make
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: lv2-devel
BuildRequires: cairo-devel
BuildRequires: pango-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel

%description
A NxM LV2 matrix mixer by x42

%prep
%autosetup -n %{name}

%build

%make_build PREFIX=/usr LV2DIR=%{_libdir}/lv2 matrixmixer_VERSION=%{version} STRIP=true

%install 

%make_install PREFIX=/usr LV2DIR=%{_libdir}/lv2 matrixmixer_VERSION=%{version} STRIP=true

%files
%doc README.md
%license COPYING
%{_bindir}/*
%{_libdir}/lv2/*
%{_datadir}/*

%changelog
* Thu Oct 06 2022 Yann Collette <ycollette.nospam@free.fr> - 0.4.2-2
- update to 0.4.2-1

* Wed Jul 21 2021 Yann Collette <ycollette.nospam@free.fr> - 0.3.3-2
- update to 0.3.3-1

* Wed Apr 07 2021 Yann Collette <ycollette.nospam@free.fr> - 0.3.2-2
- update to 0.3.2

* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-2
- fix debug build

* Fri May 8 2020 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-1
- Initial spec file
