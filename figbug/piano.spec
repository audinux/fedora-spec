# Status: active
# Tag: Jack, Synthesizer
# Type: Standalone, VST3, VST, LV2
# Category: Synthesizer

Name: piano
Version: 1.0.2
Release: 3%{?dist}
Summary: Piano VST / LV2 plugin
License: GPL-2.0-or-later
URL: https://github.com/FigBug/Piano
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./figbug-source.sh <project> <tag>
# ./figbug-source.sh Piano v1.0.2

Source0: Piano.tar.gz
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
A digital waveguide piano physical model with VST and command line interface.

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
%autosetup -n Piano

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/vst/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_bindir}/

cp -ra %{__cmake_builddir}/Piano_artefacts/Standalone/* %{buildroot}/%{_bindir}/
cp -ra %{__cmake_builddir}/Piano_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Piano_artefacts/VST/* %{buildroot}/%{_libdir}/vst/
cp -ra %{__cmake_builddir}/Piano_artefacts/LV2/* %{buildroot}/%{_libdir}/lv2/

install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Piano
Exec=Piano
Comment=Piano synthesizer
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
%license COPYING

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Fri Jan 02 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-3
- update to 1.0.2-3

* Sun Aug 31 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-3
- update to 0.0.1-3

* Sat Aug 05 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to 0.0.1-2 - fix install

* Thu Jan 12 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
