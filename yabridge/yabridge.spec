# Tag: Jack, MIDI
# Type: Standalone
# Category: Audio, DAW

%global debug_package %{nil}

Name:    yabridge
Version: 3.8.1
Release: 1%{?dist}
Summary: A modern and transparent way to use Windows VST2 and VST3 plugins on Linux
License: GPLv2+
URL:     https://github.com/robbert-vdh/yabridge

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/robbert-vdh/yabridge/archive/refs/tags/%{version}.tar.gz#/yabridge-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: lilv-devel
BuildRequires: suil-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: wine-devel
BuildRequires: boost-devel
BuildRequires: libxcb-devel
BuildRequires: meson
BuildRequires: git

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

# set_build_flags

# -Dwith-bitbridge=true
#    --unity=on --unity-size=1000

meson setup build \
    --cross-file=cross-wine.conf \
    --buildtype=release \
    --libdir=%{_libdir} \
    --bindir=%{_bindir} \
    --datadir=%{_datadir} \
    --mandir=%{_mandir} \
    --prefix=%{_prefix}

ninja -C build

%install

install -dm755 %{buildroot}%{_bindir}
install build/yabridge-{host,group}.exe %{buildroot}%{_bindir}
install -dm755 %{buildroot}%{_libdir}
install build/yabridge-{host,group}.exe.so %{buildroot}%{_libdir}

install -dm755 %{buildroot}%{_libdir}/vst
install build/libyabridge-vst2.so %{buildroot}%{_libdir}/vst
install -dm755 %{buildroot}%{_libdir}/vst3
install build/libyabridge-vst3.so %{buildroot}%{_libdir}/vst3
  
%files
%doc CHANGELOG.md README.md
%license COPYING
%{_bindir}/*
%{_libdir}/*.so
%{_libdir}/vst/*
%{_libdir}/vst3/*

%changelog
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
