# Tag: Modular, Rack
# Type: Rack
# Category: Audio, Synthesizer

%define use_static_glfw 0
%define use_static_rtaudio 0

# Global variables for github repository
%global commit0 a239b823cea2bbde28ae2a9299f51f01c95b7b93
%global gittag0 2.0.3
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    rack-v2-LyraeModules
Version: 2.0.3
Release: 1%{?dist}
Summary: LyraeModules plugin for Rack
License: GPL-2.0-or-later
URL:     https://github.com/VegaDeftwing/LyraeModules
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./rack-source.sh <tag>
# ./rack-source.sh v2.0.3

Source0: Rack.tar.gz
Source1: https://github.com/VegaDeftwing/LyraeModules/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source2: LyraeModules_plugin.json
Patch0: rack-v2-aarch64.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake sed
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
LyraeModules plugin for Rack.
Distortion at 15 Solar Radii

%prep
%setup -n Rack

%ifarch aarch64
%patch0 -p1
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

echo "CXXFLAGS += $NEW_FLAGS `pkg-config --cflags gtk+-x11-3.0` -I$CURRENT_PATH/include -I$CURRENT_PATH/dep/include -I$CURRENT_PATH/dep/nanovg/src -I$CURRENT_PATH/dep/nanovg/example -I/usr/include/rtmidi -I$CURRENT_PATH/dep/nanosvg/src -I$CURRENT_PATH/dep/oui-blendish -I$CURRENT_PATH/dep/osdialog -I$CURRENT_PATH/dep/pffft -I$CURRENT_PATH/dep/include -I$CURRENT_PATH/dep/fuzzysearchdatabase/src" >> compile.mk

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

mkdir LyraeModules_plugin
tar xvfz %{SOURCE1} --directory=LyraeModules_plugin --strip-components=1

cp -n %{SOURCE2} LyraeModules_plugin/plugin.json || true

%build

cd LyraeModules_plugin
%make_build RACK_DIR=.. PREFIX=/usr STRIP=true LIBDIR=%{_lib} dist

%install

mkdir -p %{buildroot}%{_libexecdir}/Rack2/plugins/LyraeModules/
cp -r LyraeModules_plugin/dist/LyraeModules/* %{buildroot}%{_libexecdir}/Rack2/plugins/LyraeModules/

%files
%{_libexecdir}/*

%changelog
* Tue Nov 30 2021 Yann Collette <ycollette.nospam@free.fr> - 2.0.3-1
- initial specfile
