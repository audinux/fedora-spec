# Status: active
# Tag: MIDI
# Type: Standalone
# Category: MIDI

Summary: QMidiRoute is a MIDI event router and filter
Name: qmidiroute
Version: 0.4.0.2
Release: 1%{?dist}
License: GPLv2+
URL: https://salsa.debian.org/multimedia-team/qmidiroute
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://salsa.debian.org/multimedia-team/qmidiroute/-/archive/debian/0.4.0-2/qmidiroute-debian-0.4.0-2.tar.gz
Patch0: qmidiroute-01-manpage_fix.patch

BuildRequires: gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qttools-devel
BuildRequires: desktop-file-utils

%description
MIDI event router and filterMIDI note, control change,program change and pitch bend events
are logged, and can be filtered, redirected and transformed into other events according to
MIDI maps defined as tabs in the main control surface.
You can copy midi MAPS into new tabs using the 'Clone MIDI map' button.
All MIDI maps can be saved in a .qma text file.

%prep
%autosetup -p1 -n %{name}-debian-0.4.0-2

%build

export QT_SELECT=qt5

%configure --enable-qt5

%make_build

%install

%make_install

desktop-file-edit \
    %{buildroot}/%{_datadir}/applications/qmidiroute.desktop

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/qmidiroute.desktop

%files
%doc ChangeLog README
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/man/*
%{_datadir}/qmidiroute/*

%changelog
* Thu Apr 17 2025 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-2-1
- initial build
