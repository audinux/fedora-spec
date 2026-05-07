# Status: active
# Tag: Effect
# Type: LADSPA
# Category: Audio, Effects

# Copyright (c) 2010 oc2pus
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments to toni@links2linux.de

Name: ladspa-bs2b
Summary: Bauer stereophonic-to-binaural DSP LADSPA plugins
Version: 0.9.1
Release: 1%{?dist}
License: GPL-2.0
URL: https://bs2b.sourceforge.net/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://sourceforge.net/projects/bs2b/files/plugins/LADSPA%20plugin/%{version}/ladspa-bs2b-%{version}.tar.bz2

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: libbs2b-devel
BuildRequires: ladspa-devel

%description
The Bauer stereophonic-to-binaural DSP (bs2b) library and plugins is
designed to improve headphone listening of stereo audio records.

Recommended for headphone prolonged listening to disable superstereo
fatigue without essential distortions.

This package cntains the ladspa-plugin for bs2b.

%prep
%autosetup -n %{name}-%{version}

%build

%configure
%make_build

%install

%make_install

%files
%doc AUTHORS COPYING THANKS
%dir %{_libdir}/ladspa
%{_libdir}/ladspa/*.so

%changelog
* Tue May 05 2026 Yann Collette <ycollette.nospam@free.fr> - 0.9.1-1
- initial fedora version

* Sun Apr 11 2010 Toni Graffy <toni@links2linux.de> - 0.9.1-0.pm.1
- initial build 0.9.1
