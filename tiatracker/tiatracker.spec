# Tag: Tracker, MIDI, Alsa
# Type: Standalone
# Category: Audio, Sequencer

Name:    tiatracker
Version: 0.1
Release: 1%{?dist}
Summary: A music tracker for making Atari VCS 2600 music on the PC
URL:     https://bitbucket.org/kylearan/tiatracker/src/master/
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://bitbucket.org/kylearan/tiatracker/get/master.zip#/%{name}-master.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-gui
BuildRequires: alsa-lib-devel
BuildRequires: SDL2-devel
BuildRequires: desktop-file-utils

%description
A music tracker for making Atari VCS 2600 music on the PC

%prep
%autosetup -n kylearan-tiatracker-ca0bb54ef67d

%build

%qmake_qt5 TIATracker.pro
%make_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 TIATracker %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/
cp data/keymap.cfg %{buildroot}/%{_datadir}/%{name}/
cp data/TIATracker_manual.pdf %{buildroot}/%{_datadir}/%{name}/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/guides/
cp -r guides/* %{buildroot}/%{_datadir}/%{name}/guides/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/instruments/
cp -r instruments/* %{buildroot}/%{_datadir}/%{name}/instruments/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/songs/
cp -r songs/* %{buildroot}/%{_datadir}/%{name}/songs/

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
cp -r graphics/tt_icon.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/

install -m 755 -d %{buildroot}/%{_datadir}/applications/
cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Name=tiatracker
Comment=Mod tracker
Exec=TIATracker
Icon=tt_icon
Terminal=false
Type=Application
Categories=AudioVideo;Audio;
EOF

# install polyphon.desktop properly.
desktop-file-install --vendor '' \
        --add-category=Midi \
        --add-category=Sequencer \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license license.txt data/license.txt
%{_bindir}/*
%{_datadir}/*

%changelog
* Sun Feb 13 2022 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- initial version of the spec file (git commit ca0bb54ef67d)
