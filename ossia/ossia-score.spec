# Tag: Tool, Editor, OSC, MIDI, Sequencer
# Type: Standalone
# Category: Tool, MIDI, DAW

%define _lto_cflags %{nil}

%define commit0_example 7205f76dda5e91bc7f5292c8af23b66d0f5a1c02

Name: ossia-score
Version: 3.1.14
Release: 1%{?dist}
Summary: ossia score is a sequencer for audio-visual artists, designed to create interactive shows
URL: https://github.com/OSSIA/score
License: CeCILL License v2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ossia/score/releases/download/v%{version}/ossia.score-%{version}-src.tar.xz
Source1: https://github.com/ossia/score-examples/archive/%{commit0_example}.zip#/ossia-examples-%{commit0_example}.zip

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: unzip
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: boost-devel
BuildRequires: zlib-devel
BuildRequires: llvm-devel
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtscxml-devel
BuildRequires: qt6-qtshadertools-devel
BuildRequires: qt6-qtserialport-devel
BuildRequires: qt6-qtwebsockets-devel
BuildRequires: qt6-qtbase-private-devel
BuildRequires: libxkbcommon-devel
BuildRequires: sqlite-devel
BuildRequires: lame-devel
BuildRequires: ffmpeg-devel
BuildRequires: portmidi-devel
BuildRequires: portaudio-devel
BuildRequires: lilv-devel
BuildRequires: suil-devel
BuildRequires: freetype-devel
BuildRequires: avahi-compat-libdns_sd-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: fftw-devel
BuildRequires: libsndfile-devel
BuildRequires: desktop-file-utils

Requires: faust-stdlib

%description
ossia score is a sequencer for audio-visual artists, designed to create interactive shows

%package examples
Summary: Examples for %{name}.
Requires: %{name}

%description examples
Examples for %{name}.

%prep
%autosetup -n %{name}-%{version}

unzip %{SOURCE1}

sed -i -e "1i #include <QWidget>" src/plugins/score-plugin-gfx/Gfx/Filter/PreviewWidget.hpp

%build

%set_build_flags
export CXXFLAGS="-include optional -include stdexcept $CXXFLAGS"

%cmake -DCMAKE_BUILD_TYPE=RELEASE
%cmake_build

%install

%cmake_install

# Cleanup
rm -rf %{buildroot}/usr/lib/*.a
rm -rf %{buildroot}/usr/lib/cmake/
rm -rf %{buildroot}/%{_libdir}/*.a
rm -rf %{buildroot}/%{_libdir}/cmake/mimalloc-2.0/
rm -rf %{buildroot}/%{_libdir}/mimalloc-2.0/
rm -rf %{buildroot}/%{_includedir}/
rm -rf %{buildroot}/%{_datadir}/

# Install examples
install -m 755 -d %{buildroot}/%{_datadir}/ossia/examples/
cp -r score-examples-%{commit0_example}/* %{buildroot}/%{_datadir}/ossia/examples/

%files
%doc INSTALL.md README.md AUTHORS
%license LICENSE.txt
%{_bindir}/*

%files examples
%{_datadir}/ossia/examples/*

%changelog
* Mon Apr 15 2024 Yann Collette <ycollette.nospam@free.fr> - 3.1.14-2
- update to version 3.1.14-2

* Tue Feb 06 2024 Yann Collette <ycollette.nospam@free.fr> - 3.1.13-2
- update to version 3.1.13-2

* Sat Jun 24 2023 Yann Collette <ycollette.nospam@free.fr> - 3.1.11-2
- update to version 3.1.11-2

* Sun May 07 2023 Yann Collette <ycollette.nospam@free.fr> - 3.1.10-2
- update to version 3.1.10-2

* Tue Apr 25 2023 Yann Collette <ycollette.nospam@free.fr> - 3.1.9-2
- update to version 3.1.9-2

* Sun Mar 05 2023 Yann Collette <ycollette.nospam@free.fr> - 3.1.8-2
- update to version 3.1.8-2

* Sat Feb 25 2023 Yann Collette <ycollette.nospam@free.fr> - 3.1.7-2
- update to version 3.1.7-2

* Mon Jan 09 2023 Yann Collette <ycollette.nospam@free.fr> - 3.1.6-2
- update to version 3.1.6-2

* Tue Jan 03 2023 Yann Collette <ycollette.nospam@free.fr> - 3.1.5-2
- update to version 3.1.5-2

* Thu Nov 17 2022 Yann Collette <ycollette.nospam@free.fr> - 3.1.4-2
- update to version 3.1.4-2

* Sun Jul 24 2022 Yann Collette <ycollette.nospam@free.fr> - 3.0.12-2
- update to version 3.0.12-2

* Tue Jun 14 2022 Yann Collette <ycollette.nospam@free.fr> - 3.0.11-2
- update to version 3.0.11-2

* Mon Jun 06 2022 Yann Collette <ycollette.nospam@free.fr> - 3.0.10-2
- update to version 3.0.10-2

* Sun May 22 2022 Yann Collette <ycollette.nospam@free.fr> - 3.0.9-2
- update to version 3.0.9-2

* Tue Apr 19 2022 Yann Collette <ycollette.nospam@free.fr> - 3.0.8-2
- update to version 3.0.8-2

* Mon Apr 18 2022 Yann Collette <ycollette.nospam@free.fr> - 3.0.7-2
- update to version 3.0.7-2

* Thu Mar 24 2022 Yann Collette <ycollette.nospam@free.fr> - 3.0.6-2
- update to version 3.0.6-2

* Wed Mar 09 2022 Yann Collette <ycollette.nospam@free.fr> - 3.0.5-2
- update to version 3.0.5-2

* Thu Feb 24 2022 Yann Collette <ycollette.nospam@free.fr> - 3.0.4-2
- update to version 3.0.4-2

* Sun Jan 16 2022 Yann Collette <ycollette.nospam@free.fr> - 3.0.1-2
- update to version 3.0.1-2

* Sun Oct 25 2020 Yann Collette <ycollette.nospam@free.fr> - 2.5.2-2
- fix debug build

* Wed Oct 23 2019 Yann Collette <ycollette.nospam@free.fr> - 2.5.2-1
- initial version of the spec file
