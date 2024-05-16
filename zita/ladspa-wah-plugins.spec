# Tag: Effect
# Type: LADSPA
# Category: Audio

Summary: A WAH filter LADSPA plugin
Name: WAH-plugins
Version: 0.1.0
Release: 1%{?dist}
License: GPL
URL: http://kokkinizita.linuxaudio.org/linuxaudio/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux


Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/WAH-plugins-%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: ladspa-devel

%description
Sources for WAH-plugins.

%package -n ladspa-wah-plugins
Summary: A WAH filter LADSPA plugin

%description -n ladspa-wah-plugins
A WAH filter LADSPA plugin

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

%files -n ladspa-wah-plugins
%doc AUTHORS README
%license COPYING
%{_libdir}/ladspa/*

%changelog
* Mon Jul 26 2021 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- initial spec file
