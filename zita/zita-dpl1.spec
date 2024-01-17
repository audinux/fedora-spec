# Tag: Jack, Compressor
# Type: Standalone
# Category: Audio, Effect

Summary: Look-ahead digital peak level limiter
Name:    zita-dpl1
Version: 0.3.3
Release: 1%{?dist}
License: GPL
URL:     http://kokkinizita.linuxaudio.org/linuxaudio/

Vendor:       Audinux
Distribution: Audinux

Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: cairo-devel libpng-devel
BuildRequires: clthreads-devel clxclient-devel
BuildRequires: pkgconfig(jack)
BuildRequires: freetype-devel
BuildRequires: libX11-devel libXft-devel

%description
Use special algorithms to allow fast response without excessive LF distortion.

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
mkdir -p $RPM_BUILD_ROOT%{_datadir}/zita-dpl1/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/

pushd source
%make_install
popd

%files
%defattr(-,root,root,-)
%doc AUTHORS README doc
%license COPYING
%{_bindir}/*
%{_datadir}/zita-dpl1/

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.3.3-1
- update for Fedora 29

* Fri Sep 7 2018 Yann Collette <ycollette.nospam@free.fr> - 0.3.3-1
- initial release
