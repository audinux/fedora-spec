# Status: active
# Tag: Guitar, Amp Simul
# Type: Plugin, VST
# Category: Audio, Effect
# GUIToolkit: GTK3

%define toneversion 1.0

Name: smartamppro
Version: 1.0
Release: 2%{?dist}
Summary: Guitar plugin emulating real hardware with Neural Network
License: GPL-2.0-or-later
URL: https://github.com/GuitarML/SmartAmpPro
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./source-guitarml.sh SmartAmpPro 13bdf299b5aca3de92b73163c7d74f28c77f1d96

Source0: SmartAmpPro.tar.gz
Source1: smartguitarpro_build.tar.gz
Source2: https://github.com/GuitarML/ToneLibrary/archive/refs/tags/v%{toneversion}.zip#/tonelib-%{toneversion}.zip
Source3: source-guitarml.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: eigen3-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: JUCE60
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
BuildRequires: json-devel
BuildRequires: numcpp
BuildRequires: boost-devel
BuildRequires: unzip

%description
SmartGuitarAmpPro is a guitar plugin (VST3) made with JUCE that uses neural network models to emulate real world hardware.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n SmartAmpPro

tar xvfz %{SOURCE1}

sed -i -e "s|/usr/src/JUCE|/usr/src/JUCE60|g" Builds/LinuxMakefile/Makefile

%build

%set_build_flags

export HOME=`pwd`
mkdir -p .vst3

cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true CXXFLAGS="-I/usr/include/eigen3 -I/usr/include/freetype2" LDFLAGS="$LDFLAGS -lX11 -lXext `pkg-config --libs webkit2gtk-4.0`"

%install

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
install -m 755 -d %{buildroot}/%{_bindir}/

install -m 755 -p Builds/LinuxMakefile/build/SmartAmpPro %{buildroot}/%{_bindir}/
cp -ra Builds/LinuxMakefile/build/SmartAmpPro.vst3 %{buildroot}/%{_libdir}/vst3/

mkdir -p %{buildroot}/%{_datadir}/smartamppro/models
cp  models/* %{buildroot}/%{_datadir}/smartamppro/models/

install -m 755 -d %{buildroot}%{_datadir}/smartamppro/tones/
unzip %{SOURCE2}
mv ToneLibrary-%{toneversion}/SmartAmpPro/* %{buildroot}%{_datadir}/smartamppro/tones/

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/*
%{_datadir}/smartamppro/
%{_datadir}/smartamppro/models/*
%{_datadir}/smartamppro/tones/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Fri Dec 23 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0-2
- update to 1.0-2 - add presets

* Mon Jun 14 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- Initial spec file
