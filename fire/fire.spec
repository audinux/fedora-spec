# Tag: Jack, Alsa
# Type: Plugin, Standalone, VST3
# Category: Audio, Distortion

Name:    fire
Version: 0.9.8
Release: 1%{?dist}
Summary: This is a distortion plugin developed by Wings
License: GPLv2+
URL:     https://github.com/jerryuhoo/Fire

Vendor:       Audinux
Distribution: Audinux

# Usage: ./fire-sources.sh <TAG>
# ./fire-sources.sh v0.9.8
# ./vst3-source.sh

Source0: Fire.tar.gz
Source1: Fire-makefile.tar.gz
Source2: vst3sdk.tar.gz
Source3: fire-source.sh
Source4: vst3-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: JUCE61
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel

%description
This is a multi-band distortion plugin 『Fire』.
It can be used in DAWs which supports AU and Vst3 plugins such
as Ableton Live, Fl Studio, etc.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n Fire

tar xvfz %{SOURCE1}
tar xvfz %{SOURCE2}

%build

%set_build_flags

# VST3 part

CWD=`pwd`
export CPPFLAGS="-I$CWD/JUCE/modules -I$CWD/vst3sdk -include utility $CPPFLAGS"

cd Builds/LinuxMakefile
%make_build CONFIG=Release STRIP=true

%install 

install -m 755 -d %{buildroot}%{_libdir}/vst3/Fire.vst3/

cp -ra Builds/LinuxMakefile/build/Fire.vst3/* %{buildroot}/%{_libdir}/vst3/Fire.vst3/

%files -n vst3-%{name}
%doc README.md
%license LICENSE.md
%{_libdir}/vst3/*

%changelog
* Mon Jul 04 Jul 2022 Yann Collette <ycollette.nospam@free.fr> - 0.9.8-1
- Initial spec file
