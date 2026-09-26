# Status: active
# Tag: Modular
# Type: Standalone
# Category: Audio, Video, Synthesizer

Name: infinite
Version: 0.4.5
Release: 1%{?dist}
Summary: Infinite is a node-based audiovisual workstation — real-time GPU video compositing, procedural 3D geometry, modular synths, DSP, and VST3 plugin hosting
License: MIT
URL: https://n1m21n.github.io/Infinite
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./infinite-source.sh <TAG>
#        ./infinite-source.sh v0.4.5

Source0: Infinite.tar.gz
Source1: infinite-source.sh
Patch0: infinite-0001-devendor.patch
Patch1: infinite-0002-add-missing-cstdint-header.patch
Patch2: infinite-0003-put-resources-in-share-directory.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: libxkbcommon-devel
BuildRequires: wayland-devel
BuildRequires: (ffmpeg-devel or ffmpeg-free-devel)
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: alsa-lib-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: libXi-devel
BuildRequires: flac-devel
BuildRequires: libglvnd-devel
BuildRequires: desktop-file-utils

Requires: rsms-inter-fonts

%description
A unified node-based audiovisual modular workstation for macOS, Windows, and Linux.
Real-time GPU image/video compositing, procedural 3D geometry and physics, and a full
modular synthesizer rack with native AU and VST3 plugin hosting — all interconnected
through a universal modulation graph.
Most nodes do one fixed thing; Field, Infinite's embedded programming language,
lets you write what a node does instead.

%prep
%autosetup -p1 -n Infinite

%build

%set_build_flags

export CXXFLAGS="-include cstdint $CXXFLAGS"

%cmake -DCMAKE_EXE_LINKER_FLAGS="-Wl,-rpath,'\$ORIGIN/../%{_lib}/Infinite' $LDFLAGS"
%cmake_build

%install

# /usr/share/infinite
# + icons/icon_1024.png
# + fonts/Inter-Regular.ttf
# + icons/lucide.ttf

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 %{__cmake_builddir}/Infinite %{buildroot}/%{_bindir}/
install -m 755 %{__cmake_builddir}/infinite-vst3-scanner %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_libdir}/Infinite/
install -m 755 %{__cmake_builddir}/_deps/onnxruntime_linux-src/lib/libonnxruntime.so.1 %{buildroot}/%{_libdir}/Infinite/

# Install bundle
install -m 755 -d %{buildroot}/%{_datadir}/infinite/fonts/
install -m 644 ./external/fonts/Inter/*.ttf %{buildroot}/%{_datadir}/infinite/fonts/

install -m 755 -d %{buildroot}/%{_datadir}/infinite/icons/
install -m 644 ./external/icons/Lucide/lucide.ttf %{buildroot}/%{_datadir}/infinite/icons/
install -m 644 ./assets/icon_1024.png %{buildroot}/%{_datadir}/infinite/icons/

install -m 755 -d %{buildroot}/%{_datadir}/infinite/examples/
install -m 644 ./assets/examples/*.inf %{buildroot}/%{_datadir}/infinite/examples/

install -m 755 -d %{buildroot}/%{_datadir}/infinite/models/
install -m 644 ./assets/models/*.onnx %{buildroot}/%{_datadir}/infinite/models/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp assets/Infinite.ico %{buildroot}/%{_datadir}/pixmaps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=%{name}
Icon=Infinite
Comment=Infinite is a node-based audiovisual workstation
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md ARCHITECTURE.md *.pdf docs/*
%license LICENSE
%{_bindir}/*
%{_libdir}/Infinite/*
%{_datadir}/applications/infinite.desktop
%{_datadir}/pixmaps/Infinite.ico
%{_datadir}/infinite/icons/icon_1024.png
%{_datadir}/infinite/icons/lucide.ttf
%{_datadir}/infinite/fonts/Inter-Medium.ttf
%{_datadir}/infinite/fonts/Inter-Regular.ttf
%{_datadir}/infinite/fonts/Inter-SemiBold.ttf
%{_datadir}/infinite/examples/*

%changelog
* Sat Sep 26 2026 Yann Collette <ycollette.nospam@free.fr> - 0.4.5-1
- update to 0.4.5-1

* Fri Sep 25 2026 Yann Collette <ycollette.nospam@free.fr> - 0.4.3-1
- Initial spec
