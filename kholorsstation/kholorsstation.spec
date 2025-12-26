# Status: active
# Tag: Graphic
# Type: Plugin, Standalone, VST3
# Category: Audio, Tool, Graphic

Name: kholorsstation
Version: 1.26.0
Release: 1%{?dist}
Summary: Live, color-coded spectrogram of your DAW tracks in a single window
License: GPL-3.0-or-later
URL: https://github.com/QuentinFAIDIDE/KholorsStation
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/QuentinFAIDIDE/KholorsStation/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: kholorsstation-0001-fix-cmake-version.patch
Patch1: kholorsstation-0002-devendor-third-parties.patch
Patch2: kholorsstation-0003-fix-exe-path.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: patchelf
BuildRequires: json-devel
BuildRequires: grpc-devel
BuildRequires: grpc-plugins
BuildRequires: protobuf-compiler
BuildRequires: abseil-cpp-devel
BuildRequires: spdlog-devel
BuildRequires: webkit2gtk4.1-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: desktop-file-utils

Requires: license-%{name}

%description
Achieving a perfect mxidown is hard, and there is no silver bullet.
Juggling with multiple analyzer windows is a pain, and it's hard to
see how different tracks are interacting with each other.

Kholors solves this by giving you a single, comprehensive view of your
entire mix's frequency spectrum, inside a window separate from your DAW
that you can run on an adjscent screen or desktop.
It helps you visually identify frequency clashes, tame resonant peaks,
and ultimately make more informed EQ and mixing decisions to achieve a
cleaner, more professional sound.

It's composed of two parts:
* Kholors Station: A standalone desktop application that provides the main visualization.
* Kholors Sink: A lightweight VST3 plugin that you add to tracks in your DAW.

The Sink plugin sends audio, track names, and even your DAW's track
colors to the Station. The result is a color-coded spectrogram where
you can see exactly what's happening in your mix, track by track.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -p1 -n KholorsStation-%{version}

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/src/SinkPlugin/SinkPlugin_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/src/StationApp/StationApp_artefacts/KholorsStation %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
cp res/kholors.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

install -m 755 -d %{buildroot}%{_libdir}/KholorsStation/
install -m 755 %{__cmake_builddir}/src/Utils/libUtils.so %{buildroot}%{_libdir}/KholorsStation/
install -m 755 %{__cmake_builddir}/src/AudioTransport/libAudioTransport.so %{buildroot}%{_libdir}/KholorsStation/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/KholorsStation.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name
Exec=KholorsStation
Icon=Kholors
Comment=Kholors Station
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/KholorsStation.desktop

# Fix rpath
patchelf --set-rpath '$ORIGIN/../%{_lib}/KholorsStation/' %{buildroot}/%{_bindir}/KholorsStation
patchelf --set-rpath '$ORIGIN/../../../../KholorsStation/' `find %{buildroot}/%{_libdir}/vst3/ -name "*.so"`

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE.md
%{_libdir}/KholorsStation/*

%files -n vst3-%{name}
%{_libdir}/vst3/*
%{_datadir}/icons/hicolor/scalable/apps/
%{_datadir}/applications/*

%changelog
* Fri Dec 26 2025 Yann Collette <ycollette.nospam@free.fr> - 1.26.0-1
- update to 1.26.0-1

* Sun Nov 02 2025 Yann Collette <ycollette.nospam@free.fr> - 1.25.0-1
- update to 1.25.0-1

* Thu Oct 02 2025 Yann Collette <ycollette.nospam@free.fr> - 1.24.1-1
- Initial spec file
