# Status: active
# Tag: Jack, Equalizer
# Type: Standalone
# Category: Audio, Effect

Summary: Multichannel equaliser
Name: zita-eq1
Version: 0.3.4
Release: 1%{?dist}
License: GPL
URL: http://kokkinizita.linuxaudio.org/linuxaudio/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: cairo-devel
BuildRequires: libpng-devel
BuildRequires: clthreads-devel
BuildRequires: clxclient-devel
BuildRequires: pkgconfig(jack)
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel

%description
Multichannel equaliser. Features:
* Up to 64 channels.
* 3rd order highpass, 10...320 Hz.
* LF shelf section.
* 3 parametric sections.
* HF shelf section.
* Bypass and makeup gain.
* Fully de-clicked and de-zippered.

The shelf sections have a variable slope. When this is set above
2/3 of the range, the gain will first go in the opposite direction
before going up or down to the set gain. This was a feature of some
of the most famous analog equalisers.

The rotary controls can be set by dragging up/down or left/right,
or by using the mouse wheel. Using shift with the mouse wheel will
provide smaller steps.

%prep
%autosetup

# Force Fedora's optflags
sed -i -e 's|\-O2|%{optflags}|' source/Makefile
sed -i -e 's|\/usr\/local|\/usr|g' source/Makefile

%build

%set_build_flags

export LDFLAGS="`pkg-config --libs-only-L jack` $LDFLAGS"

pushd source
%make_build PREFIX=%{_prefix}
popd

%install

pushd source
%make_install
popd

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/*
%{_datadir}/zita-eq1/

%changelog
* Fri Apr 25 2025 Yann Collette <ycollette.nospam@free.fr> - 0.3.4-1
- initial release
