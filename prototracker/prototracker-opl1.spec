# Status: active
# Tag: Tracker, Jack, Alsa
# Type: Standalone
# Category: Audio, Sequencer

Name: prototracker-opll
Version: 0.0.8
Release: 1%{?dist}
Summary: A synth tracker using YM2413 chip
License: MIT
URL: https://github.com/kometbomb/prototracker-opll
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/kometbomb/prototracker-opll/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: prototracker.png
Patch0: prototracker-modular-0001-move-assets-to-system-dir.patch

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: SDL2-devel
BuildRequires: SDL2_image-devel
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils

%description
Prototracker is a multiplatform fakebit chiptune tracker. Try the online version.
The editor is a fairly normal tracker. The synth is an absolutely minimal
single-oscillator synth (with 256 preset waveforms).
Macros are used to create "instruments" and also some normal channel effects.
Most keyboard shortcuts are the same as in Protracker.
See the docs/ directory for help.

%prep
%autosetup -p1 -n %{name}-%{version}

sed -i -e "s|-static-libstdc++ -static-libgcc||g" Makefile.linux
# Add Fedora flags
sed -i -e "s|-O3|\$(CXXFLAGS)|g" Makefile.linux
# Remove stripping
sed -i -e "s|-s | |g" Makefile.linux

%build

%set_build_flags

%make_build PLAT=linux

%install

install -m 755 -d %{buildroot}/%{_bindir}
install -m 755 prototracker-opll %{buildroot}/%{_bindir}/prototracker-opll

# install assets
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/
cp -ra assets doc templates %{buildroot}/%{_datadir}/%{name}/

# Write bash script to select audio driver

cat > %{buildroot}/%{_bindir}/%{name}-jack <<EOF
#!/bin/bash

SDL_AUDIODRIVER=jack prototracker-opll
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-jack

cat > %{buildroot}/%{_bindir}/%{name}-pulse <<EOF
#!/bin/bash

SDL_AUDIODRIVER=pulse prototracker-opll
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-pulse

cat > %{buildroot}/%{_bindir}/%{name}-alsa <<EOF
#!/bin/bash

SDL_AUDIODRIVER=alsa prototracker-opll
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-alsa

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp %{SOURCE1} %{buildroot}/%{_datadir}/pixmaps/%{name}.png

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}-jack.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name-jack
Exec=%{name}-jack
Icon=%{name}
Comment=Prototracker tracker
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/%{name}-alsa.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name-alsa
Exec=%{name}-alsa
Icon=%{name}
Comment=Prototracker tracker
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/%{name}-pulse.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name-pulse
Exec=%{name}-pulse
Icon=%{name}
Comment=Prototracker tracker
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}-jack.desktop

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}-pulse.desktop

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}-alsa.desktop

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-jack.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-pulse.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-alsa.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*

%changelog
* Wed Feb 05 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.8-1
- initial spec file
