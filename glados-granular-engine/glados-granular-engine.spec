# Status: active
# Tag: Effect
# Type: Plugin, Standalone, VST3
# Category: Effect

Name: glados
Version: 1.0
Release: 1%{?dist}
Summary: A granular texture engine
License: GPL-2.0-or-later
URL: https://github.com/JosueFabian18/glados-granular-engine
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/JosueFabian18/glados-granular-engine/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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

Requires: license-%{name}

%description
GLaDOS is a granular synthesis effect designed to transform any audio signal (vocals, synths, or drums)
into unrecognizable and complex sonic textures.
METHOD: It slices the sound into milliseconds and rearranges them using modulation, delays, and pitch
to create creative and avant-garde effects.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-2.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-2.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n glados-granular-engine-%{version}

%build

cd Glados

%cmake
%cmake_build

%install

cd Glados

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Glados_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/Glados_artefacts/Standalone/* %{buildroot}/%{_bindir}/

%files
%{_bindir}/*

%files -n license-%{name}
%doc Glados/README.md Glados/GLaDOS_User_Manual_v2.docx

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Sat Sep 05 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- update to 1.0-1

* Tue Jul 21 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
