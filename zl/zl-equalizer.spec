# Status: active
# Tag: Equalizer
# Type: LV2, VST3, Plugin
# Category: Effect

%global toolchain clang

Name: zl-equalizer
Version: 1.0.2
Release: 2%{?dist}
Summary: Equalizer plugin
License: GPL-3.0-only
URL: https://github.com/ZL-Audio/ZLEqualizer
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./zl-source.sh <project> <tag>
# ./zl-source.sh ZLEqualizer 1.0.2

Source0: ZLEqualizer.tar.gz
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
ZLEqualizer is an equalizer plugin.

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
%autosetup -n ZLEqualizer

sed -i -e "s/ZL Equalizer 2/ZL_Equalizer_2/g" CMakeLists.txt

%build

%cmake -DKFR_ENABLE_DFT=ON
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_bindir}/

cp -ra %{__cmake_builddir}/ZLEqualizer_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/ZLEqualizer_artefacts/LV2/* %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/ZLEqualizer_artefacts/Standalone/* %{buildroot}%{_bindir}/

# Cleanup rpath
chrpath --delete `find %{buildroot}%{_libdir}/vst3/ -name "*.so"`
chrpath --delete `find %{buildroot}%{_libdir}/lv2/ -name "*.so"`
chrpath --delete %{buildroot}%{_bindir}/*

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
* Sun Nov 16 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-2
- update to 1.0.2-2

* Fri Nov 14 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-2
- update to 1.0.1-2

* Fri Oct 17 2025 Yann Collette <ycollette.nospam@free.fr> - 0.6.3-2
- update to 0.6.3-2

* Wed Apr 30 2025 Yann Collette <ycollette.nospam@free.fr> - 0.6.2-2
- update to 0.6.2-2

* Tue Apr 08 2025 Yann Collette <ycollette.nospam@free.fr> - 0.6.1-2
- update to 0.6.1-2

* Sun Mar 02 2025 Yann Collette <ycollette.nospam@free.fr> - 0.6.0-2
- update to 0.6.0-2

* Fri Dec 20 2024 Yann Collette <ycollette.nospam@free.fr> - 0.5.1-2
- update to 0.5.1-2

* Mon Dec 16 2024 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-2
- update to 0.5.0-2

* Wed Dec 04 2024 Yann Collette <ycollette.nospam@free.fr> - 0.4.5-2
- update to 0.4.5-2

* Tue Nov 26 2024 Yann Collette <ycollette.nospam@free.fr> - 0.4.4-2
- update to 0.4.4-2

* Fri Oct 18 2024 Yann Collette <ycollette.nospam@free.fr> - 0.4.2-2
- update to 0.4.2-2

* Fri Oct 11 2024 Yann Collette <ycollette.nospam@free.fr> - 0.4.1-2
- update to 0.4.1-2

* Sat Oct 05 2024 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-2
- update to 0.4.0-2

* Fri Aug 23 2024 Yann Collette <ycollette.nospam@free.fr> - 0.3.5-2
- update to 0.3.5-2

* Sat Aug 10 2024 Yann Collette <ycollette.nospam@free.fr> - 0.3.4-2
- update to 0.3.4-2

* Sun Jul 14 2024 Yann Collette <ycollette.nospam@free.fr> - 0.3.3-2
- update to 0.3.3-2

* Tue Jun 18 2024 Yann Collette <ycollette.nospam@free.fr> - 0.3.2-2
- update to 0.3.2-2 - tag updated

* Fri Jun 14 2024 Yann Collette <ycollette.nospam@free.fr> - 0.3.2-1
- update to 0.3.2-1

* Sun Jun 02 2024 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-1
- update to 0.3.1-1

* Fri May 31 2024 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-1
- Initial spec file
