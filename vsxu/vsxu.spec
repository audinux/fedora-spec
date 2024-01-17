#
# spec file for package vsxu
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name: vsxu
Version: 0.6.3
Release: 2%{?dist}
Summary: Visual programming language animation tool
License: GPL-3.0 and LGPL-3.0
Url: http://www.vsxu.com/

Vendor:       Audinux
Distribution: Audinux

# git clone https://github.com/vovoid/vsxu
# cd vsxu
# git checkout v0.6.3
# git submodule init
# git submodule update
# find . -name ".git" -exec rm -rf {} \;
# cd ..
# mv vsxu vsxu-0.6.3
# tar cvfj vsxu-0.6.3.tar.gz vsxu-0.6.3/*
Source0:  %{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: fdupes
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: mesa-libEGL-devel
BuildRequires: freetype-devel
BuildRequires: libjpeg-devel
BuildRequires: desktop-file-utils
BuildRequires: alsa-lib-devel
BuildRequires: lzma-sdk-devel
BuildRequires: ftgl-devel
BuildRequires: glew-devel
BuildRequires: pkgconfig(jack)
BuildRequires: glfw-devel
BuildRequires: libpng-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: SDL2-devel
BuildRequires: zlib-devel
BuildRequires: bitstream-vera-sans-fonts
ExclusiveArch: %ix86 x86_64

%description
VSXu (VSX Ultra) is an OpenGL-based (hardware-accelerated), modular programming
environment with its main purpose to visualize music and create graphic effects
in real-time.

%package	devel
Summary:        Development files for vsxu
Requires:       %{name}-libs = %{version}

%description	devel
Those development headers are required if you plan on coding against VSXu.

%package	libs
Summary:        Visual programming language animation library

%description	libs
Shared VSXu libraries. To be installed by system dependencies.

%package	data
Summary:        VSXu artwork and other data
BuildArch:      noarch

%description	data
This package contains the core artwork and other shared data that is used by various
VSXu components.

%package	artiste
Summary:        VSXu graphic effects creator
Requires:       %{name}-data = %{version}
Requires:       %{name}-libs = %{version}

%description	artiste
VSXu VPL environment used to create visuals.

%package	player
Summary:        VSXu graphic effects player
Requires:       %{name}-data = %{version}
Requires:       %{name}-libs = %{version}

%description	player
VSXu player used to load and run the visuals created in VSXu artiste.

%package	server
Summary:        VSXu remote viewer
Requires:       %{name}-data = %{version}
Requires:       %{name}-libs = %{version}

%description	server
The server is used as a remote screen to VSXu artiste. Mainly intended for live performances.

%package	tools
Summary:        VSXu support tools
Requires:       %{name}-libs = %{version}

%description	tools
This package contains a few support tools for VSXu.

%prep
%autosetup

mkdir build
sed -e 's/\${CMAKE_INSTALL_PREFIX}\/share\/pixmaps/\${CMAKE_INSTALL_PREFIX}\/share\/icons/' \
  -i lib/engine_graphics/CMakeLists.txt
sed -e 's/lib/%{_lib}/' -i programs/artiste/vsxu-artiste-fullscreen.desktop.in \
    -i programs/artiste/vsxu-artiste.desktop.in \
    -i programs/player/vsxu-player-fullscreen.desktop.in \
    -i programs/player/vsxu-player.desktop.in \
    -i programs/server/vsxu-server-fullscreen.desktop.in \
    -i programs/server/vsxu-server.desktop.in
# for GLFW2
sed -e 's/usr\/lib/usr\/%{_lib}\/glfw2/' -i cmake/modules/FindGLFW.cmake

sed -i -e "s/lib\/vsxu\/plugins/%{_lib}\/vsxu\/plugins/g" vsx_platform.h

#   define DEFAULT_FONT "/usr/X11R6/lib/X11/fonts/TTF/Vera.ttf"
sed -i -e "s/\/usr\/X11R6\/lib\/X11\/fonts\/TTF\/Vera.ttf/\/usr\/share\/fonts\/bitstream-vera\/Vera.ttf/g" engine_graphics/thirdparty/ftgl/test/demo.cpp

%build
if [ %{_lib} = lib64 ]; then
  EXTRA_FLAGS="$EXTRA_FLAGS -DLIB_SUFFIX=64"
fi
pushd build
%cmake $EXTRA_FLAGS ..
%make_build

%install
pushd build
%make_install

desktop-file-install --vendor '' \
        --add-category=Video \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/vsxu-server-fullscreen.desktop

desktop-file-install --vendor '' \
        --add-category=Video \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/vsxu-server.desktop

desktop-file-install --vendor '' \
        --add-category=Video \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/vsxu-artiste-fullscreen.desktop

desktop-file-install --vendor '' \
        --add-category=Video \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/vsxu-artiste.desktop

desktop-file-install --vendor '' \
        --add-category=Video \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/vsxu-player-fullscreen.desktop

desktop-file-install --vendor '' \
        --add-category=Video \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/vsxu-player.desktop

# this is apparently superfluous
rm %{buildroot}/%{_bindir}/vsxu_launcher
%fdupes %{buildroot}%{_datadir}/%{name}

%files devel
%defattr(-,root,root)
%doc AUTHORS CHANGELOG COPYING COPYING.LESSER
%{_includedir}/%{name}
%{_libdir}/pkgconfig/libvsx.pc

%files libs
%defattr(-,root,root)
%doc AUTHORS CHANGELOG COPYING COPYING.LESSER
%dir %{_libdir}/vsxu
%dir %{_libdir}/vsxu/plugins
%{_libdir}/libvsx_application.so
%{_libdir}/libvsx_common.so
%{_libdir}/libvsx_compression.so
%{_libdir}/libvsx_engine.so
%{_libdir}/libvsx_engine_graphics.so
%{_libdir}/libvsx_widget.so
%{_libdir}/%{name}/plugins/_deprecated.so
%{_libdir}/%{name}/plugins/bitmap.generators.so
%{_libdir}/%{name}/plugins/bitmap.loaders.so
%{_libdir}/%{name}/plugins/bitmap.modifiers.so
%{_libdir}/%{name}/plugins/math.oscillators.so
%{_libdir}/%{name}/plugins/math.so
%{_libdir}/%{name}/plugins/mesh.generators.so
%{_libdir}/%{name}/plugins/mesh.importers.so
%{_libdir}/%{name}/plugins/mesh.modifiers.so
%{_libdir}/%{name}/plugins/mesh.render.so
%{_libdir}/%{name}/plugins/outputs.screen_opengl.so
%{_libdir}/%{name}/plugins/particlesystem.generators.so
%{_libdir}/%{name}/plugins/particlesystem.modifiers.so
%{_libdir}/%{name}/plugins/particlesystem.render.so
%{_libdir}/%{name}/plugins/render.basic.so
%{_libdir}/%{name}/plugins/render.glsl.so
%{_libdir}/%{name}/plugins/render.gravity_lines.so
%{_libdir}/%{name}/plugins/render.opengl.so
%{_libdir}/%{name}/plugins/render.text.so
%{_libdir}/%{name}/plugins/selectors.so
%{_libdir}/%{name}/plugins/sound.rtaudio.so
%{_libdir}/%{name}/plugins/string.so
%{_libdir}/%{name}/plugins/system.so
%{_libdir}/%{name}/plugins/texture.so

%files data
%defattr(-,root,root)
%doc AUTHORS CHANGELOG COPYING COPYING.LESSER
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/apps
%dir %{_datadir}/icons/hicolor/apps/16x16
%dir %{_datadir}/icons/hicolor/apps/22x22
%dir %{_datadir}/icons/hicolor/apps/24x24
%dir %{_datadir}/icons/hicolor/apps/32x32
%dir %{_datadir}/icons/hicolor/apps/36x36
%dir %{_datadir}/icons/hicolor/apps/48x48
%dir %{_datadir}/icons/hicolor/apps/64x64
%dir %{_datadir}/icons/hicolor/apps/72x72
%dir %{_datadir}/icons/hicolor/apps/96x96
%dir %{_datadir}/icons/hicolor/apps/128x128
%dir %{_datadir}/icons/hicolor/apps/192x192
%dir %{_datadir}/icons/hicolor/apps/256x256
%dir %{_datadir}/icons/hicolor/apps/512x512
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/apps/16x16/vsxu.png
%{_datadir}/icons/hicolor/apps/22x22/vsxu.png
%{_datadir}/icons/hicolor/apps/24x24/vsxu.png
%{_datadir}/icons/hicolor/apps/32x32/vsxu.png
%{_datadir}/icons/hicolor/apps/36x36/vsxu.png
%{_datadir}/icons/hicolor/apps/48x48/vsxu.png
%{_datadir}/icons/hicolor/apps/64x64/vsxu.png
%{_datadir}/icons/hicolor/apps/72x72/vsxu.png
%{_datadir}/icons/hicolor/apps/96x96/vsxu.png
%{_datadir}/icons/hicolor/apps/128x128/vsxu.png
%{_datadir}/icons/hicolor/apps/192x192/vsxu.png
%{_datadir}/icons/hicolor/apps/256x256/vsxu.png
%{_datadir}/icons/hicolor/apps/512x512/vsxu.png
%{_datadir}/icons/vsxu.xpm

%files artiste
%defattr(-,root,root)
%doc AUTHORS CHANGELOG COPYING COPYING.LESSER
%{_bindir}/vsxu_artiste
%{_datadir}/applications/vsxu-artiste-fullscreen.desktop
%{_datadir}/applications/vsxu-artiste.desktop

%files player
%defattr(-,root,root)
%doc AUTHORS CHANGELOG COPYING COPYING.LESSER
%{_bindir}/vsxu_player
%{_datadir}/applications/vsxu-player-fullscreen.desktop
%{_datadir}/applications/vsxu-player.desktop

%files server
%defattr(-,root,root)
%doc AUTHORS CHANGELOG COPYING COPYING.LESSER
%{_bindir}/vsxu_server
%{_datadir}/applications/vsxu-server-fullscreen.desktop
%{_datadir}/applications/vsxu-server.desktop

%files tools
%defattr(-,root,root)
%doc AUTHORS CHANGELOG COPYING COPYING.LESSER
%{_bindir}/obj2vxm
%{_bindir}/vsxbt
%{_bindir}/vsxl
%{_bindir}/vsxu_profiler
%{_bindir}/vsxz
%{_bindir}/raw2wav

%changelog
* Sat Nov 16 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.3-2
- fix plugin path

* Sat Nov 16 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.3-1
- first spec file for vsxu for Fedora 31

* Tue Jan  9 2018 jengelh@inai.de
- Rework vsxu-use-system-libs.patch to use lzma-sdk's C library.
- Reduce size of vsxu-use-system-libs.patch by 7K by using
  pkgconfig instead of manual searches.

* Sun Aug 27 2017 jengelh@inai.de
- Rectify RPM groups.

* Fri Aug 25 2017 aloisio@gmx.com
- Update to version 0.6.2
  * following new Luna design, Luna graphics updated
  * vsx export from artiste broken
  * when only loading one .vsx visual in player, it would hang in
    an endless loop
  * mesh particle system module ceased to work when lowering the
    number of particles in artiste
  * bitmap loading from engine when archive loaded caused crash
    because the archive was closed too early.
    Now the archive is open during the whole run of the engine,
    using more memory, but at the same time allowing for
    asynchronous load times and loading of data later.

* Thu Aug 24 2017 aloisio@gmx.com
- Added vsxu-noglew.sh to produce a tarball without unwanted
  files

* Thu Jun 29 2017 aloisio@gmx.com
- Build vsxu-data as noarch

* Fri May 19 2017 aloisio@gmx.com
- Update to version 0.6.1
  * menu text too small in sequencer
  * not possible to close master channel item / segfault
- Dropped vsxu-cal3d.patch (merged upstream)
- Refreshed vsxu-use-system-libs.patch

* Thu May 11 2017 aloisio@gmx.com
- Update to version 0.6.0 (major changes, see included CHANGELOG)
- Added vsxu-use-system-libs.patch and vsxu-cal3d.patch

* Sat Sep 26 2015 aloisio@gmx.com
- Initial version 0.5.1
