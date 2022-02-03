# Tag:  Jack, Convolution, Reverb
# Type: Presets
# Category: Audio

Summary: Impulse Responses for Jconvolver
Name:    jconvolver-reverbs
Version: 0.8.7
Release: 1%{?dist}
License: Unknown
URL:     http://kokkinizita.linuxaudio.org/

Source:  http://kokkinizita.linuxaudio.org/linuxaudio/downloads/jconvolver-reverbs.tar.bz2

Vendor:       Planet CCRMA
Distribution: Planet CCRMA

BuildArch:    noarch

Requires: jconvolver

%description
Inpulse responses for jconvolver, they match the configuration files 
distributed with jconvolver. 

%prep
%autosetup -n reverbs

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/jconvolver/reverbs
cp -pr * %{buildroot}%{_datadir}/jconvolver/reverbs

%files
%defattr(-,root,root,-)
%{_datadir}/jconvolver/reverbs

%changelog
* Sat May 15 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.8.7-1
- first release for fc14/15
