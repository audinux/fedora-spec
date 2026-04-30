# Status: active
# Tag: Effect
# Type: LADSPA
# Category: Audio, Effects

# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments to toni@links2linux.de

Name: ladspa-aweight
Summary: aweight LADSPA plugin
Version: 0.3.0
Release: 1%{?dist}
License: GPL-2.0
URL: http://users.skynet.be/solaris/linuxaudio/downloads

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ycollet/aweight/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: ladspa-aweight-0001-fix-makefile.patch

BuildRequires: gcc-c++
BuildRequires: pkgconfig(jack)
BuildRequires: ladspa-devel

%description
The package contains the aweight LADSPA plugins.

%prep
%autosetup -p1 -n aweight-%{version}

%build

%make_build awplug.so

%install

%__install -dm 755 %{buildroot}/%{_libdir}/ladspa/
%__install -m 755 -c *.so %{buildroot}/%{_libdir}/ladspa/

%files
%doc *.png
%dir %{_libdir}/ladspa
%{_libdir}/ladspa/*

%changelog
* Wed Apr 29 2026 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-1
- update to 0.3.0-1 - fist fedora version

* Sun Sep 16 2007 Toni Graffy <toni@links2linux.de> - 0.3.0-0.pm.1
- splitt-off from ladspa package
