# Tag: OSC
# Type: Standalone
# Category: Sequencer

# Global variables for github repository
%global commit0 1294f84ba809ebf5262a1c7071a18ac5ff4109b0
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    IanniX
Version: 0.9.20.%{shortcommit0}
Release: 4%{?dist}
Summary: A graphic / MIDI / OSC player
URL:     https://github.com/iannix/Iannix
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/iannix/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1: iannix.xml
Patch0:  iannix-0001-fix-missing-glew.patch
Patch1:  iannix-0002-add-missing-header.patch

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtscript-devel
BuildRequires: glew-devel
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils

%description
IanniX is a graphical open source sequencer, based on Iannis Xenakis works,
for digital art. IanniX syncs via Open Sound Control (OSC) events and curves
to your real-time environment.

%prep
%autosetup -p1 -n %{name}-%{commit0}

%build

%set_build_flags

%qmake_qt5 "CONFIG += nostrip" IanniX.pro

%make_build

%install

install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 iannix.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 iannix %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/mime/packages/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/mime/packages/%{name}.xml

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
install -m 644 iannix.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

# install polyphon.desktop properly.
desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc Readme.md
%license COPYING.txt
%{_bindir}/iannix
%{_datadir}/applications/IanniX.desktop
%{_datadir}/mime/packages/IanniX.xml
%{_datadir}/icons/hicolor/*

%changelog
* Tue Oct 20 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9.20-4
- fix debug build

* Fri Oct 2 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9.20-3
- update for Fedora 33

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9.20-2
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9.20-2
- update to the latest master

* Mon Jun 01 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9.16-1
- Initial spec file 0.9.16
