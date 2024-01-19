# Tag: Emulator
# Type: Plugin, LV2, VST, DSSI
# Category: Audio, Synthesizer

# Global variables for github repository
%global commit0 6b9c8a8bf2cac3833d2b0639cfcfef9aeea673e0
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: zynayumi
Version: 0.0.1
Release: 1%{?dist}
Summary: VST/DSSI/LV2 plugin based on ayumi, the highly precise emulator of AY-8910 and YM2149
URL: https://github.com/zynayumi/zynayumi
License: GPL3

Vendor:       Audinux
Distribution: Audinux

# Usage: ./source-zynayumi.sh <tag>
#        ./source-zynayumi.sh master

Source0: zynayumi.tar.gz
Source1: source-zynayumi.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: dssi-devel
BuildRequires: lv2-devel
BuildRequires: boost-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: desktop-file-utils

%description
Synth based on ayumi, the highly precise emulator of AY-8910 and YM2149

%package -n vst-%{name}
Summary: VST version of %{name}

%description -n vst-%{name}
A VST version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}

%description -n lv2-%{name}
A LV2 version of %{name}

%package -n dssi-%{name}
Summary: DSSI version of %{name}

%description -n dssi-%{name}
A DSSI version of %{name}

%prep

%autosetup -n %{name}

sed -i -e "s|set(CMAKE_CXX_FLAGS \"|set(CMAKE_CXX_FLAGS \"\${CMAKE_CXX_FLAGS} |g" libzynayumi/CMakeLists.txt

%build

%set_build_flags

# Build libzynayumi
cd libzynayumi
%if 0%{?fedora} >= 38
%cmake -DCMAKE_CXX_FLAGS="-include cstdint $CXXFLAGS"
%else
%cmake
%endif
%cmake_build
rm -rf build
mv %{__cmake_builddir} build
cd ..

%make_build SKIP_STRIPPING=true VERBOSE=true

# Replace integers by floats to workaround so possible incompatibility issues
PRESETS_FILE=bin/zynayumi.lv2/presets.ttl
sed 's/pset:value[[:space:]]\(-\?[[:digit:]]\+\)[[:space:]]/pset:value \1.0/' -i "${PRESETS_FILE}"

%install

%make_install SKIP_STRIPPING=true VERBOSE=true

mkdir -p %{buildroot}/%{_bindir}/
cp bin/%{name} %{buildroot}/%{_bindir}/

mkdir -p %{buildroot}/%{_libdir}/lv2/
cp -r bin/%{name}.lv2 %{buildroot}/%{_libdir}/lv2/

mkdir -p %{buildroot}/%{_libdir}/vst/
cp bin/%{name}-vst.so %{buildroot}/%{_libdir}/vst/

mkdir -p %{buildroot}/%{_libdir}/dssi/
cp bin/%{name}-dssi.so %{buildroot}/%{_libdir}/dssi/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n dssi-%{name}
%{_libdir}/dssi/*

%changelog
* Sun Nov 07 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
