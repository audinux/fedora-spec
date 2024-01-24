# Tag: Synthesizer
# Type: Plugin, VST2, CLAP, LV2, Standalone
# Category: Audio, Synthesizer

Name: minaton-xt
Version: 0.2.0
Release: 1%{?dist}
Summary: DPF port of Minaton, an analogue style synthesizer
License: GPL-3.0-or-later
URL: https://github.com/AnClark/Minaton-XT

Vendor:       Audinux
Distribution: Audinux

# Usage: ./source-minaton.sh <tag>
#        ./source-minaton.sh 0.2.0

Source0: Minaton-XT.tar.gz
Source1: source-minaton.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(jack)
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel
BuildRequires: SDL2-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: libglvnd-devel
BuildRequires: libX11-devel

%description
This project, Minaton-XT, ports Minaton to DPF, DISTRHO Plugin Framework.
The synth has three oscillators, two LFOs, One low pass resonant filter, oscillator sync,
two ADSR envelopes which can be redirected to oscillator pitch. The mod wheel controls
filter frequency.

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n vst-%{name}
VST2 version of %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n clap-%{name}
CLAP version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n Minaton-XT

sed -i -e "/binary_to_compressed_c PRIVATE -static)/d" CMakeLists.txt

%build

%set_build_flags

%cmake -DUSE_SYSTEM_LIBSAMPLERATE=ON -DUSE_SYSTEM_LIBSNDFILE=ON
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_libdir}/vst/
install -m 755 -d %{buildroot}/%{_libdir}/vst3
install -m 755 -d %{buildroot}/%{_libdir}/clap/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/
install -m 755 -d %{buildroot}/%{_bindir}/

cp %{__cmake_builddir}/bin/minaton %{buildroot}/%{_bindir}/
cp %{__cmake_builddir}/bin/minaton.clap %{buildroot}/%{_libdir}/clap/
cp -ra %{__cmake_builddir}/bin/minaton.lv2 %{buildroot}/%{_libdir}/lv2/
cp %{__cmake_builddir}/bin/minaton-vst2.so %{buildroot}/%{_libdir}/vst/
cp -ra %{__cmake_builddir}/bin/minaton.vst3 %{buildroot}/%{_libdir}/vst3/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Wed Jan 24 2024 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- Initial spec file
