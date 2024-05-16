# Tag:  Jack
# Type: Standalone
# Category: Audio, Tool

Summary: An Ambisonic decoder for first and second order.
Name: ambdec
Version: 0.7.1
Release: 1%{?dist}
License: GPL
URL: http://kokkinizita.linuxaudio.org/linuxaudio/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(jack)
BuildRequires: clthreads-devel
BuildRequires: clxclient-devel
BuildRequires: libsndfile-devel
BuildRequires: libpng-devel
BuildRequires: libXft-devel
BuildRequires: libX11-devel

%description
Main features:
* 1st, 2nd and 3rd order 2-D or 3-D decoding.
* Up to 36 speakers (could be extended).
* Optional dual frequency band decoding.
* Optional speaker delay and gain compensation.
* Optional Near-Field effect compensation.
* Built-in test and Mute/Solo for each speaker.
* Unlimited number of presets.
* Jack client with graphical user interface.

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
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
pushd source
%make_install
popd

%files
%defattr(-,root,root,-)
%doc AUTHORS README*
%license COPYING
%{_bindir}/*
%{_datadir}/*

%changelog
* Wed May 13 2020 Yann Collette <ycollette.nospam@free.fr> - 0.7.1-1
- initial spec file
