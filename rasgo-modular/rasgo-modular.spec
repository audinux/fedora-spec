# Status: active
# Tag: Modular
# Type: Standalone
# Category: Audio, Synthesizer

Name: rasgo-modular
Version: 0.1.0
Release: 1%{?dist}
Summary: A generative modular environment where the cable is an object with state.
License: AGPL-3.0-or-later
URL: https://github.com/lucioaraujo/rasgo-modular
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/lucioaraujo/rasgo-modular/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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

%description
A generative modular environment with 58 modules in eight families (SOURCE, TRANSFORM,
MODULATE, TIME, DECISION, ROUTE, SPACE, OUT), written in C++17 with no dependencies in
the core. Modules are described as data — each declares its own panel in
millimetres — and one engine drives two front-ends: a cross-platform JUCE app and an X11 test panel.

%prep
%autosetup -n %{name}-%{version}

%build

%cmake -DBUILD_TESTING:BOOL=OFF
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 %{__cmake_builddir}/rasgo_modular_panel %{buildroot}/%{_bindir}/rasgo_modular

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/examples/
cp -ra dossies/patches-estudo4/*.rmp %{buildroot}/%{_datadir}/%{name}/examples/

install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 apps/juce/assets/icon-source.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/apps/256x256/
install -m 644 apps/juce/assets/icon-256.png %{buildroot}/%{_datadir}/icons/hicolor/apps/256x256/%{name}.png

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/apps/32x32/
install -m 644 apps/juce/assets/icon-32.png %{buildroot}/%{_datadir}/icons/hicolor/apps/32x32/%{name}.png

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=%{name}
Icon=%{name}
Comment=A generative modular environment where the cable is an object with state.
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
%doc README.md CREDITS_AND_SOURCES.md CHANGELOG.md RASGO_MODULAR.md
%license LICENSE
%{_bindir}/*
%{_datadir}/%{name}/examples/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/icons/hicolor/apps/256x256/*
%{_datadir}/icons/hicolor/apps/32x32/*
%{_datadir}/applications/*

%changelog
* Fri Oct 02 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- Initial spec file
