# Status: active
# Tag: Synthesizer, Sequencer
# Type: Plugin, VST3, Standalone
# Category: Synthesizer

Name: simple303
Version: 1.0.0
Release: 1%{?dist}
Summary: Simple multi-platform virtual TB-303
License: MIT
URL: https://github.com/Fadedlimes/Simple303
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/Fadedlimes/Simple303/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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

%description
A simple, hands-on, and accessible virtual TB-303 bassline synthesizer using Open-303 with analogue-style 64-step sequencer.

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: MIT
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n Simple303-%{version}

sed -i -e "s|PRODUCT_NAME \"Simple 303\"|PRODUCT_NAME \"Simple_303\"|g" CMakeLists.txt

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 %{__cmake_builddir}/Simple303_artefacts/Standalone/* %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -vfr %{__cmake_builddir}/Simple303_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

%files
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Sun Sep 06 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
