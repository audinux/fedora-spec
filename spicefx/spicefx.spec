# Status: active
# Tag: Distortion
# Type: Plugin, Standalone, VST3, LV2
# Category: Effect

%global commit0 21f08240330cf4b60c807553ca2029c184867a27

Name: spicefx
Version: 0.0.1
Release: 1%{?dist}
Summary: A analog modeling DSP plugin with a lot of saturation models and cab simulation
License: BSD-3-Claude
URL: https://github.com/DatanoiseTV/spice-oss
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./spicefx-source.sh <TAG>
#        ./spicefx-source.sh main

Source0: spice-oss.tar.gz
Source1: spicefx-source.sh

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
A high-quality analog saturation plugin with multiple distortion models.
Open sourced in October 2025.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: BSD-3-Clause

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: BSD-3-Clause
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: BSD-3-Clause
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n spice-oss

sed -i -e "s|PRODUCT_NAME \"Spice FX\"|PRODUCT_NAME \"Spice_FX\"|g" CMakeLists.txt
sed -i -e "s|Exec=Spice\ FX|Exec=Spice_FX|g" Resources/spice-fx.desktop

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Spice_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/Spice_artefacts/LV2/* %{buildroot}/%{_libdir}/lv2/

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/Spice_artefacts/Standalone/* %{buildroot}/%{_bindir}/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp Resources/Icon.ico %{buildroot}/%{_datadir}/pixmaps/%{name}.ico

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/1024x1024/apps/
cp Resources/Icon.png %{buildroot}/%{_datadir}/icons/hicolor/1024x1024/apps/%{name}.png

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/
cp Resources/spice-fx.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop

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
%{_datadir}/icons/hicolor/1024x1024/apps/*

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Tue May 12 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
