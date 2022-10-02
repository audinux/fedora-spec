# Tag: Live, Video
# Type: Plugin, LV2
# Category: Effect

%global commit0 bedfdff6e2d85f228b8d8da7574c741da7d037af

Name:    prom
Version: 0.0.1
Release: 1%{?dist}
Summary: ProjectM LV2 plugin
License: GPLv2+
URL:     https://github.com/DISTRHO/ProM

Vendor:       Audinux
Distribution: Audinux

Source0: ProM.tar.gz
Source1: source-prom.sh

# ./source-prom.sh <tag>
# ./source-prom.sh master

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: liblo-devel
BuildRequires: projectM-mao-devel
BuildRequires: freetype-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel

%description
A ProjectM LV2 plugin

%prep
%autosetup -n ProM

%build

%make_build PREFIX=/usr LIBDIR=%{_lib} SKIP_STRIPPING=true

%install 

%make_install PREFIX=/usr LIBDIR=%{_lib} SKIP_STRIPPING=true

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Tue Oct 26 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial release
