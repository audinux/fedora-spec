# Tag:  Effect
# Type: LADSPA
# Category: Audio

Summary: A set of filter LADSPA plugins
Name:    FIL-plugins
Version: 0.3.0
Release: 1%{?dist}
License: GPL

Vendor:       Audinux
Distribution: Audinux

URL:     http://kokkinizita.linuxaudio.org/linuxaudio/

Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/FIL-plugins-%{version}.tar.bz2

BuildRequires: gcc gcc-c++ make
BuildRequires: ladspa-devel

%description
Sources for FIL-plugins.

%package -n ladspa-fil-plugins
Summary: A set of filter LADSPA plugins

%description -n ladspa-fil-plugins
A set of filter LADSPA plugins

%prep
%autosetup

# Force Fedora's optflags
sed -i 's|-O3|%{optflags}|' Makefile
sed -i 's|/usr/lib/ladspa|$(DESTDIR)/usr/%{_lib}/ladspa|g' Makefile

%build

%make_build PREFIX=%{_prefix}

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ladspa
%make_install

%files -n ladspa-fil-plugins
%doc AUTHORS
%license COPYING
%{_libdir}/ladspa/*

%changelog
* Mon Jul 26 2021 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-1
- initial spec file
