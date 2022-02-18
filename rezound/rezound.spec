# Global variables for github repository
%global commit0 4d2e1d0065b6948462995fe80b952291363097a6
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Tag: Analyzer
# Type: Standalone
# Category: Audio, Tool

Summary: Audio Editing Package
Name: rezound
Version: 0.13.1.%{shortcommit0}
Release: 5%{?dist}
License: GPL
URL: http://rezound.sourceforge.net/

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ddurham2/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: audiofile-devel
BuildRequires: boost-devel
BuildRequires: fftw-devel
BuildRequires: flac-devel
BuildRequires: jack-audio-connection-kit-devel 
BuildRequires: libogg-devel 
BuildRequires: pulseaudio-libs-devel
BuildRequires: libvorbis-devel 
BuildRequires: fox-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: mesa-libGL-devel
BuildRequires: freeglut-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: libXrender-devel
BuildRequires: libXft-devel
BuildRequires: libXi-devel
BuildRequires: libjpeg-devel
BuildRequires: libtiff-devel
BuildRequires: fox-utils
BuildRequires: bison
BuildRequires: flex
BuildRequires: desktop-file-utils

Requires: cdrdao

%description
ReZound aims to be a stable, open source, and graphical audio file editor 
primarily for but not limited to the Linux operating system.

%prep

%autosetup -n %name-%{commit0}

%build

export PATH=/usr/libexec/fox:$PATH

%cmake
%cmake_build

%install
%cmake_install

# Menu
mkdir -p %buildroot%{_datadir}/applications
cat > %buildroot%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Rezound
Comment=Digital audio editor
Exec=%{name}
Icon=sound_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Audio;AudioVideo;
EOF

%find_lang %name

desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %name.lang
%doc docs/AUTHORS
%doc docs/NEWS
%doc docs/README
%doc docs/FrontendFoxFeatures.txt
%doc docs/Features.txt
%license docs/COPYING
%{_bindir}/*
%{_datadir}/%name/* 
%{_datadir}/applications/%name.desktop
%exclude %{_includedir}/*
%exclude %{_libdir}/*
%exclude %{_usr}/doc/%name/*

%changelog
* Fri Feb 18 2022 Yann Collette <ycollette.nospam@free.fr> - 0.13.1.4d2e1d00-1
- initial version of the spec file

