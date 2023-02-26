# Tag: Jack
# Type: Standalone
# Category: Audio

Name:    sonobus
Version: 1.6.2
Release: 3%{?dist}
Summary: A peer to peer audio application
License: GPLv2+
URL:     https://github.com/essej/sonobus

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/essej/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: opus-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: openssl-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: JUCE
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: desktop-file-utils

%description
SonoBus is an easy to use application for streaming high-quality,
low-latency peer-to-peer audio between devices over the internet or a local network.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags

export HOME=`pwd`
mkdir -p .vst3

%cmake -DCMAKE_CXX_FLAGS="-include utility -fPIC"
%cmake_build 

%install 

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -p %__cmake_builddir/SonoBus_artefacts/Standalone/sonobus %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -ra %__cmake_builddir/SonoBus_artefacts/VST3/SonoBus.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/SonoBusInstrument.vst3/
cp -ra %__cmake_builddir/SonoBusInst_artefacts/VST3/SonoBusInstrument.vst3 %{buildroot}/%{_libdir}/vst3/

mkdir -p %{buildroot}/%{_datadir}/applications
cp  linux/sonobus.desktop %{buildroot}/%{_datadir}/applications/sonobus.desktop
chmod +x %{buildroot}/%{_datadir}/applications/sonobus.desktop

mkdir -p %{buildroot}/%{_datadir}/pixmaps
cp  images/sonobus_logo@2x.png %{buildroot}/%{_datadir}/pixmaps/sonobus.png

cp deps/aoo/LICENSE LICENSE-aoo
cp deps/ff_meters/LICENSE.md LICENSE-ff_meters.md
cp deps/juce/LICENSE.md LICENSE-juce.md

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/sonobus.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/sonobus.desktop

%files
%doc README.md
%license LICENSE LICENSE-aoo LICENSE-ff_meters.md LICENSE-juce.md
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Sun Feb 26 2023 Yann Collette <ycollette.nospam@free.fr> - 1.6.2-3
- update to 1.6.2-3

* Wed Jan 18 2023 Yann Collette <ycollette.nospam@free.fr> - 1.6.1-3
- update to 1.6.1-3

* Sat Jan 07 2023 Yann Collette <ycollette.nospam@free.fr> - 1.6.0-3
- update to 1.6.0-3

* Mon Apr 04 2022 Yann Collette <ycollette.nospam@free.fr> - 1.5.2-3
- update to 1.5.2-3

* Sun Jan 16 2022 Yann Collette <ycollette.nospam@free.fr> - 1.4.9-3
- update to 1.4.9-3

* Thu Jan 13 2022 Yann Collette <ycollette.nospam@free.fr> - 1.4.8-3
- update to 1.4.8-3

* Sat Jun 05 2021 Yann Collette <ycollette.nospam@free.fr> - 1.4.6-3
- update to 1.4.6-3

* Thu Apr 15 2021 Yann Collette <ycollette.nospam@free.fr> - 1.4.5-3
- update to 1.4.5-3

* Wed Apr 14 2021 Yann Collette <ycollette.nospam@free.fr> - 1.4.4-3
- update to 1.4.4-3

* Fri Apr 02 2021 Yann Collette <ycollette.nospam@free.fr> - 1.4.3-3
- update to 1.4.3-3

* Thu Mar 25 2021 Yann Collette <ycollette.nospam@free.fr> - 1.4.2-3
- update to 1.4.2-3

* Tue Mar 23 2021 Yann Collette <ycollette.nospam@free.fr> - 1.4.1-3
- update to 1.4.1-3

* Tue Mar 23 2021 Yann Collette <ycollette.nospam@free.fr> - 1.4.0-3
- update to 1.4.0-3

* Fri Mar 12 2021 Yann Collette <ycollette.nospam@free.fr> - 1.3.2-2
- Fix invalid binaries

* Sun Feb 21 2021 Yann Collette <ycollette.nospam@free.fr> - 1.3.2-1
- Initial spec file
