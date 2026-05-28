# Status: active
# Tag: Effect, Gain, Filter
# Type: Plugin, Standalone, VST3, LV2
# Category: Effect

Name: nine-strip
Version: 0.1.2
Release: 1%{?dist}
Summary: A channel strip plugin built with JUCE, incorporating classic Airwindows processing algorithms into a comprehensive mixing tool
License: AGPL-3.0-or-later
URL: https://github.com/blablack/nine-strip
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./nine-strip-source.sh <TAG>
#        ./nine-strip-source.sh v0.1.2

Source0: nine-strip.tar.gz
Source1: nine-strip.svg
Source2: nine-strip-source.sh

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
A VST3 / LV2 channel strip plugin built with JUCE, incorporating classic Airwindows processing algorithms into a comprehensive mixing tool.
Also available as a standalone application.

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

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: AGPL-3.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n nine-strip

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/src/NineStrip_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/src/NineStrip_artefacts/LV2/* %{buildroot}/%{_libdir}/lv2/

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/src/NineStrip_artefacts/Standalone/* %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
cp %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=%{name}
Icon=%{name}
Comment=A channel strip plugin built with JUCE, incorporating classic Airwindows processing algorithms into a comprehensive mixing tool
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
%{_datadir}/icons/hicolor/scalable/apps/

%files -n license-%{name}
%doc README.md doc/*
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Wed May 27 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.2-1
- Initial spec file
