# Status: active
# Tag: MIDI
# Type: Standalone
# Category: Tool, MIDI

Name: midish
Version: 1.4.1
Release: 1%{?dist}
Summary: Midish is an open-source MIDI sequencer/filter for Unix-like operating systems
License: BSD-1-Clause
URL: https://midish.org
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://midish.org/midish-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel

%description
Midish is an open-source MIDI sequencer/filter for Unix-like operating systems.
Implemented as a simple command-line interpreter (like a shell) it's intended to
be lightweight, fast and reliable for real-time performance.

Important features:
* multiple MIDI devices handling
* synchronization to external audio/MIDI hardware/software
* real-time MIDI filtering/routing (controller mapping, keyboard splitting, ...)
* track recording, editing, progressive quantisation ...
* import and export of standard MIDI files
* system exclusive messages handling
* ... 

Midish is open-source software distributed under a BSD-style license (compatible with GPL). 

%prep
%autosetup -n %{name}-%{version}

%build

./configure --prefix=%{_prefix} --bindir=%{_bindir} --datadir=%{_datadir} --mandir=%{_mandir} --enable-alsa --disable-sndio
%make_build

%install

%make_install

%files
%doc README manual.html
%{_bindir}/
%{_datadir}/examples/midish/midishrc
%{_datadir}/examples/midish/sample.msh
%{_mandir}/man1/midish.1.gz
%{_mandir}/man1/smfplay.1.gz
%{_mandir}/man1/smfrec.1.gz

%changelog
* Fri Jan 30 2026 Yann Collette <ycollette.nospam@free.fr> - 1.4.1-1
- Initial spec file
