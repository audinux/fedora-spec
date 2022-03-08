Name:    chataigne
Version: 1.9.5b11
Release: 1%{?dist}
Summary: Artist-friendly Modular Machine for Art and Technology
License: GPLv3
URL:     https://benjamin.kuperberg.fr/chataigne/fr

Vendor:       Audinux
Distribution: Audinux

# To get the sources, use:
# $ ./chataigne-source.sh 1.9.5b11

Source0: Chataigne.tar.gz
Source1: chataigne-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: JUCE
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

%description
Artist-friendly Modular Machine for Art and Technology

%prep
%autosetup -n Chataigne

Projucer5 --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE/modules/
Projucer5 --resave Chataigne.jucer

%build

# %set_build_flags
cd Builds/LinuxMakefile
%make_build

%install 

cd Builds/LinuxMakefile
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%changelog
* Tue Mar 08 2022 Yann Collette <ycollette.nospam@free.fr> - 1.9.5b11-1
- Initial spec file
