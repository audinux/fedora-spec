# Tag: Tracker, Jack, Alsa
# Type: Standalone
# Category: Audio, Sequencer

Name:    prototracker-modular
Version: 0.0.8
Release: 1%{?dist}
Summary: A modular synth tracker
License: MIT
URL:     https://github.com/kometbomb/prototracker-modular

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/kometbomb/prototracker-modular/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: prototracker.png

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: SDL2-devel
BuildRequires: SDL2_image-devel
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils

%description
Prototracker-modular is a modular synthesizer fork of Prototracker.
The idea is that the user can define his/her "sound chip" using
basic modules. Each channel has its own "sound chip".
Otherwise, the tracker is exactly like any Prototracker fork.

Double click on synth area to add a new module. Left click to connect
inputs/outputs (right click cancels). Drag to move modules.
See MODULES.md for basic info about modules.

%prep
%autosetup -n %{name}-%{version}

sed -i -e "s|-static-libstdc++ -static-libgcc||g" Makefile.linux
# Add Fedora flags
sed -i -e "s|-O3|\$(CXXFLAGS)|g" Makefile.linux
# Remove stripping
sed -i -e "s|-s | |g" Makefile.linux

%build

%set_build_flags

%make_build -f Makefile.linux

%install

install -m 755 -d %{buildroot}/%{_bindir}
install -m 755 prototracker %{buildroot}/%{_bindir}/

# install assets
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/
cp -ra assets doc templates %{buildroot}/%{_datadir}/%{name}/

# Write bash script to select audio driver

cat > %{buildroot}/%{_bindir}/%{name}-jack <<EOF
#!/bin/bash

SDL_AUDIODRIVER=jack prototracker
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-jack

cat > %{buildroot}/%{_bindir}/%{name}-pulse <<EOF
#!/bin/bash

SDL_AUDIODRIVER=pulse prototracker
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-pulse

cat > %{buildroot}/%{_bindir}/%{name}-alsa <<EOF
#!/bin/bash

SDL_AUDIODRIVER=alsa prototracker
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-alsa

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp %{SOURCE1} %{buildroot}/%{_datadir}/pixmaps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}-jack.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name-jack
Exec=%{name}-jack
Icon=%{name}
Comment=Prototracker modular tracker
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
Comment=Prototracker modular tracker
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
Comment=Prototracker modular tracker
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
%doc README.md MODULES.md module-ids.md
%license LICENSE 
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*

%changelog
* Thu Jul 13 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.8-1
- initial spec file
