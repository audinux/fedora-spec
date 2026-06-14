# Status: active
# Tag: Session, Jack
# Type: Standalone
# Category: Session Mngmt

Name: patchage
Version: 1.0.10
Release: 1%{?dist}
Summary: A modular patch bay for Jack/ALSA based audio/MIDI systems
License: GPL-3.0-or-later
URL: https://github.com/drobilla/patchage
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/drobilla/patchage/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: meson
BuildRequires: ganv-devel
BuildRequires: gtkmm2.4-devel
BuildRequires: fmt-devel
BuildRequires: gettext-devel
BuildRequires: dbus-devel
BuildRequires: dbus-glib-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: desktop-file-utils

%description
Patchage is a modular patch bay for Jack and ALSA based audio/MIDI systems

%prep
%autosetup -n %{name}-%{version}

%build

%meson
%meson_build

%install

%meson_install

%files
%doc README.md NEWS
%license COPYING
%{_bindir}/*
%{_datadir}/applications/patchage.desktop
%{_datadir}/icons/hicolor/128x128/apps/patchage.png
%{_datadir}/icons/hicolor/16x16/apps/patchage.png
%{_datadir}/icons/hicolor/16x16/apps/patchage.svg
%{_datadir}/icons/hicolor/22x22/apps/patchage.png
%{_datadir}/icons/hicolor/22x22/apps/patchage.svg
%{_datadir}/icons/hicolor/24x24/apps/patchage.png
%{_datadir}/icons/hicolor/256x256/apps/patchage.png
%{_datadir}/icons/hicolor/32x32/apps/patchage.png
%{_datadir}/icons/hicolor/32x32/apps/patchage.svg
%{_datadir}/icons/hicolor/48x48/apps/patchage.png
%{_datadir}/icons/hicolor/48x48/apps/patchage.svg
%{_datadir}/icons/hicolor/scalable/apps/patchage.svg
%{_datadir}/locale/de/LC_MESSAGES/patchage.mo
%{_datadir}/locale/fr/LC_MESSAGES/patchage.mo
%{_datadir}/locale/ko/LC_MESSAGES/patchage.mo
%{_mandir}/man1/patchage.1.gz
%{_datadir}/patchage/patchage.ui

%changelog
* Sun Jun 14 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0.10-1
- Initial build
