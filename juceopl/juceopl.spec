# Tag: Jack, Alsa
# Type: Plugin, Standalone, VST3
# Category: Audio, Synthesizer

Name: juceopl
Version: 1.0.1
Release: 1%{?dist}
Summary: A VST instrument which emulates the Yamaha OPL sound chip used in PC sound cards from the 90s
License: GPL-2.0-only
URL: https://github.com/bsutherland/JuceOPLVSTi

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/bsutherland/JuceOPLVSTi/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Source1: https://web.archive.org/web/20181016150224/https://download.steinberg.net/sdk_downloads/vstsdk3610_11_06_2018_build_37.zip
Source1: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip
Source2: Builds.zip

BuildRequires: gcc gcc-c++
BuildRequires: make
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
BuildRequires: flac-devel
BuildRequires: libogg-devel
BuildRequires: libvorbis-devel

%description
This VST instrument provides an emulated OPL sound chip. It provides all
features of the OPL2, and some features of the OPL3.
It is distributed under the GPLv2 or later.

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  GPL-3.0-only
Requires: %{name}

%description -n vst-%{name}
VST2 version of %{name}

%prep
%autosetup -n JuceOPLVSTi-%{version}

unzip %{SOURCE1}
unzip %{SOURCE2}

%build

CWD=`pwd`

cd Builds/LinuxMakefile
%make_build STRIP=true CXXFLAGS="-I$CWD/VST_SDK/VST2_SDK -I/usr/include/JUCE-7.0.5/modules"

%install

install -m 755 -d %{buildroot}%{_libdir}/vst/
install -m 755 -p Builds/LinuxMakefile/build/JuceOPLVSTi.so %{buildroot}/%{_libdir}/vst/

%files
%doc readme.md
%license COPYING

%files -n vst-%{name}
%{_libdir}/vst/*

%changelog
* Mon Feb 27 2023  Yann Collette <ycollette.nospam@free.fr> - 1.0.1-1
- Initial spec file
