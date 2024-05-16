# Type: Standalone
# Category: Graphic
# GUIToolkit: Qt5

%global debug_package %{nil}

%define	uname OpenBoard

Name: openboard
Version: 1.7.1
Release: 3%{?dist}
Summary: Interactive whiteboard for schools and universities
License: GPL-3.0-or-later
URL: https://openboard.ch
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/OpenBoard-org/OpenBoard/archive/v%{version}/%{uname}-%{version}.tar.gz
Source1: %{name}.desktop

BuildRequires: gcc gcc-c++
BuildRequires: bison
BuildRequires: flex
%if 0%{?fedora} >= 36
Buildrequires: compat-ffmpeg4-devel
%else
BuildRequires: ffmpeg-devel
%endif
BuildRequires: libpaper-devel
BuildRequires: qtsingleapplication-qt5-devel
BuildRequires: quazip-devel
BuildRequires: t1lib-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5MultimediaWidgets)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5PrintSupport)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5UiTools)
BuildRequires: pkgconfig(Qt5WebKit)
BuildRequires: pkgconfig(Qt5WebKitWidgets)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(Qt5XmlPatterns)
BuildRequires: pkgconfig(Qt5WebEngineWidgets)
BuildRequires: pkgconfig(hunspell)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(openssl)
BuildRequires: poppler-devel
BuildRequires: poppler-cpp-devel
%if 0%{?fedora} >= 36
BuildRequires: sdl12-compat-devel
%else
BuildRequires: SDL-devel
%endif
BuildRequires: libvorbis-devel
BuildRequires: libogg-devel
BuildRequires: libtheora-devel
BuildRequires: opus-devel
BuildRequires: lame-devel
BuildRequires: quazip-devel
BuildRequires: libsndfile-devel

%description
OpenBoard is an open source cross-platform interactive white board
application designed primarily for use in schools. It was originally
forked from Open-Sankor, which was itself based on Uniboard.

%prep
%autosetup -n %{uname}-%{version}

cp -pr %{SOURCE1} .

# remove unwanted and nonfree libraries
sed -i -e 's|-lfdk-aac ||' src/podcast/podcast.pri
sed -i -e 's|-lx264 ||' src/podcast/podcast.pri
sed -i -e 's|-lva-x11 ||' src/podcast/podcast.pri
sed -i -e 's|-lva ||' src/podcast/podcast.pri
sed -i -e 's|-lvpx ||' src/podcast/podcast.pri
sed -i -e 's|-lass ||' src/podcast/podcast.pri

# fix build with poppler 0.83
sed -i -e 's,std=c++11,std=c++14,g' src/podcast/podcast.pri

# fix libraries
sed -i -e 's|-lquazip5|-lquazip|' OpenBoard.pro

# fix run.sh
sed -i -e "s|\$DIR/OpenBoard|/usr/libexec/OpenBoard|g" resources/linux/run.sh

%build
lrelease-qt5 -removeidentical %{uname}.pro

%if 0%{?fedora} >= 36
export LDFLAGS="-L/usr/lib64/compat-ffmpeg4 $LDFLAGS"
export CFLAGS="-I/usr/include/compat-ffmpeg4 $CFLAGS"
export CXXFLAGS="-I/usr/include/compat-ffmpeg4 $CXXFLAGS"
%else
export LDFLAGS="-L/usr/lib64/ffmpeg $LDFLAGS"
export CFLAGS="-I/usr/include/ffmpeg $CFLAGS"
export CXXFLAGS="-I/usr/include/ffmpeg $CXXFLAGS"
%endif

%qmake_qt5 INCLUDEPATH+="/usr/include/quazip"  QMAKE_CXXFLAGS+="-include utility -include optional"
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_libdir}/%{name}/
cp -pr build/linux/release/product/etc %{buildroot}%{_libdir}/%{name}/
cp -pr build/linux/release/product/i18n %{buildroot}%{_libdir}/%{name}/
cp -pr build/linux/release/product/library %{buildroot}%{_libdir}/%{name}/

# icons
install -D -m 0644 resources/images/%{uname}.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

# desktop file
install -D -m 0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

# internalization
mkdir -p %{buildroot}%{_libdir}/%{name}/i18n/
cp -R resources/i18n/%{uname}*.qm %{buildroot}%{_libdir}/%{name}/i18n/

# customizations
cp -R resources/customizations %{buildroot}%{_libdir}/%{name}/

# binary
mkdir -p %{buildroot}%{_bindir}/
install -m 755 resources/linux/run.sh %{buildroot}%{_bindir}/%{name}

# clean some exe bits
find %{buildroot} -executable -type f -name *.js -exec chmod -x '{}' \+
find %{buildroot} -executable -type f -name *.svg -exec chmod -x '{}' \+
find %{buildroot} -executable -type f -name *.css -exec chmod -x '{}' \+
find %{buildroot} -executable -type f -name *.xml -exec chmod -x '{}' \+
find %{buildroot} -executable -type f -name *.html -exec chmod -x '{}' \+

%files
%doc README.md
%license COPYRIGHT LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Wed May 08 2024 Yann Collette <ycollette.nospam@free.fr> - 1.7.1-3
- update to 1.7.1-3

* Fri Dec 08 2023 Yann Collette <ycollette.nospam@free.fr> - 1.7.0-3
- update to 1.7.0-3

* Fri Oct 14 2022 Yann Collette <ycollette.nospam@free.fr> - 1.6.4-3
- update to 1.6.4-3

* Mon Jun 13 2022 Yann Collette <ycollette.nospam@free.fr> - 1.6.3-3
- update to 1.6.3-3

* Fri Oct 01 2021 Yann Collette <ycollette.nospam@free.fr> - 1.6.1-3
- Fix for Fedora 35

* Tue Jun 22 2021 Yann Collette <ycollette.nospam@free.fr> - 1.6.1-2
- Fix binary installation

* Mon Jun 21 2021 Yann Collette <ycollette.nospam@free.fr> - 1.6.1-1
- update for 1.6.1 and Fedora

* Thu Dec 17 2020 umeabot <umeabot> 1.5.4-5.mga8
+ Revision: 1659209
- Rebuild for new Qt5

* Sun Dec 06 2020 wally <wally> 1.5.4-4.mga8
+ Revision: 1653359
- rebuild for poppler 20.12.0

* Thu Aug 06 2020 wally <wally> 1.5.4-3.mga8
+ Revision: 1611570
- rebuild for poppler 20.08.0

* Sat May 02 2020 wally <wally> 1.5.4-2.mga8
+ Revision: 1577942
- rebuild for poppler 0.88.0

* Sat May 02 2020 daviddavid <daviddavid> 1.5.4-1.mga8
+ Revision: 1577727
- new version: 1.5.4

* Sat Apr 04 2020 wally <wally> 1.5.3-5.mga8
+ Revision: 1564378
- rebuild for poppler 0.87.0

* Wed Mar 04 2020 wally <wally> 1.5.3-4.mga8
+ Revision: 1553717
- rebuild for poppler 0.86.1

* Tue Mar 03 2020 wally <wally> 1.5.3-3.mga8
+ Revision: 1553515
- rebuild for poppler 0.86.0

* Wed Feb 19 2020 umeabot <umeabot> 1.5.3-2.mga8
+ Revision: 1544125
- Mageia 8 Mass Rebuild

* Fri Jan 24 2020 daviddavid <daviddavid> 1.5.3-1.mga8
+ Revision: 1482592
- new version: 1.5.3
- remove merged upstream openssl 1.1 patch

* Thu Jan 23 2020 wally <wally> 1.5.2-8.mga8
+ Revision: 1482554
- rebuild for poppler 0.84.0

* Mon Dec 23 2019 wally <wally> 1.5.2-7.mga8
+ Revision: 1469673
- rebuild for poppler 0.83.0

* Thu Oct 31 2019 wally <wally> 1.5.2-6.mga8
+ Revision: 1457170
- rebuild for new poppler 0.82.0

* Thu Oct 10 2019 wally <wally> 1.5.2-5.mga8
+ Revision: 1451110
- rebuild for poppler 0.81.0

* Thu Sep 19 2019 wally <wally> 1.5.2-4.mga8
+ Revision: 1443907
- rebuild for poppler 0.80.0

* Mon Jul 15 2019 wally <wally> 1.5.2-3.mga8
+ Revision: 1421639
- rebuild with poppler 0.78.0

* Sun Mar 31 2019 umeabot <umeabot> 1.5.2-2.mga7
+ Revision: 1383608
- Qt5 Rebuild

* Fri Feb 22 2019 daviddavid <daviddavid> 1.5.2-1.mga7
+ Revision: 1369303
- new version: 1.5.2
- rediff and rename no_Third-Party patch

* Mon Feb 18 2019 wally <wally> 1.4.1-7.mga7
+ Revision: 1368162
- rebuild for new poppler 0.74.0

* Thu Feb 14 2019 alexl <alexl> 1.4.1-6.mga7
+ Revision: 1367096
- update desktop file

* Sat Jan 26 2019 wally <wally> 1.4.1-5.mga7
+ Revision: 1361108
- rebuild for new poppler 0.73.0

* Wed Jan 23 2019 daviddavid <daviddavid> 1.4.1-4.mga7
+ Revision: 1360402
- add patch to fix build with Qt5 >= 5.12

* Sat Dec 08 2018 wally <wally> 1.4.1-3.mga7
+ Revision: 1339038
- add patch to build with poppler 0.72.0

* Sat Nov 17 2018 wally <wally> 1.4.1-2.mga7
+ Revision: 1330540
- add patch and rebuild for new poppler 0.71.0

* Thu Nov 01 2018 daviddavid <daviddavid> 1.4.1-1.mga7
+ Revision: 1327342
- new version: 1.4.1

* Wed Oct 31 2018 wally <wally> 1.4.0-5.mga7
+ Revision: 1327003
- add patch to fix build with gcc 8

* Sun Sep 23 2018 umeabot <umeabot> 1.4.0-4.mga7
+ Revision: 1299978
- Mageia 7 Mass Rebuild

* Sat Apr 28 2018 daviddavid <daviddavid> 1.4.0-3.mga7
+ Revision: 1223011
- rebuild for new ffmpeg 4.0

* Sun Apr 15 2018 kekepower <kekepower> 1.4.0-2.mga7
+ Revision: 1219058
- Rebuild for new Poppler

* Fri Apr 13 2018 daviddavid <daviddavid> 1.4.0-1.mga7
+ Revision: 1218354
- new version: 1.4.0

* Thu Feb 15 2018 daviddavid <daviddavid> 1.3.6-2.mga7
+ Revision: 1201415
- rebuild against OpenSSL 1.1
- add patch to fix build with OpenSSL 1.1
- change XPDFRenderer_with_poppler.patch to make it work with poppler >= 0.55
+ tv <tv>
- rebuild for new openssl
- rebuild for new poppler

* Fri Aug 25 2017 daviddavid <daviddavid> 1.3.6-1.mga7
+ Revision: 1147722
- new version: 1.3.6
- remove merged upstream patch

* Mon Jan 02 2017 luigiwalser <luigiwalser> 1.3.4-3.mga6
+ Revision: 1079509
- rebuild for poppler

* Tue Nov 29 2016 luigiwalser <luigiwalser> 1.3.4-2.mga6
+ Revision: 1070882
- rebuild for poppler

* Wed Sep 28 2016 daviddavid <daviddavid> 1.3.4-1.mga6
+ Revision: 1057248
- initial package openboard
