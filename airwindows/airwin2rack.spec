# Tag: Effect
# Type: Plugin, VST
# Category: Audio, Effect

Name: airwin2rack
Version: 2.11.0
Release: 1%{?dist}
Summary: Airwindows, Consolidated into a single Library, Rack Plugin and DAW Plugin
License: MIT
URL: https://github.com/baconpaul/airwin2rack

Vendor:       Audinux
Distribution: Audinux

# Usage: ./airwin2rack-source.sh <TAG>
#        ./airwin2rack-source.sh v2.11.0

Source0: airwin2rack.tar.gz
Source2: airwin2rack-source.sh

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
BuildRequires: pkgconfig(jack)
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel

%description
Airwindows, Consolidated into a single Library, Rack Plugin and DAW Plugin

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: MIT
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: MIT
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: MIT
Requires: %{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n %{name}

sed -i -e "s/Airwindows Consolidated/Airwindows_Consolidated/g" src-juce/CMakeLists.txt

%build

%cmake -DBUILD_JUCE_PLUGIN=ON

%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -rav %{__cmake_builddir}/src-juce/airwin-consolidated_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -rav %{__cmake_builddir}/src-juce/airwin-consolidated_artefacts/LV2/* %{buildroot}/%{_libdir}/lv2/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -rav %{__cmake_builddir}/src-juce/airwin-consolidated_artefacts/CLAP/* %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}%{_bindir}/
cp -rav %{__cmake_builddir}/src-juce/airwin-consolidated_artefacts/Standalone/* %{buildroot}/%{_bindir}/

%files
%doc README.md
%license LICENSE.md
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Tue May 07 2024 Yann Collette <ycollette.nospam@free.fr> - 2.11.0-1
- Initial spec file
