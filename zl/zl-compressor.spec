# Status: active
# Tag: Compressor
# Type: LV2, VST3, Plugin
# Category: Effect

%global toolchain clang

Name: zl-compressor
Version: 0.1.1
Release: 1%{?dist}
Summary: Compressor plugin
License: GPL-3.0-only
URL: https://github.com/ZL-Audio/ZLEqualizer
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./zl-source.sh <project> <tag>
# ./zl-source.sh ZLCompressor 0.1.1

Source0: ZLCompressor.tar.gz
Source1: zl-source.sh

BuildRequires: clang
BuildRequires: cmake
BuildRequires: libX11-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: boost-devel
BuildRequires: libatomic
BuildRequires: chrpath

Requires: license-%{name}

%description
ZLCompressor is a compressor plugin.

%package -n license-%{name}
Summary:  License and documentation of %{name}
License:  GPL-3.0-only

%description -n license-%{name}
License and documentation of %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-only
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-3.0-only
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n ZLCompressor

sed -i -e "s/ZL Compressor/ZL_Compressor/g" CMakeLists.txt

%build

%cmake -DKFR_ENABLE_DFT=ON
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_bindir}/

cp -ra %{__cmake_builddir}/ZLCompressor_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/ZLCompressor_artefacts/LV2/* %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/ZLCompressor_artefacts/Standalone/* %{buildroot}%{_bindir}/

# Cleanup rpath
chrpath --delete `find %{buildroot}%{_libdir}/vst3/ -name "*.so"`
chrpath --delete `find %{buildroot}%{_libdir}/lv2/ -name "*.so"`
chrpath --delete %{buildroot}%{_bindir}/ZL_Compressor

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md CHANGELOG.md
%license LICENSE.md

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Wed Jul 16 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.1-1
- Initial spec file
