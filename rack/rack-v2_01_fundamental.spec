# Tag: Modular, Rack
# Type: Rack
# Category: Audio, Synthesizer

%global debug_package %{nil}

# Global variables for github repository
%global commit0 9693f7fc7f404f19b04cd1fa6bfa84375f781045
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    rack-v2-Fundamental
Version: 2.0.0
Release: 1%{?dist}
Summary: A plugin for Rack
License: GPLv2+
URL:     https://github.com/VCVRack/Fundamental

# ./rack-source.sh <tag>
# ./rack-source.sh v2.0.0

Source0: Rack.tar.gz
Source1: https://github.com/VCVRack/Fundamental/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake sed
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
BuildRequires: rtmidi-devel
BuildRequires: speex-devel
BuildRequires: speexdsp-devel
BuildRequires: jq
BuildRequires: Rack-v2

%description
The Fundamental plugin pack gives you a basic foundation to create simple synthesizers,
route and analyze signals, complement other more complicated modules,
and build some not-so-simple patches using brute force (lots of modules).
They are also a great reference for creating your own plugins in C++.

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

# Remove static gcc lib
sed -i -e "s/-static-libstdc++ -static-libgcc//g" Makefile
sed -i -e "s/-static-libstdc++ -static-libgcc//g" plugin.mk

echo "CXXFLAGS += $NEW_FLAGS -I$CURRENT_PATH/include -I$CURRENT_PATH/dep/include -I$CURRENT_PATH/dep/nanovg/src -I$CURRENT_PATH/dep/nanovg/example -I/usr/include/rtmidi -I$CURRENT_PATH/dep/nanosvg/src -I$CURRENT_PATH/dep/oui-blendish -I$CURRENT_PATH/dep/osdialog -I$CURRENT_PATH/dep/pffft -I$CURRENT_PATH/dep/include -I$CURRENT_PATH/dep/fuzzysearchdatabase/src" >> compile.mk

sed -i -e "s/-Wl,-Bstatic//g" Makefile

sed -i -e "s/dep\/lib\/libGLEW.a/-lGLEW/g" Makefile
sed -i -e "s/dep\/lib\/libglfw3.a/-lglfw/g" Makefile
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
sed -i -e "s/dep\/lib\/librtaudio.a/dep\/%{_lib}\/librtaudio.a -lpulse-simple -lpulse/g" Makefile
sed -i -e "s/systemDir = \".\";/systemDir = \"\/usr\/libexec\/Rack2\";/g" src/asset.cpp

# Disable an assert triggered with pipewire
sed -i -e "s/assert(!err);/\/\/assert(!err);/g" src/system.cpp

# Remove rpath
sed -i -e "/-rpath/d" Makefile
sed -i -e "/-rpath/d" plugin.mk

mkdir fundamental_plugin
tar xvfz %{SOURCE1} --directory=fundamental_plugin --strip-components=1 

%build

cd dep
cd rtaudio
cmake -DCMAKE_INSTALL_PREFIX=.. -DBUILD_SHARED_LIBS=FALSE -DCMAKE_BUILD_TYPE=DEBUG .
make
make install
cd ..
cd ..

cd fundamental_plugin

%make_build RACK_DIR=.. PREFIX=/usr LIBDIR=%{_lib} dist

%install 

mkdir -p %{buildroot}%{_libexecdir}/Rack2/plugins/Fundamental/
cp -r fundamental_plugin/dist/Fundamental/* %{buildroot}%{_libexecdir}/Rack2/plugins/Fundamental/

%files
%{_libexecdir}/*

%changelog
* Sun Nov 29 2020 Yann Collette <ycollette.nospam@free.fr> - 1.4.0-6
- fix rtaudio + debug build

* Fri OCt 29 2020 Yann Collette <ycollette.nospam@free.fr> - 1.4.0-5
- update to 1.4.0-5

* Tue Sep 8 2020 Yann Collette <ycollette.nospam@free.fr> - 1.4.0-4
- update to 1.4.0-4.

* Thu Feb 13 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.1-4
- update to 1.3.1-4. Update to last master to add Pulse plugin

* Mon Jan 27 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.1
- update to 1.3.1

* Sun Nov 18 2018 Yann Collette <ycollette.nospam@free.fr> - 0.6.1
- initial specfile
