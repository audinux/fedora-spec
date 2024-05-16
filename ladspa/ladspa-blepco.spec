# Tag: OSC
# Type: LADSPA
# Category: Audio, Synthesizer

Name: ladspa-blepco
Version: 0.1.0
Release: 1%{?dist}
Summary: a LADSPA plugin library containing three anti-aliased, minBLEP-based, hard-sync-capable oscillator plugins
License: GPL-2.0+
URL: https://www.sirlab.de/linux/download
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: http://smbolton.com/linux/blepvco-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: ladspa-devel

%description
a LADSPA plugin library containing three anti-aliased, minBLEP-based,
hard-sync-capable oscillator plugins. The oscillators are intended to
be used with modular synthesis systems, such as Alsa Modular Synth.

%prep
%autosetup -n blepvco-%{version}

%build
%make_build

%install

install -m 755 -d %{buildroot}/%{_libdir}/ladspa/
install -m 755 blepvco.so %{buildroot}/%{_libdir}/ladspa/

%files
%doc README
%license COPYING
%{_libdir}/ladspa

%changelog
* Mon Nov 28 2022 Yann Collette <ycollette dot nospam at free.fr> 0.1.0-1
- initial spec
