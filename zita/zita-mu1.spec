# Tag: Jack
# Type: Standalone
# Category: Audio, Tool

Summary: MU1 is a simple Jack app used to organise stereo monitoring.
Name:    zita-mu1
Version: 0.3.3
Release: 1%{?dist}
License: GPL
URL:     http://kokkinizita.linuxaudio.org/linuxaudio/

Vendor:       Audinux
Distribution: Audinux

Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: zita-resampler-devel clthreads-devel clxclient-devel
BuildRequires: cairo-devel libpng-devel libsndfile-devel
BuildRequires: libX11-devel libXft-devel

%description
Written originally for use with Ardour2, but still useful with Ardour3
as it provides some extra functions.
Main features:
* Four stereo inputs.
* K20 RMS/peak meters and stereo correlation meter.
* Two monitoring outputs with individual volume controls.
* Left / Right / Mono and Dim swithes.
* Output of unmodified selected input, e.g. for metering.
* Talkback level controls and buttons with automatic dimming of speakers

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
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/zita-mu1/

pushd source
%make_install
popd

%files
%defattr(-,root,root,-)
%doc AUTHORS README* 
%{_bindir}/*
%{_datadir}/zita-mu1/

%changelog
* Tue May 12 2020 Yann Collette <ycollette.nospam@free.fr> - 0.3.3-1
- update 0.3.3

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.2.2-1
- update for Fedora 29

* Fri Aug 17 2018 Yann Collette <ycollette.nospam@free.fr> - 0.2.2-1
- initial release
