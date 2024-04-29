# Tag: Jack, Analyzer
# Type: Plugin, Standalone, VST3
# Category: Graphic, Audio

%global commit0 dd0dc1a6587e14f9bf67bba0c4161a6cb8e844b4

Name: multimeter
Version: 1.0.0
Release: 1%{?dist}
Summary: A comprehensive set of plugin real-time audio analysis tools in one window
License: GPL-3.0-or-later
URL: https://github.com/RealAlexZ/MultiMeter

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/RealAlexZ/MultiMeter/archive/%{commit0}.zip#/%{name}-%{version}.zip
Source1: Build.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: JUCE61
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
BuildRequires: pkgconfig(jack)
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel

%description
MultiMeter, an aesthetic AU/VST audio analyzer, caters to audio engineers, producers,
and musicians who seek precision and versatility. Leveraging the JUCE framework,
MultiMeter delivers a robust array of functions for pristine real-time audio analysis
to empower mixing, mastering, and sound design.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n MultiMeter-%{commit0}

tar xvfz %{SOURCE1}

sed -i -e "s/std::log10f/log10f/g" Source/SpectrumAnalyzer/SpectrumAnalyzer.cpp

%build

%set_build_flags
export CXXFLAGS="-include utility $CFLAGS"

cd Builds/LinuxMakefile/
%make_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra Builds/LinuxMakefile/build/MultiMeter.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 Builds/LinuxMakefile/build/MultiMeter %{buildroot}/%{_bindir}/

%files -n %{name}
%doc README.md
%license LICENSE.md
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Mon Apr 29 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
