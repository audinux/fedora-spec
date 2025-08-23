# Status: active
# Tag: Effect, Distortion
# Type: Plugin, Standalone, VST3, CLAP
# Category: Effect, Distortion

Name: hamburger
Version: 0.5
Release: 2%{?dist}
Summary: Hamburger is a distortion plugin with inbuilt dynamics controls and equalisation that can deliver both subtle tangy harmonics and absolute annilhilation and noise-wall-ification to any sound
License: AGPL-3.0-or-later
URL: https://github.com/Davit-G/Hamburger
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/Davit-G/Hamburger/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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

Requires: license-%{name}

%description
Hamburger is a distortion plugin with inbuilt dynamics controls and equalisation that can
deliver both subtle tangy harmonics and absolute annihilation and noise-wall-ification to
any sound.

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

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: AGPL-3.0-or-later
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n Hamburger-%{version}

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Hamburger_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra %{__cmake_builddir}/Hamburger_artefacts/CLAP/*  %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}%{_bindir}/
cp %{__cmake_builddir}/Hamburger_artefacts/Standalone/*  %{buildroot}/%{_bindir}/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE.md

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Fri Aug 22 2025 Yann Collette <ycollette.nospam@free.fr> - 0.5-2
- update to 0.5-2 - remove unused dep

* Mon Jun 16 2025 Yann Collette <ycollette.nospam@free.fr> - 0.5-1
- Initial spec file
