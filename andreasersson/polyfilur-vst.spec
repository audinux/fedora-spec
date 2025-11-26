# Status: active
# Tag: Synthesizer
# Type: Plugin, Standalone, VST3
# Category: Audio, Synthesizer

%global commit0 aa89a20b19f7b416849a0b2441e0bc085555b69d

Name: polyfilur
Version: 0.2.0
Release: 1%{?dist}
Summary: Virtual analog synthesizer VST3 plug-in
License: GPL-3.0-or-Later
URL: https://gitlab.com/andreasersson/polyfilur-vst
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://gitlab.com/andreasersson/polyfilur-vst/-/archive/%{commit0}/polyfilur-vst-%{commit0}.tar.gz

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
Virtual analog synthesizer VST3 plug-in

%package -n vst3-%{name}
Summary: VST3 plugins from %{name}
License: GPL-3.0-or-later

%description -n vst3-%{name}
VST3 plugins from %{name}

%prep
%autosetup -n polyfilur-vst-%{commit0}

%build

%set_build_flags

export CXXFLAGS="-include limits -include exception -DRELEASE -include cstdint -fPIC $CXXFLAGS"
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
* Wed Nov 26 2025 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- Initial packaging.
