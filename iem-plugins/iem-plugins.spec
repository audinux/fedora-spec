# Tag: Effect
# Type: Standalone, VST3, LV2
# Category: Effect, Plugin

Name: iem-plugins
Version: 1.14.1
Release: 1%{?dist}
Summary: The IEM Plug-in Suite is a free and Open-Source audio plug-in suite.
License: GPL-3.0-or-later
URL: https://plugins.iem.at

Vendor:       Audinux
Distribution: Audinux

# Usage: ./iem-plugins-source.sh <TAG>
#        ./iem-plugins-source.sh v1.14.1

Source0: IEMPluginSuite.tar.gz
Source1: iem-plugins-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel

%description
The IEM Plug-in Suite is a free and Open-Source audio plug-in suite including
Ambisonic plug-ins up to 7th order created by staff and students of the Institute
of Electronic Music and Acoustics.
The suite provides plug-ins for a full Ambisonic production: encoders, reverbs,
dynamics including limiter and multi-band compression, rotators, and decoders for
both headphones and arbitrary loudspeaker layouts, and many more. The plug-ins are
created with the JUCE framework and can be compiled to any major plug-in format
(VST, VST3, LV2, AU, AAX).
All the plug-ins can be built as standalones, e.g. for use with JACK or virtual soundcards.
For more information, installation guides and plug-in descriptions see:
Website: https://plugins.iem.at
Repository: https://git.iem.at/audioplugins/IEMPluginSuite/

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n IEMPluginSuite

%build

%cmake -DIEM_BUILD_VST3=ON \
       -DIEM_BUILD_LV2=ON \
       -DIEM_BUILD_STANDALONE=ON \
       -DIEM_STANDALONE_JACK_SUPPORT=ON
%cmake_build

%install

PLUGINS="CoordinateConverter
	GranularEncoder
	ToolBox
	MultiEncoder
	DistanceCompensator
	SimpleDecoder
	DirectivityShaper
	OmniCompressor
	BinauralDecoder
	MultiEQ
	MultiBandCompressor
	ProbeDecoder
	StereoEncoder
	RoomEncoder
	SceneRotator
	AllRADecoder
	FdnReverb
	DualDelay
	MatrixMultiplier
	DirectionalCompressor
	EnergyVisualizer"

install -m 755 -d %{buildroot}%{_libdir}/vst3/
for plugin in $PLUGINS
do
    cp -ra %{__cmake_builddir}/"$plugin"/"$plugin"_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/
done

install -m 755 -d %{buildroot}%{_libdir}/lv2/
for plugin in $PLUGINS
do
    cp -ra %{__cmake_builddir}/"$plugin"/"$plugin"_artefacts/LV2/*  %{buildroot}/%{_libdir}/lv2/
done

install -m 755 -d %{buildroot}%{_bindir}/
for plugin in $PLUGINS
do
    cp -ra %{__cmake_builddir}/"$plugin"/"$plugin"_artefacts/Standalone/*  %{buildroot}/%{_bindir}/
done

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Mon Sep 18 2023 Yann Collette <ycollette.nospam@free.fr> - 1.14.1-1
- Initial spec file
