# Tag: Modular, Rack
# Type: Rack
# Category: Audio, Synthetizer

# Global variables for github repository
%global commit0 6a5651c2538d8eb358ac7bf84ba3b0b3df88dfd7
%global gittag0 v1.1.0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    rack-v1-VCV-Recorder
Version: 1.1.0
Release: 3%{?dist}
Summary: A plugin for Rack
License: GPLv2+
URL:     https://github.com/VCVRack/VCV-Recorder.git

# ./rack-source.sh <tag>
# ./rack-source.sh v1.1.6

Source0: Rack.tar.gz
Source1: https://github.com/VCVRack/VCV-Recorder/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source2: VCVRecorder-Makefile

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

%description
VCV Rack plugin dedicated to recording

%prep
%autosetup -n Rack

CURRENT_PATH=`pwd`

sed -i -e "s/-march=core2//g" compile.mk
sed -i -e "s/-march=nocona//g" compile.mk
sed -i -e "s/-ffast-math//g" compile.mk
sed -i -e "s/-fno-finite-math-only//g" compile.mk
sed -i -e "s/-O3/-O2/g" compile.mk

# %{build_cxxflags} 
echo "CXXFLAGS += -I$CURRENT_PATH/include -I$CURRENT_PATH/dep/nanovg/src -I$CURRENT_PATH/dep/nanovg/example -I$CURRENT_PATH/dep/nanosvg/src -I/usr/include/rtaudio -I/usr/include/rtmidi -I$CURRENT_PATH/dep/oui-blendish -I$CURRENT_PATH/dep/osdialog -I$CURRENT_PATH/dep/jpommier-pffft-29e4f76ac53b -I$CURRENT_PATH/dep/include" >> compile.mk

sed -i -e "s/-Wl,-Bstatic//g" Makefile
sed -i -e "s/-lglfw3/dep\/lib\/libglfw3.a/g" Makefile

sed -i -e "s/dep\/lib\/libGLEW.a/-lGLEW/g" Makefile
sed -i -e "s/dep\/lib\/libglfw3.a/dep\/%{_lib}\/libglfw3.a/g" Makefile
sed -i -e "s/dep\/lib\/libjansson.a/-ljansson/g" Makefile
sed -i -e "s/dep\/lib\/libcurl.a/-lcurl/g" Makefile
sed -i -e "s/dep\/lib\/libssl.a/-lssl/g" Makefile
sed -i -e "s/dep\/lib\/libcrypto.a/-lcrypto/g" Makefile
sed -i -e "s/dep\/lib\/libzip.a/-lzip/g" Makefile
sed -i -e "s/dep\/lib\/libz.a/-lz/g" Makefile
sed -i -e "s/dep\/lib\/libspeexdsp.a/-lspeexdsp/g" Makefile
sed -i -e "s/dep\/lib\/libsamplerate.a/-lsamplerate/g" Makefile
sed -i -e "s/dep\/lib\/librtmidi.a/-lrtmidi/g" Makefile
sed -i -e "s/dep\/lib\/librtaudio.a/-lrtaudio/g" Makefile

mkdir vcv_recorder_plugin
tar xvfz %{SOURCE1} --directory=vcv_recorder_plugin --strip-components=1 

cp %{SOURCE2} vcv_recorder_plugin/Makefile

%build

cd vcv_recorder_plugin
%make_build RACK_DIR=.. PREFIX=/usr LIBDIR=%{_lib} dist

%install 

mkdir -p %{buildroot}%{_libexecdir}/Rack1/plugins-v1/VCV-Recorder/
cp -r vcv_recorder_plugin/dist/VCV-Recorder/* %{buildroot}%{_libexecdir}/Rack1/plugins-v1/VCV-Recorder/

%files
%{_libexecdir}/*

%changelog
* Fri May 07 2021 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-3
- update to last master + fix link

* Tue Sep 8 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- update to 1.1.0

* Wed Feb 5 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-1
- initial specfile
