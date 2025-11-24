# Status: active
# Tag: Drum
# Type: Plugin, Standalone, VST3
# Category: Audio, Sequencer

%global commit0 7bf4b48632deb9ff5dd4c404675ab68d07e21c2d

Name: drumelidrum
Version: 0.2.0
Release: 1%{?dist}
Summary: Drum machine VST3 plug-in
License: GPL-3.0-or-Later
URL: https://gitlab.com/andreasersson/drumelidrum-vst
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://gitlab.com/andreasersson/drumelidrum-vst/-/archive/%{commit0}/drumelidrum-vst-%{commit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libxcb-devel
BuildRequires: libX11-devel
BuildRequires: freetype-devel
BuildRequires: xcb-util-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel
BuildRequires: pango-devel
BuildRequires: gtkmm30-devel
BuildRequires: sqlite-devel

%description
Drum machine VST3 plug-in

%package -n vst3-%{name}
Summary: VST3 plugins from %{name}
License: GPL-3.0-or-later

%description -n vst3-%{name}
VST3 plugins from %{name}

%prep
%autosetup -n drumelidrum-vst-%{commit0}

%build

%set_build_flags

export CXXFLAGS="-include limits -DRELEASE -include exception -include cstdint -fPIC $CXXFLAGS"
export CFLAGS="-fPIC $CFLAGS"

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/VST3/* %{buildroot}/%{_libdir}/vst3/

%files -n vst3-%{name}
%doc README.md
%license COPYING
%{_libdir}/vst3/*

%changelog
* Mon Nov 24 2025 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- Initial packaging.
