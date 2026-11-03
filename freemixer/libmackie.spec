# SPDX-License-Identifier: GPL-3.0-or-later
# libmackie, the Mackie Control (MCU) protocol of motorised MIDI control surfaces such as the
# Behringer X-Touch, as a codec with no I/O.
Name:           libmackie
Version:        0.1.0
# The soname's major. rpm derives this package's provides and every consumer's requires from
# it. It copies MACKIE_ABI of include/mackie/mackie.h, and tests/conformance-packaging.sh (in
# make test) refuses a copy that disagrees.
%global abi 0
Release:        1%{?dist}
Summary:        Encode and decode the Mackie Control protocol of MIDI control surfaces

License:        GPL-3.0-or-later
URL:            https://github.com/FreeMixer/libmackie
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  git-core
BuildRequires:  pkgconf-pkg-config

%description
libmackie speaks Mackie Control (MCU), the MIDI protocol of motorised control surfaces such
as the Behringer X-Touch: motor faders, buttons and their lamps, V-Pots and their LED rings,
meters, the scribble strips and their backlights, the seven-segment displays, the jog wheel
and the host-connection handshake.

It is a codec and nothing else: pure functions over byte buffers, with no MIDI port, no
clock, no thread and no allocation. The host carries the bytes over whatever MIDI transport
it already owns.

%package devel
Summary:        Development files for libmackie
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and the pkg-config file (libmackie) for building programs that drive a Mackie
Control surface.

%prep
%autosetup -n %{name}-%{version}

%build
%make_build CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}" shared

%install
# not %%make_install: it names the `install` target (the static archive) as well
make DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir} INCDIR=%{_includedir} install-shared

%check
make CFLAGS="%{optflags}" test

%files
%license LICENSE
%doc README.md
%{_libdir}/libmackie.so.%{version}
%{_libdir}/libmackie.so.%{abi}

%files devel
%doc BUILDING.md
%dir %{_includedir}/mackie
%{_includedir}/mackie/*.h
%{_libdir}/libmackie.so
%{_libdir}/pkgconfig/libmackie.pc

%changelog
* Thu Oct 29 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.0-1
- First release: the Mackie Control codec ported from the TypeScript X-Touch
  adapter, byte for byte: faders, buttons and lamps, V-Pots and rings, the jog
  wheel, meters, scribble strips and backlights, the seven-segment displays,
  the device reset and the host-connection handshake. Held to golden bytes
  generated from the TypeScript encoders and to the handshake captured live
  on an X-Touch.
