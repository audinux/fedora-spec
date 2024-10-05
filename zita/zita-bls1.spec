# Status: active
# Tag: Jack
# Type: Standalone
# Category: Audio, Tool

Summary: Convert binaural signals for reproduction on conventional stereo speakers
Name: zita-bls1
Version: 0.4.0
Release: 1%{?dist}
License: GPL
URL: http://kokkinizita.linuxaudio.org/linuxaudio/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: cairo-devel
BuildRequires: clthreads-devel
BuildRequires: clxclient-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: zita-convolver-devel
BuildRequires: fftw-devel

%description
Digital implementation of the 'Blumlein Shuffler',
used to convert binaural signals into a form suitable for reproduction on a conventional stereo speaker pair.

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
mkdir -p $RPM_BUILD_ROOT%{_datadir}/zita-bls1/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/

pushd source
%make_install
popd

%files
%defattr(-,root,root,-)
%doc AUTHORS README doc
%license COPYING
%{_bindir}/*
%{_datadir}/zita-bls1/

%changelog
* Sat Oct 05 2024 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-1
- update to 0.4.0-1

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.3.3-1
- update for Fedora 29

* Fri Sep 7 2018 Yann Collette <ycollette.nospam@free.fr> - 0.3.3-1
- initial release
