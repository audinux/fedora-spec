# Status: active
# Tag: Tracker, Jack, Alsa
# Type: Standalone
# Category: Audio, Sequencer

# Global variables for github repository
%global commit0 f6aa7078c3f39e9c8b025e70e7dbeab19119e213
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: Chiptune tracker for making chiptune-like music on a modern computer.
Name: plebtracker
Version: 0.1
Release: 3%{?dist}
License: GPL
URL: https://github.com/danfrz/PLEBTracker
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/danfrz/PLEBTracker/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: ncurses-devel
BuildRequires: fftw-devel

Requires: alsa-utils
Requires: inotify-tools

%description
Chiptune tracker for making chiptune-like music on a modern computer.

%prep
%autosetup -n PLEBTracker-%{commit0}

sed -i -e "s|-lncurses|-lncurses -lncursesw|g"  Tracker/src/Makefile
sed -i -e "s|CFLAGS=|CFLAGS=\$(DEPFLAGS) |g" Tracker/src/Makefile
sed -i -e "s|CFLAGS=|CFLAGS=\$(DEPFLAGS) |g" Interpreter/src/Makefile

%build

%set_build_flags

export DEPFLAGS=`echo $CFLAGS | sed -e "s/-Werror=format-security//g"`

cd Interpreter/src
%make_build PREFIX=/usr
cd ../..
cd Tracker/src
%make_build PREFIX=/usr

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_datadir}/man/man1
install -m 755 -d %{buildroot}/%{_datadir}/plebtracker/docs/
install -m 755 -d %{buildroot}/%{_datadir}/plebtracker/examples/

## INTERPRETER

cd Interpreter/src
install -m 755 plebplay   %{buildroot}/%{_bindir}/
install -m 755 plebitp    %{buildroot}/%{_bindir}/
install -m 755 plebrender %{buildroot}/%{_bindir}/

install -m 644 ../doc/plebitp.1    %{buildroot}/%{_datadir}/man/man1/
install -m 644 ../doc/plebplay.1   %{buildroot}/%{_datadir}/man/man1/
install -m 644 ../doc/plebrender.1 %{buildroot}/%{_datadir}/man/man1/
cd ../..

## TRACKER

cd Tracker/src
install -m 755 plebtrk       %{buildroot}/%{_bindir}/
install -m 755 plebtrkdaemon %{buildroot}/%{_bindir}/
install -m 755 plebtrkraw    %{buildroot}/%{_bindir}/

install -m 644 ../doc/plebtrk.1       %{buildroot}/%{_datadir}/man/man1/
install -m 644 ../doc/plebtrkdaemon.1 %{buildroot}/%{_datadir}/man/man1/
install -m 644 ../doc/plebtrkraw.1    %{buildroot}/%{_datadir}/man/man1/
cd ../..

## DIVERS

install -m 644 docs/*.txt %{buildroot}/%{_datadir}/plebtracker/docs/
install -m 644 docs/*.pdf %{buildroot}/%{_datadir}/plebtracker/docs/
install -m 644 examples/*.plb %{buildroot}/%{_datadir}/plebtracker/examples/

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/*

%changelog
* Sun Dec 05 2021 Yann Collette <ycollette dot nospam at free.fr> 0.1-3
- fix permissions

* Mon Oct 19 2020 Yann Collette <ycollette dot nospam at free.fr> 0.1-2
- fix debug build

* Fri Jun 7 2019 Yann Collette <ycollette dot nospam at free.fr> 0.1-1
- Initial release of spec file
