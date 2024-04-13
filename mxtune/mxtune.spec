# Tag: Effect
# Type: Plugin, VST
# Category: Audio, Effect

%global commit0 c4e08a69de0720a99540c687ccb0e679ba221a3a

Name: mxtune
Version: 1.2.0
Release: 1%{?dist}
Summary: pitch correction plugin for VST 
License: GPL-3.0-or-later
URL: https://github.com/liuanlin-mx/MXTune

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/liuanlin-mx/MXTune/archive/%{commit0}.zip#/%{name}-%{version}.zip
# Source1: https://web.archive.org/web/20181016150224/https://download.steinberg.net/sdk_downloads/vstsdk3610_11_06_2018_build_37.zip
Source1: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip
Source2: build.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
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
BuildRequires: aubio-devel
BuildRequires: soundtouch-devel
BuildRequires: rubberband-devel

%description
Pitch correction plugin for VST

%prep
%autosetup -n MXTune-%{commit0}

unzip %{SOURCE1}

cd JUCE
tar xvfz %{SOURCE2}
cd ..

sed -i -e "s|-Os -O2 -std=c++17| -I$PWD/VST_SDK/VST2_SDK/ \${CMAKE_CXX_FLAGS} -include cstdint -Os -O2 -std=c++17|g" CMakeLists.txt
sed -i -e "s|-Wl,--strip-all||g" CMakeLists.txt
sed -i -e "s|-s ||g" CMakeLists.txt

%build

PWD=`pwd`

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst/
install -m 755 %{__cmake_builddir}/*.so %{buildroot}/%{_libdir}/vst/

%files
%doc README.md
%license COPYING-autotalent COPYING-mayer_fft LICENSE
%{_libdir}/*

%changelog
* Sat Apr 13 2024 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-1
- Initial spec file
