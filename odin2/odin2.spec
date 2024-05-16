# Tag: Jack, Alsa
# Type: Plugin, Standalone, VST3, CLAP, LV2
# Category: Audio, Synthesizer

Name: odin2
Version: 2.3.4
Release: 5%{?dist}
Summary: A VST3 Synthesizer
License: GPL-2.0-or-later
URL: https://github.com/TheWaveWarden/odin2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./odin-sources.sh <TAG>
#        ./odin-sources.sh v2.3.4

Source0: odin2.tar.gz
Source1: odin-sources.sh
Patch0:  odin2-0001-soundbanks-in-share.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: lv2-devel
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
BuildRequires: desktop-file-utils

%description
Odin 2 Synthesizer Plugin

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n clap-%{name}
CLAP version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -p1 -n %{name}

sed -i -e "s/\"-DJUCE_BUILD_HELPER_TOOLS=ON\"/\"-DJUCE_BUILD_HELPER_TOOLS=ON\" \"-DCMAKE_CXX_FLAGS='-include utility -fPIC'\"/g" libs/JUCE/extras/Build/juceaide/CMakeLists.txt

sed -i -e "s/\"-DJUCE_BUILD_HELPER_TOOLS=ON\"/\"-DJUCE_BUILD_HELPER_TOOLS=ON\" \"-DCMAKE_CXX_FLAGS='-include utility -fPIC'\"/g" libs/JUCELV2/extras/Build/juceaide/CMakeLists.txt

%build

%set_build_flags
%cmake -DCMAKE_CXX_FLAGS="-include utility -fPIC $CXXFLAGS"
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_libdir}/clap/
install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -d %{buildroot}%{_datadir}/odin2/Soundbanks/

cp -r Soundbanks/* %{buildroot}%{_datadir}/odin2/Soundbanks/
rm %{buildroot}%{_datadir}/odin2/Soundbanks/User\ Patches/.gitignore

install -m 755 -p %{__cmake_builddir}/Odin2_artefacts/Standalone/Odin2 %{buildroot}/%{_bindir}/
cp -ra %{__cmake_builddir}/Odin2_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Odin2_artefacts/LV2/* %{buildroot}/%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/Odin2_artefacts/CLAP/* %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp screenshot.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name
Exec=Odin2
Icon=/usr/share/pixmaps/%{name}
Comment=Odin 2 Synthesizer
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md change_log.md
%license LICENSE
%{_bindir}/*
%{_datadir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Sat Feb 25 2023 Yann Collette <ycollette.nospam@free.fr> - 2.3.4-5
- update to 2.3.4-5 - fix desktop file - use cmake

* Tue Aug 09 2022 Yann Collette <ycollette.nospam@free.fr> - 2.3.4-4
- update to 2.3.4-4

* Tue Jun 14 2022 Yann Collette <ycollette.nospam@free.fr> - 2.3.3-4
- update to 2.3.3-4

* Sat Jun 11 2022 Yann Collette <ycollette.nospam@free.fr> - 2.3.2-4
- update to 2.3.2-4

* Fri Aug 20 2021 Yann Collette <ycollette.nospam@free.fr> - 2.3.1-4
- add LV2 version

* Wed Aug 18 2021 Yann Collette <ycollette.nospam@free.fr> - 2.3.1-2
- update to 2.3.1-2

* Mon Oct 26 2020 Yann Collette <ycollette.nospam@free.fr> - 2.2.4-2
- fix install

* Sat Oct 24 2020 Yann Collette <ycollette.nospam@free.fr> - 2.2.4-1
- Initial spec file
