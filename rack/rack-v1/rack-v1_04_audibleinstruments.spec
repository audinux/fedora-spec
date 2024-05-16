# Tag: Modular, Rack
# Type: Rack
# Category: Audio, Synthesizer

# Global variables for github repository
%global commit0 d14a3e3833e0c7c4330b24eef3958c090d8815f9
%global gittag0 v1.4.0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    rack-v1-AudibleInstruments
Version: 1.4.0
Release: 4%{?dist}
Summary: A plugin for Rack
License: GPL-2.0-or-later
URL:     https://github.com/VCVRack/AudibleInstruments
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./rack-source.sh <tag>
# ./rack-source.sh v1.1.6

# ./audible-instruments-source.sh <tag>
# ./audible-instruments-source.sh v1.4.0

Source0: Rack.tar.gz
Source1: AudibleInstruments.tar.gz
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
Based on Mutable Instruments - https://mutable-instruments.net/ Eurorack modules.

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

mkdir audibleinstruments_plugin
tar xvfz %{SOURCE1} --directory=audibleinstruments_plugin --strip-components=1

%build

cd audibleinstruments_plugin
%make_build RACK_DIR=.. PREFIX=/usr LIBDIR=%{_lib} dist

%install

mkdir -p %{buildroot}%{_libexecdir}/Rack1/plugins-v1/AudibleInstruments/
cp -r audibleinstruments_plugin/dist/AudibleInstruments/* %{buildroot}%{_libexecdir}/Rack1/plugins-v1/AudibleInstruments/

%files
%{_libexecdir}/*

%changelog
* Thu Nov 03 2020 Yann Collette <ycollette.nospam@free.fr> - 1.4.0-3
- update to 1.4.0-3

* Thu Jan 30 2020 Yann Collette <ycollette.nospam@free.fr> - 0.6.0-3
- update to 0.6.0-3

* Thu Jan 30 2020 Yann Collette <ycollette.nospam@free.fr> - 0.6.0-3
- update to a9f8dfbb3a6c0d4123a987bfab431c045594b2a9 to get plugin.json

* Sun Nov 18 2018 Yann Collette <ycollette.nospam@free.fr> - 0.6.0-2
- initial specfile
