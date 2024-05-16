# Tag: Audio, Tool, Editor
# Type: Standalone
# Category: Audio, Tool

Name: shuriken
Version: 0.5.2
Release: 2%{?dist}
Summary: beat slicer
License: GPL-2.0-only
URL: https://github.com/rock-hopper/shuriken/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/rock-hopper/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: aubio-devel
BuildRequires: liblo-devel
BuildRequires: rubberband-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: libuuid-devel
BuildRequires: qt5-qtbase-devel

%description
Shuriken is an open source beat slicer which harnesses the power of aubio's onset detection algorithms and Rubber Band's time stretching capabilities.
A simple Qt interface makes it easy to slice up drum loops, assign individual drum hits to MIDI keys, and change the tempo of loops in real-time.
The JUCE library takes care of handling audio and MIDI behind the scenes.

%prep
%autosetup

%ifarch aarch64
sed -i -e "/-msse2/d" Shuriken.pro
sed -i -e s"/-msse//g" Shuriken.pro
%endif

%build

mkdir -p lib
cd src/SndLibShuriken
%configure --without-audio --without-s7
%make_build
mv -v libsndlib_shuriken.a ../../lib/

cd ../../

%qmake_qt5 ./Shuriken.pro
%make_build

%install

mkdir -p %{buildroot}/%{_bindir}/
install -m 755 -p release/shuriken %{buildroot}/%{_bindir}/shuriken

%files
%doc README.md LICENSE TODO
%{_bindir}/shuriken

%changelog
* Tue May 5 2020 Yann Collette <ycollette.nospam@free.fr> - 0.5.2-2
- update for Fedora 32

* Mon May 06 2019 L.L.Robinson <baggypants@fedoraproject.org> - 0.5.2-2
- qlib changes

* Fri Oct 12 2018 L.L.Robinson <baggypants@fedoraproject.org> - 0.5.2-1
- new version

* Thu Dec 08 2016 L.L.Robinson <baggypants@fedoraproject.org> - 0.5.1-2
- added compilation fix patch

* Tue Sep 22 2015 L.L.Robinson <baggypants@fedoraproject.org> - 0.5-1
- initial-version

