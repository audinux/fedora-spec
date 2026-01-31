# Status: active
# Tag: Effect
# Type: Plugin, VST3, Standalone
# Category: Audio, Effect

Name: cstop
Version: 2.0.0
Release: 1%{?dist}
Summary: Free tape stop audio effect plugin
License: MIT
URL: https://github.com/calgoheen/cStop
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./cstop-source.sh <tag>
#        ./cstop-source.sh v2.0.0

Source0: cStop.tar.gz
Source1: cstop.png
Source2: cstop-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: nodejs-npm
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
BuildRequires: gtk3-devel
BuildRequires: pkgconfig(jack)
BuildRequires: webkit2gtk4.1-devel
BuildRequires: desktop-file-utils

%description
cStop is a tape stop audio effect plugin

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

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: MIT
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n cStop

# Release the requirement on cmake 4.0.0
sed -i -e "s|cmake_minimum_required(VERSION 4.0 FATAL_ERROR)|cmake_minimum_required(VERSION 3.30 FATAL_ERROR)|g" CMakeLists.txt

# Create a missing directory
mkdir -p ui/dist

%build

# Fix a problem on rawhide: nodejs has no node executable only a node-22.
# Same for npm
if [ ! -f /usr/bin/npm ]; then
  mkdir -p `pwd`/npm/bin/
  ln -s /usr/bin/npm-22 `pwd`/npm/bin/npm
  ln -s /usr/bin/node-22 `pwd`/npm/bin/node
  export PATH=`pwd`/npm/bin/:$PATH
fi

%set_build_flags

%cmake -DCMAKE_CXX_FLAGS="`pkg-config --cflags webkit2gtk-4.1` `pkg-config --cflags gtk+-3.0` $CXXFLAGS"
%cmake_build

%install

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/clap/

cp -ra %{__cmake_builddir}/cStop_artefacts/Standalone/* %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/cStop_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/cStop_artefacts/CLAP/* %{buildroot}%{_libdir}/clap/

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
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%files -n license-%{name}
%doc README.md VERSION
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Fri Jan 30 2026 Yann Collette <ycollette.nospam@free.fr> - 2.0.0-1
- update to 2.0.0-1

* Thu Jun 26 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-1
- update to 1.0.1-1

* Sun Aug 20 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
