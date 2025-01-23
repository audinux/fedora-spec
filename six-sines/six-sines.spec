# Status: active
# Tag: Synthesizer
# Type: Plugin, Standalone, VST3
# Category: Audio, Synthesizer

Name: six-sines
Version: 1.0.1
Release: 2%{?dist}
Summary: Six Sines is a small synthesizer which explores audio rate inter-modulation of signals
License: MIT
URL: https://github.com/baconpaul/six-sines
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./six-sines-source.sh <TAG>
#        ./six-sines-source.sh v1.0.1

Source0: six-sines.tar.gz
Source1: version_information.cpp 
Source2: six-sines-source.sh

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
BuildRequires: pulseaudio-libs-devel
BuildRequires: pkgconfig(jack)
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: rtaudio-devel
BuildRequires: rtmidi-devel
BuildRequires: gulrak-filesystem-devel
BuildRequires: simde-devel
BuildRequires: pkgconfig(jack)
BuildRequires: patchelf

Requires: license-%{name}

%description
Six Sines is a small synthesizer which explores audio rate inter-modulation of signals.
Some folks would call it "an FM synth" but it's really a bit more PM/AM, and anyway
that's kinda not the point.

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

%package -n license-%{name}
Summary: License and documentation for %{name}
License: MIT

%description -n license-%{name}
License and documentation for %{name}

%prep
%autosetup -n six-sines

# Rename project from "Six Sines" to "Six_Sines"
sed -i -e "s/set(PRODUCT_NAME \"Six Sines\")/set(PRODUCT_NAME \"Six_Sines\")/g" CMakeLists.txt
# Remove -march=nehalem gcc flag
%ifarch x86_64
#sed -i -e "s/-march=nehalem/-m64/g" cmake/compile-options.cmake
%else
sed -i -e "/nehalem/d" cmake/compile-options.cmake
%endif

%build

%set_build_flags

export CFLAGS=`echo $CFLAGS | sed -e "s/-Werror=format-security//g"`
export CXXFLAGS=`echo $CXXFLAGS | sed -e "s/-Werror=format-security//g"`

export CFLAGS="-Wno-error=deprecated-declarations $CFLAGS"
export CXXFLAGS="-include ghc/filesystem.hpp -Wno-error=deprecated-declarations $CXXFLAGS"

%cmake -DBUILD_SHARED_LIBS:BOOL=OFF

mkdir -p %{__cmake_builddir}/geninclude
cp %{SOURCE1} %{__cmake_builddir}/geninclude

%cmake_build --target six-sines_all

%install

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Release/Six_Sines.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -ra %{__cmake_builddir}/Six_Sines.clap %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}/%{_bindir}/
cp -ra %{__cmake_builddir}/Six_Sines %{buildroot}/%{_bindir}/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md doc/manual.md
%license LICENSE.md

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Wed Jan 22 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-2
- update to 1.0.1-2

* Mon Jan 20 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-2
- update to 1.0.0-2

* Thu Jan 16 2025 Yann Collette <ycollette.nospam@free.fr> - 0.9999999-2
- update to 0.9999999-2

* Thu Jan 09 2025 Yann Collette <ycollette.nospam@free.fr> - 0.999999-2
- update to 0.999999-2

* Sat Jan 04 2025 Yann Collette <ycollette.nospam@free.fr> - 0.9999-2
- update to 0.9999-2

* Sat Jan 04 2025 Yann Collette <ycollette.nospam@free.fr> - 0.999-2
- update to 0.999-2 - fix rpath modification

* Fri Jan 03 2025 Yann Collette <ycollette.nospam@free.fr> - 0.999-1
- update to 0.999-1

* Thu Jan 02 2025 Yann Collette <ycollette.nospam@free.fr> - 0.99-1
- Initial spec file
