%define commit0 c5567a3fe737ae76d9083bd664d1b93b501333b4
Name:    modeq
Version: 0.4.0
Release: 1%{?dist}
Summary: Free EQ audio plugin with modulation
License: GPL-3.0-only
URL:     https://github.com/tobanteAudio/modEQ

Vendor:       Audinux
Distribution: Audinux

# ./modeq-source.sh <tag>
# ./modeq-source.sh c5567a3fe737ae76d9083bd664d1b93b501333b4

Source0: modEQ.tar.gz
Source1: modeq.png
Source2: modeq-source.sh

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
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: desktop-file-utils

%description
EQ audio effects plugin with modulation.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-only
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n modEQ

%build

%cmake
%cmake_build

%install

install -d 755 %{buildroot}/%{_bindir}/
install -d 755 %{buildroot}/%{_libdir}/vst3/

cp -ra %{__cmake_builddir}/plugin/modEQ_artefacts/Standalone/* %{buildroot}/%{_bindir}
cp -ra %{__cmake_builddir}/plugin/modEQ_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp %{SOURCE1} %{buildroot}/%{_datadir}/pixmaps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/modeq.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=modEQ
Exec=modEQ
Icon=modeq
Comment=modEQ
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/modeq.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/modeq.desktop

%files
%doc README.md
%license LICENSE.md
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Mon Aug 28 2023 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-1
- Initial build
