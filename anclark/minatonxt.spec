# Status: active
# Tag: Synthesizer
# Type: Standalone, Plugin, LV2, VST, VST3, CLAP
# Category: Synthesizer

Name: minaton-xt
Version: 0.2.0
Release: 1%{?dist}
Summary: DPF port of Minaton, an analogue style synthesizer
License: GPL-3.0-or-later
URL: https://github.com/AnClark/Minaton-XT
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./anclark-source.sh <project> <tag>
# ./anclark-source.sh Minaton-XT 0.2.0

Source0: Minaton-XT.tar.gz
Source1: anclark-source.sh
Patch0: minatonxt-0001-remove-static-link.patch

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

%description
Minaton - A monophonic, subtractive, beefy analogue style bass and lead synthesizer.
Originally written by Nick Bailey (ThunderOx Software) (@thunderox)

This project, Minaton-XT, ports Minaton to DPF, DISTRHO Plugin Framework.

With DPF powered, Minaton is alive again. It is not limited to the only LV2
format any more, instead it can run in multiple formats.

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
%autosetup -p1 -n Minaton-XT

%build

%cmake -DUSE_SYSTEM_LIBSAMPLERATE=ON \
       -DUSE_SYSTEM_LIBSNDFILE=ON
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/lv2
install -m 755 -d %{buildroot}/%{_libdir}/vst
install -m 755 -d %{buildroot}/%{_libdir}/vst3
install -m 755 -d %{buildroot}/%{_libdir}/clap

cp %{__cmake_builddir}/bin/minaton          %{buildroot}/%{_bindir}/
cp -ra %{__cmake_builddir}/bin/minaton.lv2  %{buildroot}/%{_libdir}/lv2/
cp %{__cmake_builddir}/bin/minaton-vst2.so  %{buildroot}/%{_libdir}/vst/
cp -ra %{__cmake_builddir}/bin/minaton.vst3 %{buildroot}/%{_libdir}/vst3/
cp %{__cmake_builddir}/bin/minaton.clap     %{buildroot}/%{_libdir}/clap/

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

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Sat Feb 01 2025 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- Initial build
