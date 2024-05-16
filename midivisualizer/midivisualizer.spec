# Tag: MIDI, Video, Tool
# Type: Standalone
# Category: MIDI, Tool

Name: midivisualizer
Version: 7.2
Release: 1%{?dist}
Summary: A small MIDI visualizer tool, using OpenGL
URL: https://github.com/kosua20/MIDIVisualizer
ExclusiveArch: x86_64 aarch64
License: MIT

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/kosua20/MIDIVisualizer/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: chrpath
BuildRequires: alsa-lib-devel
BuildRequires: compat-ffmpeg4
BuildRequires: glfw-devel
BuildRequires: gtk3-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libnotify-devel
BuildRequires: desktop-file-utils

%description
A small MIDI visualizer, written in C++/OpenGL.

%prep
%autosetup -n MIDIVisualizer-%{version}

sed -i -e "/add_subdirectory(libs\/glfw\/)/d" CMakeLists.txt

%build

%set_build_flags

%cmake -DCMAKE_CXX_FLAGS="-include span -fPIC $CXXFMAGS" \
       -DGLFW_BUILD_TESTS=OFF \
       -DGLFW_BUILD_EXAMPLES=OFF \
       -DLIBREMIDI_EXAMPLES=OFF \

%cmake_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
cp  %{__cmake_builddir}/MIDIVisualizer %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_libdir}/midivisualizer/
cp  %{__cmake_builddir}/libs/libremidi/liblibremidi.so %{buildroot}/%{_libdir}/midivisualizer/

# chrpath --delete %{buildroot}/%{_bindir}/MIDIVisualizer
chrpath --replace %{_libdir}/midivisualizer %{buildroot}/%{_bindir}/MIDIVisualizer

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/
cp resources/icon/MIDIVisualizer.ico %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=MIDI Visualizer
Exec=%{name}
Icon=MIDIVisualizer
Comment=MIDI Visualizer
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%dir %{_libdir}/midivisualizer/
%{_libdir}/midivisualizer/liblibremidi.so
%{_datadir}/icons/hicolor/256x256/apps/*
%{_datadir}/applications/*

%changelog
* Wed Sep 20 2023 Yann Collette <ycollette.nospam@free.fr> - 7.2-1
- update to 7.2-1

* Wed Aug 30 2023 Yann Collette <ycollette.nospam@free.fr> - 7.1-1
- update to 7.1-1

* Sun Mar 12 2023 Yann Collette <ycollette.nospam@free.fr> - 7.0-1
- Initial spec file
