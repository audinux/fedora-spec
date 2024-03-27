# Tag: Sampler, Synthesizer, Library
# Type: Plugin, LV2, VST3, Devel
# Category: Synthesizer, Programming

Name: sfizz-ui
Version: 1.2.3
Release: 1%{?dist}
License: BSD-2-Clause
Summary: SFZ based sampler, providing LV2 / VST3 plugins using the sfizz
URL: https://github.com/sfztools/sfizz-ui

Vendor:       Audinux
Distribution: Audinux

# Usage: ./sfizz-ui-source.sh <tag>
#        ./sfizz-ui-source.sh 1.2.3

Source0: sfizz-ui.tar.gz
Source1: sfizz-ui-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: libatomic
BuildRequires: libsndfile-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libX11-devel
BuildRequires: freetype-devel
BuildRequires: xcb-util-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: cairo-devel
BuildRequires: pango-devel
BuildRequires: simde-devel
BuildRequires: kiss-fft-devel
BuildRequires: pugixml-devel
BuildRequires: cxxopts-devel
BuildRequires: catch2-devel
BuildRequires: lv2-devel
BuildRequires: pkgconfig(jack)

%description
SFZ parser and synth c++ library, providing LV2 / VST3 plugins and JACK standalone client

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  BSD-2-Clause
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  BSD-2-Clause
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package devel
Summary:  Header files for Sfizz
Requires: %{name} = %{version}-%{release}

%description devel
Header files for the Sfizz library.

%prep
%autosetup -n %{name}

%build

%cmake -DPLUGIN_LV2=ON \
       -DPLUGIN_LV2_UI=ON \
       -DPLUGIN_VST3=ON \
       -DSFIZZ_USE_SYSTEM_LV2=ON \
       -DSFIZZ_USE_SYSTEM_VST3SDK=OFF \
       -DVST3_PLUGIN_INSTALL_DIR=%{_libdir}/vst3/ \
       -DLV2_PLUGIN_INSTALL_DIR=%{_libdir}/lv2/ \
       -DCMAKE_SKIP_RPATH=ON \
       -DSFIZZ_JACK=ON \
       -DSFIZZ_USE_SYSTEM_SIMDE=ON \
%if 0%{?fedora} <= 39
       -DSFIZZ_USE_SYSTEM_KISS_FFT=ON \
%endif
       -DSFIZZ_USE_SYSTEM_PUGIXML=ON \
       -DSFIZZ_USE_SYSTEM_CXXOPTS=ON \
       -DSFIZZ_USE_SYSTEM_CATCH=ON \
       -DSFIZZ_USE_SNDFILE=ON

%cmake_build

%install

%cmake_install

%files
%doc README.md GOVERNANCE.md CONTRIBUTING.md AUTHORS.md
%license LICENSE
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/sfizz.pc

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Mon Jan 15 2024 Yann Collette <ycollette.nospam@free.fr> - 1.2.3-1
- update to 1.2.3-1

* Tue Aug 29 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.2-1
- initial release of the spec file
