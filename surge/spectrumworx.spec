# Status: active
# Tag: Effect
# Type: Plugin, CLAP
# Category: Effect

%global _cmake_shared_libs %{nil}

Name: spectrumworx
Version: 20260901
Release: 1%{?dist}
Summary: A port of Little Endian's SpectrumWorx effect plugin to modern plugin standards
License: GPL-3.0-or-later
URL: https://github.com/surge-synthesizer/SpectrumWorx
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./source-surge.sh <project> <tag>
#        ./source-surge.sh SpectrumWorx main

Source0: SpectrumWorx.tar.gz
Source1: source-surge.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libcurl-devel
BuildRequires: gtk3-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libX11-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: desktop-file-utils

Requires: license-%{name}
Requires: common-%{name}

%description
SpectrumWorx is an awesome spectral effect originally developed and released by Little Endian,
where development ended in 2016 and the plugin was open sourced in 2024.
You can find the original source code dump here: https://github.com/LittleEndianLtd/SpectrumWorx
As with all folks who have decided to open source great commercial products at the end of their
development, we are very grateful to Little Endian for making this decision.
In 2026, when a KvR thread brought this to our attention, we grabbed it and started modernizing.
This involved heavy use of Claude Opus 5 and Fable 5 to port the product to modern standards,
including:
- Moving from VST2 Windows and macOS only to CLAP, clap-wrapper for Windows, macOS and Linux
- Setting up reliable GitHub action pipelines and binary builds
- Modernizing the code, including removing old libraries (JUCE 2, Boost...)
- Making substantial improvements to the threading and ownership model
- Adding tests to cover the engine
- Vectorizing the skin
- Inferring technical documentation
That was a heavy three weeks of plan/iterate/generate/test/repeat cycle using machine tools almost
entirely to generate the ported code, while preserving the DSP code and operating model.
Right now, this is a bit of a work-in-prgoress as we figure out if we can move it from a two week
sprint to an official 3.0 release from the team.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n common-%{name}
Summary: Common data files for %{name}
License: GPL-3.0-or-later

%description -n common-%{name}
Common data files for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}
Requires: common-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}
Requires: common-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n SpectrumWorx

sed -i -e "/swWarningBaseline -Werror/d" cmake/sw-our-sources.cmake

%build

%set_build_flags
export CXXFLAGS=`echo $CXXFLAGS | sed -e "s/-Werror=format-security//g"`
export LDFLAGS="`pkg-config --libs-only-L jack` $LDFLAGS"

%cmake -DGIT_COMMIT_HASH="00000000" \
       -DBUILD_SHARED_LIBS:BOOL=OFF \
       -DSW_BUILD_TOOLS=OFF \
       -DSW_BUILD_TESTS=OFF \
       -DSW_WERROR=OFF
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 %{__cmake_builddir}/sw_assets/SpectrumWorx %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}/%{_libdir}/clap/
install -m 755 %{__cmake_builddir}/sw_assets/SpectrumWorx.clap %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/sw_assets/SpectrumWorx.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/
cp -ra assets/presets %{buildroot}/%{_datadir}/%{name}/
cp -ra assets/samples %{buildroot}/%{_datadir}/%{name}/
cp -ra assets/skin %{buildroot}/%{_datadir}/%{name}/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp assets/installer/SpectrumWorxIcon.ico %{buildroot}/%{_datadir}/pixmaps/%{name}.ico

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/1024x1024/apps/
cp assets/installer/SpectrumWorxIcon.png %{buildroot}/%{_datadir}/icons/hicolor/1024x1024/apps/%{name}.png

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=%{name}
Icon=%{name}
Comment=A port of Little Endian's SpectrumWorx effect plugin to modern plugin standards
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.ico
%{_datadir}/icons/hicolor/1024x1024/apps/%{name}.png

%files -n common-%{name}
%{_datadir}/%{name}/presets/*
%{_datadir}/%{name}/samples/*
%{_datadir}/%{name}/skin/*

%files -n license-%{name}
%doc README.md
%license LICENSE LICENSING.md

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Tue Sep 01 2026 Yann Collette <ycollette.nospam@free.fr> - 20260901-1
- update to 20260901-1

* Sun Aug 23 2026 Yann Collette <ycollette.nospam@free.fr> - 20260822-1
- Initial spec file
