# Status: active
# Tag: Mixer
# Type: Standalone
# Category: Audio, Tool

Name: alsa-scarlett-gui
Version: 0.5.0
Summary: ALSA Scarlett Control Panel
Release: 2%{?dist}
License: GPL-2.0-or-later
URL: https://github.com/geoffreybennett/alsa-scarlett-gui
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source: https://github.com/geoffreybennett/alsa-scarlett-gui/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: gtk4-devel
BuildRequires: alsa-lib-devel
BuildRequires: openssl-devel
BuildRequires: desktop-file-utils

%description
The Focusrite Scarlett interfaces are class compliant USB audio interfaces meaning
that they work “out of the box” on Linux as audio and MIDI interfaces (although on
Gen 3 you need to disable MSD mode first).
However, the Gen 2 6i6+ and Gen 3 4i4+ interfaces have a bunch of proprietary
functionality that required a kernel driver to be written specifically for those
devices.

%prep
%autosetup -n alsa-scarlett-gui-%{version}

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
%doc README.md FAQ.md docs/*
%{_bindir}/*
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/256x256/apps/*.png

%changelog
* Tue Feb 25 2025 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-2
- update to 0.5.0-2

* Mon Feb 24 2025 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-2
- update to 0.4.0-2

* Thu Nov 30 2023 Yann Collette <ycollette.nospam@free.fr> - 0.3.3-2
- update to 0.3.3-2

* Tue Nov 14 2023 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-2
- update to 0.3.1-2

* Mon Nov 13 2023 Yann Collette <ycollette.nospam@free.fr> - 0.3-2
- update to 0.3-2

* Wed Oct 18 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2-2
- update to last master - e176fad933ac152ebf9acc7c3e987794ee4f1c5e

* Mon Jul 04 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2-1
- initial build
