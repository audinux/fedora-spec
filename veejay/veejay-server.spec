# Status: active
# Tag: Video, Tool
# Type: Standalone
# Category: Tool

# Disable production of debug package.
%global debug_package %{nil}

Name: veejay-server
Version: 1.6.0
Release: 5%{?dist}
Summary: A 'visual' instrument and realtime video sampler (for live video improvisation) - server part
URL: https://github.com/c0ntrol/veejay
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/game-stop/veejay/archive/refs/tags/%{version}.tar.gz#/veejay-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: libgomp
BuildRequires: (ffmpeg or ffmpeg-free)
BuildRequires: SDL2-devel
BuildRequires: aalib-devel
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: gmic-devel
BuildRequires: gtk2-devel
BuildRequires: libX11-devel
BuildRequires: libglade2-devel
BuildRequires: libjpeg-devel
BuildRequires: liblo-devel
BuildRequires: libpng-devel
BuildRequires: libv4l-devel
BuildRequires: libxml2-devel
BuildRequires: pkgconfig(jack)
BuildRequires: qrencode-devel
BuildRequires: chrpath
BuildRequires: veejay-core
BuildRequires: desktop-file-utils

%description
Veejay is a Visual Instrument

A 'visual' instrument and realtime video sampler (for live video improvisation)
It allows you to "play" the video like you would play a piano.
While playing, you can record the resulting video directly to disk (video sampling),
all effects are realtime and optimized for use on modern processors.
Veejay likes the sound of your video's as much as their images: sound is kept in sync
(pitched when needed - trickplay) and delivered to [JACK](http://www.jackaudio.org/)
for possible further processing.
You can cluster to allow a number of machines to work together over the network
(uncompressed streaming, veejay chaining) And much more...
The engine is historically based upon mjpegtools's lavplay and processes all video in
YUV planar It performs at its best, currently with MJPEG AVI (through ffmpeg/libav) or
one of veejay's internal formats. Veejay is built upon a servent architecture.

%prep
%autosetup -n veejay-%{version}

%build

%set_build_flags

cd veejay-current
cd veejay-server

./autogen.sh
%configure --prefix=%{_prefix} --libdir=%{_libdir}
%make_build

# Build plugins

cd ..
cd plugin-packs
cd lvdasciiart

./autogen.sh
%configure --prefix=%{_prefix} --libdir=%{_libdir}
%make_build

cd ..
cd lvdcrop

./autogen.sh
%configure --prefix=%{_prefix} --libdir=%{_libdir}
%make_build

cd ..
cd lvdgmic

./autogen.sh
%configure --prefix=%{_prefix} --libdir=%{_libdir}
%make_build

cd ..
cd lvdshared

./autogen.sh
%configure --prefix=%{_prefix} --libdir=%{_libdir}
%make_build

%install

cd veejay-current
cd veejay-server
%make_install

# Install plugins

cd ..
cd plugin-packs
cd lvdasciiart
%make_install

cd ..
cd lvdcrop
%make_install

cd ..
cd lvdgmic
%make_install

cd ..
cd lvdshared
%make_install

%files
%doc veejay-current/veejay-server/README.md veejay-current/veejay-server/AUTHORS veejay-current/veejay-server/ChangeLog
%license veejay-current/veejay-server/COPYING
%{_bindir}/*
%{_datadir}/*
%{_libdir}/*

%changelog
* Fri Sep 04 2026 Yann Collette <ycollette.nospam@free.fr> - 1.6.0-1
- update to 1.6.0-1

* Fri Apr 02 2021 Yann Collette <ycollette.nospam@free.fr> - 1.5.57-5
- fixes for fedora 34

* Mon Mar 29 2021 Yann Collette <ycollette.nospam@free.fr> - 1.5.57-4
- update to last master

* Thu Oct 22 2020 Yann Collette <ycollette.nospam@free.fr> - 1.5.57-3
- fix debug build

* Sun Nov 17 2019 Yann Collette <ycollette.nospam@free.fr> - 1.5.57-2
- fix illegal instruction pb

* Sat Nov 16 2019 Yann Collette <ycollette.nospam@free.fr> - 1.5.57-1
- Initial spec file
