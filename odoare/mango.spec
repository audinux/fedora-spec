# Status: active
# Tag: Jack, Alsa, Distortion
# Type: Plugin, Standalone, VST3
# Category: Effect

%global commit0 d0004db50c37e76e50c06d25ce31f19ed63d3895

Name: mango
Version: 0.2.0
Release: 1%{?dist}
Summary: Modular sound glitcher / mangler
License: AGPL-3.0-or-later
URL: https://github.com/odoare/Mango
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/odoare/Mango/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz

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
Mango is a rubber step sequencer of up to eight lanes, each driving one effect.
You draw blocks on a lane's strip; while the playhead is inside a block, that
lane's effect is processing; outside it, the lane is transparent. So you paint
when each effect happens, in time with the host, and the lanes stack into a
chain from top to bottom.
The character is seeded randomness. Effects that need a rhythmic rate don't
take a fixed value: you weight how likely each note length is, and the actual
rate is drawn per block. Every draw is a pure function of the seed, the lane
and the block, so a pattern always plays back identically (in real time and
in an offline bounce alike), and changing the seed re-rolls everything at once.

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

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: AGPL-3.0-or-later
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n Mango-%{commit0}

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Mango_artefacts/Release/VST3/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra %{__cmake_builddir}/Mango_artefacts/Release/CLAP/* %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/Mango_artefacts/Release/Standalone/* %{buildroot}/%{_bindir}/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp Source/Assets/logo686.png %{buildroot}/%{_datadir}/pixmaps/mango.png

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=Mango
Icon=%{name}
Comment=Modular sound glitcher / mangler
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
%license LICENSE.md LICENSE LICENSE.LGPL LICENSE.LGPL.GPL

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Tue Nov 10 2026 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- Initial spec file
