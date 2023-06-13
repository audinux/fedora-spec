# Tag: Tracker, Jack, Alsa
# Type: Standalone
# Category: Audio, Sequencer

Name:    famitracker
Version: 1.0.0
Release: 1%{?dist}
Summary: FamiTracker is a tracker for producing music for the NES/Famicom-systems
URL:     https://github.com/Prichman/famitracker-qt
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/Prichman/famitracker-qt/archive/refs/heads/master.zip#/%{name}-%{version}.zip

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: boost-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: desktop-file-utils

%description
FamiTracker is a tracker for producing music for the NES/Famicom-systems

%prep
%autosetup -n %{name}-qt-master

sed -i -e "1i #include <QIcon>" src/qt-gui/AboutDialog.cpp

%build

cd src
%qmake_qt5 CONFIG+=nostrip famitracker-qt.pro
%make_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 src/famitracker %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/
install -m 644 src/qt-gui/res/famitracker.png %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/

install -m 755 -d %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name
Exec=famitracker
Icon=/usr/share/pixmaps/famitracker.png
Comment=FamiTracker tracker
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

# install famitracker.desktop properly.
desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Sequencer \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license GPL.txt
%{_datadir}/applications
%{_bindir}/famitracker
%{_datadir}/icons/hicolor/*

%changelog
* Thu Jan 06 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
