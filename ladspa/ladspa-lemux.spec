# Status: active
# Tag: Effect
# Type: LADSPA
# Category: Audio, Synthesizer

# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments to toni@links2linux.de

Name: ladspa-lemux
Summary: lemux - LADSPA instrument plugins based on openMSX devices
Version: 0.2
Release: 1%{?dist}
License: GPL-2.0
URL: http://lumatec.be/joost
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ycollet/ladspa-lemux/archive/refs/tags/v%{version}.tar.gz#/lemux-%{version}.tar.gz
Patch0: lemux-0001-remove-int-check.patch
Patch1: lemux-0002-fix-CFLAGS.patch

BuildRequires: gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: ladspa-devel

%description
lemux - LADSPA instrument plugins based on openMSX devices.

%prep
%autosetup -p1 -n ladspa-lemux-%{version}

%build

%set_build_flags
export CFLAGS="-fPIC $CFLAGS"
export CXXFLAGS="-fPIC $CXXFLAGS"

pushd dev/SID/resid
  autoreconf --force --install
  ./configure
  make
popd

%make_build

%install

install -m755 -d %{buildroot}/%{_libdir}/ladspa/
install -m755 gen/lemux.so %{buildroot}/%{_libdir}/ladspa/

%files
%doc FAQ README AUTHORS ChangeLog
%doc gen/scc_presets.txt
%doc contrib/*.ams
%license COPYING GPL
%_libdir/ladspa/*

%changelog
* Wed May 06 2026 Yann Collette <ycollette dot nospam at free.fr> 0.2-1
- initial spec
