# Tag: Jack, Compressor
# Type: Standalone
# Category: Audio, Effect

Summary: Dynamics Compressor. 
Name:    zita-dc1
Version: 0.3.3
Release: 1%{?dist}
License: GPL
URL:     http://kokkinizita.linuxaudio.org/linuxaudio/

Vendor:       Audinux
Distribution: Audinux

Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: clthreads-devel clxclient-devel
BuildRequires: cairo-devel fftw-devel libpng-devel libXft-devel libX11-devel

%description
Dynamic range compression reduces the volume of loud sounds or amplifies quiet sounds thus reducing or compressing an audio signal's dynamic range.
DC1 provides a dynamics compressor for use with JACK Audio Connection Kit.
It can be used as master effect or as an effect on individual instrument tracks as well.

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
pushd source
%make_install
popd

%files
%defattr(-,root,root,-)
%doc AUTHORS
%license COPYING

%{_bindir}/*
%{_datadir}/*

%changelog
* Wed May 13 2020 Yann Collette <ycollette.nospam@free.fr> - 0.3.3-1
- initial spec file
