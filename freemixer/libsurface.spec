# SPDX-License-Identifier: GPL-3.0-or-later
# libsurface, the device behaviour of motorised control surfaces: the motor-fader policy, touch,
# the bank window, the board shadow and its replay, meter steps and ring rendering; and its
# DigiNet module, libsurface-diginet (a Control|24 over libdiginet), with surface-c24; and its
# Mackie module, libsurface-mackie (an X-Touch over libmackie).
#
# rpmbuild --without diginet --without mackie builds the core alone.
%bcond_without diginet
%bcond_without mackie
Name:           libsurface
Version:        0.2.1
# The soname's major. rpm derives this package's provides and every consumer's requires from it.
# It copies SURFACE_ABI of include/surface/surface.h, and tests/conformance-packaging.sh (in make
# test) refuses a copy that disagrees.
%global abi 0
# The DigiNet module's soname major: SURFACE_DIGINET_ABI of include/surface/surface_diginet.h, held
# to this copy by the same check.
%global dabi 0
# The Mackie module's: SURFACE_MACKIE_ABI of include/surface/surface_mackie.h, the same way.
%global mabi 0
Release:        1%{?dist}
Summary:        Motor faders, touch and banks for any motorised control surface

License:        GPL-3.0-or-later
URL:            https://github.com/FreeMixer/libsurface
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  git-core
BuildRequires:  pkgconf-pkg-config
%if %{with diginet}
# the desk mux (diginet/transport/diginet_mux.h) is in libdiginet from 0.1.4
BuildRequires:  pkgconfig(libdiginet-transport) >= 0.1.4
%endif
%if %{with mackie}
BuildRequires:  pkgconfig(libmackie) >= 0.1.0
%endif

%description
libsurface is the device behaviour of a motorised control surface, written once in C for every
surface and every host: a motor-fader policy that never fights the hand, touch with a self-heal
for a lost release and a debounce for a chattering sensor, the bank window, a shadow of the
whole board replayed when a device comes back blank, meter steps with hysteresis, LED ring
rendering. It speaks no wire and knows no mixing semantics: a backend encodes, a host names what each strip shows.

%package devel
Summary:        Development files for libsurface
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The header and the pkg-config file (libsurface) for building a control-surface host or backend
on libsurface.

%if %{with diginet}
%package -n libsurface-diginet
Summary:        A Digidesign Control|24 under libsurface, over DigiNet
Requires:       %{name}%{?_isa} = %{version}-%{release}
# the soname alone does not say it: the desk mux is in libdiginet from 0.1.4
Requires:       libdiginet%{?_isa} >= 0.1.4

%description -n libsurface-diginet
libsurface-diginet is libsurface's DigiNet module: a Digidesign Control|24 driven by libsurface's
device behaviour over libdiginet's desk mux. One listener hears every interface and every desk;
each desk the host attaches is a libsurface surface whose board is replayed on every new
session, with its faders, keys, V-Pots, jog, LEDs, rings, meters, scribbles and counter mapped
to and from the wire, and a deaf desk or one owned by another host raised as a warning.

%package -n libsurface-diginet-devel
Summary:        Development files for libsurface-diginet
Requires:       libsurface-diginet%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description -n libsurface-diginet-devel
The header and the pkg-config file (libsurface-diginet) for building a host that drives a
Control|24 through libsurface.

%package -n surface-c24
Summary:        Drive a Control|24 through libsurface, with no privilege of its own
Requires:       libsurface-diginet%{?_isa} = %{version}-%{release}
# the packet socket comes from diginet-packet-helper
Requires:       diginet-tools

%description -n surface-c24
surface-c24 takes its packet socket from diginet-packet-helper, attaches the first Control|24
that announces on any interface, labels its strips, mirrors each fader on its meter, prints
every event, and takes writes (scribbles, LEDs, fader targets, rings) from a FIFO.
%endif

%prep
%autosetup -n %{name}-%{version}

%if %{with mackie}
%package -n libsurface-mackie
Summary:        An MCU surface such as the Behringer X-Touch under libsurface

%description -n libsurface-mackie
libsurface-mackie is libsurface's Mackie module: one surface per MCU device, the X-Touch's geometry,
touch from the touch notes and the host-connection handshake, driven by libsurface's device
behaviour with libmackie as its codec. The MIDI transport stays the host's: encoded messages go to a
write callback and received ones come in by call. It owns no port, thread or clock.

%package -n libsurface-mackie-devel
Summary:        Development files for libsurface-mackie
Requires:       libsurface-mackie%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(libmackie) >= 0.1.0

%description -n libsurface-mackie-devel
The header and the pkg-config file (libsurface-mackie) for building a host that drives an MCU
surface through libsurface.
%endif

%build
# DIGINET=yes: the module or a failed build, never a silent skip; DIGINET=no: the core alone.
# SURFACE_C24_HELPER empty: surface-c24 finds diginet-packet-helper in PATH.
%global mkflags DIGINET=%{?with_diginet:yes}%{!?with_diginet:no} MACKIE=%{?with_mackie:yes}%{!?with_mackie:no} SURFACE_C24_HELPER=
%make_build CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}" %{mkflags} shared

%install
# not %%make_install: it names the `install` target (the static archives) as well
make DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir} INCDIR=%{_includedir} \
    BINDIR=%{_bindir} MANDIR=%{_mandir} %{mkflags} install-shared

%check
make CFLAGS="%{optflags}" %{mkflags} test

%files
%license LICENSE
%doc README.md
%{_libdir}/libsurface.so.%{version}
%{_libdir}/libsurface.so.%{abi}

%files devel
%doc BUILDING.md
%dir %{_includedir}/surface
%{_includedir}/surface/surface.h
%{_libdir}/libsurface.so
%{_libdir}/pkgconfig/libsurface.pc

%if %{with diginet}
%files -n libsurface-diginet
%license LICENSE
%{_libdir}/libsurface-diginet.so.%{version}
%{_libdir}/libsurface-diginet.so.%{dabi}

%files -n libsurface-diginet-devel
%{_includedir}/surface/surface_diginet.h
%{_includedir}/surface/surface_diginet_keys.h
%{_libdir}/libsurface-diginet.so
%{_libdir}/pkgconfig/libsurface-diginet.pc

%files -n surface-c24
%license LICENSE
%{_bindir}/surface-c24
%{_mandir}/man1/surface-c24.1*
%endif

%if %{with mackie}
%files -n libsurface-mackie
%license LICENSE
%{_libdir}/libsurface-mackie.so.%{version}
%{_libdir}/libsurface-mackie.so.%{mabi}

%files -n libsurface-mackie-devel
%{_includedir}/surface/surface_mackie.h
%{_libdir}/libsurface-mackie.so
%{_libdir}/pkgconfig/libsurface-mackie.pc
%endif

%changelog
* Sat Oct 31 2026 Pau Aliagas <linuxnow@gmail.com> - 0.2.1-1
- A desk that returns under another name no longer crashes the host.
* Fri Oct 30 2026 Pau Aliagas <linuxnow@gmail.com> - 0.2.0-1
- The Mackie module, libsurface-mackie: an MCU surface such as the X-Touch
  under libsurface over libmackie, the MIDI transport the host's. The
  handshake brings the surface online and replays the board and the
  assignment display.
- The core gains surface_ring_code() with its optional ring_code op,
  surface_fader_paint_strip(), surface_fader_is_report(),
  surface_touch_reset() and surface_meters_reset(). A suspended target's
  cap moves go up and leave the motor state alone, and its release drives
  nothing.
- The Control|24 tests follow libdiginet 0.1.4: ONLINE on the a0, ONLINE
  again on the first e1, one board replay after it. libdiginet 0.1.4 is
  now the floor.
* Thu Oct 29 2026 Pau Aliagas <linuxnow@gmail.com> - 0.1.0-1
- First release: the device behaviour core, ported from a TypeScript
  X-Touch driver with its tests. The motor-fader policy (touch flag plus
  target, an implicit-touch window, the echo guard, a trailing coalesce),
  touch with a self-heal and a release debounce, the bank window, the
  board shadow and its replay, meter steps, ring rendering, and the
  Control|24's release debounce and set-point echo. Caller time, no
  threads.
- The DigiNet module, libsurface-diginet: a Control|24 under libsurface
  over libdiginet's desk mux, one surface per attached desk, the board
  replayed on every session, DESK_DEAF and FOREIGN as warnings; and
  surface-c24, which drives a desk with no privilege of its own.
