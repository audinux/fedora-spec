Name:    midimonster
Version: 0.6
Release: 2%{?dist}
Summary: Multi-protocol translation software (ArtNet, MIDI, OSC, JACK MIDI/CV ...)
License: BSD
URL:     https://github.com/cbdevnet/midimonster

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/cbdevnet/midimonster/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: lua-devel
BuildRequires: libevdev-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: openssl-devel
BuildRequires: python3-devel

%description
Named for its scary math, the MIDIMonster is a universal control and translation
tool for multi-channel absolute-value-based control and/or bus protocols.

%prep
%autosetup -p1 -n %{name}-%{version}

sed -i -e "s/lua53/lua/g" backends/Makefile

%build

%make_build PREFIX=/usr PLUGINS=%{_libdir}/midimonster

%install

%make_install PREFIX=/usr PLUGINS=%{_libdir}/midimonster

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/*
%{_libdir}/%{name}/
%{_datadir}/%{name}/

%changelog
* Wed Jun 30 2021 Yann Collette <ycollette.nospam@free.fr> - 0.6.0-1
- update to version 0.1.0-2

* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-2
- update to version 0.5.0-2 - fix for fedora 33

* Mon May 4 2020 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-1
- update to version 0.5.0-1

* Thu Mar 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-1
- initial spec file -  version 0.4.0-1
