# Global variables for github repository
%global commit0 330a3e25b1134b6ab1d92ccdf34f3ede659f17e6
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    veejay-server
Version: 1.5.57
Release: 5%{?dist}
Summary: A 'visual' instrument and realtime video sampler (for live video improvisation) - server part
URL:     https://github.com/c0ntrol/veejay
License: GPLv2+

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/c0ntrol/veejay/archive/%{commit0}.tar.gz#/veejay-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++ sed make
BuildRequires: libgomp
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: gtk2-devel
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: ffmpeg-devel
BuildRequires: libX11-devel
BuildRequires: libxml2-devel
BuildRequires: SDL2-devel
BuildRequires: qrencode-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: freetype-devel
BuildRequires: liblo-devel
BuildRequires: libv4l-devel
BuildRequires: libglade2-devel
BuildRequires: compat-ffmpeg28-devel
BuildRequires: gmic-devel
BuildRequires: chrpath
BuildRequires: veejay-core
BuildRequires: aalib-devel

%description
Veejay is a Visual Instrument

A 'visual' instrument and realtime video sampler (for live video improvisation)
It allows you to "play" the video like you would play a piano.
While playing, you can record the resulting video directly to disk (video sampling), all effects are realtime and optimized for use on modern processors.
Veejay likes the sound of your video's as much as their images: sound is kept in sync ( pitched when needed - trickplay) and delivered to [JACK](http://www.jackaudio.org/) for possible further processing.
You can cluster to allow a number of machines to work together over the network (uncompressed streaming, veejay chaining) And much more...
The engine is historically based upon mjpegtools's lavplay and processes all video in YUV planar It performs at its best, currently with MJPEG AVI (through ffmpeg/libav) or one of veejay's internal formats. Veejay is built upon a servent architecture.

%prep
%autosetup -n veejay-%{commit0}

%build

%set_build_flags

export LIBAVUTIL_CFLAGS=-I/usr/include/compat-ffmpeg28
export LIBAVCODEC_CFLAGS=-I/usr/include/compat-ffmpeg28
export LIBAVFORMAT_CFLAGS=-I/usr/include/compat-ffmpeg28
export LIBSWSCALE_CFLAGS=-I/usr/include/compat-ffmpeg28
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig

cd veejay-current
cd veejay-server

export CFLAGS="-fPIC $CFLAGS"
export CXXFLAGS="-fPIC $CXXFLAGS"
export LDFLAGS="-fPIC $LDFLAGS"

./autogen.sh
%configure --prefix=%{_prefix} --libdir=%{_libdir} 

find . -name "Makefile" -exec sed -i -e "s/-march=native//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-O3/-O2/g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-msse2//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-msse//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-mfpmath=sse//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-m64//g" {} \; -print

%make_build CFLAGS="$CFLAGS -I/usr/include/compat-ffmpeg28" LDFLAGS="$LDFLAGS -L/usr/lib64/compat-ffmpeg28 -lpng -lgomp"

# Build plugins

cd ..
cd plugin-packs
cd lvdasciiart

./autogen.sh
%configure --prefix=%{_prefix} --libdir=%{_libdir} 
find . -name "Makefile" -exec sed -i -e "s/-march=native//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-O3/-O2/g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-msse2//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-msse//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-mfpmath=sse//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-m64//g" {} \; -print

%make_build CFLAGS="$CFLAGS -I/usr/include/compat-ffmpeg28" LDFLAGS="$LDFLAGS -L/usr/lib64/compat-ffmpeg28 -lpng -lgomp"

cd ..
cd lvdcrop

./autogen.sh
%configure --prefix=%{_prefix} --libdir=%{_libdir} 
find . -name "Makefile" -exec sed -i -e "s/-march=native//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-O3/-O2/g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-msse2//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-msse//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-mfpmath=sse//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-m64//g" {} \; -print

%make_build CFLAGS="$CFLAGS -I/usr/include/compat-ffmpeg28" LDFLAGS="$LDFLAGS -L/usr/lib64/compat-ffmpeg28 -lpng -lgomp"

cd ..
cd lvdgmic

./autogen.sh
%configure --prefix=%{_prefix} --libdir=%{_libdir} 
find . -name "Makefile" -exec sed -i -e "s/-march=native//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-O3/-O2/g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-msse2//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-msse//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-mfpmath=sse//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-m64//g" {} \; -print

%make_build CFLAGS="$CFLAGS -I/usr/include/compat-ffmpeg28" LDFLAGS="$LDFLAGS -L/usr/lib64/compat-ffmpeg28 -lpng -lgomp"

cd ..
cd lvdshared

./autogen.sh
%configure --prefix=%{_prefix} --libdir=%{_libdir} 
find . -name "Makefile" -exec sed -i -e "s/-march=native//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-O3/-O2/g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-msse2//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-msse//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-mfpmath=sse//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-m64//g" {} \; -print

%make_build CFLAGS="$CFLAGS -I/usr/include/compat-ffmpeg28" LDFLAGS="$LDFLAGS -L/usr/lib64/compat-ffmpeg28 -lpng -lgomp"

%install

cd veejay-current
cd veejay-server
%make_install CFLAGS="$CFLAGS -I/usr/include/compat-ffmpeg28 -I%{buildroot}%{_includedir}" LDFLAGS="$LDFLAGS -L/usr/lib64/compat-ffmpeg28/ -L%{buildroot}%{_libdir} -lpng -lgomp"

# Install plugins

cd ..
cd plugin-packs
cd lvdasciiart
%make_install CFLAGS="$CFLAGS -I/usr/include/compat-ffmpeg28 -I%{buildroot}%{_includedir}" LDFLAGS="$LDFLAGS -L/usr/lib64/compat-ffmpeg28/ -L%{buildroot}%{_libdir} -lpng -lgomp"

cd ..
cd lvdcrop
%make_install CFLAGS="$CFLAGS -I/usr/include/compat-ffmpeg28 -I%{buildroot}%{_includedir}" LDFLAGS="$LDFLAGS -L/usr/lib64/compat-ffmpeg28/ -L%{buildroot}%{_libdir} -lpng -lgomp"

cd ..
cd lvdgmic
%make_install CFLAGS="$CFLAGS -I/usr/include/compat-ffmpeg28 -I%{buildroot}%{_includedir}" LDFLAGS="$LDFLAGS -L/usr/lib64/compat-ffmpeg28/ -L%{buildroot}%{_libdir} -lpng -lgomp"

cd ..
cd lvdshared
%make_install CFLAGS="$CFLAGS -I/usr/include/compat-ffmpeg28 -I%{buildroot}%{_includedir}" LDFLAGS="$LDFLAGS -L/usr/lib64/compat-ffmpeg28/ -L%{buildroot}%{_libdir} -lpng -lgomp"

%files
%doc veejay-current/veejay-server/README veejay-current/veejay-server/AUTHORS veejay-current/veejay-server/ChangeLog
%license veejay-current/veejay-server/COPYING
%{_bindir}/*
%{_datadir}/*
%{_libdir}/*

%changelog
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
