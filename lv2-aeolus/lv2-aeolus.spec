# Status: active
# Tag: Organ, Jack, Alsa
# Type: Standalone
# Category: Audio, Synthesizer

Name: lv2-aeolus
Summary: A synthesized pipe organ with LV2 version
Version: 1.0.0
Release: 1%{?dist}
License: GPL-2.0-or-later
URL: https://github.com/ycollet/aeolus
ExclusiveArch: x86_64 aarch64

Source0: https://github.com/ycollet/aeolus/archive/refs/tags/lv2-%{version}.tar.gz#/%{name}-%{version}.tar.gz

Vendor:       Audinux
Distribution: Audinux


BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: lv2-devel
BuildRequires: zita-alsa-pcmi-devel
BuildRequires: clthreads-devel
BuildRequires: clxclient-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: readline-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: desktop-file-utils

%description
lv2-aeolus is a LV2 version of the famous Aeolus organ.
Aeolus is a synthesised (i.e. not sampled) pipe organ emulator that
should be good enough to make an organist enjoy playing it. It is a
software synthesiser optimised for this job, with possibly hundreds of
controls for each stop, that enable the user to "voice" his
instrument. Main features of the default instrument: three manuals and
one pedal, five different temperaments, variable tuning, IDI control
of course, stereo, surround or Ambisonics output, flexible audio
controls including a large church reverb.

%prep
%autosetup -n aeolus-lv2-%{version}

%build

%cmake
%cmake_build

%install

%cmake_install

# Cleanup

rm -rf %{buildroot}/%{_bindir}/
rm -rf %{buildroot}/%{_libdir}/*.so
rm -rf %{buildroot}/%{_sysconfdir}/
rm -rf %{buildroot}/%{_datadir}/applications/aeolus.desktop

%files
%{_libdir}/lv2/*

%changelog
* Thu Jul 16 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-2
- initial build
