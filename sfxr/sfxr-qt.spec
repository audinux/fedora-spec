# Tag: Alsa
# Type: Standalone
# Category: Synthesizer

Name: sfxr-qt
Version: 1.5.0
Release: 1%{?dist}
Summary: Qt port of SFXR, a sound effect generator, to generate retro-gaming like sound effects.
License: MIT
URL: https://github.com/agateau/sfxr-qt
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./sfxr-qt-source.sh <TAG>
#        ./sfxr-qt-source.sh 1.5.0

Source0: sfxr-qt.tar.gz
Source1: sfxr-qt-source.sh

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: SDL-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: extra-cmake-modules
BuildRequires: python3-pyyaml
BuildRequires: python3-jinja2
BuildRequires: desktop-file-utils

%description
This a QtQuick Controls 2 port of SFXR. SFXR is a sound effect generator
created by DrPetter to quickly produce retro-sounding sound effects for games.
This project has the same features as the original SFXR with a more modern user
interface.
This means DrPetter did all the hard work, I just refactored and plugged a new
UI on top of it.

%prep
%autosetup -n %{name}

sed -i -e "1 a #include <QPainterPath>" src/ui/SoundPreview.cpp

%build

%cmake -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

desktop-file-install --vendor '' \
        --add-category=AudioVideo \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/com.agateau.sfxr-qt.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/com.agateau.sfxr-qt.desktop

%files
%doc CHANGELOG.md README.md readme-sfxr-sdl.txt
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/com.agateau.sfxr-qt.desktop
%{_datadir}/icons/hicolor/16x16/apps/sfxr-qt.png
%{_datadir}/icons/hicolor/32x32/apps/sfxr-qt.png
%{_datadir}/icons/hicolor/48x48/apps/sfxr-qt.png

%changelog
* Tue Dec 14 2021 Yann Collette <ycollette.nospam@free.fr> - 1.5.0-1
- initial version of the spec
