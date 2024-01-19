# Tag:  Jack, Alsa, Convolution
# Type: Standalone
# Category: Audio, Tool

Summary: Measure Impulse Responses using a sine sweep and deconvolution
Name: aliki
Version: 0.3.0
Release: 1%{?dist}
License: GPL
URL: http://kokkinizita.linuxaudio.org/linuxaudio/

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
BuildRequires: libsndfile-devel
BuildRequires: zita-alsa-pcmi-devel

%description
Measure Impulse Responses using a sine sweep and deconvolution

%prep
%autosetup

# Force Fedora's optflags
sed -i 's|-O2|%{optflags}|' source/Makefile

%build
rm -rf $RPM_BUILD_ROOT

pushd source
%make_build
popd

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/

pushd source
%make_install
popd

%files
%defattr(-,root,root,-)
%doc AUTHORS README doc
%license COPYING
%{_bindir}/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-1
- update for Fedora 29

* Fri Sep 7 2018 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-1
- initial release
