# Status: active
# Tag: Synthesizer
# Type: Standalone, Plugin, LV2, VST, VST3, CLAP
# Category: Synthesizer

%global commit0 6a1675109ef28b7f01088749dae860a885d6f472

Name: miriyaki-xt
Version: 0.0.1
Release: 1%{?dist}
Summary: Port BordaSynth's Miriyaki to DPF
License: GPL-3.0-or-later
URL: https://github.com/AnClark/Miriyaki-XT
ExclusiveArch: x86_64

Vendor:       Audinux
Distribution: Audinux

# ./anclark-source.sh <project> <tag>
# ./anclark-source.sh Miriyaki-XT develop

Source0: Miriyaki-XT.tar.gz
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

%description
Subtractive VST synth

%package -n license-%{name}
Summary:  License and documentation for %{name}
License:  GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n vst-%{name}
VST2 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n Miriyaki-XT

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_libdir}/lv2
install -m 755 -d %{buildroot}/%{_libdir}/vst
install -m 755 -d %{buildroot}/%{_libdir}/vst3
install -m 755 -d %{buildroot}/%{_libdir}/clap

cp -ra %{__cmake_builddir}/bin/Miriyaki-XT.lv2  %{buildroot}/%{_libdir}/lv2/
cp %{__cmake_builddir}/bin/Miriyaki-XT-vst2.so  %{buildroot}/%{_libdir}/vst/
cp -ra %{__cmake_builddir}/bin/Miriyaki-XT.vst3 %{buildroot}/%{_libdir}/vst3/
cp %{__cmake_builddir}/bin/Miriyaki-XT.clap     %{buildroot}/%{_libdir}/clap/

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Sat Feb 01 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial build
