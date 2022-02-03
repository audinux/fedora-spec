# Tag: Jack
# Type: Standalone
# Category: Audio, Tool

Summary: Provides A/B processing with file input and output. 
Name:    octofile
Version: 0.3.2
Release: 1%{?dist}
License: GPL
URL:     http://kokkinizita.linuxaudio.org/linuxaudio/

Vendor:       Audinux
Distribution: Audinux

Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: libsndfile-devel fftw-devel

%description
The DSP part is completely separated from the file I/O, and can 
be used safely in a real-time context such as an ASIO or VST callback.

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
pushd source
%make_install
popd

%files
%defattr(-,root,root,-)
%doc AUTHORS README* 
%license COPYING
%{_bindir}/*
%{_mandir}/*

%changelog
* Wed May 13 2020 Yann Collette <ycollette.nospam@free.fr> - 0.3.2-1
- Initial spec file
