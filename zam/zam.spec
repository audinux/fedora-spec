# Tag: Jack, Compressor, Overdrive, Equalizer, Delay, Gate
# Type: Plugin, LV2, VST
# Category: Audio, Effect

Name:    zam-plugins
Version: 3.14
Release: 3%{?dist}
Summary: Set of LV2 plugins
License: GPLv2+
URL:     https://github.com/zamaudio/zam-plugins

Vendor:       Audinux
Distribution: Audinux

# ./zam-source.sh 3.14
Source0: zam-plugins-%{version}.tar.xz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libsamplerate-devel

%description
Zam LV2 set of plugins
Compressors, Limiters, Saturation, Tube emulation, 
Equalizers, Delay, Gates

%package -n ladspa-zam
Summary: Zam LADSPA plugin

%description -n ladspa-zam
Zam LADSPA plugin

%package -n vst-zam
Summary: Zam VST plugin

%description -n vst-zam
Zam VST plugin

%prep
%autosetup -n zam-plugins-%{version}

%build

%define _lto_cflags %{nil}

%make_build PREFIX=/usr LIBDIR=%{_lib} SKIP_STRIPPING=true CFLAGS="%optflags" CXXFLAGS="%optflags" all

%install 

%make_install PREFIX=/usr LIBDIR=%{_lib} SKIP_STRIPPING=true CFLAGS="%optflags" CXXFLAGS="%optflags" install

%files
%doc changelog NOTICE.DPF NOTICE.SFZero README.md
%license COPYING
%{_bindir}/*
%{_libdir}/lv2/*

%files -n ladspa-zam
%{_libdir}/ladspa/* 

%files -n vst-zam
%{_libdir}/vst/* 

%changelog
* Sun Dec 20 2020 Yann Collette <ycollette.nospam@free.fr> - 3.14-3
- update to 3.14

* Sun Jul 19 2020 Yann Collette <ycollette.nospam@free.fr> - 3.13-3
- fix debug build

* Sun Jul 19 2020 Yann Collette <ycollette.nospam@free.fr> - 3.13-2
- update to zam-plugins-3.13

* Sun Dec 15 2019 Yann Collette <ycollette.nospam@free.fr> - 3.12-2
- update to zam-plugins-3.12

* Tue Jun 4 2019 Yann Collette <ycollette.nospam@free.fr> - 3.11-2
- update to zam-plugins-3.11

* Tue Apr 30 2019 Yann Collette <ycollette.nospam@free.fr> - 3.10-2
- update to zam-plugins-3.10-10-g7232969

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 3.10-2
- update for Fedora 29
- update to zam-plugins-3.10-10-g7232969.tar.xz

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 3.10
- update version to 3.10

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 3.9
- update version to 3.9

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 3.5
- Initial build
