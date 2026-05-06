# Status: active
# Tag: Effect
# Type: LADSPA
# Category: Audio, Effects

# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments to toni@links2linux.de

%global commit0 0b2ba9796174a027fe447d2316718e53e0ad871d

Name: ladspa-clipper
Summary: Clipper LADSPA plugin - Hard clipping, without any aliasing protection
Version: 1.0
Release: 1%{?dist}
License: GPL-2.0
URL: http://quitte.de/dsp/

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ycollet/ladspa-clipper/archive/%{commit0}.tar.gz#/clipper-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: ladspa-devel

%description
Hard clipping, without any aliasing protection. Amplify the
incoming signal by 30 dB and more to get good, harsh distortion.

%prep
%autosetup -n ladspa-clipper-%{commit0}

%build

%make_build

%install

install -m 755 -d %{buildroot}/%{_libdir}/ladspa/

%make_install DESTDIR=%{buildroot} INSTALL_PATH=%{_libdir}/ladspa/

%files
%{_libdir}/ladspa/*

%changelog
* Tue May 05 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- initial spec
