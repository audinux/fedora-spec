Name:    jackmidi2osc
Version: 0.2
Release: 1%{?dist}
Summary: Jack Midi to OSC 
License: GPL-2.0-or-later
URL:     https://github.com/x42/jackmidi2osc

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/x42/jackmidi2osc/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel

%description
A configurable tool to generate OSC triggered by JACK MIDI events.

The main use-case is to perform complex actions with a simple
midi-event. e.g set ardour-mixer scenes (mute, gain, plugin-settings)
with a single button press.

jackmidi2osc also facilitates to translating MIDI note and CC-events
to OSC in realtime.

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags

%make_build PREFIX=%{_prefix} STRIP=true VERSION=%{version}

%install

%make_install PREFIX=%{_prefix} STRIP=true VERSION=%{version}

%files
%doc README.md
%license COPYING
%{_bindir}/*
%{_mandir}/*

%changelog
* Wed Dec 27 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2-1
- Initial spec file
