# Tag: Guitar, Effect
# Type: Plugin, LV2, VST
# Category: Audio, Effect

Name:    BYOD
Version: 1.2.0
Release: 1%{?dist}
Summary: Build-your-own guitar distortion !
License: GPL-3.0-or-later
URL:     https://github.com/Chowdhury-DSP/BYOD

Vendor:       Audinux
Distribution: Audinux

# Usage: ./source_byod.sh <tag>
#        ./source_byod.sh v1.2.0

Source0: BYOD.tar.gz
Source1: source_byod.sh

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: libcurl-devel
BuildRequires: freetype-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel
BuildRequires: lv2-devel
BuildRequires: xorg-x11-server-Xvfb
BuildRequires: desktop-file-utils

%description
BYOD is a guitar distortion plugin with a customisable signal chain
that allows users to create their own guitar distortion effects.
The plugin contains a wide variety of distortion effects from analog
modelled circuits to purely digital creations, along with some
musical tone-shaping filters, and a handful of other useful
processing blocks.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n %{name}

sed -i -e "s|\"-DCMAKE_BUILD_TYPE=Debug\"|\"-DCMAKE_BUILD_TYPE=Debug\" \"-DCMAKE_CXX_FLAGS='-include utility -fPIC'\"|g" modules/JUCE/extras/Build/juceaide/CMakeLists.txt

%build

%define X_display ":98"
#############################################
### Launch a virtual framebuffer X server ###
#############################################
export DISPLAY=%{X_display}
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 10

%set_build_flags

%cmake -DCMAKE_CXX_FLAGS="$CXXFLAGS -include utility -fPIC"
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -m 755 -d %{buildroot}%{_datadir}/applications/

cp -ra %{__cmake_builddir}/BYOD_artefacts/VST3/BYOD.vst3 %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/BYOD_artefacts/LV2/BYOD.lv2 %{buildroot}%{_libdir}/lv2/
cp %{__cmake_builddir}/BYOD_artefacts/Standalone/BYOD %{buildroot}%{_bindir}/

cp res/logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/BYOD.svg

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%name
Exec=%{name}
Icon=BYOD
Comment="Build Your Own Distortion"
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --add-category="AudioVideo;Audio;Music"    \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/BYOD.svg

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Wed Aug 02 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-1
- update to 1.2.0-1

* Sat Jan 14 2023 Yann Collette <ycollette.nospam@free.fr> - 1.1.3-1
- update to 1.1.3-1

* Tue Jul 26 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-1
- Initial spec file
