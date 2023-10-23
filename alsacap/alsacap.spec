# Tag: Alsa
# Type: Standalone
# Category: Audio, Tool

Name:    alsacap
Version: 1.0
Release: 1%{?dist}
Summary: Command line tool for showing capabilities of alsa devices
License: LicenseRef-Fedora-Public-Domain
URL:     https://github.com/bubbapizza/alsacap

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/bubbapizza/alsacap/archive/refs/heads/master.zip#/%{name}-%{version}.zip

BuildRequires: gcc
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: alsa-lib-devel

%description
Command line tool for showing capabilities of alsa devices

%prep
%autosetup -n %{name}-master

%build

./bootstrap

%configure
%make_build

%install

%make_install

%files
%license COPYING
%doc README

%{_bindir}/*
%{_mandir}/*

%changelog
* Mon Jul 12 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- initial release
