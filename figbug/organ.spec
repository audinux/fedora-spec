# Status: active
# Tag: Jack, Synthesizer, Organ
# Type: Standalone, VST3, VST, LV2
# Category: Synthesizer

Name: organ
Version: 1.0.1
Release: 5%{?dist}
Summary: Organ VST / LV2 plugin
License: GPL-3.0-or-later
URL: https://github.com/FigBug/Organ
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./figbug-source.sh <project> <tag>
# ./figbug-source.sh Organ v1.0.1

Source0: Organ.tar.gz
Source1: figbug-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: gtk3-devel
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
BuildRequires: desktop-file-utils

%description
Organ VST / LV2 plugin

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-2.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-2.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n vst-%{name}
Summary: VST2 version of %{name}
License: GPL-2.0-or-later
Requires: license-%{name}

%description -n vst-%{name}
VST2 version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-2.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n Organ

%build

%set_build_flags
export CXXFLAGS="-Wno-implicit-function-declaration $CXXFLAGS"
export CFLAGS="-Wno-implicit-function-declaration $CFLAGS"

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/vst/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_bindir}/

install -m 755 -p %{__cmake_builddir}/Organ_artefacts/Standalone/Organ %{buildroot}/%{_bindir}/
cp -ra %{__cmake_builddir}/Organ_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Organ_artefacts/VST/* %{buildroot}/%{_libdir}/vst/
cp -ra %{__cmake_builddir}/Organ_artefacts/LV2/* %{buildroot}/%{_libdir}/lv2/

install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp plugin/setBfree/doc/setBfree.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Organ
Exec=Organ
Icon=/usr/share/pixmaps/%{name}
Comment=Organ synthesizer
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
%{_bindir}/*
%{_datadir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Fri Jan 02 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-5
- update to 1.0.1-5

* Sun Aug 31 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-5
- update to 0.0.1-5 - remove unused dep, update to last master

* Sat Apr 06 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-4
- update to 0.0.1-4 - update to last master e68789573184c92fe9b6ae1b3139864283f7b762

* Wed Sep 06 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-3
- update to 0.0.1-3 - update to last master b4c6cbe29e8bd69c65afef1e8e4db94a995abce9

* Sat Aug 05 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to 0.0.1-2 - fix install and update to last master - b082cd2b

* Thu Jan 12 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
