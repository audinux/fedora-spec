# Status: active
# Tag: Graphic
# Type: Plugin, Standalone, VST3, CLAP
# Category: Graphic

Name: glslplugin
Version: 1.2
Release: 2%{?dist}
Summary: GLSL Editor for Audio Plugin
License: MIT
URL: https://github.com/COx2/glslEditor_AudioPlugin
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./glslplugin-source.sh <TAG>
#        ./glslplugin-source.sh next

Source0: glslEditor_AudioPlugin.tar.gz
Source1: glslplugin-source.sh

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
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel

%description
GLSL Editor running on VST host Applications Cubase, StudioOne, Ableton Live, Logic, and more...
This Editor already defined uniform variables, and GLSL code compatible for "GLSL Sandbox".
http://glslsandbox.com/

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: MIT
Requires: license-%{name}}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: MIT
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%package -n license-%{name}
Summary: License and documentation for %{name}
License: MIT
Requires: license-%{name}

%description -n license-%{name}
License and documentation for %{name}

%prep
%autosetup -n glslEditor_AudioPlugin

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/GLSLPlugIn/GLSLPlugIn_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra %{__cmake_builddir}/GLSLPlugIn/GLSLPlugIn_artefacts/CLAP/*  %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/GLSLPlugIn/GLSLPlugIn_artefacts/Standalone/*  %{buildroot}/%{_bindir}/

%files -n license-%{name}
%doc README.md
%license LICENSE

%files
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Fri Aug 29 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2-2
- update to 1.2-2 - remove unused dep - update to ec8d5662

* Sun Dec 15 2024 Yann Collette <ycollette.nospam@free.fr> - 1.2-1
- Initial spec file
