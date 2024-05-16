# Tag: Modular, Rack
# Type: Rack
# Category: Audio, Synthesizer

# Global variables for github repository
%global commit0 dafb8da64e92ae3216627f75865281c9b74ae2d2
%global gittag0 v1.1.0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    rack-v1-Befaco
Version: 1.1.0
Release: 4%{?dist}
Summary: A plugin for Rack
License: GPL-2.0-or-later
URL:     https://github.com/VCVRack/Befaco
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./rack-source.sh <tag>
# ./rack-source.sh v1.1.6

Source0: Rack.tar.gz
Source1: https://github.com/VCVRack/Befaco/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0: rack-v1-aarch64.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake sed
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
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
BuildRequires: simde-devel
BuildRequires: speexdsp-devel
BuildRequires: jq

%description
Based on Befaco - https://www.befaco.org/en/ Eurorack modules.

%prep
%setup -n Rack

%ifarch aarch64
%patch0 -p1
%endif

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

mkdir befaco_plugin
tar xvfz %{SOURCE1} --directory=befaco_plugin --strip-components=1

%build

cd befaco_plugin
%make_build RACK_DIR=.. PREFIX=/usr LIBDIR=%{_lib} dist

%install

mkdir -p %{buildroot}%{_libexecdir}/Rack1/plugins-v1/Befaco/
cp -r befaco_plugin/dist/Befaco/* %{buildroot}%{_libexecdir}/Rack1/plugins-v1/Befaco/

%files
%{_libexecdir}/*

%changelog
* Sat Jul 10 2021 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-4
- update to dafb8da64e92ae3216627f75865281c9b74ae2d2

* Sat Jul 10 2021 Yann Collette <ycollette.nospam@free.fr> - 0.6.0-4
- update to 3b80c5cdd34d98d6448bbed5c5dd441220f28bd5

* Thu Jan 30 2020 Yann Collette <ycollette.nospam@free.fr> - 0.6.0-3
- update to 1467acb4b4ba3257ffc93941b2bae61b42c0c6f5 to get plugin.json

* Sun Nov 18 2018 Yann Collette <ycollette.nospam@free.fr> - 0.6.0-2
- initial specfile
