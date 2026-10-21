# Status: active
# Tag: Looper
# Type: Plugin, Standalone, VST3
# Category: Effect

Name: frippertron
Version: 2.2.0
Release: 1%{?dist}
Summary: An audio vst plugin simulating a frippertronic
License: AGPL-3.0-or-later
URL: https://github.com/elgaucholoco/Frippertron
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/elgaucholoco/Frippertron/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
An effect plugin (VST3 / standalone) based on the "Frippertronics" concept developed by Robert Fripp.
The original setup connects two Revox tape machines using a single continuous tape loop.
Machine A records the input, while machine B—positioned at a distance—plays back the tape and feeds
the signal back into the input of machine A.
This creates overlapping layers of sound that gradually fade away.
Frippertron features two such signal paths (A and B). In "2 REVOX" mode, each path has its own
independent loop length, causing two loops of different durations to constantly drift in relation to
one another. In "1 REVOX" mode, path B follows path A, replicating Fripp’s original single-machine
setup in stereo.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: AGPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: AGPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n Frippertron-%{version}

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Frippertron_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/Frippertron_artefacts/Standalone/* %{buildroot}/%{_bindir}/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp Resources/icon.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=%{name}
Icon=%{name}
Comment=An audio vst plugin simulating a frippertronic
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
%doc README.md CHANGELOG.md

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Fri Oct 16 2026 Yann Collette <ycollette.nospam@free.fr> - 2.1.0-1
- Initial spec file
