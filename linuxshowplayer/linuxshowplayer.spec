Name:    linux-show-player
Version: 0.5.3
Release: 1%{?dist}
Summary: A Cue player designed for stage productions
License: GPL-2.0-or-later
URL:     https://github.com/FrancescoCeruti/linux-show-player

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/FrancescoCeruti/linux-show-player/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools

BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils

Requires(pre): python3-gobject
Requires(pre): python3-qt5-base-gui
Requires(pre): python3-mido
Requires(pre): portmidi
Requires(pre): python-jack-client
Requires(pre): gstreamer1-plugins-good
Requires(pre): gstreamer1-libav
Requires(pre): python3-sortedcontainers

%description
Linux Show Player (LiSP) - Sound player designed for stage productions.

%prep
%autosetup -n %{name}-%{version}

%build

%py3_build

%install

%py3_install

install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 755 -d %{buildroot}%{_datadir}/pixmaps
install -m 755 -d %{buildroot}%{_datadir}/mime/packages

install -m 644 dist/linuxshowplayer.desktop %{buildroot}%{_datadir}/applications
install -m 644 dist/linuxshowplayer.png %{buildroot}%{_datadir}/pixmaps
install -m 644 dist/linuxshowplayer.xml %{buildroot}%{_datadir}/mime/packages
  
desktop-file-install                         \
  --add-category="Audio"                     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/linuxshowplayer.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/linuxshowplayer.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/*
%{python3_sitelib}/*

%changelog
* Sat Dec 25 2021 Yann Collette <ycollette.nospam@free.fr> - 0.5.3-1
- update to version 0.5.3-1

* Fri Mar 12 2021 Yann Collette <ycollette.nospam@free.fr> - 0.5.2-1
- Initial spec file
