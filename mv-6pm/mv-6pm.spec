# Tag: Jack, PM
# Type: Standalone
# Category: Audio, Synthetizer
# GUIToolkit: Qt5

Name:    6PM
Version: 0.9
Release: 2%{?dist}
Summary: Phase Modulation synthetizer made of 6 oscillators
URL:     https://sourceforge.net/projects/mv-6pm/
License: GPLv2+

Source0: https://sourceforge.net/projects/mv-6pm/files/6PM_v0.9.tgz
Source1: mv-6pm.desktop
Patch0:  mv-6pm-use-global-presets.patch

BuildRequires: gcc gcc-c++
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5Location)
BuildRequires: pkgconfig(Qt5OpenGL)

BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel

%description
6PM is a phase modulation (PM) synthesizer made of six oscillators.
It works with Jack sound server and Qt5 GUI.
Phase Modulation is a kind of Frequency modulation (FM) synthesis 

%prep
%autosetup -p1 -n %{name}_v%{version}

%build

cd src
%qmake_qt5 "CONFIG+=nostrip" 6PM.pro
%make_build

%install

install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

install -m 755 -d %{buildroot}/%{_datadir}/mv-6pm/
install -m 755 -d %{buildroot}/%{_datadir}/mv-6pm/MidiMaps
install -m 755 -d %{buildroot}/%{_datadir}/mv-6pm/Presets
cp -r MidiMaps/* %{buildroot}%{_datadir}/mv-6pm/MidiMaps/
cp -r Presets/* %{buildroot}%{_datadir}/mv-6pm/Presets/

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 src/6pm %{buildroot}%{_bindir}/%{name}

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
install -m 644 src/images/icon.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

# install mv-6pm.desktop properly.
desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README Changelog
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mv-6pm/*
%{_datadir}/icons/hicolor/*

%changelog
* Wed Oct 21 2020 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-2
- fix debug build

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-1
- update for Fedora 29

* Mon Jun 01 2015 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-1
- Initial spec file 0.5.0
