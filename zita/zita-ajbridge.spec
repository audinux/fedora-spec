# Tag: Jack
# Type: Standalone
# Category: Audio, Tool

Summary: Full quality multichannel audio over a local IP network
Name: zita-ajbridge
Version: 0.8.4
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
BuildRequires: alsa-lib-devel
BuildRequires: zita-resampler-devel
BuildRequires: zita-alsa-pcmi-devel

%description
Zita-ajbridge provides two applications, zita-a2j and zita-j2a. They
allow to use an ALSA device as a Jack client, to provide additional
capture (a2j) or playback (j2a) channels. Functionally these are
equivalent to the alsa_in and alsa_out clients that come with Jack,
but they provide much better audio quality. The resampling ratio will
typically be stable within 1 PPM and change only very smoothly. Delay
will be stable as well even under worst case conditions, e.g. the Jack
client running near the end of the cycle.

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
pushd source
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
%make_install
popd

%files
%defattr(-,root,root,-)
%doc AUTHORS README*
%{_bindir}/zita-*
%{_mandir}/*/*

%changelog
* Tue May 12 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.4-1
- update to 0.8.4

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.7.0-1
- update for Fedora 29

* Fri Aug 17 2018 Yann Collette <ycollette.nospam@free.fr> - 0.7.0-1
- update to 0.7.0

* Thu Sep 22 2016 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.6.0-1
- update to 0.6.0

* Wed Aug  6 2014 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.4.0-1
- initial build.
