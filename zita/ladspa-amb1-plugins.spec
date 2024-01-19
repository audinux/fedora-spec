# Tag: Effect
# Type: Plugin, LADSPA
# Category: Audio

Summary: A collection of LADSPA plugins for third order Ambisonics.
Name: AMB1-plugins
Version: 0.3.0
Release: 1%{?dist}
License: GPL
URL: http://kokkinizita.linuxaudio.org/linuxaudio/

Vendor:       Audinux
Distribution: Audinux

Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/AMB1-plugins-%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: ladspa-devel

%description
Sources for AMB1-plugins.

%package -n ladspa-amb1-plugins
Summary: A collection of LADSPA plugins for third order Ambisonics

%description -n ladspa-amb1-plugins
AMB1-plugins is a collection of LADSPA plugins for
third order Ambisonics.

All plugins use the 'Ambix' format: SN3D gains and ACN
channel ordering.

Processing in plugins having control inputs is fully
'dezippered'.

All plugins are 'in-place safe' and can be used in Ardour.

Note that azimuth and Z-rotation control inputs assume
that a positive azimuth is to the right hand side. This
is done because most plugin hosts would create GUI controls
assuming that a positive value is to the right for a slider
or clockwise for a rotary control.

%prep
%autosetup

# Force Fedora's optflags
sed -i 's|-O2|%{optflags}|' source/Makefile
sed -i 's|/usr/lib/ladspa|$(DESTDIR)/usr/%{_lib}/ladspa|g' source/Makefile
%build

pushd source
%make_build PREFIX=%{_prefix}
popd

%install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ladspa
pushd source
%make_install PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT install
popd

%files -n ladspa-amb1-plugins
%doc AUTHORS README*
%license COPYING
%{_libdir}/ladspa/*

%changelog
* Mon Jul 26 2021 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-1
- initial spec file
