# Status: active
# Tag: Guitar, Delay
# Type: Plugin, LV2, VST
# Category: Audio, Effect

Name: ChowMatrix
Version: 1.3.0
Release: 1%{?dist}
Summary: Matrix delay effect
License: BSD-3-Clause
URL: https://github.com/Chowdhury-DSP/ChowMatrix
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# to generater code archive:
# ./source_chowmatrix.sh <tag>
# ./source_chowmatrix.sh v1.3.0

Source0: ChowMatrix.tar.gz
Source1: source_chowmatrix.sh

BuildRequires: gcc-c++
BuildRequires: JUCE
BuildRequires: cmake
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gtk+-x11-3.0)
BuildRequires: pkgconfig(jack)
BuildRequires: libcurl-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: xsimd-devel
BuildRequires: lv2-devel

Requires: license-%{name}

%description
CHOW Matrix is a delay effect, made up of an infinitely growable tree
of delay lines, each with individual controls for feedback, panning,
distortion, and more.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: BSD-3-Clause

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: CHOW Matrix plugin (VST3)
License: BSD-3-Clause
Requires: license-%{name}

%description -n vst3-%{name}
CHOW Matrix is a delay effect, made up of an infinitely growable tree
of delay lines, each with individual controls for feedback, panning,
distortion, and more.

%package -n lv2-%{name}
Summary: CHOW Matrix plugin (LV2)
License: BSD-3-Clause
Requires: license-%{name}

%description -n lv2-%{name}
CHOW Matrix is a delay effect, made up of an infinitely growable tree
of delay lines, each with individual controls for feedback, panning,
distortion, and more.

%prep
%autosetup -n ChowMatrix

%build
%set_build_flags

%cmake -B cmake-build -DCMAKE_BUILD_TYPE=Release -DRTNEURAL_XSIMD=ON -DCMAKE_PREFIX_PATH=/usr/lib64/juce
touch cmake-build/ChowMatrix_artefacts/JuceLibraryCode/AppConfig.h
cmake --build cmake-build %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
install cmake-build/ChowMatrix_artefacts/Release/Standalone/* %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_libdir}/vst3
cp -r cmake-build/ChowMatrix_artefacts/Release/VST3/*.vst3 %{buildroot}%{_libdir}/vst3/
mkdir -p %{buildroot}%{_libdir}/lv2
cp -r cmake-build/ChowMatrix_artefacts/Release/LV2/*.lv2 %{buildroot}%{_libdir}/lv2/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/

%files -n lv2-%{name}
%{_libdir}/lv2/

%changelog
* Tue Dec 21 2021 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-1
- update to 1.3.0-1

* Mon Jun 07 2021 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-1
- Initial spec file
