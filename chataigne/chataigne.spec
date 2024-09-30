# Status: active
# Tag: Jack, Alsa, Modular
# Type: Standalone
# Category: Audio, DAW, Sequencer

Name: chataigne
Version: 1.9.20
Release: 1%{?dist}
Summary: Artist-friendly Modular Machine for Art and Technology
License: GPL-3.0-only
URL: https://benjamin.kuperberg.fr/chataigne/fr
ExclusiveArch: x86_64 

Vendor:       Audinux
Distribution: Audinux

# To get the sources, use:
# $ ./source-chataigne.sh 1.9.20

Source0: Chataigne.tar.gz
Source1: JUCE.tar.gz
Source2: source-chataigne.sh

BuildRequires: gcc gcc-c++
BuildRequires: boost-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: lv2-devel
%if 0%{?fedora} > 40
BuildRequires: openssl-devel-engine
%endif
BuildRequires: openssl-devel
BuildRequires: hidapi-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel
BuildRequires: libglvnd-devel
BuildRequires: bluez-libs-devel
BuildRequires: SDL2-devel
BuildRequires: libusb1-devel
BuildRequires: chrpath
BuildRequires: desktop-file-utils

%description
Artist-friendly Modular Machine for Art and Technology

%prep
%autosetup -n Chataigne

tar xvfz %{SOURCE1}

rm -rf Modules/juce_simpleweb/openssl/
ln -s /usr/include/openssl Modules/juce_simpleweb/openssl

%build

%set_build_flags
export CXXFLAGS="-Wno-implicit-function-declaration $CXXFLAGS"

CURRENT_DIR=`pwd`

cd JUCE/extras/Projucer/Builds/LinuxMakefile
%make_build

cd ../../../../..

JUCE/extras/Projucer/Builds/LinuxMakefile/build/Projucer --resave Chataigne.jucer

cd Builds/LinuxMakefile
%ifarch aarch64
sed -i -e "s/-m64//g" Makefile
%endif

%make_build CPPFLAGS="-I$CURRENT_DIR/JUCE/modules -I$CURRENT_DIR/External/asio/asio/ -Wno-implicit-function-declaration"

%install

install -m 755 -d %{buildroot}%{_bindir}/
cp -a Builds/LinuxMakefile/build/Chataigne %{buildroot}%{_bindir}/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/
cp Builds/LinuxMakefile/Chataigne.AppDir/chataigne.desktop %{buildroot}/%{_datadir}/applications/

install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp Builds/LinuxMakefile/Chataigne.AppDir/chataigne.png %{buildroot}/%{_datadir}/pixmaps/

# Install some libs
install -m 755 -d %{buildroot}%{_libdir}/
cp -rav Builds/LinuxMakefile/Chataigne.AppDir/usr/lib/libartnet.so* %{buildroot}%{_libdir}/
cp -rac Builds/LinuxMakefile/Chataigne.AppDir/usr/lib/libServus.so* %{buildroot}%{_libdir}/

chrpath --delete %{buildroot}%{_bindir}/Chataigne

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_libdir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
* Sun Sep 29 2024 Yann Collette <ycollette.nospam@free.fr> - 1.9.20-1
- Update to 1.9.20-1

* Tue Jun 25 2024 Yann Collette <ycollette.nospam@free.fr> - 1.9.19-1
- Update to 1.9.19-1

* Sat Jun 22 2024 Yann Collette <ycollette.nospam@free.fr> - 1.9.18-1
- Update to 1.9.18-1

* Mon Nov 27 2023 Yann Collette <ycollette.nospam@free.fr> - 1.9.17-1
- Update to 1.9.17-1

* Mon Jul 31 2023 Yann Collette <ycollette.nospam@free.fr> - 1.9.16-1
- Update to 1.9.16-1

* Mon May 15 2023 Yann Collette <ycollette.nospam@free.fr> - 1.9.15-1
- Update to 1.9.15-1

* Mon Apr 10 2023 Yann Collette <ycollette.nospam@free.fr> - 1.9.14-1
- Update to 1.9.14-1

* Wed Apr 05 2023 Yann Collette <ycollette.nospam@free.fr> - 1.9.14b12-1
- Update to 1.9.14b12-1

* Sun Mar 19 2023 Yann Collette <ycollette.nospam@free.fr> - 1.9.14b11-1
- Update to 1.9.14b11-1

* Tue Mar 07 2023 Yann Collette <ycollette.nospam@free.fr> - 1.9.14b9-1
- Update to 1.9.14b9-1

* Tue Mar 08 2022 Yann Collette <ycollette.nospam@free.fr> - 1.9.14b8-1
- Initial spec file
