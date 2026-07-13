# Status: active
# Tag: Plugin
# Type: Plugin, LV2, MODGUI
# Category: Audio, Effect

Name: sitar
Version: 0.0.6
Release: 1%{?dist}
Summary: Simple LADSPA/LV2/CLAP vocoder plugin using DPF
License: GPL-2.0-or-later
URL: https://github.com/stefdoerr/sitar
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./stefdoerr-source.sh <PROJECT> <TAG>
#        ./stefdoerr-source.sh sitar v0.0.6

Source0: sitar.tar.gz
Source1: stefdoerr-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: pkgconfig(jack)
BuildRequires: liblo-devel

%description
A sympathetic-resonance LV2 pluginfor any standard LV2 host.
Drives up to 48 tuned feedback comb-filter strings from the input signal to produce sitar-like ringing,
microtonal accompaniment — the same idea as a real sitar's taraf (sympathetic strings beneath the frets).

What it does:
Send a guitar, synth, voice, or anything else through the plugin. Each internal "string" is a tuned
resonator that rings whenever the input has energy at (or near) the string's frequency or one of its
harmonics.
The result is a shimmering, slowly-decaying halo of pitched overtones that follow whatever you play,
harmonized against the scale you pick. The 48-string bank spans roughly four octaves above the root,
and N STRINGS cursors over how many of them ring at once.

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
cp -ra bin/sitar.lv2 %{buildroot}/%{_libdir}/lv2/

%files
%doc README.md

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Tue Jun 09 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.6-1
- Initial build
