# Tag: Effect
# Type: LADSPA
# Category: Audio, Synthesizer

Name: ladspa-leet
Version: 0.2
Release: 1%{?dist}
Summary: LADSPA equalizers and chorus plugin
License: GPL-2.0+
Url: https://code.google.com/archive/p/leetplugins/

Vendor:       Audinux
Distribution: Audinux

Source0: https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/leetplugins/LEET-plugins-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: ladspa-devel

%description
LADSPA equalizers and chorus plugin

%prep
%autosetup -n LEET-plugins-%{version}

%build
%make_build all

%install

install -m 755 -d %{buildroot}/%{_libdir}/ladspa/
install -m 755 *.so %{buildroot}/%{_libdir}/ladspa/

%files
%doc README
%license COPYING
%{_libdir}/ladspa

%changelog
* Sat Dec 03 2022 Yann Collette <ycollette dot nospam at free.fr> 0.2-1
- initial spec
