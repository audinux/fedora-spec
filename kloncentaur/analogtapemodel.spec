# Tag: Guitar, Tape
# Type: Plugin, LV2, VST
# Category: Audio, Effect

Name:    AnalogTapeModel
Version: 2.8.0
Release: 1%{?dist}
Summary: Physical modelling signal processing for analog tape recording
License: BSD-3-Clause
URL:     https://github.com/jatinchowdhury18/AnalogTapeModel

# to generater code archive:
# ./source_analogtapemodel.sh <tag>
# ./source_analogtapemodel.sh 2.8.0

Source0: AnalogTapeModel.tar.gz
Source1: source_analogtapemodel.sh

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
CHOW Tape Model is a physical model of an analog tape machine,
implemented as an audio plugin.

%package -n vst3-%{name}
Summary: CHOW Tape Model plugin (VST3)

%description -n vst3-%{name}
CHOW Tape Model is a physical model of an analog tape machine,
implemented as an audio plugin.

%package -n lv2-%{name}
Summary: CHOW Tape Model plugin (LV2)

%description -n lv2-%{name}
CHOW Tape Model is a physical model of an analog tape machine,
implemented as an audio plugin.

%prep
%autosetup -n AnalogTapeModel

%build
%set_build_flags

cd Plugin
%cmake -B cmake-build -DCMAKE_BUILD_TYPE=Release -DRTNEURAL_XSIMD=ON -DCMAKE_PREFIX_PATH=/usr/lib64/juce
touch cmake-build/CHOWTapeModel_artefacts/JuceLibraryCode/AppConfig.h
cmake --build cmake-build %{?_smp_mflags}

%install
cd Plugin
mkdir -p %{buildroot}%{_bindir}
install cmake-build/CHOWTapeModel_artefacts/Release/Standalone/* %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_libdir}/vst3
cp -r cmake-build/CHOWTapeModel_artefacts/Release/VST3/*.vst3 %{buildroot}%{_libdir}/vst3/
mkdir -p %{buildroot}%{_libdir}/lv2
cp -r cmake-build/CHOWTapeModel_artefacts/Release/LV2/*.lv2 %{buildroot}%{_libdir}/lv2/

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
* Mon Jun 07 2021 Yann Collette <ycollette.nospam@free.fr> - 2.8.0-1
- Initial spec file
