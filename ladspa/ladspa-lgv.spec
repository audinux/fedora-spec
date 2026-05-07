# Status: active
# Tag: Effect
# Type: LADSPA
# Category: Audio, Effects

# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments to toni@links2linux.de

Name: ladspa-lgv
Summary: Luis Garrido's LADSPA plugin collection
Version: 0.1
Release: 1%{?dist}
License: GPL-2.0
URL: https://sourceforge.net/projects/ladspa-lgv/

Vendor:       Audinux
Distribution: Audinux

Source0: https://sourceforge.net/projects/ladspa-lgv/files/ladspa-lgv/%{version}/ladspa-lgv-plugins-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: ladspa

%description
A set of audio plugins for LADSPA. Includes: monomix.

%prep
%autosetup -n ladspa-lgv-plugins-%{version}

%build

%configure
%make_build

%install

%make_install plugindir=%{buildroot}%{_libdir}/ladspa

%files
%doc AUTHORS ChangeLog COPYING README
%dir %{_libdir}/ladspa
%{_libdir}/ladspa/lgv.so
%{_datadir}/ladspa/rdf/lgv.rdf

%changelog
* Mon Feb 02 2009 Toni Graffy <toni@links2linux.de> - 0.1-0.pm.1
- initial build 0.1
