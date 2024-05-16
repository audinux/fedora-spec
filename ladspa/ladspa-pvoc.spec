# Tag: OSC
# Type: LADSPA
# Category: Audio, Synthesizer

Name: ladspa-pvoc
Version: 0.1.12
Release: 1%{?dist}
Summary: LADSPA plugins for time compression/expansion of sound data making use of the phase-vocoding technique
License: GPL-3.0+
URL: http://quitte.de/dsp/pvoc.html
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: http://quitte.de/dsp/pvoc_%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: ladspa-devel
BuildRequires: fftw-devel
BuildRequires: libsndfile-devel

%description
pvoc is a collection of LADSPA units and a command line tool for time
compression/expansion of sound data making use of the phase-vocoding technique

%prep
%autosetup -n pvoc-%{version}

sed -i -e "s/-O6/\$(DEPCFLAGS)/g" Makefile

%build

%set_build_flags
export DEPCFLAGS=`echo $CFLAGS | sed -e "s/-Werror=format-security//g"`

%make_build

%install

install -m 755 -d %{buildroot}/%{_libdir}/ladspa/
install -m 755 pvoc.so %{buildroot}/%{_libdir}/ladspa/

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 stretch %{buildroot}/%{_bindir}/

%files
%doc README
%license COPYING
%{_bindir}/*
%{_libdir}/ladspa/*

%changelog
* Thu Jan 26 2023 Yann Collette <ycollette dot nospam at free.fr> 0.1.12-1
- initial spec
