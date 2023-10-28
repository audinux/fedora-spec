%define commit0 c5ef4cb50faa4acbb78bd339558f37f2b050cd8e

Name:    minigbs
Summary: Small .gbs chiptune player for Linux
Version: 1.4.2
Release: 1%{?dist}
License: MIT
URL:     https://github.com/baines/MiniGBS

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/baines/MiniGBS/archive/c5ef4cb50faa4acbb78bd339558f37f2b050cd8e.zip#/%{name}-%{commit0}.zip

BuildRequires: gcc
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: alsa-lib-devel
BuildRequires: libconfig-devel
BuildRequires: libX11-devel

%description
MiniGBS is a small .gbs file (gameboy music) player with an ncurses UI.
It's not cycle-accurate, but still sounds good for most of the files I've tested.

%prep
%autosetup -n MiniGBS-%{commit0}

sed -i -e "s/CFLAGS  := -g/CFLAGS  := \$(RPMFLAGS)/g" Makefile

%build

%set_build_flags
export RPMFLAGS="$CFLAGS"

%make_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 minigbs %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/MiniGBS/examples/
install -m 644 gbs/pocket.gbs %{buildroot}/%{_datadir}/MiniGBS/examples/

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/MiniGBS/examples/*

%changelog
* Sat Oct 28 2023 Yann Collette <ycollette.nospam@free.fr> - 1.4.2-1
- initial spec file
