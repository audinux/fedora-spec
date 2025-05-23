# Status: active
# Tag: Synthesizer
# Type: Standalone
# Category: Synthesizer

Name: mx44
Version: 2.0.0
Release: 1%{?dist}
Summary: A JACK synthesizer
URL: http://web.comhem.se/luna/
ExclusiveArch: x86_64 
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/linuxmao-org/Mx44/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(jack)
BuildRequires: gtk2-devel
BuildRequires: alsa-lib-devel

%description
Mx44 is a polyphonic multichannel midi realtime software synthesizer.

%prep
%autosetup -n Mx44-%{version}

%build

%set_build_flags

cd src
%make_build

%install

cd src

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 mx44 %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_datadir}/Mx44/
install -m 644 ../data/mx44patch %{buildroot}/%{_datadir}/Mx44/
install -m 644 ../data/gtk-2.0/gtkrc %{buildroot}/%{_datadir}/Mx44/

%files
%doc README.md
%license COPYING
%{_bindir}/*
%{_datadir}/*

%changelog
* Thu May 08 2025 Yann Collette <ycollette.nospam@free.fr> - 2.0.0-1
- update to 2.0.0-1

* Mon Oct 26 2020 Yann Collette <ycollette.nospam@free.fr> - 0.44.3-1
- change source URL + fix debug build + fix makefiles

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.44.2-1
- Update for Fedora 29

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.44.2-1
- inital release
