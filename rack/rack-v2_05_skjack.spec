# Tag: Modular, Rack
# Type: Rack
# Category: Audio, Synthesizer

%define use_static_glfw 0
%define use_static_rtaudio 1

# Disable production of debug package.
%global debug_package %{nil}
%define _lto_cflags %{nil}

Name:    rack-v2-skjack
Version: 0.6.8
Release: 2%{?dist}
Summary: A plugin for Rack
License: GPLv2+
URL:     https://github.com/nielszweistein/skjack-vcv2

Vendor:       Audinux
Distribution: Audinux

# ./rack-source.sh <tag>
# ./rack-source.sh v2.0.3

# wget https://github.com/nielszweistein/skjack-vcv2/archive/486e3bdb3488dcab1ef776b92896a67c2b714883.zip
# unzip 486e3bdb3488dcab1ef776b92896a67c2b714883.zip
# tar cvfz rack-v2-skjack.tar.gz skjack-vcv2-486e3bdb3488dcab1ef776b92896a67c2b714883
# rm -rf skjack-vcv2-486e3bdb3488dcab1ef776b92896a67c2b714883

Source0: Rack.tar.gz
Source1: rack-v2-skjack.tar.gz
Source2: https://raw.githubusercontent.com/nielszweistein/skjack-vcv2/master/plugin.json

BuildRequires: gcc gcc-c++
BuildRequires: sed
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsamplerate-devel
BuildRequires: libzip-devel
BuildRequires: glew-devel
BuildRequires: glfw-devel
BuildRequires: portmidi-devel
BuildRequires: portaudio-devel
BuildRequires: libcurl-devel
BuildRequires: openssl-devel
BuildRequires: jansson-devel
BuildRequires: gtk2-devel
BuildRequires: rtaudio-devel
BuildRequires: rtmidi-devel
BuildRequires: speex-devel
BuildRequires: speexdsp-devel
BuildRequires: jq
BuildRequires: ffmpeg-devel
BuildRequires: opus-devel
BuildRequires: lame-devel
BuildRequires: Rack-v2

%description
VCV Rack plugin dedicated to recording

%prep
%autosetup -n Rack

CURRENT_PATH=`pwd`

# Remove some architectures optimization
sed -i -e "s/-march=nehalem//g" compile.mk
sed -i -e "s/-march=nehalem//g" dep.mk
# For -O2 usage
sed -i -e "s/-O3/-O2/g" compile.mk
sed -i -e "s/-O3/-O2/g" dep.mk
sed -i -e "s/DEP_FLAGS += -g -O2/DEP_FLAGS += -g -O2 \$(CFLAGS)/g" dep.mk 

sed -i -e "47,49d" dep.mk

# Remove static gcc lib
sed -i -e "s/-static-libstdc++ -static-libgcc//g" Makefile
sed -i -e "s/-static-libstdc++ -static-libgcc//g" plugin.mk

%if !%{use_static_glfw}
NEW_FLAGS="-I/usr/include/GLFW"
%endif
%if !%{use_static_rtaudio}
NEW_FLAGS="$NEW_FLAGS -I/usr/include/rtaudio"
%endif

echo "CXXFLAGS += $NEW_FLAGS `pkg-config --cflags gtk+-x11-3.0` -I$CURRENT_PATH/include -I$CURRENT_PATH/dep/include -I$CURRENT_PATH/dep/nanovg/src -I$CURRENT_PATH/dep/nanovg/example -I/usr/include/rtmidi -I$CURRENT_PATH/dep/nanosvg/src -I$CURRENT_PATH/dep/oui-blendish -I$CURRENT_PATH/dep/osdialog -I$CURRENT_PATH/dep/pffft -I$CURRENT_PATH/dep/include -I$CURRENT_PATH/dep/fuzzysearchdatabase/src -I/usr/include/ffmpeg" >> compile.mk

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

mkdir skjack_plugin
tar xvfz %{SOURCE1} --directory=skjack_plugin --strip-components=1 
cp %{SOURCE2} skjack_plugin

%build

%set_build_flags
export CXXFLAGS="-O2 -fPIC -funsafe-math-optimizations -fno-omit-frame-pointer -mtune=generic -fpermissive -include libavutil/channel_layout.h $CXXFLAGS"

cd skjack_plugin
%make_build RACK_DIR=.. PREFIX=/usr LIBDIR=%{_lib} dist

%install 

mkdir -p %{buildroot}%{_libexecdir}/Rack2/plugins/SkJack/
cp -r skjack_plugin/dist/SkJack/* %{buildroot}%{_libexecdir}/Rack2/plugins/SkJack/

%files
%{_libexecdir}/*

%changelog
* Wed Jul 27 2022 Yann Collette <ycollette.nospam@free.fr> - 0.6.8-1
- initial specfile
