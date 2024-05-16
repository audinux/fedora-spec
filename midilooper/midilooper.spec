# Tag: MIDI
# Type: Standalone
# Category: MIDI

Summary: MIDI Looper
Name: midilooper
Version: 0.0.2.1
Release: 1%{?dist}
URL: https://github.com/supergilbert/midilooper
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-or-later

# ./midilooper-source.sh <tag>
# ./midilooper-source.sh 0.0.2.1

Source0: midilooper.tar.gz
Source1: midilooper-source.sh

Vendor:       Audinux
Distribution: Audinux

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: qt5-qtbase-devel
BuildRequires: freetype-devel
BuildRequires: libglvnd-devel
BuildRequires: glfw-devel
BuildRequires: libconfig-devel
BuildRequires: liblo-devel

%description
MIDI Looper

%prep
%autosetup -n %{name}

sed -i -e "/CMAKE_C_FLAGS_DEBUG/d" CMakeLists.txt
sed -i -e "/CMAKE_CXX_FLAGS_DEBUG/d" CMakeLists.txt
sed -i -e "/CMAKE_C_FLAGS_RELEASE/d" CMakeLists.txt
sed -i -e "/CMAKE_CXX_FLAGS_RELEASE/d" CMakeLists.txt

%build

%set_build_flags

export CXXFLAGS=`echo $CXXFLAGS | sed -e "s/-Werror=maybe-uninitialized//g"`
export CFLAGS=`echo $CFLAGS | sed -e "s/-Werror=maybe-uninitialized//g"`
export CXXFLAGS="-Wno-incompatible-pointer-types $CXXFLAGS"
export CFLAGS="-Wno-incompatible-pointer-types $CFLAGS"

%cmake
%cmake_build

%install

%cmake_install

install -m 755 -d %{buildroot}/%{_mandir}/man1/
install -m 644 src/midilooper.1 %{buildroot}/%{_mandir}/man1/

%files
%doc README.md
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Thu Nov 09 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.2.1-1
- Initial build.
