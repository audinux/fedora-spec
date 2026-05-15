# Status: active
# Tag: Tool, Rack
# Type: Plugin, LV2, Standalone
# Category: Audio, Effect, Tool

Name: dsp4guitar
Version: 1.1
Release: 1%{?dist}
Summary: Multi-Effect for guitar
License: MIT
URL: https://github.com/GizzZmo/DSP4Guitar
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./dsp4guitar-source.sh <TAG>
#        ./dsp4guitar-source.sh 1.1

Source0: DSP4Guitar.tar.gz
Source1: dsp4guitar-source.sh

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
A professional-grade, multi-effect plugin built with the JUCE framework, wrapped in a full cyberpunk / Matrix-terminal
aesthetic — neon-green-on-black UI, scrolling Matrix-rain header animation, glowing LED toggles, and custom rotary knobs.
The plugin provides a 10-effect processing chain, each independently bypassable, running in a fixed signal-flow order
optimised for guitar. Parameters are DAW-automatable via JUCE's AudioProcessorValueTreeState and plugin state is
persisted across sessions.

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
%autosetup -n DSP4Guitar

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/DSP4Guitar_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_bindir}/
install -m755 %{__cmake_builddir}/DSP4Guitar_artefacts/Standalone/*  %{buildroot}/%{_bindir}/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/apps/256x256/
cp assets/icons/dsp4guitar_logo.png %{buildroot}/%{_datadir}/icons/hicolor/apps/256x256/DSP4Guitar.png

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
cp assets/icons/dsp4guitar_logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/DSP4Guitar.svg

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%name
Exec=DSP4Guitar
Icon=DSP4Guitar
Comment=Guitar multi-effects
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
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/apps/256x256/*
%{_datadir}/icons/hicolor/scalable/apps/*

%files -n license-%{name}
%doc README.md CONTRIBUTING.md Documentation/*
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Fri May 15 2026 Yann Collette <ycollette.nospam@free.fr> - 1.1-1
- Initial spec file
