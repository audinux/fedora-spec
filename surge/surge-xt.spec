%define _lto_cflags %{nil}

# Tag: Reverb, Compressor, Equalizer, Overdrive
# Type: Plugin, VST3, Standalone
# Category: Audio, Effect, Synthesizer

Name:    surge-xt
Version: 1.1.1
Release: 1%{?dist}
Summary: A VST3 Synthesizer and Effects, including Airwindows
License: GPLv2+
URL:     https://github.com/surge-synthesizer/surge

Vendor:       Audinux
Distribution: Audinux

# To get the sources, use:
# $ ./source-surge.sh release_xt_1.1.1

Source0: surge.tar.gz
Source1: source-surge.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: rsync
BuildRequires: git
BuildRequires: python3
BuildRequires: alsa-lib-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel
BuildRequires: freetype-devel
BuildRequires: libcurl-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel
BuildRequires: jack-audio-connection-kit-devel

%description
A VST3 Synthesizer and Effects, including Airwindows

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -p1 -n surge

sed -i -e "/Werror=/d" CMakeLists.txt
sed -i -e "/:-Werror/d" CMakeLists.txt

sed -i -e "s/Surge XT/Surge_XT/g" CMakeLists.txt
sed -i -e "s/Surge XT/Surge_XT/g" resources/CMakeLists.txt
sed -i -e "s/Surge XT/Surge_XT/g" src/surge-fx/CMakeLists.txt
sed -i -e "s/Surge XT/Surge_XT/g" src/CMakeLists.txt
sed -i -e "s/Surge XT/Surge_XT/g" src/surge-xt/CMakeLists.txt

sed -i -e "s/Surge_XT Effects/Surge_XT_Effects/g" src/surge-fx/CMakeLists.txt

%build

%cmake -DBUILD_SHARED_LIBS=OFF
%cmake_build

%install 

%cmake_install

%files
%{_bindir}/*
%{_datadir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Fri Aug 26 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1.1-1
- update to 1.1.1-1

* Thu Aug 04 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- update to 1.1.0-1

* Tue Jan 18 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
