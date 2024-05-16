# Tag: Jack, Alsa
# Type: Plugin, Standalone, VST3
# Category: Audio

%global commit0 e69ebe0eb2752243de4678fe84df298555730c94

Name: bridgelite
Version: 1.0.5
Release: 1%{?dist}
Summary: 8 string guitar virtual instrument with one extra octave below for good measure!
License: GPL-3.0-or-later
URL: https://github.com/JamesStubbsEng/8ridgelite
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/JamesStubbsEng/8ridgelite/archive/%{commit0}.zip#/%{name}-%{version}.zip
Source1: build.tar.gz
Patch0: bridgelite-0001-fix-path.patch

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: JUCE60
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
BuildRequires: webkit2gtk3-devel

%description
8 string guitar virtual instrument with one extra octave below for good measure!

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -p1 -n 8ridgelite-%{commit0}

tar xvfz %{SOURCE1}

%build

%set_build_flags

cd Builds/LinuxMakefile/

export CXXFLAGS="-I/usr/src/JUCE61/modules/ $CXXFLAGS"

%make_build STRIP=true CONFIG=Release

%install

install -m 755 -d %{buildroot}%{_datadir}/Bridgelite/sound/
cp -r 8ridgelite_20sec_wav/* %{buildroot}%{_datadir}/Bridgelite/sound/

cd Builds/LinuxMakefile/build/

install -m 755 -d %{buildroot}%{_bindir}/
cp -a 8ridge_lite %{buildroot}/%{_bindir}/Bridgelite

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra 8ridge_lite.vst3 %{buildroot}/%{_libdir}/vst3/

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/Bridgelite/sound/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Wed Apr 03 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.5-1
- Initial spec file
