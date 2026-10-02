# Status: active
# Tag: Effect, Tool, Devel
# Type: Plugin, Standalone, VST3, CLAP, LV2
# Category: Effect, Programming

%global commit0 056cea68387f53bc64978581dd3820e85b844fec

Name: protoplug
Version: 0.0.1
Release: 4%{?dist}
Summary: Create audio plugins on-the-fly with Lua
License: MIT
URL: https://github.com/ycollet/protoplug
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./protoplug-source.sh <TAG>
#        ./protoplug-source.sh fixes

Source0: protoplug.tar.gz
Source1: protoplug-source.sh

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
BuildRequires: lua-devel
BuildRequires: luajit-devel

%description
Protoplug is a VST3/CLAP/LV2 plugin that lets you load and edit Lua scripts as audio effects and instruments.
The scripts can process audio and MIDI, display their own interface, and use external libraries.
Transform any music software into a live coding environment!

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

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: MIT
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: MIT
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n protoplug

%build

%cmake -DPLUGIN_USE_CLAP=ON \
       -DPLUGIN_USE_LV2=ON
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/protoplug_fx_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/protoplug_gen_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra %{__cmake_builddir}/protoplug_fx_artefacts/CLAP/* %{buildroot}/%{_libdir}/clap/
cp -ra %{__cmake_builddir}/protoplug_gen_artefacts/CLAP/* %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/protoplug_fx_artefacts/LV2/* %{buildroot}/%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/protoplug_gen_artefacts/LV2/* %{buildroot}/%{_libdir}/lv2/

install -m 755 -d %{buildroot}%{_datadir}/%{name}/
cp -ra ProtoplugFiles/* %{buildroot}%{_datadir}/%{name}/

%files -n license-%{name}
%doc readme.md
%license license.txt
%{_datadir}/%{name}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Thu Oct 01 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-4
- update to last fixe branch

* Wed Sep 30 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-3
- update to last fixe branch

* Wed Sep 30 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to last fixe branch

* Tue Apr 28 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
