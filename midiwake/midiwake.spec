# Tag: MIDI, Tool
# Type: Standalone
# Category: MIDI, Tool

Name: midiwake
Version: 1.0.0
Release: 1%{?dist}
Summary: A utility to block the screen saver during MIDI activity
License: GPL-2.0-or-later
URL: https://github.com/jpcima/midiwake

Source0: https://github.com/jpcima/midiwake/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist

%description
This program shows up in the notification area, and it listens for output
produced by hardware MIDI devices, such as a synthesizer keyboard.

While the device is being played with, the program prevents the desktop from
entering idle mode, which might lock the session or activate the screen saver.
For instance, one can practice a piece of music on screen without risks of
interruption.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_bindir}/midiwake
%{_datadir}/applications/midiwake.desktop
%{_datadir}/pixmaps/midiwake.png

%changelog
* Thu Sep 22 2022 Jean Pierre Cimalando <jp-dev@gmx.com> - 1.0.0-1
- initial release of the spec file
