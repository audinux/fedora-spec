Name:    ninjam-server
Version: 0.0.1
Release: 2%{?dist}
Summary: A realtime network sound server
License: GPLv2+
URL:     http://www.cockos.com/ninjam/

Vendor:       Audinux
Distribution: Audinux

Source0: http://www.cockos.com/ninjam/downloads/src/ninjam_server_0.06.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: ncurses-devel
BuildRequires: alsa-lib-devel
BuildRequires: libvorbis-devel

%description
A realtime network sound client

%prep
%autosetup -n ninjam_server_0.06

sed -i -e "s|CFLAGS =  -O2 -s -Wall|CFLAGS = %{build_cflags}|g" ninjam/server/makefile

%build

cd ninjam/server
%make_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 ninjam/server/ninjamsrv %{buildroot}%{_bindir}/
install -m 755 -d %{buildroot}/%{_datadir}/ninjam/
install -m 644 ninjam/server/example.cfg %{buildroot}%{_datadir}/ninjam/

%files
%doc ninjam/server/license.txt ninjam/server/cclicense.txt
%{_bindir}/*
%{_datadir}/ninjam/

%changelog
* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- fix debug build

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- update for Fedora 29

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial build
