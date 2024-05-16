# Tag: Audio, Mixer, Tool
# Type: Standalone
# Category: Audio, Mixer, Tool

# Global variables for github repository
%global commit0 25b76aa0cdcaf6bded5876d6072c5446ec3b93d9
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: ultranova4linux
Version: 0.0.%{shortcommit0}
Release: 4%{?dist}
Summary: userspace Novation Synthesizer driver
URL: https://github.com/hansfbaier/ultranova4linux
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-only

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/hansfbaier/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1: 92-novation.rules

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(jack)
%if 0%{?fedora} < 37
BuildRequires: libusb-devel
%else
BuildRequires: libusb1-devel
%endif
BuildRequires: liblo-devel
BuildRequires: boost-devel

Requires:bash

%description
Userspace driver for the Novation Ultranova and Mininova synthesizers

%prep
%autosetup -n %{name}-%{commit0}

sed -i -e "s/-g /-g $\(CXXFLAGS\) /g" Makefile

%build

%set_build_flags

export CXXFLAGS="-std=c++11 -include map $CXXFLAGS"

%make_build

%install

mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/etc/udev/rules.d/
cp ultranova4linux %{buildroot}/%{_bindir}/
cp %SOURCE1 %{buildroot}/etc/udev/rules.d/

%files
%doc
%{_bindir}/ultranova4linux
%{_sysconfdir}/udev/rules.d/92-novation.rules

%changelog
* Thu Apr 30 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.25b76aa0-4
- update for Fedora 32

* Wed Oct 31 2018 L.L.Robinson <baggypants@fedoraproject.org> - 0.0-4.20160101git25b76aa0
- new buildrequires for copr/koji

* Mon Jul 18 2016 L.L.Robinson <baggypants@fedoraproject.org> - 0.0-3.20160101git25b76aa0
- put udev ruules in right place

* Fri Jan 01 2016 L.L.Robinson <l.l.robinson@therobinsonfamily.net> - 0.0-2.20160101git25b76aa0
- Update to git: 25b76aa0

* Fri Jan  1 2016 L.L.Robinson <baggypants@fedoraproject.org>
-
