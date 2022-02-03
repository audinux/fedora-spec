# Tag:  Jack, Analyzer
# Type: Standalone
# Category: Audio, Tool

Summary: Loudness measurement according to EBU-R128.
Name:    ebumeter
Version: 0.4.2
Release: 1%{?dist}
License: GPL
URL:     http://kokkinizita.linuxaudio.org/linuxaudio/

Vendor:       Audinux
Distribution: Audinux

Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: zita-resampler-devel
BuildRequires: clthreads-devel clxclient-devel
BuildRequires: libpng-devel libsndfile-devel
BuildRequires: libX11-devel libXft-devel xorg-x11-proto-devel

%description
Loudness measurement according to EBU-R128.
Presented at LAC 2011 (thanks to Joern Nettingsmeier !).
The only documentation available ATM are the paper, the presentation
slides and the video of the LAC 2011 session.

%prep
%autosetup

%build
rm -rf $RPM_BUILD_ROOT

# Force Fedora's optflags
sed -i 's|-O2|%{optflags}|' source/Makefile

pushd source
make PREFIX=%{_prefix}
popd

%install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
pushd source
make PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT install
popd

%files
%defattr(-,root,root,-)
%doc AUTHORS README* 
%{_bindir}/ebu*
%{_datadir}/ebumeter/*

%changelog
* Tue May 12 2020 Yann Collette <ycollette.nospam@free.fr> - 0.4.2-1
- update to 0.4.2

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-1
- update for Fedora 29

* Fri Aug 17 2018 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-1
- initial release
