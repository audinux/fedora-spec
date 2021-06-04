# Tag: Jack, Convolution
# Type: Standalone
# Category: Audio, Effect

Summary: Convolution Engine for JACK, based on FFT convolution and using non-uniform partition sizes
Name:    jconvolver
Version: 1.0.2
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia

URL:     http://kokkinizita.linuxaudio.org/linuxaudio/
Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: zita-convolver-devel
BuildRequires: libsndfile-devel
BuildRequires: clthreads-devel
BuildRequires: fftw-devel

%description
Real-time convolution engine. It can execute up to a 64 by 64 convolution matrix
(i.e. 4096 simultaneous convolutions) as long as your CPU(s) can handle the load. 
It is designed to be efficient also for sparse (e.g. diagonal) matrices, 
and for sparse impulse responses. 
Unused matrix elements and unused partitions do not take any CPU time.

%prep
%setup -q

%build
rm -rf $RPM_BUILD_ROOT

# Force Fedora's optflags
sed -i 's|-O2|%{optflags}|' source/Makefile

pushd source
make PREFIX=%{_prefix}
popd

%install
pushd source
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/jconvolver/config/
cp -r ../config-files/* $RPM_BUILD_ROOT%{_datadir}/jconvolver/config/

make PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT install
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS README* 
%{_bindir}/*
%{_datadir}/jconvolver/config/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-1
- update for Fedora 29

* Mon Sep 17 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-1
- Initial build
