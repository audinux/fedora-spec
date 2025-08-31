# Status: inactive
# Tag: Jack, Synthesizer
# Type: Standalone, VST3, LV2
# Category: Synthesizer

# Build failure

%define commit0 b513412581e3adeaf91cc4996edb2650894ebad6

Name: virtualanalog
Version: 0.0.1
Release: 3%{?dist}
Summary: Virtual Analog VST
License: BSD-3-Clause
URL: https://github.com/FigBug/VirtualAnalog
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./figbug-source.sh <project> <tag>
# ./figbug-source.sh VirtualAnalog master

Source0: VirtualAnalog.tar.gz
Source1: figbug-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: gtk3-devel
BuildRequires: JUCE
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
Virtual Analog VST / LV2 plugin

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

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-2.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n VirtualAnalog

%build

%set_build_flags
export CFLAGS="`pkg-config --cflags gtk+-x11-3.0` $CFLAGS"
export CXXFLAGS="`pkg-config --cflags gtk+-x11-3.0` $CXXFLAGS"

cd plugin
Projucer --resave VirtualAnalog.jucer

cd Builds/LinuxMakefile
sed -i -e "s/-Wl,--strip-all/ /g" Makefile

%make_build CONFIG=Release STRIP=true

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_bindir}/

install -m 755 -p plugin/Builds/LinuxMakefile/build/VirtualAnalog %{buildroot}/%{_bindir}/
cp -ra plugin/Builds/LinuxMakefile/build/VirtualAnalog.vst3 %{buildroot}/%{_libdir}/vst3/
cp -ra plugin/Builds/LinuxMakefile/build/VirtualAnalog.lv2 %{buildroot}/%{_libdir}/lv2/

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

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Sun Aug 31 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-3
- update to 0.0.1-2 - remove unused dep

* Sat Aug 05 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to 0.0.1-2 - fix install

* Thu Jan 12 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
