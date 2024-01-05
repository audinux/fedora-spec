# Tag: Effect
# Type: VST3, Standalone
# Category: Audio, Plugin

Name: cstop
Version: 1.0.0
Release: 1%{?dist}
Summary: Free tape stop audio effect plugin
License: MIT
URL: https://github.com/calgoheen/cStop

Vendor:       Audinux
Distribution: Audinux

# Usage: ./cstop-source.sh <tag>
#        ./cstop-source.sh v1.0.0

Source0: cStop.tar.gz
Source1: cstop.png
Source2: cstop-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
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
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: desktop-file-utils

%description
cStop is a tape stop audio effect plugin

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  MIT
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -p1 -n cStop

%build

%set_build_flags

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -d %{buildroot}%{_libdir}/vst3/

cp -ra %{__cmake_builddir}/cStop_artefacts/Standalone/* %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/cStop_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp %{SOURCE1} %{buildroot}/%{_datadir}/pixmaps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/cstop.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=cStop
Exec=cStop
Icon=cstop
Comment=cStop
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/cstop.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/cstop.desktop

%files
%doc README.md VERSION
%license LICENSE
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Sun Aug 20 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
