# Filtering of private libraries
%global privlibs libOSC
%global privlibs %{privlibs}|libOSC_client
%global privlibs %{privlibs}|libweed
%global privlibs %{privlibs}|libweed-utils
%global privlibs %{privlibs}|libweed-utils_scripting
%global privlibs %{privlibs}|libweed_slice
%global privlibs %{privlibs}|libweed_gslice
%global privlibs %{privlibs}|libweed_slice_scripting
%global privlibs %{privlibs}|libweed_gslice_scripting
%global privlibs %{privlibs}|libav_stream

%global __provides_exclude ^(%{privlibs})\\.so
%global __requires_exclude ^(%{privlibs})\\.so

# Note from upstream:
# the SDL playback plugin is now deprecated in favour of the openGL playback plugin.
# For one thing the program will crash if you use the SDL plugin and projectM plugin at the same time.
# If you have both SDL 1 and SDL 2 installed, LiVES will detect both, since it will use SDL2 for projectM and SDL1 for the SDL playback plugin.
# Use 'SDL2' and 'projectM' together.

Name:    lives-mao
Version: 2022.03.08
Release: 1%{?dist}
Summary: Video editor and VJ tool
License: GPL-3.0-or-later AND LGPL-3.0-or-later
URL:     http://lives-video.com

Vendor:       Audinux
Distribution: Audinux

# Usage: ./lives-sources.sh <TAG>
# ./lives-sources.sh master

Source0: LiVES.tar.gz
Source1: LiVES.appdata.xml
Source2: lives-sources.sh

BuildRequires: gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: make
BuildRequires: doxygen
BuildRequires: chrpath
BuildRequires: bison
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: libunicap-devel
BuildRequires: libdv-devel
BuildRequires: libavc1394-devel
BuildRequires: libraw1394-devel
BuildRequires: libv4l-devel
BuildRequires: libfreenect-devel
BuildRequires: frei0r-devel
BuildRequires: liboil-devel
BuildRequires: libtheora-devel
BuildRequires: libvorbis-devel
BuildRequires: schroedinger-devel
BuildRequires: libpng-devel
BuildRequires: alsa-lib-devel
BuildRequires: opencv-devel
BuildRequires: fftw-devel

# 'tirpc' is required by 'musl-libc'
BuildRequires: libtirpc-devel
BuildRequires: libmatroska-devel
BuildRequires: mjpegtools-devel
BuildRequires: ladspa-devel
BuildRequires: x264-libs
BuildRequires: gettext-devel
BuildRequires: binutils-devel
BuildRequires: gtk3-devel
BuildRequires: compat-ffmpeg4-devel
BuildRequires: bzip2-devel
BuildRequires: libappstream-glib
BuildRequires: perl-generators
BuildRequires: python3-devel
BuildRequires: desktop-file-utils

Requires: mplayer%{?_isa}
Requires: mpv%{?_isa}
Requires: sox%{?_isa}
Requires: ImageMagick%{?_isa}
Requires: ogmtools%{?_isa}
Requires: oggvideotools%{?_isa}
Requires: perl-interpreter%{?_isa}
Requires: theora-tools%{?_isa}
Requires: youtube-dl
Requires: dvgrab%{?_isa}
Requires: icedax%{?_isa}
Requires: frei0r-plugins%{?_isa}
Requires: mkvtoolnix%{?_isa}
Requires: vorbis-tools%{?_isa}
Requires: dvgrab%{?_isa}
Requires: hicolor-icon-theme

%description
LiVES began in 2002 as the Linux Video Editing System.
Since it now runs on more operating systems: LiVES is a Video Editing System.
It's video editor, VJ tool and video programming environment,
designed to be simple to use, yet powerful.
It is small in size, yet it has many advanced features.

%prep
%autosetup -n LiVES

# Remove spurious executable permissions
find . -type f -name "*.h" -exec chmod 0644 '{}' \;
find . -type f -name "*.txt" -exec chmod 0644 '{}' \;
find . -type f -name "*.c" -exec chmod 0644 '{}' \;

# Prepare autotools
#./autogen.sh --verbose

%build

./autogen.sh

%configure --disable-silent-rules \
	   --enable-threads=posix \
	   --disable-rpath \
	   --enable-profiling \
	   --enable-doxygen \
	   --disable-libvisual \
	   --disable-system-weed \
	   --disable-sdl2 \
	   --disable-projectM

%make_build CPPFLAGS="`pkg-config --cflags libtirpc` `pkg-config --cflags opencv4`"

%install
%make_install

# Remove libtools archives and static libraries
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

# Move icon
mkdir -p %{buildroot}%{_datadir}/icons/lives
mv %{buildroot}%{_datadir}/app-install/icons/lives.png %{buildroot}%{_datadir}/icons/lives/
rm -rf %{buildroot}%{_datadir}/app-install

# We want that these libraries are private
mv %{buildroot}%{_libdir}/libOSC* %{buildroot}%{_libdir}/lives/
mv %{buildroot}%{_libdir}/libweed* %{buildroot}%{_libdir}/lives/

# Weed's devel files removed
rm -rf %{buildroot}%{_libdir}/pkgconfig
rm -rf %{buildroot}%{_includedir}/weed

# Remove bad documentation file's location
rm -rf %{buildroot}%{_docdir}

# Remove rpath
chrpath -d %{buildroot}%{_bindir}/lives-exe

# Remove Python2 script
find %{buildroot} -name 'multi_encoder' -exec rm -f {} ';'
find %{buildroot}%{_bindir} -name '*_encoder' -exec rm -f {} ';'

# Fix unversioned Python interpreter
for Files in `find %{buildroot} -name '*_encoder3'`
do
    sed -i -e "s/#!\/usr\/bin\/env python$/#!\/usr\/bin\/env python3/g" $Files
done

rm -f %{buildroot}%{_bindir}/lives
cat > %{buildroot}%{_bindir}/lives <<EOF
#!/bin/sh
echo "Setting private libraries path"
export LD_LIBRARY_PATH=%{_libdir}/lives
echo "Setting frei0r library path"
export FREI0R_PATH=%{_libdir}/frei0r-1
echo "Setting ladspa library path"
export LADSPA_PATH=%{_libdir}/ladspa
echo "Running LiVES"
%{_bindir}/lives-exe "\$@"
EOF
chmod a+x %{buildroot}%{_bindir}/lives

# Set Exec key
desktop-file-edit --set-key=Exec \
 		  --set-value=lives \
 		  %{buildroot}%{_datadir}/applications/LiVES.desktop

# Register as an application to be visible in the software center
install -Dp -m 644 %{SOURCE1} %{buildroot}%{_metainfodir}/LiVES.appdata.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/LiVES.desktop

%files
%doc README AUTHORS ChangeLog FEATURES
%doc GETTING.STARTED NEWS OMC/*.txt RFX/*
%license COPYING
%{_bindir}/*lives*
%{_bindir}/sendOSC
%{_bindir}/smogrify
%{_libdir}/lives/
%{_datadir}/applications/LiVES.desktop
%{_datadir}/lives/
%{_datadir}/icons/lives/
%{_datadir}/pixmaps/lives.png
%{_datadir}/pixmaps/lives.xpm
%{_datadir}/icons/hicolor/*/apps/lives.png
%{_datadir}/locale/*
%{_metainfodir}/LiVES.appdata.xml

%changelog
* Tue Mar 08 2022 Yann Collette <ycollette.nospam@free.fr> - 2022.03.08-23
- create version 2022.03.08-23

* Sat Jan 01 2022 Yann Collette <ycollette.nospam@free.fr> - 2022.01.01-23
- create version 2022.01.01-23

* Mon Nov 01 2021 Yann Collette <ycollette.nospam@free.fr> - 2021.11.01-23
- create version 2021.11.01-23

* Wed Mar 10 2021 Antonio Trande <sagitter@fedoraproject.org> - master-1
- create a master version

* Fri Dec 18 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.2.0-2
- Filter gslice* libraries

* Mon Nov 09 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.2.0-1
- Release 3.2.0

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Leigh Scott <leigh123linux@gmail.com> - 3.0.2-7
- Rebuilt for opencv-4.3

* Fri Jun 05 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0.2-6
- Patch renamed
- Use pathfix.py commands
- Rebuild for Python 3.9
- Set opencv cflags

* Wed Apr 01 2020 Nicolas Chauvet <kwizart@gmail.com> - 3.0.2-5
- Rebuilt for libfreenect

* Tue Mar 10 2020 Nicolas Chauvet <kwizart@gmail.com> - 3.0.2-4
- Fix build for OpenCV

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 3.0.2-3
- Rebuild for ffmpeg-4.3 git

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.0.2-1
- Release 3.0.2

* Tue Aug 13 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.0.1-1
- Release 3.0.1

* Wed Aug 07 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.0.0-1
- Release 3.0.0

* Wed Aug 07 2019 Leigh Scott <leigh123linux@gmail.com> - 2.10.2-3
- Rebuild for new ffmpeg version

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.10.2-1
- Release 2.10.2

* Wed Dec 26 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.10.1-2
- Patch mencoder3 plugins

* Sun Dec 23 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.10.1-1
- Release 2.10.1

* Tue Sep 04 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.10.0-1
- Release 2.10.0
- Drop Python2 scripts

* Tue Aug 28 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.10.0-0.1
- lives 2.10.0 pre-release

* Mon Aug 20 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.8.9-5
- Some minor changes

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.8.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Miro Hrončok <mhroncok@redhat.com> - 2.8.9-3
- Rebuilt for Python 3.7

* Thu Mar 15 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.8.9-2
- Filtering of libav_stream.so

* Thu Mar 15 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.8.9-1
- Update to 2.8.9

* Sun Mar 11 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.8.8-1
- Update to 2.8.8
- Remove obsolete scriptlets
- Remove obsolete ffmpeg patch
- Use metainfo directory for appdata files

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.8.7-11
- Rebuilt for new ffmpeg snapshot

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.8.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.8.7.9
- Rename patch for ffmpeg-3.5 and applied on fedora 28+

* Sat Jan 20 2018 Sérgio Basto <sergio@serjux.com> - 2.8.7-8
- Enable libprojectM

* Fri Jan 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.8.7-7
- Add build fix for ffmpeg-3.5 git

* Thu Jan 18 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.8.7-6
- Add tirpc BR package

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.8.7-5
- Rebuilt for ffmpeg-3.5 git

* Tue Oct 17 2017 Leigh Scott <leigh123linux@googlemail.com> - 2.8.7-4
- Rebuild for ffmpeg update

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Paul Howarth <paul@city-fan.org> - 2.8.7-2
- Perl 5.26 rebuild
- Require perl-interpreter rather than perl
  (https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules)

* Fri Jun 30 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.8.7-1
- Update to 2.8.7

* Wed May 24 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.8.6-1
- Update to 2.8.6

* Wed May 17 2017 Leigh Scott <leigh123linux@googlemail.com> - 2.8.5-3
- Rebuild for ffmpeg update

* Sun Apr 30 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.8.5-2
- Add patch for removing GLee dependency

* Sat Apr 29 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.8.5-1
- Update to the release 2.8.5
- GLee support dropped (retired on Fedora)

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 2.8.5-0.3.svn2608
- Rebuild for ffmpeg update

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.8.5-0.2.svn2608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 28 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.8.5-0.1.svn2608
- Update to svn2608 (rpmfusion bug #4467)

* Mon Feb 27 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.8.4-3
- Set lives shell script (rpmfusion bug #4466)

* Mon Feb 13 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.8.4-2
- Rebuild for GCC 7

* Sat Jan 14 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.8.4-1
- Update to 2.8.4

* Thu Dec 29 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.8.3-1
- Update to 2.8.3

* Mon Nov 28 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.8.2-1
- Update to 2.8.2

* Wed Oct 26 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.8.1-3
- Fix python interpreter of 'lives_*_encoder*' scripts (bz#4304)

* Tue Oct 25 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.8.1-2
- Fix python interpreter of 'multiencoder3' script (bz#4304)

* Mon Oct 24 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.8.1-1
- Update to 2.8.1

* Mon Oct 24 2016 Paul Howarth <paul@city-fan.org> - 2.8.0-2
- BR: perl-generators for proper dependency generation (https://fedoraproject.org/wiki/Changes/Build_Root_Without_Perl)
- BR: python2-devel for %%__python2 macro definition

* Mon Sep 19 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.8.0-2
- Drop mencoder as Requires package

* Sat Sep 03 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.8.0-1
- Update to 2.8.0

* Sat Aug 27 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.6.8-1
- Update to 2.6.8

* Fri Aug 19 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.6.7-1
- Update to 2.6.7

* Thu Aug 18 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.6.6-3
- Fix icon installation

* Thu Aug 18 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.6.6-2
- Add ProjectM support on Fedora >= 24

* Wed Aug 17 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.6.6-1
- Update to 2.6.6

* Sun Aug 14 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.6.5-1
- Update to 2.6.5

* Fri Aug 12 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.6.4-4
- Fix Python interpreter
- Filtering of private libraries

* Thu Aug 11 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.6.4-3
- Update appdata file

* Mon Aug 08 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.6.4-2
- Drop old patch

* Mon Aug 08 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.6.4-1
- Update to 2.6.4

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 2.6.3-5
- Rebuilt for ffmpeg-3.1.1

* Sat Jul 09 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.6.3-4
- Fix again conditional macros

* Sat Jul 09 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.6.3-3
- Patched for ffmpeg-3.0 on f24 too

* Fri Jul 08 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.6.3-2
- Fix compatibility with ffmpeg-3.0

* Mon May 09 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.6.3-1
- Update to 2.6.3

* Mon Mar 28 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.6.2-1
- Update to 2.6.2

* Sun Mar 27 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.6.1-1
- Update to 2.6.1

* Mon Feb 01 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0

* Sun Jan 24 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.4.8-1
- Update to 2.4.8

* Wed Jan 20 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.4.7-2
- Added patch from upstream commit 2363

* Mon Jan 18 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.4.7-1
- Update to 2.4.7

* Wed Jan 13 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.4.6-7
- Included new documentation

* Mon Dec 28 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.4.6-6
- Update from revision 2353
- libvisual support disabled

* Mon Dec 28 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.4.6-5
- Patched to fix Tools->Preference menu crash

* Wed Dec 23 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.4.6-4
- libprojectM-2.0.1 not supported

* Mon Dec 21 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.4.6-3
- List BRequires and Requires packages completed
- Weed's devel files removed

* Mon Dec 21 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.4.6-2
- License fixed
- frei0r support enabled

* Sat Dec 19 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.4.6-1
- First package
