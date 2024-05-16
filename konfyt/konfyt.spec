# Tag: MIDI, Sfz, Sf2, Keyboard, Live
# Type: Standalone
# Category: Audio

Name: konfyt
Version: 1.6.1
Release: 3%{?dist}
Summary: A patch manager
URL: https://github.com/noedigcode/konfyt
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/noedigcode/konfyt/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-gui
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
%ifarch aarch64
BuildRequires: Carla-devel
%else
BuildRequires: Carla-mao-devel
%endif
BuildRequires: liblscp-devel
BuildRequires: fluidsynth-devel
BuildRequires: desktop-file-utils

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

install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 desktopentry/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 %{name} %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps/
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/

install -m 644 icons/konfyt\ 16.png  %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -m 644 icons/konfyt\ 32.png  %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -m 644 icons/konfyt\ 64.png  %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -m 644 icons/konfyt\ 128.png %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

# install konfyt.desktop properly.
desktop-file-install --vendor '' \
        --add-category=AudioVideo \
        --add-category=X-Midi \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*

%changelog
* Tue Apr 16 2024 Yann Collette <ycollette.nospam@free.fr> - 1.6.1-3
- update to 1.6.1-3

* Sun Jan 14 2024 Yann Collette <ycollette.nospam@free.fr> - 1.6.0-3
- update to 1.6.0-3

* Sat Dec 16 2023 Yann Collette <ycollette.nospam@free.fr> - 1.5.0-3
- update to 1.5.0-3

* Sun Aug 06 2023 Yann Collette <ycollette.nospam@free.fr> - 1.4.0-3
- update to 1.4.0-3

* Mon May 15 2023 Yann Collette <ycollette.nospam@free.fr> - 1.3.1-3
- update to 1.3.1-3

* Mon Apr 17 2023 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-3
- update to 1.3.0-3

* Sun Jan 22 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.3-3
- update to 1.2.3-3

* Tue Oct 11 2022 Yann Collette <ycollette.nospam@free.fr> - 1.2.1-3
- update to 1.2.1-3

* Sun Jul 17 2022 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-3
- update to 1.2.0-3

* Tue Jan 18 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1.7-3
- update to 1.1.7-3

* Wed Oct 13 2021 Yann Collette <ycollette.nospam@free.fr> - 1.1.6-3
- update to 1.1.6-3

* Thu Jul 15 2021 Yann Collette <ycollette.nospam@free.fr> - 1.1.5-3
- update to 1.1.5-3

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
