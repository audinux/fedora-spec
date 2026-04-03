# Status: active
# Tag: Tool
# Type: Standalone, Plugin, VST3
# Category: Audio, Tool, Programming

Name: formula
Version: 1.2.2
Release: 1%{?dist}
Summary: Formula is an open-source VST3 plugin to create custom audio effects inside your DAW
License: BSL-1.0
URL: https://github.com/soundspear/formula
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./formula-source.sh <TAG>
#        ./formula-source.sh v1.2.2

Source0: formula.tar.gz
Source1: formula-source.sh

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
BuildRequires: cpprest-devel
BuildRequires: llvm18-devel
BuildRequires: desktop-file-utils

Requires: license-%{name}

%description
Formula is an open-source VST & AU plugin to create custom audio effects inside your DAW.
For developers: Live code and test your effects right inside your DAW. Share your effects with the community.
For end-users: Browse and use hundreds of bundled open-source effects made by developers from around the world.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: BSL-1.0

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: BSL-1.0
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n formula

sed -i -e "s|Boost 1.84.0 COMPONENTS REQUIRED|Boost COMPONENTS REQUIRED|g" CMakeLists.txt

%build

%cmake -DFORMULA_STANDALONE=ON
%cmake_build

%install

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/Formula_artefacts/Standalone/* %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Formula_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

# Install icon
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/apps/256x256
cp assets/formula_icon.png %{buildroot}/%{_datadir}/icons/hicolor/apps/256x256/%{name}.png

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%name
Exec=Formula
Icon=formula
Comment=An open-source VST3 plugin to create custom audio effects inside your DAW
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/apps/256x256/*

%files -n license-%{name}
%doc README.md formulas/* assets/manual/*
%license LICENSE.txt

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Thu Apr 02 2026 Yann Collette <ycollette.nospam@free.fr> - 1.2.2-1
- Initial spec file
