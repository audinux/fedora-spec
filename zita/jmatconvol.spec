# Tag: Jack, Convolution
# Type: Standalone
# Category: Audio, Effect

Summary: Real-time convolution engine.
Name:    jmatconvol
Version: 0.5.2
Release: 1%{?dist}
License: GPL
URL:     http://kokkinizita.linuxaudio.org/linuxaudio/

Vendor:       Audinux
Distribution: Audinux

Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: gcc gcc-c++ make
BuildRequires: pkgconfig(jack)
BuildRequires: zita-convolver-devel
BuildRequires: libsndfile-devel
BuildRequires: clthreads-devel
BuildRequires: fftw-devel

%description
In contrast to jconvolver, jmatconvol uses a single partition
size equal to the Jack period, and is optimised
for dense matrices of short convolutions, e.g.
for processing signals from spherical microphones
such as the Eigenmic. The maximum convolution
length is limited to 4096 samples in this release.

%prep
%autosetup

# Force Fedora's optflags
sed -i 's|-O2|%{optflags}|' source/Makefile

%build

pushd source
%make_build PREFIX=%{_prefix}
popd

%install
pushd source
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/jmatconvol/config/
cp -r ../config_files/* $RPM_BUILD_ROOT%{_datadir}/jmatconvol/config/

%make_install PREFIX=%{_prefix}
popd

%files
%doc AUTHORS README*
%license COPYING
%{_bindir}/*
%{_datadir}/jmatconvol/
%{_datadir}/jmatconvol/config/*

%changelog
* Sat Dec 10 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5.2-1
- update to 0.5.2-1

* Mon Jul 26 2021 Yann Collette <ycollette.nospam@free.fr> - 0.4.2-1
- update to 0.4.2-1

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.3.3-1
- update for Fedora 29

* Mon Sep 17 2018 Yann Collette <ycollette.nospam@free.fr> - 0.3.3-1
- Initial build
