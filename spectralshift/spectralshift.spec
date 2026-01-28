# Status: active
# Tag: Pitch
# Type: Plugin, VST3, LV2, CLAP
# Category: Effect

Name: spectralshift
Version: 0.1.1
Release: 1%{?dist}
Summary: Pitch shifter plugin made using SignalSmith Stretch Library and JUCE
License: MIT
URL: https://github.com/trencrumb/SpectralShift
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/trencrumb/SpectralShift/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
Spectral Shift is a pitch-shifting plugin built with JUCE and Signalsmith’s Stretch library.
The project was developed as part of the MyWorld Fellowship in Residence with Wounded Buffalo Studios.
More info about the fellowship can be found here.
It’s loosely inspired by Minimal Audio’s Formant Shift, but takes a different approach by combining
pitch and formant shifting into a 2D control space.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: MIT

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: MIT
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: MIT
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: MIT
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n SpectralShift-%{version}

sed -i -e "s|set(PRODUCT_NAME \"Spectral Shift\")|set(PRODUCT_NAME \"Spectral_Shift\")|g" CMakeLists.txt

%ifarch aarch64
sed -i -e "/(-march=x86-64-v2)/d" CMakeLists.txt
%endif

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/SpectralShift_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/SpectralShift_artefacts/LV2/*  %{buildroot}/%{_libdir}/lv2/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra %{__cmake_builddir}/SpectralShift_artefacts/CLAP/*  %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/SpectralShift_artefacts/Standalone/*  %{buildroot}/%{_bindir}/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE.txt

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Tue Jan 27 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.1-1
- Initial spec file
