# Status: active
# Tag: Jack, Alsa, Modular
# Type: Standalone
# Category: Audio, DAW, Sequencer

Name: chataigne
Version: 1.10.1
Release: 1%{?dist}
Summary: Artist-friendly Modular Machine for Art and Technology
License: GPL-3.0-only
URL: https://benjamin.kuperberg.fr/chataigne/fr
ExclusiveArch: x86_64 

Vendor:       Audinux
Distribution: Audinux

# To get the sources, use:
# $ ./source-chataigne.sh 1.10.1

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
BuildRequires: openssl-devel-engine
BuildRequires: openssl-devel
BuildRequires: hidapi-devel
BuildRequires: gtk3-devel
BuildRequires: libglvnd-devel
BuildRequires: bluez-libs-devel
BuildRequires: SDL2-devel
BuildRequires: libusb1-devel
BuildRequires: webkit2gtk4.1-devel
BuildRequires: chrpath
BuildRequires: JUCE7
BuildRequires: desktop-file-utils

%description
Artist-friendly Modular Machine for Art and Technology

%prep
%autosetup -n Chataigne

tar xvfz %{SOURCE1}

rm -rf Modules/juce_simpleweb/libs/
rm -rf Modules/juce_simpleweb/openssl/
# ln -s /usr/include/openssl Modules/juce_simpleweb/openssl

%build

%set_build_flags

CURRENT_DIR=`pwd`

cd JUCE/extras/Projucer/Builds/LinuxMakefile
%make_build

cd ../../../../..

JUCE/extras/Projucer/Builds/LinuxMakefile/build/Projucer --resave Chataigne.jucer

cd Builds/LinuxMakefile
%ifarch aarch64
sed -i -e "s/-m64//g" Makefile
%endif
sed -i -e "s/webkit2gtk-4.0/webkit2gtk-4.1/g" Makefile

%make_build CPPFLAGS="-I$CURRENT_DIR/JUCE/modules/ -I$CURRENT_DIR/modules/ -I$CURRENT_DIR/External/asio/asio/"

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
cp -rav External/servus/lib/linux/libServus.so.6 %{buildroot}%{_libdir}/
cp -rav External/mosquitto/lib/linux/libmosquittopp.so %{buildroot}%{_libdir}/libmosquittopp.so.1

chrpath --delete %{buildroot}%{_bindir}/Chataigne

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_libdir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
* Tue Feb 24 2026 Yann Collette <ycollette.nospam@free.fr> - 1.10.1-1
- Update to 1.10.1-1

* Tue Oct 08 2024 Yann Collette <ycollette.nospam@free.fr> - 1.9.24-1
- Update to 1.9.24-1

* Mon Oct 07 2024 Yann Collette <ycollette.nospam@free.fr> - 1.9.23-1
- Update to 1.9.23-1

* Sat Oct 05 2024 Yann Collette <ycollette.nospam@free.fr> - 1.9.22-1
- Update to 1.9.22-1

* Sat Oct 05 2024 Yann Collette <ycollette.nospam@free.fr> - 1.9.21-1
- Update to 1.9.21-1

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
