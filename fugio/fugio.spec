# Tag: MIDI
# Type: Standalone, IDE
# Category: Programming, Audio, Graphic
# GUIToolkit: Qt5
# LastSourceUpdate: 2020

%define _lto_cflags %{nil}

Name:    fugio
Version: 3.1.0
Release: 4%{?dist}
Summary: Fugio is an open visual programming system for building digital art and creative projects quickly, with no programming experience required
URL:     https://www.bigfug.com/software/fugio/
License: LGPL-3.0

Vendor:       Audinux
Distribution: Audinux

# ./fugio-source.sh <tag>
# ./fugio-source.sh v3.1.0

Source0: Fugio.tar.gz
Source1: fugio-source.sh
Patch0:  fugio-0002-fix-for-lua-5.4.patch

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: cmake
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-gui
BuildRequires: qt5-qttools
BuildRequires: qt5-qtserialport-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-qtwebsockets-devel
BuildRequires: qt5-qtquickcontrols2-devel
Buildrequires: compat-ffmpeg4-devel
BuildRequires: portmidi-devel
BuildRequires: portaudio-devel
BuildRequires: opencv-devel
BuildRequires: fftw-devel
BuildRequires: lua-devel
BuildRequires: eigen3-devel
BuildRequires: desktop-file-utils

%description
Fugio is an open visual programming system for building digital art and creative projects quickly, with no programming experience required

%prep
%autosetup -p1 -n Fugio

%ifarch x86_64 amd64
sed -i -e "s/lib\/fugio/lib64\/fugio/g" CMakeLists.txt
%endif

sed -i -e "s/Fugio;//g" FugioApp/fugio.desktop

%build

%set_build_flags
export CXXFLAGS="$CXXFLAGS -std=c++17 -I/usr/include/compat-ffmpeg4"
export CFLAGS="$CFLAGS -I/usr/include/compat-ffmpeg4"
export LDFLAGS="$LDFLAGS -L/usr/lib64/compat-ffmpeg4"

%cmake

%cmake_build

%install

%cmake_install

# Warning: to be fixed
# value item "Audio" in key "Categories" in group "Desktop Entry"
# requires another category to be present among the following categories:
# AudioVideo

desktop-file-install --vendor '' \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/fugio.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/fugio.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_includedir}/*
%{_libdir}/fugio/*
%{_datadir}/*

%changelog
* Fri Dec 01 2023 Yann Collette <ycollette.nospam@free.fr> - 3.1.0-4
- update to 3.1.0-4

* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 3.1.0-3
- fix for Fedora 33

* Tue Jan 21 2020 Yann Collette <ycollette.nospam@free.fr> - 3.1.0-1
- initial version of the spec file
