# Tag: Modular, Rack
# Type: Rack
# Category: Audio, Synthesizer

# Global variables for github repository
%global commit0 58755a32837522a64b6b886b764dbefc9a2b8fd3
%global gittag0 1.1.4
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    rack-v1-DrumKit
Version: 1.1.4
Release: 3%{?dist}
Summary: DrumKit plugin for Rack
License: GPL-2.0-or-later
URL:     https://github.com/SVModular/DrumKit
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./rack-source.sh <tag>
# ./rack-source.sh v1.1.6

# git clone --recursive --branch v1.1.6  https://github.com/SVModular/DrumKit.git
# find DrumKit -name ".git" -exec rm -rf {} \;
# tar cvfz DrumKit.tar.gz DrumKit/*

Source0: Rack.tar.gz
Source1: DrumKit.tar.gz
Source2: DrumKit_plugin.json
Patch0: rack-v1-aarch64.patch

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
BuildRequires: gtk2-devel
BuildRequires: rtmidi-devel
BuildRequires: speex-devel
BuildRequires: simde-devel
BuildRequires: speexdsp-devel
BuildRequires: jq

%description
DrumKit plugin for Rack.
Bass Drum Kit based on 909

%prep
%setup -n Rack

%ifarch aarch64
%patch 0 -p1
%endif

CURRENT_PATH=`pwd`

sed -i -e "s/-march=nocona//g" compile.mk
sed -i -e "s/-O3/-O2/g" compile.mk

# %{build_cxxflags}
echo "CXXFLAGS += -I$CURRENT_PATH/include -I$CURRENT_PATH/dep/include -I$CURRENT_PATH/dep/nanovg/src -I$CURRENT_PATH/dep/nanovg/example -I$CURRENT_PATH/dep/nanosvg/src -I/usr/include/rtmidi -I$CURRENT_PATH/dep/oui-blendish -I$CURRENT_PATH/dep/osdialog -I$CURRENT_PATH/dep/jpommier-pffft-29e4f76ac53b -I$CURRENT_PATH/dep/include  -I$CURRENT_PATH/dep/rtaudio" >> compile.mk

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
# We use provided RtAudio library because Rack hangs when using jack and fedora rtaudio
sed -i -e "s/dep\/lib\/librtaudio.a/dep\/%{_lib}\/librtaudio.a -lpulse-simple -lpulse/g" Makefile

mkdir DrumKit_plugin
tar xvfz %{SOURCE1} --directory=DrumKit_plugin --strip-components=1

cp -n %{SOURCE2} DrumKit_plugin/plugin.json || true

%build

cd DrumKit_plugin
%make_build RACK_DIR=.. PREFIX=/usr STRIP=true LIBDIR=%{_lib} dist

%install

mkdir -p %{buildroot}%{_libexecdir}/Rack1/plugins-v1/DrumKit/
cp -r DrumKit_plugin/dist/DrumKit/* %{buildroot}%{_libexecdir}/Rack1/plugins-v1/DrumKit/

%files
%{_libexecdir}/*

%changelog
* Tue Feb 11 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.4-3
- initial specfile
