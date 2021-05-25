
# Tag: MIDI, Sfz, Sf2, Keyboard, Live
# Type: Standalone
# Category: Audio

Name:    konfyt
Version: 1.1.4
Release: 3%{?dist}
Summary: A patch manager
URL:     https://github.com/noedigcode/konfyt
License: GPLv2+

Source0: https://github.com/noedigcode/konfyt/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++ sed
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-gui
BuildRequires: qt5-qtsvg-devel
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: Carla-devel 
BuildRequires: liblscp-devel 
BuildRequires: fluidsynth-devel

%description
Konfyt is a digital keyboard workstation for Linux which allows you to set up
patches, each with multiple layers, and instantly switch between these patches
for live keyboard playing. Patches may consist of multiple layers of soundfonts
(.sf2), SFZs, audio input ports and MIDI output ports. Konfyt features a library
which scans the filesystem for and allows quick access to soundfont programs and
SFZs.

%prep
%autosetup -n %{name}-%{version}

%ifarch x86_64
sed -i -e "s/usr\/lib/usr\/lib64/g" konfyt.pro
%endif

sed -i -e "/AudioVideo/d" desktopentry/konfyt.desktop
sed -i -e "s/\/home\/gideon\/bin\///g" desktopentry/konfyt.desktop

%build

%qmake_qt5 konfyt.pro 
%make_build

%install

%__install -m 755 -d %{buildroot}/%{_datadir}/applications/
%__install -m 644 desktopentry/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 755 %{name} %{buildroot}%{_bindir}/

%__install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps/
%__install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
%__install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/
%__install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/

%__install -m 644 icons/konfyt\ 16.png  %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%__install -m 644 icons/konfyt\ 32.png  %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%__install -m 644 icons/konfyt\ 64.png  %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%__install -m 644 icons/konfyt\ 128.png %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

# install konfyt.desktop properly.
desktop-file-install --vendor '' \
        --add-category=AudioVideo \
        --add-category=X-Midi \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*

%changelog
* Fri Apr 16 2021 Yann Collette <ycollette.nospam@free.fr> - 1.1.4-3
- update to 1.1.4-3 

* Tue Jan 12 2021 Yann Collette <ycollette.nospam@free.fr> - 1.1.3-3
- update to 1.1.3-3 

* Wed Oct 14 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.2-3
- update to 1.1.2-3 

* Sat Oct 10 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.1-3
- update 1.1.1-3  ...

* Tue Oct 6 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-3
- update for Fedora 33 - activate carla  ...

* Tue Oct 6 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-2
- update for Fedora 33 - disable carla for now ...

* Fri Dec 27 2019 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- Initial spec file 1.1.0
