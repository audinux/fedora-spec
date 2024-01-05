# Tag: Jack, Synthesizer
# Type: Standalone, VST3, LV2
# Category: Synthesizer

%define commit0 c5c2db18f522ddf0e287d242877668f674c2c910

Name: voc
Version: 0.0.1
Release: 2%{?dist}
Summary: wacky vocal synth VST
License: GPL-2.0-or-later
URL: https://github.com/FigBug/Voc

Vendor:       Audinux
Distribution: Audinux

# ./figbug-source.sh <project> <tag>
# ./figbug-source.sh Voc master

Source0: Voc.tar.gz
Source1: figbug-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel
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
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: desktop-file-utils

%description
wacky vocal synth VST

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-2.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-2.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n Voc

%build

%set_build_flags
export CFLAGS="`pkg-config --cflags gtk+-x11-3.0` $CFLAGS"
export CXXFLAGS="`pkg-config --cflags gtk+-x11-3.0` $CXXFLAGS"

cd plugin
Projucer --resave Voc.jucer

cd Builds/LinuxMakefile
sed -i -e "s/-Wl,--strip-all/ /g" Makefile

%make_build CONFIG=Release STRIP=true

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_bindir}/

install -m 755 -p plugin/Builds/LinuxMakefile/build/Voc %{buildroot}/%{_bindir}/
cp -ra plugin/Builds/LinuxMakefile/build/Voc.vst3 %{buildroot}/%{_libdir}/vst3/
cp -ra plugin/Builds/LinuxMakefile/build/Voc.lv2 %{buildroot}/%{_libdir}/lv2/
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp plugin/Resources/logo.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Voc
Exec=Voc
Icon=/usr/share/pixmaps/%{name}
Comment=wacky vocal synth
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
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Sat Aug 05 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to 0.0.1-2 - fix install

* Wed Jan 11 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
