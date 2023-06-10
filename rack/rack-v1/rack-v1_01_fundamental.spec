# Tag: Modular, Rack
# Type: Rack
# Category: Audio, Synthesizer

%global debug_package %{nil}

# Global variables for github repository
%global commit0 5799ee2a9b21492b42ebcb9b65d5395ef5c1cbe2
%global gittag0 v1.4.0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    rack-v1-Fundamental
Version: 1.4.0
Release: 6%{?dist}
Summary: A plugin for Rack
License: GPL-2.0-or-later
URL:     https://github.com/VCVRack/Fundamental

Vendor:       Audinux
Distribution: Audinux

# ./rack-source.sh <tag>
# ./rack-source.sh v1.1.6

Source0: Rack.tar.gz
Source1: https://github.com/VCVRack/Fundamental/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0: rack-v1-aarch64.patch

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
BuildRequires: simde-devel
BuildRequires: speexdsp-devel
BuildRequires: libsndfile-devel
BuildRequires: jq

%description
The Fundamental plugin pack gives you a basic foundation to create simple synthesizers, route and analyze signals, complement other more complicated modules, and build some not-so-simple patches using brute force (lots of modules).
They are also a great reference for creating your own plugins in C++.

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

echo "CXXFLAGS += %{build_cxxflags} -I$CURRENT_PATH/include -I$CURRENT_PATH/dep/include -I$CURRENT_PATH/dep/nanovg/src -I$CURRENT_PATH/dep/nanovg/example -I$CURRENT_PATH/dep/nanosvg/src -I/usr/include/rtmidi -I$CURRENT_PATH/dep/oui-blendish -I$CURRENT_PATH/dep/osdialog -I$CURRENT_PATH/dep/jpommier-pffft-29e4f76ac53b -I$CURRENT_PATH/dep/include" >> compile.mk

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

mkdir fundamental_plugin
tar xvfz %{SOURCE1} --directory=fundamental_plugin --strip-components=1 

# Remove libsamplerate download and install
sed -i -e "7,20d" fundamental_plugin/Makefile

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

mkdir -p %{buildroot}%{_libexecdir}/Rack1/plugins-v1/Fundamental/
cp -r fundamental_plugin/dist/Fundamental/* %{buildroot}%{_libexecdir}/Rack1/plugins-v1/Fundamental/

%files
%{_libexecdir}/*

%changelog
* Sun Nov 29 2020 Yann Collette <ycollette.nospam@free.fr> - 1.4.0-6
- fix rtaudio + debug build

* Thu Oct 29 2020 Yann Collette <ycollette.nospam@free.fr> - 1.4.0-5
- update to 1.4.0-5

* Tue Sep 8 2020 Yann Collette <ycollette.nospam@free.fr> - 1.4.0-4
- update to 1.4.0-4.

* Thu Feb 13 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.1-4
- update to 1.3.1-4. Update to last master to add Pulse plugin

* Mon Jan 27 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.1
- update to 1.3.1

* Sun Nov 18 2018 Yann Collette <ycollette.nospam@free.fr> - 0.6.1
- initial specfile
