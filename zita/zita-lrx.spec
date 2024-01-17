# Tag: Jack, Equalizer
# Type: Standalone
# Category: Audio, Effect

Summary: 4th order crossover filters
Name:    zita-lrx
Version: 0.1.2
Release: 1%{?dist}
License: GPL
URL:     http://kokkinizita.linuxaudio.org/linuxaudio/

Vendor:       Audinux
Distribution: Audinux

Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: pkgconfig(jack)
BuildRequires: clthreads-devel clxclient-devel freetype-devel
BuildRequires: libX11-devel libXft-devel cairo-devel
BuildRequires: desktop-file-utils

%description
Zita-lrx is a command line jack application providing 2, 3, or 4-band,
4th order crossover filters. The filter type is continuously variable
between Linkwitz-Riley (-6dB at the xover frequency) and Butterworth
(-3 dB at the xover frequency). Outputs are exactly phase matched in
the crossover regions.

%prep
%autosetup

%build
rm -rf $RPM_BUILD_ROOT

# Force Fedora's optflags
sed -i 's|-march=native|%{optflags}|' source/Makefile

pushd source
%make_build
popd

%install
pushd source
%make_install
popd

%files
%defattr(-,root,root,-)
%doc AUTHORS README* examples/
%{_bindir}/zita-lrx

%changelog
* Tue May 12 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.2-1
- update to 0.1.2

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- update for Fedora 29

* Thu Aug  8 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.0-1
- initial build.
