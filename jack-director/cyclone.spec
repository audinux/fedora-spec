# Tag: Jack
# Type: Standalone
# Category: Audio, Tool

Summary: Cyclone Loop Giant is a music application for GNU/Linux that allows users to manipulate loops in various ways.
Name:    cyclone
Version: 0.1.3
Release: 1%{?dist}
License: GPL-2.0-only
URL:     https://toxic.cubicarea.it/

Vendor:       Audinux
Distribution: Audinux

Source0: https://sourceforge.net/projects/cycloneloop/files/cyclone_%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: qt-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel
BuildRequires: desktop-file-utils

Requires: sooperlooper

%description
Cyclone Loop Giant is a music application for GNU/Linux that
allows users to manipulate loops in various ways.
It works with professional audio formats
like .wav .aif .flac, and professional audio environment
(Jack Audio Connection Kit).
Now it's in early stage of development;
it's goal is to make a professional audio application for GNU/Linux that can compete
with Ableton Live in loop handling power.


%prep
%autosetup -n cyclone

%build

%set_build_flags

export LDFLAGS="-z muldefs $MDFLAGS"

%qmake_qt4
%make_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 cyclone %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/applications/
cp %{name}.desktop %{buildroot}/%{_datadir}/applications/

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp icons/%{name}.png %{buildroot}/%{_datadir}/pixmaps/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/help/
cp -r help/* %{buildroot}/%{_datadir}/%{name}/help/

install -m 755 -d %{buildroot}/%{_datadir}/mime/packages/
cp %{name}.xml %{buildroot}/%{_datadir}/mime/packages/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/%{name}/
%{_datadir}/%{name}/help/*
%{_datadir}/mime/packages/*

%changelog
* Fri Dec 02 2022 Yann Collette <ycollette.nospam@free.fr> - 0.1.3-1
- initial build.
