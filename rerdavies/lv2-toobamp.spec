# Status: active
# Tag: Guitar, Effect
# Type: Plugin, LV2
# Category: Audio, Effect

Name: lv2-toobamp-plugins
Version: 1.1.61
Release: 2%{?dist}
Summary: A set of high-quality guitar effect plugins for Raspberry Pi with specific support for PiPedal.
License: GPL-2.0-or-later
URL: https://github.com/rerdavies/ToobAmp
ExclusiveArch: x86_64 aarch64

# ./rerdavies-source.sh <project> <tag>
# ./rerdavies-source.sh ToobAmp v1.1.61

Source0: ToobAmp.tar.gz
Source1: rerdavies-source.sh

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: lv2-devel
BuildRequires: lilv-devel
BuildRequires: boost-devel
BuildRequires: boost-static
BuildRequires: flac-devel
BuildRequires: libogg-devel
BuildRequires: zlib-devel
BuildRequires: librsvg2-devel
BuildRequires: cairo-devel
BuildRequires: catch-devel
BuildRequires: pango-devel
BuildRequires: lsb_release
BuildRequires: libXrandr-devel
BuildRequires: libzstd-devel
BuildRequires: libzstd-static

%description
ToobAmp LV2 plugins are a set of high-quality guitar effect plugins for Raspberry Pi.
They are specifically designed for use with the PiPedal project, but work perfectly
well with any LV2 Plugin host.

%prep
%autosetup -n ToobAmp

sed -i -e "/add_subdirectory(\"debian\/src\")/d" CMakeLists.txt
sed -i -e "s/-Werror//g" src/CMakeLists.txt

sed -i -e "s/boost_iostreams.a/boost_iostreams/g" src/CMakeLists.txt
sed -i -e "s/z.a/z/g" src/CMakeLists.txt
sed -i -e "s/ogg.a/ogg/g" src/CMakeLists.txt
sed -i -e "s/FLAC.a/FLAC/g" src/CMakeLists.txt
sed -i -e "s/FLAC++.a/FLAC++/g" src/CMakeLists.txt

sed -i -e "s/usr\/lib\/lv2/usr\/%{_lib}\/lv2/g" src/CMakeLists.txt

# Disable static link with catch2
sed -i -e "s/\.a//g" modules/lv2cairo/src/test/CMakeLists.txt

%build

%set_build_flags

%cmake -DBUILD_TESTING=OFF \
       -DBoost_USE_STATIC_LIBS=OFF \
       -DCMAKE_CXX_FLAGS="$CXXFLAGS -Wno-template-body -include algorithm -include cstdint"
%cmake_build

%install

%cmake_install

%files
%doc README.md
%{_libdir}/lv2/*

%changelog
* Thu Oct 09 2025 Yann Collette <ycollette.nospam@free.fr> - 1.1.61-2
- update to 1.1.61-2 - add zstd

* Wed May 14 2025 Yann Collette <ycollette.nospam@free.fr> - 1.1.61-1
- update to 1.1.61-1

* Tue Mar 18 2025 Yann Collette <ycollette.nospam@free.fr> - 1.1.58-1
- update to 1.1.58-1

* Wed Aug 07 2024 Yann Collette <ycollette.nospam@free.fr> - 1.1.31-1
- update to 1.1.31-1

* Sun Sep 10 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.29-1
- Initial build
