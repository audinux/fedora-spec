# Tag: Analyzer, Effect
# Type: Standalone
# Category: Tool

Name:    drc
Version: 3.2.3
Release: 1%{?dist}
Summary: Digital Room Correction
License: LGPLv2+
URL:     https://sourceforge.net/projects/drc-fir/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://sourceforge.net/projects/drc-fir/files/drc-fir/%{version}/drc-%{version}.tar.gz

BuildRequires: gsl-devel gcc gcc-c++ make

%description
Welcome to the home page of DRC.
DRC is a program used to generate correction filters for acoustic compensation of HiFi
and audio systems in general, including listening room compensation.
DRC generates just the FIR correction filters, which can be used with a real time or
offline convolver to provide real time or offline correction. DRC doesn't provide
convolution features, and provides only some simplified, although really accurate,
measuring tools.
For further informations see the documentation section, which includes the full manual
of the current version of DRC and a complete set of measurements showing the effect of
the DRC correction in a real life situation.
DRC is available for free and is released under the terms of the GNU General Public
License. See the documentation for details.

%prep
%autosetup -n drc-%{version}

%build

%set_build_flags

cd source

%make_build

%install

cd source

%make_install

cd ..

mkdir %{buildroot}%{_datadir}/drc/doc
cp -r doc/* %{buildroot}%{_datadir}/drc/doc

mkdir %{buildroot}%{_datadir}/drc/samples
cp sample/*.drc sample/*.txt sample/*.pcm %{buildroot}%{_datadir}/drc/samples/

%files
%doc readme.txt drc-%{version}.lsm
%license COPYING
%{_bindir}/*
%{_datadir}/*

%changelog
* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 3.2.3-2
- fix debug build

* Mon Aug 5 2019 Yann Collette <ycollette.nospam@free.fr> - 3.2.3-1
- initial spec file
