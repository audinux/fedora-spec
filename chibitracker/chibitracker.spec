# Status: active
# Tag: Tracker, Jack, Alsa
# Type: Standalone
# Category: Audio, Sequencer

Name: chibitracker
Version: 0.0.1
Release: 1%{?dist}
Summary: Fast music tracker
License: GPLv2+
URL: https://github.com/reduz/chibitracker
ExclusiveArch: x86_64

Vendor:       Audinux
Distribution: Audinux

Source0: %{url}/archive/refs/heads/master/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: scons
BuildRequires: SDL2-devel
BuildRequires: SDL2_gfx-devel
BuildRequires: sdl12-compat-devel
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils

Requires: SDL2
Requires: alsa-lib

%description
ChibiTracker is a fast and lightweight music tracker inspired by Impulse Tracker.

%prep
%autosetup -n %{name}-master

%build

scons %{?_smp_mflags}

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 program/chibitracker %{buildroot}%{_bindir}/
install -m 755 program/chibiconvert %{buildroot}%{_bindir}/

# Write bash script to select audio driver

cat > %{buildroot}/%{_bindir}/%{name}-jack <<EOF
#!/bin/bash

SDL_AUDIODRIVER=jack chibitracker
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-jack

cat > %{buildroot}/%{_bindir}/%{name}-pulse <<EOF
#!/bin/bash

SDL_AUDIODRIVER=pulse chibitracker
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-pulse

# Skins (data)
install -m 755 -d %{buildroot}%{_datadir}/%{name}/skins/
cp -a skins/* %{buildroot}%{_datadir}/%{name}/skins/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%name
Exec=%{name}
Icon=cticon
Comment=Chibi tracker for ALSA
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/%{name}-jack.desktop <<EOF
[Desktop Entry]
Name=%name-jack
Exec=%{name}-jack
Icon=cticon
Comment=Chibi tracker for Jack Audio
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/%{name}-pulse.desktop <<EOF
[Desktop Entry]
Name=%name-pulse
Exec=%{name}-pulse
Icon=cticon
Comment=Chibi tracker for PulseAudio
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}-jack.desktop

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}-pulse.desktop

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp program/cticon.ico %{buildroot}/%{_datadir}/pixmaps/
cp program/cticon.png %{buildroot}/%{_datadir}/pixmaps/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-jack.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-pulse.desktop

%files
%license COPYING
%doc NEWS ChangeLog AUTHORS
%{_bindir}/chibitracker
%{_bindir}/chibitracker-pulse
%{_bindir}/chibitracker-jack
%{_bindir}/chibiconvert
%{_datadir}/%{name}/skins/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-jack.desktop
%{_datadir}/applications/%{name}-pulse.desktop

%changelog
* Sun Apr 26 2026 Yann Collette Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial package
