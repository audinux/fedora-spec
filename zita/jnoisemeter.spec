# Tag: Jack, Analyzer
# Type: Standalone
# Category: Audio, Tool

Summary: Small app designed to measure audio test signals and in particular noise signals.
Name:    jnoisemeter
Version: 0.4.1
Release: 1%{?dist}
License: GPL
URL:     http://kokkinizita.linuxaudio.org/linuxaudio/

Vendor:       Audinux
Distribution: Audinux

Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: clthreads-devel
BuildRequires: clxclient-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: libpng-devel
BuildRequires: freetype-devel

%description
The simplest use is to measure the S/N ratio of your
sound card. If you can calibrate the input levels of
your soundcard it can also be used (with some external
hardware) to measure noise levels of any type of audio
equipment, including preamps and microphones.

There are various 'standard' ways to measure noise
(and S/N ratio). All amount to some combination of a
particular weighting filter and a particular detector.

%prep
%autosetup

# Force Fedora's optflags
sed -i 's|-O2|%{optflags}|' source/Makefile

%build

pushd source
%make_build PREFIX=%{_prefix}
popd

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/

pushd source
%make_install PREFIX=%{_prefix}
popd


%files
%doc AUTHORS README
%license COPYING
%{_bindir}/*

%changelog
* Tue Oct 24 2023 Yann Collette <ycollette.nospam@free.fr> - 0.4.1-1
- update to 0.4.1-1

* Mon Jul 26 2021 Yann Collette <ycollette.nospam@free.fr> - 0.2.2-1
- update to 0.2.2-1

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.2.2-1
- update for Fedora 29

* Fri Sep 7 2018 Yann Collette <ycollette.nospam@free.fr> - 0.2.2-1
- initial release
