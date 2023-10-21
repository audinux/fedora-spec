%define commit0 e176fad933ac152ebf9acc7c3e987794ee4f1c5e

Name: alsa-scarlett-gui
Version: 0.2
Summary: ALSA Scarlett Gen 2/3 Control Panel
Release: 2%{?dist}
License: GPL-2.0-or-later
URL: https://github.com/geoffreybennett/alsa-scarlett-gui

Vendor:       Audinux
Distribution: Audinux

Source: https://github.com/geoffreybennett/alsa-scarlett-gui/archive/%{commit0}.zip#/%{name}-%{version}.zip

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: gtk4-devel
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils

%description 
The Focusrite Scarlett interfaces are class compliant USB audio interfaces meaning
that they work “out of the box” on Linux as audio and MIDI interfaces (although on
Gen 3 you need to disable MSD mode first).
However, the Gen 2 6i6+ and Gen 3 4i4+ interfaces have a bunch of proprietary
functionality that required a kernel driver to be written specifically for those
devices.

%prep
%autosetup -n alsa-scarlett-gui-%{commit0}

sed -i -e "s/-Wall/\${RPMFLAGS}/g" src/Makefile
sed -i -e "/Value=1.5/d" src/vu.b4.alsa-scarlett-gui.desktop.template

%build

%set_build_flags

export RPMFLAGS="$CFLAGS"

cd src
%make_build PREFIX=/usr

%install

%set_build_flags

export RPMFLAGS="$CFLAGS"

cd src
%make_install PREFIX=/usr
cd ..

DOCDIR=%{buildroot}/%{_datadir}/%{name}/
mkdir -p $DOCDIR/img
mkdir $DOCDIR/demo
cp img/* $DOCDIR/img
cp demo/* $DOCDIR/demo

desktop-file-install                         \
  --add-category="Audio;AudioVideo"          \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/*.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.md USAGE.md INTERFACES.md
%{_bindir}/*
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/256x256/apps/alsa-scarlett-gui.png

%changelog
* Wed Oct 18 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2-2
- update to last master - e176fad933ac152ebf9acc7c3e987794ee4f1c5e

* Mon Jul 04 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2-1
- initial build
