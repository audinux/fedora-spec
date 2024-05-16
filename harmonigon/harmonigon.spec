# Tag: Sequencer, MIDI
# Type: Standalone
# Category: Synthesizer, MIDI

Name: harmonigon
Version: 0.1.2
Release: 1%{?dist}
Summary: A simple harmonic table MIDI sequencer
License: GPL-3.0-only
URL: https://github.com/StrangeLoopsAudio/Harmonigon
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./harmonigon-source.sh <TAG>
#        ./harmonigon-source.sh v0.1.2

Source0: Harmonigon.tar.gz
Source1: harmonigon.png
Source2: harmonigon-source.sh

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: xcb-util-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: alsa-lib-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXrandr-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: JUCE
BuildRequires: desktop-file-utils

%description
A simple harmonic table MIDI sequencer.

Create repeating paths with the notes and intersections (chords)
on the harmonic table!

%prep
%autosetup -n Harmonigon

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/Harmonigon_artefacts/Harmonigon %{buildroot}%{_bindir}/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp %{SOURCE1} %{buildroot}/%{_datadir}/pixmaps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name
Exec=Harmonigon
Icon=Harmonigon
Comment=Harmonigon Sequencer
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*

%changelog
* Wed Dec 27 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.2-1
- update to 0.1.2-1

* Tue Dec 26 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.1-1
- update to 0.1.1-1

* Tue Jul 18 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- Initial spec file
