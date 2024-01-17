Name:    osmid
Version: 0.8.0
Release: 2%{?dist}
Summary: osmid is a tool to bridge MIDI and OSC
URL:     https://github.com/llloret/osmid
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/llloret/osmid/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: libX11-devel
BuildRequires: patchelf

%description
osmid aims to provide a lightweight, portable, easy to use tool to
convert MIDI to OSC and OSC to MIDI.

It is the software handling the communication with MIDI devices in Sonic Pi.

osmid is divided in 2 tools:
 * m2o: MIDI to OSC conversion
 * o2m: OSC to MIDI conversion

Having two separate tools follows Unix ideas of having a number of smaller
standalone tools instead of bigger monolithic ones. Since some projects might
want to use just one direction for the conversion, it makes sense to keep this separation.

%prep
%autosetup -n %{name}-%{version}

%build

%cmake
%cmake_build

%install

%cmake_install

install -m 755 -d %{buildroot}/%{_libdir}/%{name}/
cp %{__cmake_builddir}/external_libs/oscpack_1_1_0/liboscpack.so %{buildroot}/%{_libdir}/%{name}/

patchelf --set-rpath '$ORIGIN/../%{_lib}/%{name}/' %{buildroot}/%{_bindir}/m2o
patchelf --set-rpath '$ORIGIN/../%{_lib}/%{name}/' %{buildroot}/%{_bindir}/o2m

%files
%doc README.md
%license LICENSE.md
%{_bindir}/*
%{_libdir}/%{name}/*

%changelog
* Thu Apr 14 2022 Yann Collette <ycollette.nospam@free.fr> - 0.7.0-2
- Fix - set rpath to liboscpack.

* Fri Nov 06 2020 Yann Collette <ycollette.nospam@free.fr> - 0.7.0-1
- Initial spec file
