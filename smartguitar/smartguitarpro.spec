# Tag: Guitar, Amp Simul
# Type: Plugin, VST
# Category: Audio, Effect
# GUIToolkit: GTK3

Name:    smartamppro
Version: 1.0
Release: 1%{?dist}
Summary: Guitar plugin emulating real hardware with Neural Network
License: GPLv2+
URL:     https://github.com/GuitarML/SmartAmpPro

# Source0: https://github.com/GuitarML/SmartAmpPro/archive/v{version}.tar.gz#/{name}-{version}.tar.gz
Source0: SmartAmpPro.tar.gz
Source1: smartguitarpro_build.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: eigen3-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: JUCE
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: json-devel
BuildRequires: numcpp
BuildRequires: boost-devel

%description
SmartGuitarAmpPro is a guitar plugin (VST3) made with JUCE that uses neural network models to emulate real world hardware.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
# autosetup -n SmartAmpPro-{version}
%autosetup -n SmartAmpPro

tar xvfz %{SOURCE1}

%build

%set_build_flags

export HOME=`pwd`
mkdir -p .vst3

cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true CXXFLAGS="-I/usr/include/eigen3 -I/usr/include/freetype2"

%install 

install -m 755 -d %{buildroot}/%{_libdir}/vst3/SmartAmpPro.vst3/Contents/x86_64-linux/
install -m 755 -d %{buildroot}/%{_bindir}/

install -m 755 -p Builds/LinuxMakefile/build/SmartAmpPro %{buildroot}/%{_bindir}/
cp -ra Builds/LinuxMakefile/build/SmartAmpPro.vst3/Contents/x86_64-linux/* %{buildroot}/%{_libdir}/vst3/SmartAmpPro.vst3//Contents/x86_64-linux/
chmod a+x %{buildroot}/%{_libdir}/vst3/SmartAmpPro.vst3/Contents/x86_64-linux/SmartAmpPro.so

mkdir -p %{buildroot}/%{_datadir}/smartamppro/models
cp  models/* %{buildroot}/%{_datadir}/smartamppro/models/

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/*
%{_datadir}/smartamppro/models/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Mon Jun 14 2021 Yann Collette <ycollette.nospam@free.fr> - 1.°-1
- Initial spec file
