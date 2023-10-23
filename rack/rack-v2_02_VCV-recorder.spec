# Tag: Modular, Rack
# Type: Rack
# Category: Audio, Synthesizer

%define use_static_glfw 0
%define use_static_rtaudio 1

# Disable production of debug package.
%global debug_package %{nil}
%define _lto_cflags %{nil}

Name:    rack-v2-VCV-Recorder
Version: 2.0.2
Release: 3%{?dist}
Summary: A plugin for Rack
License: GPL-2.0-or-later
URL:     https://github.com/VCVRack/VCV-Recorder

Vendor:       Audinux
Distribution: Audinux

# ./rack-source.sh <tag>
# ./rack-source.sh v2.0.3

# ./vcv-recorder-source.sh <tag>
# ./vcv-recorder-source.sh v2.0.2

Source0: Rack.tar.gz
Source1: VCV-Recorder.tar.gz
Source2: VCV-Recorder-Makefile
Source3: vcv-recorder-source.sh
Patch0: rack-v2-aarch64.patch

BuildRequires: gcc gcc-c++
BuildRequires: sed
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
BuildRequires: gtk2-devel
BuildRequires: rtaudio-devel
BuildRequires: rtmidi-devel
BuildRequires: speex-devel
BuildRequires: wget
BuildRequires: simde-devel
BuildRequires: speexdsp-devel
BuildRequires: jq
BuildRequires: ffmpeg-devel
BuildRequires: opus-devel
BuildRequires: lame-devel
BuildRequires: Rack-v2

%description
VCV Rack plugin dedicated to recording

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

mkdir vcv_recorder_plugin
tar xvfz %{SOURCE1} --directory=vcv_recorder_plugin --strip-components=1
cp %{SOURCE2} vcv_recorder_plugin/Makefile

%build

%set_build_flags
export CXXFLAGS="-fpermissive -include libavutil/channel_layout.h $CXXFLAGS"

cd vcv_recorder_plugin
%make_build RACK_DIR=.. PREFIX=/usr LIBDIR=%{_lib} dist

%install

mkdir -p %{buildroot}%{_libexecdir}/Rack2/plugins/VCV-Recorder/
cp -r vcv_recorder_plugin/dist/VCV-Recorder/* %{buildroot}%{_libexecdir}/Rack2/plugins/VCV-Recorder/

%files
%{_libexecdir}/*

%changelog
* Tue Sep 05 2023 Yann Collette <ycollette.nospam@free.fr> - 2.0.2-3
- update to 2.0.2-3

* Sun May 15 2022 Yann Collette <ycollette.nospam@free.fr> - 2.0.0-3
- update to last v2 branch

* Fri May 07 2021 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-3
- update to last master + fix link

* Tue Sep 8 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- update to 1.1.0

* Wed Feb 5 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-1
- initial specfile
