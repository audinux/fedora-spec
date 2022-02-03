# Tag: Jack
# Type: Standalone
# Category: Audio, Tool

Summary: Full quality multichannel audio over a local IP network
Name:    zita-njbridge
Version: 0.4.8
Release: 1%{?dist}
License: GPL
URL:     http://kokkinizita.linuxaudio.org/linuxaudio/

Vendor:       Audinux
Distribution: Audinux

Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: gcc gcc-c++ make
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: zita-resampler-devel

%description
Command line Jack clients to transmit full quality multichannel audio
over a local IP network, with adaptive resampling by the
receiver(s). Zita-njbridge can be used for a one-to-one connection
(using UDP) or in a one-to-many system (using multicast). Sender and
receiver(s) can each have their own sample rate and period size, and
no word clock sync between them is assumed. Up 64 channels can be
transmitted, receivers can select any combination of these. On a
lightly loaded or dedicated network zita-njbridge can provide low
latency (same as for an analog connection). Additional buffering can
be specified in case there is significant network delay jitter. IPv6
is fully supported.

%prep
%autosetup

# Force Fedora's optflags
sed -i 's|-O2|%{optflags}|' source/Makefile

%build

pushd source
%make_build PREFIX=%{_prefix} 
popd

%install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
pushd source
%make_install PREFIX=%{_prefix} 
popd

%files
%doc AUTHORS README* 
%{_bindir}/zita-*
%{_mandir}/man1/*

%changelog
* Mon Jul 26 2021 Yann Collette <ycollette.nospam@free.fr> - 0.4.8-1
- update to 0.4.8-1

* Tue May 12 2020 Yann Collette <ycollette.nospam@free.fr> - 0.4.4-1
- update to 0.4.4

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.4.2-1
- update for Fedora 29

* Fri Aug 17 2018 Yann Collette <ycollette.nospam@free.fr> - 0.4.2-1
- update to 0.4.2.0

* Wed Aug  6 2014 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.0-1
- initial build.
