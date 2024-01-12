# Tag: Audio, Live, Session
# Type: Plugin, LV2, VST
# Category: Audio, Tool, Session Mngmt

Name: ninjam-client
Version: 0.0.1
Release: 2%{?dist}
Summary: A realtime network sound client
License: GPL-2.0-or-later
URL: http://www.cockos.com/ninjam/

Vendor:       Audinux
Distribution: Audinux

Source0: http://www.cockos.com/ninjam/downloads/src/cclient_src_v0.01a.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: alsa-lib-devel
BuildRequires: libvorbis-devel

%description
A realtime network sound client

%prep
%autosetup -n ninjam

sed -i -e "s/-s //g" cursesclient/Makefile

%build

%set_build_flags

cd cursesclient
%make_build OPTFLAGS="-fpermissive $CFLAGS"

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 cursesclient/cninjam %{buildroot}%{_bindir}/

%files
%{_bindir}/*

%changelog
* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- fix debug build

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- update for Fedora 29

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial build
