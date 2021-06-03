# Tag: Jack, Analyzer
# Type: Standalone
# Category: Audio, Tool

Summary: Small app designed to measure audio test signals and in particular noise signals.
Name:    jnoisemeter
Version: 0.2.2
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia

URL:     http://kokkinizita.linuxaudio.org/linuxaudio/
Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: clthreads-devel clxclient-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libX11-devel libXft-devel
BuildRequires: libpng-devel freetype-devel

%description
The simplest use is to measure the S/N ratio of your
sound card. If you can calibrate the input levels of
your soundcard it can also be used (with some external
hardware) to measure noise levels of any type of audio
equipment, including preamps and microphones.

There are various 'standard' ways to measure noise
(and S/N ratio). All amount to some combination of a
particular weighting filter and a particular detector.

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
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/

pushd source
make PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT install
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS README
%license COPYING
%{_bindir}/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.2.2-1
- update for Fedora 29

* Fri Sep 7 2018 Yann Collette <ycollette.nospam@free.fr> - 0.2.2-1
- initial release
