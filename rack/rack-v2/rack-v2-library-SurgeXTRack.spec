# Status: active
# Tag: Modular, Rack
# Type: Rack
# Category: Audio, Synthesizer

%define use_static_glfw 0
%define use_static_rtaudio 0

# Global variables for github repository
%global commit0 640153d4e70896a707bc3a7cbff1d375c44581b6
%global gittag0 2.2.9.0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    rack-v2-SurgeXTRack
Version: 2.2.9.0
Release: 2%{?dist}
Summary: SurgeXTRack plugin for Rack
License: GPL-2.0-or-later
URL:     https://github.com/surge-synthesizer/surge-rack/
ExclusiveArch: x86_64 

Vendor:       Audinux
Distribution: Audinux

# ./rack-source.sh <tag>
# ./rack-source.sh v2.1.3

Source0: Rack.tar.gz
Source1: surge-rack.tar.gz
Source2: SurgeXTRack_plugin.json
Patch0: rack-v2-aarch64.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: cmake
BuildRequires: git
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
BuildRequires: chrpath

%description
SurgeXTRack plugin for Rack.
The Surge Filter VCFs

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

mkdir SurgeXTRack_plugin
tar xvfz %{SOURCE1} --directory=SurgeXTRack_plugin --strip-components=1

cp -n %{SOURCE2} SurgeXTRack_plugin/plugin.json || true

sed -i -e "s/\$(EXTRA_CMAKE)/\$(EXTRA_CMAKE) -DCMAKE_CXX_FLAGS='\$(MYCXXFLAGS)'/g" SurgeXTRack_plugin/Makefile
sed -i -e "s/SURGE_LIBS surge-common/SURGE_LIBS surge-common jansson/g" SurgeXTRack_plugin/CMakeLists.txt

sed -i -e "/,-march=nehalem/d" SurgeXTRack_plugin/RackSDK.cmake
sed -i -e "/static-libstdc/d" SurgeXTRack_plugin/RackSDK.cmake

sed -i -e "1i add_compile_options(-Wno-error=dangling-reference)" SurgeXTRack_plugin/surge/CMakeLists.txt

%build

CURRENT_PATH=`pwd`
MYCXXFLAGS="`pkg-config --cflags gtk+-x11-3.0` -I$CURRENT_PATH/include -I$CURRENT_PATH/dep/include -I$CURRENT_PATH/dep/nanovg/src -I$CURRENT_PATH/dep/nanovg/example -I/usr/include/rtmidi -I$CURRENT_PATH/dep/nanosvg/src -I$CURRENT_PATH/dep/oui-blendish -I$CURRENT_PATH/dep/osdialog -I$CURRENT_PATH/dep/pffft -I$CURRENT_PATH/dep/include -I$CURRENT_PATH/dep/fuzzysearchdatabase/src -Wno-error -include cstdint"
%ifarch x86_64 arm64
MYCXXFLAGS="$MYCXXFLAGS -DSIMDE_X86_AVX_NATIVE -DSIMDE_X86_SSE4_2_NATIVE -DSIMDE_X86_SSE4_1_NATIVE -DSIMDE_X86_SSSE3_NATIVE -DSIMDE_X86_SSE3_NATIVE -DSIMDE_X86_SSE2_NATIVE -DSIMDE_X86_SSE_NATIVE -DSIMDE_X86_MMX_NATIVE"
%endif
export MYCXXFLAGS="$MYCXXFLAGS"

cd SurgeXTRack_plugin
%make_build RACK_DIR=.. PREFIX=/usr STRIP=true LIBDIR=%{_lib} dist

%install

mkdir -p %{buildroot}%{_libexecdir}/Rack2/plugins/SurgeXTRack/
cp -r SurgeXTRack_plugin/dist/SurgeXTRack/* %{buildroot}%{_libexecdir}/Rack2/plugins/SurgeXTRack/

chrpath --delete %{buildroot}%{_libexecdir}/Rack2/plugins/SurgeXTRack/plugin.so

%files
%{_libexecdir}/*

%changelog
* Tue Nov 30 2021 Yann Collette <ycollette.nospam@free.fr> - 2.2.9.0-1
- initial specfile
