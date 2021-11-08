# Tag: Modular, Jack, Alsa
# Type: Plugin, LV2
# Category: Audio, Synthesizer

Name:    infamousPlugins
Version: 0.3.0
Release: 2%{?dist}
Summary: LV2 Audio Plugins for Linux 
URL:     https://github.com/ssj71/infamousPlugins
License: GPLv2+

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ssj71/infamousPlugins/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: qt5-qtbase-devel
BuildRequires: non-ntk-devel
BuildRequires: non-ntk-fluid
BuildRequires: cairo-devel
BuildRequires: lv2-devel
BuildRequires: zita-resampler-devel
BuildRequires: fftw3-devel

%description
Infamous Plugins is a collection of open-source LV2 plugins.
It hopefully helps fill some holes, supplying non-existing plugins for linux audio.
There is little interest in creating ANOTHER compressor, or ANOTHER EQ when myriad
other excellent lv2 versions of such already exist. At least until I become
interested in making one of those things and feel I can do something different...

%package -n lv2-%{name}
Summary: Infamous set of LV2 Plugins

%description -n lv2-%{name}
Infamous Plugins is a collection of open-source LV2 plugins.
It hopefully helps fill some holes, supplying non-existing
plugins for linux audio.
There is little interest in creating ANOTHER compressor, or
ANOTHER EQ when myriad other excellent lv2 versions of such
already exist.
At least until I become interested in making one of those
things and feel I can do something different...

%prep
%autosetup -n %{name}-%{version}

%build

%cmake -DLIBDIR=%{_lib}

%cmake_build

%install

%cmake_install

%files -n lv2-%{name}
%doc README CHANGELOG
%license COPYING
%{_bindir}/*
%{_libdir}/lv2/*

%changelog
* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-2
- fix for fedora 33

* Tue Apr 16 2019 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-1
- Initial version of spec file
