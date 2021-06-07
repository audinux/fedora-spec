# Tag: Guitar, Delay
# Type: Plugin, LV2, VST
# Category: Audio, Effect

Name:    ChowMatrix
Version: 1.2.0
Release: 1%{?dist}
Summary: Matrix delay effect
License: BSD-3-Clause
URL:     https://github.com/Chowdhury-DSP/ChowMatrix

# to generater code archive:
# ./source_chowmatrix.sh <tag>
# ./source_chowmatrix.sh 1.2.0

Source0: ChowMatrix.tar.gz
Source1: source_chowmatrix.sh

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(webkit2gtk-4.0)
BuildRequires: pkgconfig(gtk+-x11-3.0)
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libcurl-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: xsimd-devel
BuildRequires: lv2-devel
BuildRequires: JUCE
BuildRequires: cmake

%description
CHOW Matrix is a delay effect, made up of an infinitely growable tree
of delay lines, each with individual controls for feedback, panning,
distortion, and more.

%package -n vst3-%{name}
Summary: CHOW Matrix plugin (VST3)

%description -n vst3-%{name}
CHOW Matrix is a delay effect, made up of an infinitely growable tree
of delay lines, each with individual controls for feedback, panning,
distortion, and more.

%package -n lv2-%{name}
Summary: CHOW Matrix plugin (LV2)

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
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n vst3-%{name}
%doc README.md
%license LICENSE
%{_libdir}/vst3/

%files -n lv2-%{name}
%doc README.md
%license LICENSE
%{_libdir}/lv2/

%changelog
* Mon Jun 07 2021 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-1
- Initial spec file
