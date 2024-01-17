# Tag: Jack, Analyzer
# Type: Standalone
# Category: Audio, Tool

Summary: Yet Another Scrolling Scope. Oscilloscope
Name:    yass
Version: 0.1.0
Release: 1%{?dist}
License: GPL
URL:     http://kokkinizita.linuxaudio.org/linuxaudio/

Vendor:       Audinux
Distribution: Audinux

Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: clthreads-devel clxclient-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libX11-devel libXft-devel

%description
Main features: up to 32 channels, variable scrolling speed, automatic gain control, and very light on CPU usage. Beta release available.

%prep
%autosetup

%build
rm -rf $RPM_BUILD_ROOT

# Force Fedora's optflags
sed -i 's|-O2|%{optflags}|' source/Makefile

pushd source
%make_build
popd

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/
cp .yassrc $RPM_BUILD_ROOT%{_datadir}/doc/yassrc.sample

pushd source
%make_install
popd

%files
%defattr(-,root,root,-)
%doc AUTHORS README
%license COPYING
%{_bindir}/*
%{_docdir}/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- update for Fedora 29

* Fri Sep 7 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- initial release
