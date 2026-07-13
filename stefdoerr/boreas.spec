# Status: active
# Tag: Plugin
# Type: Plugin, LV2, MODGUI
# Category: Audio, Effect

Name: boreas
Version: 0.0.2
Release: 1%{?dist}
Summary: A MOD freeze plugin
License: GPL-2.0-or-later
URL: https://github.com/stefdoerr/boreas
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./stefdoerr-source.sh <PROJECT> <TAG>
#        ./stefdoerr-source.sh boreas v0.0.2

Source0: boreas.tar.gz
Source1: stefdoerr-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: pkgconfig(jack)
BuildRequires: liblo-devel

%description
Freeze / infinite-sustain pedal LV2 plugin.
Capture a moment of sound and hold it as a smooth, endless drone — stack layers, slide them in by pitch,
shape the tone, and add organic movement.
Built with the DISTRHO Plugin Framework (DPF) as a mono-in / mono-out LV2 plugin.
Boreas freezes by spectral resynthesis, not looping: it analyses the captured sound into a bank of
steady sine oscillators and plays those, so the sustain is dead steady with no loop seam, no choppiness,
and no buzz.

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-2.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n %{name}

%build

%make_build SKIP_STRIPPING=true

%install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -ra bin/boreas.lv2 %{buildroot}/%{_libdir}/lv2/

%files
%doc README.md

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Tue Jun 09 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.2-1
- Initial build
