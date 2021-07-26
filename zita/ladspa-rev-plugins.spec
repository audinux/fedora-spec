# Tag:  Effect
# Type: LADSPA
# Category: Audio

Summary: A reverberation LADSPA plugin
Name:    REV-plugins
Version: 0.7.1
Release: 1%{?dist}
License: GPL

Vendor:       Audinux
Distribution: Audinux

URL:     http://kokkinizita.linuxaudio.org/linuxaudio/

Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/REV-plugins-%{version}.tar.bz2

BuildRequires: gcc gcc-c++ make
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
sed -i 's|-O2|%{optflags}|' Makefile
sed -i 's|/usr/lib/ladspa|$(DESTDIR)/usr/%{_lib}/ladspa|g' Makefile

%build

%make_build PREFIX=%{_prefix}

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ladspa
%make_install

%files -n ladspa-rev-plugins
%doc AUTHORS
%license COPYING
%{_libdir}/ladspa/*

%changelog
* Mon Jul 26 2021 Yann Collette <ycollette.nospam@free.fr> - 0.7.1-1
- initial spec file
