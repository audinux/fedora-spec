# Tag: Jack, Alsa, Modular
# Type: Standalone
# Category: Audio, DAW, Sequencer

Name:    chataigne
Version: 1.9.14b12
Release: 1%{?dist}
Summary: Artist-friendly Modular Machine for Art and Technology
License: GPLv3
URL:     https://benjamin.kuperberg.fr/chataigne/fr

Vendor:       Audinux
Distribution: Audinux

# To get the sources, use:
# $ ./source-chataigne.sh 1.9.14b12

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
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: lv2-devel
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

CURRENT_DIR=`pwd`

cd JUCE/extras/Projucer/Builds/LinuxMakefile
%make_build

cd ../../../../..

JUCE/extras/Projucer/Builds/LinuxMakefile/build/Projucer --resave Chataigne.jucer

cd Builds/LinuxMakefile
%ifarch aarch64
sed -i -e "s/-m64//g" Makefile
%endif

%make_build CPPFLAGS="-I$CURRENT_DIR/JUCE/modules -I$CURRENT_DIR/External/asio/asio/"

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
* Wed Apr 05 2023 Yann Collette <ycollette.nospam@free.fr> - 1.9.14b12-1
- Update to 1.9.14b12-1

* Sun Mar 19 2023 Yann Collette <ycollette.nospam@free.fr> - 1.9.14b11-1
- Update to 1.9.14b11-1

* Tue Mar 07 2023 Yann Collette <ycollette.nospam@free.fr> - 1.9.14b9-1
- Update to 1.9.14b9-1

* Tue Mar 08 2022 Yann Collette <ycollette.nospam@free.fr> - 1.9.14b8-1
- Initial spec file
