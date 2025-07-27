# Status: active
# Tag: MIDI, Tool
# Type: Standalone
# Category: MIDI, Tool

%global commit0 ef199f7ce58a14c70acafe6f7cb65294da27faad

Name: midi-utils
Version: 0.0.1
Release: 1%{?dist}
Summary: A set of MIDI utilities for Linux-based musical composing
License: GPL-2.0-or-later
URL: https://github.com/aiobofh/midi-utils
ExclusiveArch: x86_64 aarch64

Source0: https://github.com/aiobofh/midi-utils/archive/%{commit0}.zip#/%{name}-%{version}.zip

BuildRequires: gcc
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)

%description
This is a set (one for now) of useful MIDI-translation tools for Linux-based
Digital Audio Workstations. These tools are mainly simplistic hacks but they
do come in handy in some cases. At least in my studio.

%prep
%autosetup -n %{name}-%{commit0}

%build

%make_build

%install

mkdir -p %{buildroot}/%{_bindir}/

%make_install PREFIX=%{buildroot}/

mkdir -p %{buildroot}/%{_datadir}/%{name}/conf/
cp contrib/* %{buildroot}/%{_datadir}/%{name}/conf/

rm -rf %{buildroot}/etc/midi-utils/

%files
%doc README
%{_bindir}/*
%{_datadir}/%{name}/conf/*

%changelog
* Sat Jul 26 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- initial release of the spec file
