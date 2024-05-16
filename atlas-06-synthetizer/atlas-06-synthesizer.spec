# Tag: Synthesizer
# Type: Standalone, VST3
# Category: Audio, Synthesizer

Name:    atlas-06-synthesizer
Version: 0.0.1
Release: 1%{?dist}
Summary: A subtractive software synthesizer built using the JUCE framework
License: GPL-3.0-or-later
URL:     https://github.com/sbadon122/ATLAS-06-Synthesizer
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./source-atlas.sh <tag>
#        ./source-atlas.sh master

Source0: ATLAS-06-Synthesizer.tar.gz
Source1: atlas-06-synthesizer.png
Source2: source-atlas.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel
BuildRequires: freetype-devel
BuildRequires: libcurl-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel
BuildRequires: pkgconfig(jack)
BuildRequires: vst3sdk
BuildRequires: desktop-file-utils

%description
A subtractive software synthesizer built using the JUCE framework.
It currently builds to vst, vst3 and audio unit. This synthesizer
is inspired by 80s synths and its signal flow is a mix of a Roland
Juno-06 and Roland Juno-106. Installer included with repo.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n ATLAS-06-Synthesizer

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -rav %{__cmake_builddir}/ATLAS-06_artefacts/ATLAS-06.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_bindir}/
cp -rav %{__cmake_builddir}/ATLAS-06_artefacts/ATLAS-06 %{buildroot}/%{_bindir}

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp %{SOURCE1} %{buildroot}/%{_datadir}/pixmaps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name
Exec=%{name}
Icon=%{name}
Comment=ATLAS 06 Synthesizer
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
# validator %{buildroot}/%{_libdir}/vst3/ATLAS-06.vst3

%files
%doc README.md
%license LICENSE.md
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Thu Jul 27 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
