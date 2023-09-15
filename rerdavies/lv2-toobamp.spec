Name:    lv2-toobamp-plugins
Version: 1.0.29
Release: 1%{?dist}
Summary: A set of high-quality guitar effect plugins for Raspberry Pi with specific support for PiPedal.
License: GPL-2.0-or-later
URL:     https://github.com/rerdavies/ToobAmp

# ./rerdavies-source.sh <project> <tag>
# ./rerdavies-source.sh ToobAmp v1.0.29

Source0: ToobAmp.tar.gz
Source1: rerdavies-source.sh

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: lv2-devel
BuildRequires: boost-devel
BuildRequires: flac-devel
BuildRequires: libogg-devel
BuildRequires: zlib-devel

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

%build

%set_build_flags

%cmake -DBUILD_TESTING=OFF \
       -DCMAKE_CXX_FLAGS="$CXXFLAGS -include algorithm -include cstdint"
%cmake_build

%install

%cmake_install

%files
%doc README.md
%{_libdir}/lv2/*

%changelog
* Sun Sep 10 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.29-1
- Initial build
