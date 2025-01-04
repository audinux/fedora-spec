# Status: active
# Tag: Synthesizer
# Type: Plugin, Standalone, VST3
# Category: Audio, Synthesizer

Name: six-sines
Version: 0.9999
Release: 2%{?dist}
Summary: Six Sines is a small synthesizer which explores audio rate inter-modulation of signals
License: MIT
URL: https://github.com/baconpaul/six-sines
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./six-sines-source.sh <TAG>
#        ./six-sines-source.sh v0.9999

Source0: six-sines.tar.gz
Source1: six-sines-source.sh

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

%cmake
%cmake_build --target six-sines_all

%install

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Release/Six_Sines.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -ra %{__cmake_builddir}/Six_Sines.clap %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}/%{_bindir}/
cp -ra %{__cmake_builddir}/Six_Sines %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_libdir}/six_sines/
install -m 755 %{__cmake_builddir}/libs/sst/sst-plugininfra/libs/strnatcmp/libstrnatcmp.so %{buildroot}/%{_libdir}/six_sines/
install -m 755 %{__cmake_builddir}/libs/sst/sst-plugininfra/libs/filesystem/libfilesystem.so %{buildroot}/%{_libdir}/six_sines/

patchelf --set-rpath '$ORIGIN/../%{_lib}/six_sines/' %{buildroot}/%{_bindir}/Six_Sines
patchelf --set-rpath '$ORIGIN/../six_sines/' %{buildroot}/%{_libdir}/clap/Six_Sines.clap
patchelf --set-rpath '$ORIGIN/../../../../six_sines/' `find %{buildroot}/%{_libdir}/vst3/Six_Sines.vst3/ -name "*.so"`

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md doc/manual.md
%license LICENSE.md
%{_libdir}/six_sines/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Sat Jan 04 2025 Yann Collette <ycollette.nospam@free.fr> - 0.9999-2
- update to 0.9999-2

* Sat Jan 04 2025 Yann Collette <ycollette.nospam@free.fr> - 0.999-2
- update to 0.999-2 - fix rpath modification

* Fri Jan 03 2025 Yann Collette <ycollette.nospam@free.fr> - 0.999-1
- update to 0.999-1

* Thu Jan 02 2025 Yann Collette <ycollette.nospam@free.fr> - 0.99-1
- Initial spec file
