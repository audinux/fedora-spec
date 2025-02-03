# Status: active
# Tag: Synthesizer
# Type: Standalone, Plugin, LV2, VST, VST3
# Category: Synthesizer

%global commit0 0ee0a7fdef3505d730cef6aa219fba5001a2cc05

Name: rp2a03
Version: 0.0.1
Release: 1%{?dist}
Summary: Nintendo RP2A03 Synthesizer
License: LGPL-2.1
URL: https://github.com/AnClark/RP2A03
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./anclark-source.sh <project> <tag>
# ./anclark-source.sh RP2A03 master

Source0: RP2A03.tar.gz
Source1: anclark-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: pkgconfig(jack)
BuildRequires: liblo-devel
BuildRequires: mesa-libGL-devel
BuildRequires: cairo-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel

%description
Nintendo RP2A03 Synthesizer

%package -n license-%{name}
Summary:  License and documentation for %{name}
License:  LGPL-2.1

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  LGPL-2.1
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  LGPL-2.1
Requires: license-%{name}

%description -n vst-%{name}
VST2 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  LGPL-2.1
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n RP2A03

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/lv2
install -m 755 -d %{buildroot}/%{_libdir}/vst
install -m 755 -d %{buildroot}/%{_libdir}/vst3

cp %{__cmake_builddir}/RP2A03_artefacts/Standalone/* %{buildroot}/%{_bindir}/
cp -ra %{__cmake_builddir}/RP2A03_artefacts/LV2/*    %{buildroot}/%{_libdir}/lv2/
cp %{__cmake_builddir}/RP2A03_artefacts/VST/*        %{buildroot}/%{_libdir}/vst/
cp -ra %{__cmake_builddir}/RP2A03_artefacts/VST3/*   %{buildroot}/%{_libdir}/vst3/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Sat Feb 01 2025 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- Initial build
