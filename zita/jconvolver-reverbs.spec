# Tag:  Jack, Convolution, Reverb
# Type: Presets
# Category: Audio

Summary: Impulse Responses for Jconvolver
Name:    jconvolver-reverbs
Version: 0.8.7
Release: 1%{?dist}
License: Unknown
Group:   Applications/Multimedia
URL:     http://kokkinizita.linuxaudio.org/
Source:  http://kokkinizita.linuxaudio.org/linuxaudio/downloads/jconvolver-reverbs.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Vendor:       Planet CCRMA
Distribution: Planet CCRMA
BuildArch:    noarch

Requires: jconvolver

%description
Inpulse responses for jconvolver, they match the configuration files 
distributed with jconvolver. 

%prep
%setup -q -n reverbs

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}%{_datadir}/jconvolver/reverbs
%{__cp} -pr * %{buildroot}%{_datadir}/jconvolver/reverbs

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_datadir}/jconvolver/reverbs

%changelog
* Sat May 15 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.8.7-1
- first release for fc14/15
