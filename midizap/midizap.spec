# Tag: MIDI, Tool
# Type: Standalone
# Category: MIDI, Tool

# Global variables for github repository
%global commit0 dc626710e6c0cb7634c159eebcc5242241f402fb
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: midizap
Version: 1.0.0.%{shortcommit0}
Release: 1%{?dist}
Summary: Control your multimedia applications with MIDI
License: GPL-2.0-or-later
URL: https://github.com/agraef/midizap

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/agraef/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildReauires: make
BuildRequires: emacs
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: libXtst-devel

%description
midizap lets you control your multimedia applications using MIDI,
the venerable "Musical Instrument Digital Interface" protocol which has been around
since the 1980s. Modern MIDI controllers are usually USB class devices which don't
require any special interface or driver, and they are often much cheaper than more specialized gear.
With midizap you can leverage these devices to control just about any X11-based application.
To these ends, it translates Jack MIDI input into X keyboard and mouse events, and optionally
MIDI output. It does this by matching the class and title of the focused window against the regular
expressions for each application section in its configuration (midizaprc) file. If a regex matches,
the corresponding set of translations is used. If a matching section cannot be found, or if it
doesn't define a suitable translation, the program falls back to a set of default translations.

%package emacs
Summary: Midizap support for Emacs
Requires: midizap = %{version}-%{release}

%description emacs
Midizap support for the Emacs text editor.

%prep
%autosetup -n %{name}-%{commit0}

sed -i -e "s/prefix=\/usr\/local/prefix=\/usr/g" Makefile
sed -i -e "/CFLAGS=/d" Makefile

%build

%%make_build CFLAGS="%{build_cflags}"

%install

rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{_bindir}/*
%{_datadir}/*
%{_mandir}/*
%{_sysconfdir}/*

%files emacs
%defattr(-,root,root,-)
%{_datadir}/emacs/site-lisp/*

%changelog
* Thu Mar 28 2019 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- initial spec file
