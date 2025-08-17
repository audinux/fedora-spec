# Status: active
# Tag: Modular, Rack
# Type: Rack
# Category: Audio, Synthesizer

%define use_static_glfw 0
%define use_static_rtaudio 1

%global debug_package %{nil}

# Global variables for github repository
%global commit0 e7567e5f27073433cea7f714b46cb62cf89c72a2 
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    rack-v2-Fundamental
Version: 2.6.4
Release: 3%{?dist}
Summary: A plugin for Rack
License: GPL-2.0-or-later
URL:     https://github.com/VCVRack/Fundamental
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./rack-source-v2.sh <tag>
# ./rack-source-v2.sh v2.1.1

Source0: Rack.tar.gz
Source1: https://github.com/VCVRack/Fundamental/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2: rack-source-v2.sh
Patch0: rack-v2-aarch64.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: libsamplerate-devel
BuildRequires: libzip-devel
BuildRequires: glew-devel
BuildRequires: glfw-devel
BuildRequires: portmidi-devel
BuildRequires: portaudio-devel
BuildRequires: libcurl-devel
BuildRequires: openssl-devel
BuildRequires: jansson-devel
BuildRequires: gtk3-devel
BuildRequires: rtmidi-devel
%if !%{use_static_rtaudio}
BuildRequires: rtaudio-devel
%endif
BuildRequires: speex-devel
BuildRequires: wget
BuildRequires: simde-devel
BuildRequires: speexdsp-devel
BuildRequires: gulrak-filesystem-devel
BuildRequires: libarchive-devel
BuildRequires: libzstd-devel
BuildRequires: Rack-v2
BuildRequires: jq

%description
The Fundamental plugin pack gives you a basic foundation to create simple synthesizers,
route and analyze signals, complement other more complicated modules,
and build some not-so-simple patches using brute force (lots of modules).
They are also a great reference for creating your own plugins in C++.

%prep
%setup -n Rack

%ifarch aarch64
%patch 0 -p1
%endif

CURRENT_PATH=`pwd`

# Remove some architectures optimization
sed -i -e "s/-march=nehalem//g" compile.mk
sed -i -e "s/-march=nehalem//g" dep.mk
# For -O2 usage
sed -i -e "s/-O3/-O2/g" compile.mk
sed -i -e "s/-O3/-O2/g" dep.mk
sed -i -e "s/DEP_FLAGS += -g -O2/DEP_FLAGS += -g -O2 \$(CFLAGS)/g" dep.mk

# Remove static gcc lib
sed -i -e "s/-static-libstdc++ -static-libgcc//g" Makefile
sed -i -e "s/-static-libstdc++ -static-libgcc//g" plugin.mk

%if !%{use_static_glfw}
NEW_FLAGS="-I/usr/include/GLFW"
%endif
%if !%{use_static_rtaudio}
NEW_FLAGS="$NEW_FLAGS -I/usr/include/rtaudio"
%endif

echo "CXXFLAGS += $NEW_FLAGS -O2 -fPIC -funsafe-math-optimizations -fno-omit-frame-pointer -mtune=generic `pkg-config --cflags gtk+-x11-3.0` -I$CURRENT_PATH/include -I$CURRENT_PATH/dep/include -I$CURRENT_PATH/dep/nanovg/src -I$CURRENT_PATH/dep/nanovg/example -I/usr/include/rtmidi -I$CURRENT_PATH/dep/tinyexpr -I$CURRENT_PATH/dep/nanosvg/src -I$CURRENT_PATH/dep/oui-blendish -I$CURRENT_PATH/dep/osdialog -I$CURRENT_PATH/dep/pffft -I$CURRENT_PATH/dep/include -I$CURRENT_PATH/dep/fuzzysearchdatabase/src" >> compile.mk

%if %{use_static_glfw}
echo "Use Static GLFW"
%else
echo "Do not use static GLFW"
%endif
%if %{use_static_rtaudio}
echo "Use Static RTAUDIO"
%else
echo "Do not use static RTAUDIO"
%endif

sed -i -e "s/-Wl,-Bstatic//g" Makefile

sed -i -e "s/dep\/lib\/libGLEW.a/-lGLEW/g" Makefile
%if !%{use_static_glfw}
sed -i -e "s/dep\/lib\/libglfw3.a/-lglfw/g" Makefile
%else
sed -i -e "s/dep\/lib\/libglfw3.a/dep\/%{_lib}\/libglfw3.a/g" Makefile
%endif
sed -i -e "s/dep\/lib\/libjansson.a/-ljansson/g" Makefile
sed -i -e "s/dep\/lib\/libcurl.a/-lcurl/g" Makefile
sed -i -e "s/dep\/lib\/libssl.a/-lssl/g" Makefile
sed -i -e "s/dep\/lib\/libcrypto.a/-lcrypto/g" Makefile
sed -i -e "s/dep\/lib\/libzip.a/-lzip/g" Makefile
sed -i -e "s/dep\/lib\/libz.a/-lz/g" Makefile
sed -i -e "s/dep\/lib\/libspeexdsp.a/-lspeexdsp/g" Makefile
sed -i -e "s/dep\/lib\/libsamplerate.a/-lsamplerate/g" Makefile
sed -i -e "s/dep\/lib\/librtmidi.a/-lrtmidi/g" Makefile
sed -i -e "s/dep\/lib\/libarchive.a/-larchive/g" Makefile
sed -i -e "s/dep\/lib\/libzstd.a/-lzstd/g" Makefile
# We use provided RtAudio library because Rack hangs when using jack and fedora rtaudio
%if !%{use_static_rtaudio}
sed -i -e "s/dep\/lib\/librtaudio.a/-lrtaudio -lpulse-simple -lpulse/g" Makefile
%else
sed -i -e "s/dep\/lib\/librtaudio.a/dep\/%{_lib}\/librtaudio.a -lpulse-simple -lpulse/g" Makefile
%endif

# Remove rpath
sed -i -e "/-rpath/d" Makefile
sed -i -e "/-rpath/d" plugin.mk

mkdir fundamental_plugin
tar xvfz %{SOURCE1} --directory=fundamental_plugin --strip-components=1

# TODO: C++ error - check periodically if the problem is fixed or not.
sed -i -e "s/using VCVBezelLightBigWhite = LightButton/using VCVBezelLightBigWhite = struct rack::componentlibrary::Lightbutton/g" fundamental_plugin/src/Logic.cpp

%Build

cd fundamental_plugin
%make_build RACK_DIR=.. PREFIX=/usr STRIP=true LIBDIR=%{_lib} dist

%install

mkdir -p %{buildroot}%{_libexecdir}/Rack2/plugins/Fundamental/
cp -r fundamental_plugin/dist/Fundamental/* %{buildroot}%{_libexecdir}/Rack2/plugins/Fundamental/

%files
%{_libexecdir}/*

%changelog
* Sun Aug 17 2025 Yann Collette <ycollette.nospam@free.fr> - 2.6.4-3
- update to 2.6.4-3

* Sun May 04 2025 Yann Collette <ycollette.nospam@free.fr> - 2.6.3-3
- update to 2.6.3-3

* Thu Apr 17 2025 Yann Collette <ycollette.nospam@free.fr> - 2.6.2-3
- update to 2.6.2-3

* Fri Nov 22 2024 Yann Collette <ycollette.nospam@free.fr> - 2.6.1-3
- update to 2.6.1-3

* Tue Oct 10 2023 Yann Collette <ycollette.nospam@free.fr> - 2.6.0-3
- update to 2.6.0-3

* Fri Aug 25 2023 Yann Collette <ycollette.nospam@free.fr> - 2.5.1-3
- update to 2.5.1-3

* Sun Aug 06 2023 Yann Collette <ycollette.nospam@free.fr> - 2.5.0-3
- update to 2.5.0-3 - last master

* Sun Apr 02 2023 Yann Collette <ycollette.nospam@free.fr> - 2.3.0-3
- update to 2.3.0-3 - last master

* Tue Aug 09 2022 Yann Collette <ycollette.nospam@free.fr> - 2.3.0-2
- update to 2.3.0-2

* Fri Mar 04 2022 Yann Collette <ycollette.nospam@free.fr> - 2.1.0-2
- update to last master - 4484ad68ab5f51a1225ac3cd7d3dc1ea689a52e9 - 2.1.0-2

* Fri Mar 04 2022 Yann Collette <ycollette.nospam@free.fr> - 2.1.0-1
- update to 2.1.0-1

* Sun Nov 29 2020 Yann Collette <ycollette.nospam@free.fr> - 1.4.0-6
- fix rtaudio + debug build

* Fri Oct 30 2020 Yann Collette <ycollette.nospam@free.fr> - 1.4.0-5
- update to 1.4.0-5

* Tue Sep 8 2020 Yann Collette <ycollette.nospam@free.fr> - 1.4.0-4
- update to 1.4.0-4.

* Thu Feb 13 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.1-4
- update to 1.3.1-4. Update to last master to add Pulse plugin

* Mon Jan 27 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.1
- update to 1.3.1

* Sun Nov 18 2018 Yann Collette <ycollette.nospam@free.fr> - 0.6.1
- initial specfile
