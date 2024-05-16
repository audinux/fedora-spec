# Tag: Guitar, Tape
# Type: Plugin, LV2, VST3, CLAP
# Category: Audio, Effect

Name: ChowKick
Version: 1.2.0
Release: 1%{?dist}
Summary: Kick synthesizer based on old-school drum machine circuits
License: BSD-3-Clause
URL: https://github.com/Chowdhury-DSP/ChowKick
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# to generater code archive:
# ./source_chowkick.sh <tag>
# ./source_chowkick.sh v1.2.0

Source0: ChowKick.tar.gz
Source1: source_chowkick.sh

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: JUCE
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(webkit2gtk-4.0)
BuildRequires: pkgconfig(gtk+-x11-3.0)
BuildRequires: pkgconfig(jack)
BuildRequires: libcurl-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: xsimd-devel
BuildRequires: lv2-devel
BuildRequires: chrpath

%description
ChowKick is a kick drum synthesizer plugin based on creative modelling
of old-school drum machine circuits. MIDI input to the plugin triggers
a pulse with a parameterized size and shape.
The pulse is then passed into a resonant filter which can be tuned to a
specific frequency, or matched to the frequency of the incoming MIDI notes.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  BSD-3-Clause

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  BSD-3-Clause

%description -n clap-%{name}
CLAP version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  BSD-3-Clause

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n ChowKick

%build
%set_build_flags

%cmake -DCHOWKICK_BUILD_CLAP=ON
%cmake_build

%install

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/vst3/
mkdir -p %{buildroot}%{_libdir}/clap/
mkdir -p %{buildroot}%{_libdir}/lv2/

install %{__cmake_builddir}/ChowKick_artefacts/Standalone/* %{buildroot}%{_bindir}/
cp -r %{__cmake_builddir}/ChowKick_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/
cp -r %{__cmake_builddir}/ChowKick_artefacts/CLAP/* %{buildroot}%{_libdir}/clap/
cp -r %{__cmake_builddir}/ChowKick_artefacts/LV2/* %{buildroot}%{_libdir}/lv2/

# Fix RPATH
chrpath --delete %{buildroot}%{_libdir}/vst3/ChowKick.vst3/Contents/*/ChowKick.so
chrpath --delete %{buildroot}%{_libdir}/lv2/ChowKick.lv2/libChowKick.so
chrpath --delete %{buildroot}%{_libdir}/clap/ChowKick.clap
chrpath --delete %{buildroot}%{_bindir}/ChowKick

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/

%files -n clap-%{name}
%{_libdir}/clap/

%files -n lv2-%{name}
%{_libdir}/lv2/


%changelog
* Mon Aug 21 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-1
- Initial spec file
