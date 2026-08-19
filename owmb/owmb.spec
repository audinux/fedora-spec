# Status: active
# Tag: Tool
# Type: Plugin, Standalone, VST3
# Category: Tool

Name: owmb
Version: 1.0.0
Release: 1%{?dist}
Summary: Open wav media browser
License: MIT
URL: https://github.com/samplaman/owmb
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/samplaman/owmb/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
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
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: gtk3-devel
BuildRequires: desktop-file-utils

Requires: license-%{name}

%description
OWMB (OpenWav Media Browser) is an open-source, high-performance audio plugin (VST3, Standalone) and
sample library management system built with JUCE 8 and C++17. Designed for music producers, sound
designers, and sample collectors, OWMB features an interactive 2D Sample Cloud Constellation
Visualizer, multi-tag filtering, ultra-fast asynchronous WAV scanning, and direct DAW
drag-and-drop integration.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: MIT

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: MIT
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n %{name}-%{version}

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/OpenWav_artefacts/Standalone/* %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/OpenWav_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
install -m 644 owmbico.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=OWMB
Icon=%{name}
Comment=Open wav media browser
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
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%files -n license-%{name}
%doc README.md

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Sun Jan 01 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.9-1
- Initial spec file
