# Tag: Jack, MIDI
# Type: Standalone
# Category: Audio, DAW

%global debug_package %{nil}
%define _lto_cflags %{nil}

Name:    yabridge
Version: 5.0.1
Release: 6%{?dist}
Summary: A modern and transparent way to use Windows VST2 and VST3 plugins on Linux
License: GPLv2+
URL:     https://github.com/robbert-vdh/yabridge

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/robbert-vdh/yabridge/archive/refs/tags/%{version}.tar.gz#/yabridge-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: meson
BuildRequires: git
BuildRequires: rust
BuildRequires: cargo
BuildRequires: cmake
BuildRequires: boost-devel
BuildRequires: lv2-devel
BuildRequires: lilv-devel
BuildRequires: suil-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: wine-devel
BuildRequires: boost-devel
BuildRequires: libxcb-devel
BuildRequires: libxcb-devel(x86-32)
BuildRequires: glibc-devel(x86-32)
BuildRequires: wine-devel(x86-32)
BuildRequires: libstdc++-devel(x86-32)
BuildRequires: dbus-devel
BuildRequires: gulrak-filesystem-devel

%description
Yet Another way to use Windows VST plugins on Linux.
Yabridge seamlessly supports using both 32-bit and 64-bit
Windows VST2 and VST3 plugins in a 64-bit Linux VST host as
if they were native VST2 and VST3 plugins, with optional
support for plugin groups to enable inter-plugin communication
for VST2 plugins and quick startup times.
Its modern concurrent architecture and focus on transparency
allows yabridge to be both fast and highly compatible, while
also staying easy to debug and maintain.

%prep
%autosetup -n %{name}-%{version}

%build

%meson --cross-file=cross-wine.conf \
    --buildtype=release \
    --wrap-mode=default \
    -Dbitbridge=true

%meson_build

pushd tools/yabridgectl
cargo build --release
popd

%install

install -dm755 %{buildroot}%{_bindir}/
install -dm755 %{buildroot}%{_libdir}/

install %{_vpath_builddir}/yabridge-host.exe %{buildroot}%{_bindir}/
install %{_vpath_builddir}/yabridge-host.exe.so %{buildroot}%{_bindir}/
install %{_vpath_builddir}/yabridge-host-32.exe %{buildroot}%{_bindir}/
install %{_vpath_builddir}/yabridge-host-32.exe.so %{buildroot}%{_bindir}/

install %{_vpath_builddir}/libyabridge-vst2.so %{buildroot}%{_libdir}/
install %{_vpath_builddir}/libyabridge-chainloader-vst2.so %{buildroot}%{_libdir}/

install %{_vpath_builddir}/libyabridge-vst3.so %{buildroot}%{_libdir}/
install %{_vpath_builddir}/libyabridge-chainloader-vst3.so %{buildroot}%{_libdir}/

install %{_vpath_builddir}/libyabridge-clap.so  %{buildroot}%{_libdir}/
install %{_vpath_builddir}/libyabridge-chainloader-clap.so %{buildroot}%{_libdir}/

# install tool
install tools/yabridgectl/target/release/yabridgectl %{buildroot}%{_bindir}/

%files
%doc CHANGELOG.md README.md
%license COPYING
%{_bindir}/*
%{_libdir}/*

%changelog
* Mon Nov 14 2022 Yann Collette <ycollette.nospam@free.fr> - 5.0.1-6
- update to 5.0.1-6

* Thu Nov 03 2022 Yann Collette <ycollette.nospam@free.fr> - 5.0.0-6
- update to 5.0.0-6 - add clap

* Wed Nov 02 2022 Yann Collette <ycollette.nospam@free.fr> - 5.0.0-5
- update to 5.0.0-5

* Sat Jul 30 2022 Yann Collette <ycollette.nospam@free.fr> - 4.0.2-5
- update to 4.0.2-5 - add 32 bridge

* Wed Jul 27 2022 Yann Collette <ycollette.nospam@free.fr> - 4.0.2-4
- update to 4.0.2-4 - fix installation

* Mon Jun 27 2022 Yann Collette <ycollette.nospam@free.fr> - 4.0.2-3
- update to 4.0.2-3

* Mon Jun 27 2022 Yann Collette <ycollette.nospam@free.fr> - 4.0.2-2
- update to 4.0.2-2

* Sun Jun 12 2022 Yann Collette <ycollette.nospam@free.fr> - 4.0.1-2
- update to 4.0.1-2

* Sun Jun 12 2022 Yann Collette <ycollette.nospam@free.fr> - 4.0.0-2
- update to 4.0.0-2

* Sat Mar 26 2022 Vincent Tassy <timetre@free.fr> - 3.8.1-2
- ship yabridgectl
- yabridgectl expects both vst and vst3 libs in the same folder. moving libyabridge-vst3.so to vst folder
- Moved yabridge-{host,group}.exe.so to bin folder, where they are expected by yabridge-{host,group}.exe

* Wed Mar 09 2022 Yann Collette <ycollette.nospam@free.fr> - 3.8.1-1
- update to 3.8.1-1

* Sat Jan 15 2022 Yann Collette <ycollette.nospam@free.fr> - 3.8.0-1
- update to 3.8.0-1

* Thu Oct 21 2021 Yann Collette <ycollette.nospam@free.fr> - 3.7.0-1
- update to 3.7.0-1

* Fri Oct 15 2021 Yann Collette <ycollette.nospam@free.fr> - 3.6.0-1
- update to 3.6.0-1

* Sun Aug 08 2021 Yann Collette <ycollette.nospam@free.fr> - 3.5.2-1
- update to 3.5.2-1

* Sun Aug 01 2021 Yann Collette <ycollette.nospam@free.fr> - 3.5.1-1
- update to 3.5.1-1

* Fri Jul 23 2021 Yann Collette <ycollette.nospam@free.fr> - 3.5.0-1
- update to 3.5.0-1

* Thu Jul 15 2021 Yann Collette <ycollette.nospam@free.fr> - 3.4.0-1
- Initial build
