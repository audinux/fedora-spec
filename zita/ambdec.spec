# Tag:  Jack
# Type: Standalone
# Category: Audio, Tool

Summary: An Ambisonic decoder for first and second order. 
Name:    ambdec
Version: 0.7.1
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia

URL:     http://kokkinizita.linuxaudio.org/linuxaudio/
Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: clthreads-devel clxclient-devel
BuildRequires: libsndfile-devel libpng-devel libXft-devel libX11-devel

%description
Main features:
* 1st, 2nd and 3rd order 2-D or 3-D decoding.
* Up to 36 speakers (could be extended).
* Optional dual frequency band decoding.
* Optional speaker delay and gain compensation.
* Optional Near-Field effect compensation.
* Built-in test and Mute/Solo for each speaker.
* Unlimited number of presets.
* Jack client with graphical user interface.

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
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
pushd source
make PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT install
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS README*
%license COPYING
%{_bindir}/*
%{_datadir}/*

%changelog
* Wed May 13 2020 Yann Collette <ycollette.nospam@free.fr> - 0.7.1-1
- initial spec file
