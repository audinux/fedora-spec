# Tag: MIDI
# Type: Standalone, IDE
# Category: Programming, Audio, Graphic
# GUIToolkit: Qt5
# LastSourceUpdate: 2020

Name:    fugio
Version: 3.1.0
Release: 3%{?dist}
Summary: Fugio is an open visual programming system for building digital art and creative projects quickly, with no programming experience required
URL:     https://www.bigfug.com/software/fugio/
License: LGPL-3.0

Vendor:       Audinux
Distribution: Audinux

# git clone https://github.com/bigfug/Fugio
# cd Fugio
# git checkout v3.0.0
# git submodule init
# git submodule update
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz Fugio.tar.gz Fugio/*

Source0: Fugio.tar.gz
Patch0:  fugio-0001-fix-opencv.patch
Patch1:  fugio-0002-fix-for-lua-5.4.patch

BuildRequires: gcc gcc-c++ sed
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-gui
BuildRequires: qt5-qttools
BuildRequires: qt5-qtserialport-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-qtwebsockets-devel
BuildRequires: qt5-qtquickcontrols2-devel
BuildRequires: ffmpeg-devel
BuildRequires: portmidi-devel
BuildRequires: portaudio-devel
BuildRequires: opencv-devel
BuildRequires: fftw-devel
BuildRequires: lua-devel
BuildRequires: ffmpeg-devel
BuildRequires: eigen3-devel

%description
Fugio is an open visual programming system for building digital art and creative projects quickly, with no programming experience required

%prep
%autosetup -p1 -n Fugio

%ifarch x86_64 amd64
sed -i -e "s/lib\/fugio/lib64\/fugio/g" CMakeLists.txt
%endif

sed -i -e "s/Fugio;//g" FugioApp/fugio.desktop

%build

%define _lto_cflags %{nil}

%cmake -DCMAKE_BUILD_TYPE=RELEASE

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
* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 3.1.0-3
- fix for Fedora 33

* Tue Jan 21 2020 Yann Collette <ycollette.nospam@free.fr> - 3.1.0-1
- initial version of the spec file
