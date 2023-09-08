# Tag: Jack
# Type: Standalone
# Category: Audio, Tool

Summary: An A/B convertor and the metering and monitoring. 
Name:    tetraproc
Version: 0.9.2
Release: 2%{?dist}
License: GPL
URL:     http://kokkinizita.linuxaudio.org/linuxaudio/

Vendor:       Audinux
Distribution: Audinux

Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: clthreads-devel
BuildRequires: clxclient-devel
BuildRequires: libsndfile-devel
BuildRequires: fftw-devel
BuildRequires: libpng-devel
BuildRequires: libXft-devel
BuildRequires: libX11-devel

%description
Tetraproc consists of two parts: the A/B convertor and the
metering and monitoring. Tetrafile only has the A/B conversion
part which is otherwise identical.

%prep
%autosetup

# Force Fedora's optflags
sed -i 's|-O2|%{optflags}|' source/Makefile

%build

pushd source
%make_build PREFIX=%{_prefix} LDLIBS="-lpthread -lsndfile -lfftw3f -lclxclient -lclthreads -ljack -lpng -lXft -lX11 -lrt"
popd

%install

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
pushd source
%make_install PREFIX=%{_prefix}
popd

%files
%doc AUTHORS README* 
%{_bindir}/tetra*
%{_datadir}/tetraproc/

%changelog
* Thu Sep 07 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.2-2
- update to 0.9.2

* Tue Oct 20 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.6-2
- fix debug build

* Tue May 12 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.6-1
- update to 0.8.6

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.8.2-1
- update for Fedora 29

* Fri Aug 17 2018 Yann Collette <ycollette.nospam@free.fr> - 0.8.2-1
- first release
