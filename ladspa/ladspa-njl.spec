# Status: active
# Tag: Effect
# Type: LADSPA
# Category: Audio, Effects

# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments to toni@links2linux.de

%global commit0 bd0244bfd7b6d1de18190c75bfc8da3da938372a

Name: ladspa-njl
Summary: NJL LADSPA plugin
Version: 0.2.1
Release: 1%{?dist}
License: GPL-2.0
URL: http://users.ecs.soton.ac.uk/njl98r/code/audio/

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ycollet/ladspa-njl/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz

BuildRequires: gcc-c++
BuildRequires: ladspa

%description
The package contains the njl LADSPA plugins:

noise_1921.so
1921 IEEE Single Precision Noise
  Sign, Mantissa and Exponent are fed by a pseudo-random number generator
  resulting in a sort of crackling white noise with 0dB peak amplitude.

noise_1922.so
1922 Integer Noise
  White noise with variable precision from a pseudo-random number generator

eir_1923.so
1923 Experiments in Representation
  Simulate half-precision floating point and other representations

risset_1924.so
1924 Continuos Risset Scales
  Popular aural illusion in which a sound appears to continuously increase
  (or decrease) in pitch.

%prep
%autosetup -n %{name}-%{commit0}

%build

%make_build

%install

install -m755 -d %{buildroot}/%{_libdir}/ladspa/
install -m755 *.so %{buildroot}/%{_libdir}/ladspa/

%files
%doc PLUGINS README
%license COPYING
%{_libdir}/ladspa/*

%changelog
* Thu May 07 2026 Yann Collette <ycollette.nospam@free.fr> - 0.2.1-1
- initial fedora version
