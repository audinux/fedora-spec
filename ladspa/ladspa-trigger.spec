# Status: active
# Tag: Effect
# Type: LADSPA
# Category: Audio, Effects

# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments to toni@links2linux.de

%global revision r24
%global commit0 33bb845b0891e3fbbfe4628d1d914548bf504b70

Name: ladspa-trigger
Summary: Trigger LADSPA plugin
Version: 20080510
Release: 1%{?dist}
License: GPL-2.0
URL: https://sourceforge.net/projects/ladspa-trigger/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ycollet/ladspa-trigger/archive/%{commit0}.tar.gz#/ladspa-trigger-code-%{commit0}.tar.gz
Patch0: ladspa-trigger-0001-fix-makefile.patch

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: ladspa-devel
BuildRequires: libsndfile-devel

%description
The package contains the LADSPA trigger plugins.

%prep
%autosetup -p1 -n ladspa-trigger-%{commit0}

%build

%set_build_flags
export CFLAGS="-fPIC $CFLAGS"
export CXXFLAGS="-fPIC $CXXFLAGS"

mkdir plugins

%make_build

%install

install -m755 -d %{buildroot}/%{_libdir}/ladspa/
install -m755 plugins/*.so %{buildroot}/%{_libdir}/ladspa/

install -m755 -d %{buildroot}/%{_datadir}/%{name}/samples/
install -m644 samples/* %{buildroot}/%{_datadir}/%{name}/samples/

%files
%doc COPYING README
%dir %{_libdir}/ladspa
%{_libdir}/ladspa/*
%{_datadir}/%{name}/samples/*

%changelog
* Thu May 07 2026 Yann Collette <ycollette.nospam@free.fr> - 20080510-1
- initial fedora version

* Sat May 10 2008 Toni Graffy <toni@links2linux.de> - 20080510-0.pm.1
- update to 20080510

* Sun Sep 16 2007 Toni Graffy <toni@links2linux.de> - 20070826-0.pm.1
- splitt-off from ladspa package
