# Tag:  Effect, Reverb
# Type: Plugin, LADSPA
# Category: Audio

Summary: A reverberation LADSPA plugin
Name: REV-plugins
Version: 0.8.1
Release: 1%{?dist}
License: GPL
URL: http://kokkinizita.linuxaudio.org/linuxaudio/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux


Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/REV-plugins-%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: ladspa-devel

%description
Sources for REV-plugins.

%package -n ladspa-rev-plugins
Summary: A reverberation LADSPA plugin

%description -n ladspa-rev-plugins
A reverberation LADSPA plugin

%prep
%autosetup

# Force Fedora's optflags
sed -i 's|-O2|%{optflags}|' source/Makefile
sed -i 's|/usr/lib/ladspa|$(DESTDIR)/usr/%{_lib}/ladspa|g' source/Makefile

%build

cd source
%make_build PREFIX=%{_prefix}

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ladspa
cd source
%make_install

%files -n ladspa-rev-plugins
%doc README AUTHORS
%{_libdir}/ladspa/*

%changelog
* Sat Dec 10 2022 Yann Collette <ycollette.nospam@free.fr> - 0.8.1-1
- update to 0.8.1-1

* Mon Jul 26 2021 Yann Collette <ycollette.nospam@free.fr> - 0.7.1-1
- initial spec file
