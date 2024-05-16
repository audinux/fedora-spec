# Tag: Video, Tool
# Type: Standalone
# Category: Tool

# Global variables for github repository
%global commit0 8a6e66ed4ac1fce43725e66afc4aaf5b649c73ce
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: veejay-gui
Version: 1.5.57
Release: 4%{?dist}
Summary: A 'visual' instrument and realtime video sampler (for live video improvisation)
URL: https://github.com/c0ntrol/veejay
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/c0ntrol/veejay/archive/%{commit0}.tar.gz#/veejay-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libjpeg-devel
%if 0%{?fedora} >= 37
Buildrequires: compat-ffmpeg4-devel
%else
BuildRequires: ffmpeg-devel
%endif
BuildRequires: libX11-devel
BuildRequires: libxml2-devel
BuildRequires: SDL-devel
BuildRequires: qrencode-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: freetype-devel
BuildRequires: liblo-devel
BuildRequires: libv4l-devel
BuildRequires: libglade2-devel
BuildRequires: gmic-devel
BuildRequires: chrpath
BuildRequires: veejay-server
BuildRequires: gtk3-devel
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
The engine is historically based upon mjpegtools's lavplay and processes all video
in YUV planar It performs at its best, currently with MJPEG AVI (through ffmpeg/libav)
or one of veejay's internal formats. Veejay is built upon a servent architecture.

%prep
%autosetup -n veejay-%{commit0}

find . -name "*.c" ! -name vj-vloopback.c ! -name v4l2utils.c -exec sed -i -e "s/PIX_FMT/AV_PIX_FMT/g" {} \;

sed -i -e "0,/AC_CONFIG_MACRO_DIR/{/AC_CONFIG_MACRO_DIR/d;}" veejay-current/veejay-client/configure.ac
sed -i -e "0,/AC_CONFIG_MACRO_DIR/{/AC_CONFIG_MACRO_DIR/d;}" veejay-current/veejay-utils/configure.ac
sed -i -e "0,/AC_CONFIG_MACRO_DIR/{/AC_CONFIG_MACRO_DIR/d;}" veejay-current/plugin-packs/lvdgmic/configure.ac

%ifarch aarch64
sed -i -e "/Architecture/d" veejay-current/plugin-packs/lvdcrop/configure.ac
sed -i -e "/Architecture/d" veejay-current/plugin-packs/lvdshared/configure.ac
sed -i -e "/Architecture/d" veejay-current/plugin-packs/lvdasciiart/configure.ac
sed -i -e "/Architecture/d" veejay-current/plugin-packs/lvdgmic/configure.ac
sed -i -e "/Architecture/d" veejay-current/veejay-client/configure.ac
sed -i -e "/Architecture/d" veejay-current/veejay-server/configure.ac
sed -i -e "/Architecture/d" veejay-current/veejay-utils/configure.ac
sed -i -e "/Architecture/d" veejay-current/veejay-core/configure.ac
%endif

%build

%set_build_flags

export LIBAVUTIL_CFLAGS=-I/usr/include/compat-ffmpeg4
export LIBAVCODEC_CFLAGS=-I/usr/include/compat-ffmpeg4
export LIBAVFORMAT_CFLAGS=-I/usr/include/compat-ffmpeg4
export LIBSWSCALE_CFLAGS=-I/usr/include/compat-ffmpeg4
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig

export CFLAGS="-fPIC $CFLAGS"
export CFLAGS=`echo $CFLAGS | sed -e "s/-Werror=format-security//g"`
export CXXFLAGS="-fPIC $CXXFLAGS"
export LDFLAGS="-fPIC $LDFLAGS"

cd veejay-current
cd veejay-client
./autogen.sh
%configure --prefix=%{_prefix} --libdir=%{_libdir}

sed -i -e "s/libpng16/freetype/g" config.h

find . -name "Makefile" -exec sed -i -e "s/-march=native//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-O3/-O2/g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-msse2//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-msse//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-mfpmath=sse//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-m64//g" {} \; -print

%make_build CFLAGS="$CFLAGS -I/usr/include/compat-ffmpeg3" LDFLAGS="$LDFLAGS -L/usr/lib64/compat-ffmpeg3"

cd ..

cd veejay-utils
./autogen.sh
%configure --prefix=%{_prefix} --libdir=%{_libdir}

sed -i -e "s/libpng16/freetype/g" config.h

find . -name "Makefile" -exec sed -i -e "s/-march=native//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-O3/-O2/g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-msse2//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-msse//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-mfpmath=sse//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-m64//g" {} \; -print

%make_build CFLAGS="$CFLAGS -I/usr/include/compat-ffmpeg4" LDFLAGS="$LDFLAGS -L/usr/lib64/compat-ffmpeg4"

cd ..

cd plugin-packs/lvdgmic/
./autogen.sh
%configure --prefix=%{_prefix} --libdir=%{_libdir}

sed -i -e "s/libpng16/freetype/g" config.h

find . -name "Makefile" -exec sed -i -e "s/-march=native//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-O3/-O2/g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-msse2//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-msse//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-mfpmath=sse//g" {} \; -print
find . -name "Makefile" -exec sed -i -e "s/-m64//g" {} \; -print

%make_build CFLAGS="$CFLAGS -I/usr/include/compat-ffmpeg4" LDFLAGS="$LDFLAGS -L/usr/lib64/compat-ffmpeg4"

%install

cd veejay-current
cd veejay-client
%make_install CFLAGS="$CFLAGS -I/usr/include/compat-ffmpeg4" LDFLAGS="$LDFLAGS -L/usr/lib64/compat-ffmpeg4"
cd ..

cd veejay-utils
%make_install CFLAGS="$CFLAGS -I/usr/include/compat-ffmpeg4" LDFLAGS="$LDFLAGS -L/usr/lib64/compat-ffmpeg4"
cd ..

cd plugin-packs/lvdgmic/
%make_install CFLAGS="$CFLAGS -I/usr/include/compat-ffmpeg4" LDFLAGS="$LDFLAGS -L/usr/lib64/compat-ffmpeg4"
cd ../..

chrpath --delete $RPM_BUILD_ROOT/usr/bin/reloaded
chrpath --delete $RPM_BUILD_ROOT/usr/bin/sayVIMS

%files
%doc veejay-current/veejay-server/README veejay-current/veejay-server/AUTHORS veejay-current/veejay-server/ChangeLog
%license veejay-current/veejay-server/COPYING
%{_bindir}/*
%{_datadir}/*
%{_libdir}/*

%changelog
* Mon Mar 29 2021 Yann Collette <ycollette.nospam@free.fr> - 1.5.57-4
- update to last master

* Thu Oct 22 2020 Yann Collette <ycollette.nospam@free.fr> - 1.5.57-3
- fix debug build

* Sun Nov 17 2019 Yann Collette <ycollette.nospam@free.fr> - 1.5.57-2
- fix illegal instruction pb and rename to veejay-gui

* Sat Nov 16 2019 Yann Collette <ycollette.nospam@free.fr> - 1.5.57-1
- Initial spec file
