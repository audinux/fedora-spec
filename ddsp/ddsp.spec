# Tag: Synthesizer, Effect
# Type: Standalone, VST3
# Category: Synthesizer, Effect

Name:    ddsp
Version: 1.1.0
Release: 1%{?dist}
Summary: Realtime DDSP Neural Synthesizer and Effect
URL:     https://github.com/tank-trax/ddsp-vst
ExclusiveArch: x86_64 aarch64
License: Apache-v2

Vendor:       Audinux
Distribution: Audinux

# Usage: ./ddps-source.sh <TAG>
# ./ddsp-source.sh v1.1.0

Source0: ddsp-vst.tar.gz
Source1: ddsp-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: libX11-devel
BuildRequires: mesa-libGL-devel
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel
BuildRequires: libcurl-devel
BuildRequires: libXinerama-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel
BuildRequires: chrpath
BuildRequires: desktop-file-utils

%description
VST3/AU plugins and desktop applications built using the JUCE framework and DDSP.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n %{name}-vst

sed -i -e "s/DDSP Effect/DDSP_Effect/g" CMakeLists.txt
sed -i -e "s/DDSP Synth/DDSP_Synth/g" CMakeLists.txt

%build

%set_build_flags
%cmake -DCMAKE_CXX_FLAGS="-include cstdint -include utility -fPIC $CXXFLAGS" \
       -DCMAKE_C_FLAGS="-fPIC $CFLAGS"

# Remove -Werror from content downloaded by cmake
sed -i -e "s/-Werror / /g" %{__cmake_builddir}/flatbuffers/CMakeLists.txt
sed -i -e "s/-Werror / /g" %{__cmake_builddir}/flatbuffers/tests/fuzzer/CMakeLists.txt
sed -i -e "/-Werror/d" %{__cmake_builddir}/eigen/CMakeLists.txt

%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/models/

install -m 755 %{__cmake_builddir}/DDSPEffect_artefacts/Standalone/* %{buildroot}%{_bindir}/
install -m 755 %{__cmake_builddir}/DDSPSynth_artefacts/Standalone/* %{buildroot}%{_bindir}/

cp -ra  %{__cmake_builddir}/DDSPEffect_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra  %{__cmake_builddir}/DDSPSynth_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/

cp -ra models/* %{buildroot}%{_datadir}/%{name}/models/

# Fix RPATH

chrpath --delete %{buildroot}%{_bindir}/DDSP_Effect
chrpath --delete %{buildroot}%{_bindir}/DDSP_Synth

chrpath --delete `find %{buildroot}%{_libdir}/vst3/DDSP_Effect.vst3 -name DDSP_Effect.so`
chrpath --delete `find %{buildroot}%{_libdir}/vst3/DDSP_Synth.vst3 -name DDSP_Synth.so`

# Install icon

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 assets/icons/logo_thin.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/ddsp.svg

# Install desktop files

install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/DDSP_Effect.desktop <<EOF
[Desktop Entry]
Name=DDSP Effect
Exec=DDSP_Effect
Icon=ddsp
Comment=DDSP Effect
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/DDSP_Synth.desktop <<EOF
[Desktop Entry]
Name=DDSP Synth
Exec=DDSP_Synth
Icon=ddsp
Comment=DDSP Synth
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/DDSP_Effect.desktop

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/DDSP_Synth.desktop

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/DDSP_Effect.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/DDSP_Synth.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/%{name}/models/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/scalable/apps/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Tue Feb 07 2023 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- Initial spec file
