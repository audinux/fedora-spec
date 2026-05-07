# Status: active
# Tag: Effect
# Type: LADSPA
# Category: Audio, Effects

# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments to toni@links2linux.de

Name: ladspa-wasp
Summary: LADSPA Wave Sculpting Plugins
Version: 0.1.5
Release: 1%{?dist}
License: GPL-2.0
URL: http://artemiolabs.com/software/wasp/

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ycollet/wasp/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: wasp-docs-0.1.4.tar.bz2

BuildRequires: gcc-c++
BuildRequires: ladspa-devel

%description
WASP stands for 'WAve Sculpting Plugins'. It is a growing collection
of software plugins written according to the LADSPA standard, which
can be used in a very wide range of applications including audio
editors, synthesisers and effect processors. All the processors and
generators in the WASP set include two variants - mono and stereo.

WASP doesn't have any sophisticated plugins (yet), but it does fill
the gap in the variety of currently-available LADSPA sets. The plugins
are pretty simple, but very useful in many situations. For example,
here you will find a non-linear amplifier with various transmission
curves - from round and parabolic to sine and non-linear sine - which
can be used to create a wide variety of interesting and even unique
distortion effects. Also there are some nice plugins like hard
clipping booster and noisifier.

%prep
%autosetup -n wasp-%{version}

%build

%set_build_flags

%make_build

%install

%make_install \
	INSTALL_PATH=%{_libdir}/ladspa

chmod a+x %{buildroot}/%{_libdir}/ladspa/*.so

tar xvfj %{SOURCE1}

%files
%doc AUTHORS ChangeLog LICENSE
%doc wasp-docs-0.1.4/data/* wasp-docs-0.1.4/*.html
%dir %{_libdir}/ladspa
%{_libdir}/ladspa/*

%changelog
* Wed Apr 29 2026 Yann Collette <ycollette dot nospam at free.fr> 0.1.5-1
- update to 0.1.5-1

* Tue Apr 28 2026 Yann Collette <ycollette dot nospam at free.fr> 0.1.4-1
- update to 0.1.4-1 - first Fedora version

* Sun May 20 2012 seife+obs@b1-systems.com
- remove obsolete %%suse_update_libdir to fix Factory build

* Sun Sep 16 2007 toni@links2linux.de
- splitt-off from ladspa package
