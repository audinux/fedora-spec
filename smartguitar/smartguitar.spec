# Tag: Guitar, Amp Simul
# Type: Plugin, VST
# Category: Audio, Effect
# GUIToolkit: GTK3

Name:    smartamp
Version: 1.2
Release: 1%{?dist}
Summary: Guitar plugin emulating real hardware with Neural Network
License: GPLv2+
URL:     https://github.com/GuitarML/SmartGuitarAmp

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/GuitarML/SmartGuitarAmp/archive/v_%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: smartguitar_build.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: eigen3-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: JUCE5
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

%description
SmartGuitarAmp is a guitar plugin (VST3) made with JUCE that uses neural network models to emulate real world hardware.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n SmartGuitarAmp-v_%{version}

tar xvfz %{SOURCE1}

sed -i -e "s|/usr/src/JUCE|/usr/src/JUCE5|g" plugins/SmartAmp/Builds/LinuxMakefile/Makefile

%build

%set_build_flags

export HOME=`pwd`
mkdir -p .vst3

cd plugins/SmartAmp/Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true CXXFLAGS="-I/usr/include/eigen3 -I/usr/include/freetype2" LDFLAGS="$LDFLAGS -lX11 -lXext `pkg-config --libs webkit2gtk-4.0`"

%install 

install -m 755 -d %{buildroot}/%{_libdir}/vst3/SmartAmp.vst3/Contents/x86_64-linux/
install -m 755 -d %{buildroot}/%{_bindir}/

install -m 755 -p plugins/SmartAmp/Builds/LinuxMakefile/build/SmartAmp %{buildroot}/%{_bindir}/
cp -ra plugins/SmartAmp/Builds/LinuxMakefile/build/SmartAmp.vst3/Contents/x86_64-linux/* %{buildroot}/%{_libdir}/vst3/SmartAmp.vst3//Contents/x86_64-linux/
chmod a+x %{buildroot}/%{_libdir}/vst3/SmartAmp.vst3/Contents/x86_64-linux/SmartAmp.so

mkdir -p %{buildroot}/%{_datadir}/smartamp/models
cp  models/* %{buildroot}/%{_datadir}/smartamp/models/

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/smartamp/models/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Sun Feb 21 2021 Yann Collette <ycollette.nospam@free.fr> - 1.2-1
- Initial spec file
