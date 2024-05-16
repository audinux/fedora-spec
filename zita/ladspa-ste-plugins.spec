# Tag: Effect
# Type: LADSPA
# Category: Audio

Summary: A stereo width LADSPA plugin
Name: STE-plugins
Version: 0.0.2
Release: 1%{?dist}
License: GPL
URL: http://kokkinizita.linuxaudio.org/linuxaudio/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux


Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/STE-plugins-%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: ladspa-devel

%description
Sources for STE-plugins.

%package -n ladspa-ste-plugins
Summary: A stereo width LADSPA plugin

%description -n ladspa-ste-plugins
A stereo width LADSPA plugin

%prep
%autosetup

# Force Fedora's optflags
sed -i 's|-O2|%{optflags}|' Makefile
sed -i 's|/usr/lib/ladspa|$(DESTDIR)/usr/%{_lib}/ladspa|g' Makefile

%build

%make_build PREFIX=%{_prefix}

%install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ladspa
%make_install BINDIR=%{_libdir}/ladspa

%files -n ladspa-ste-plugins
%doc AUTHORS
%license COPYING
%{_libdir}/ladspa/*

%changelog
* Mon Jul 26 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.2-1
- initial spec file
