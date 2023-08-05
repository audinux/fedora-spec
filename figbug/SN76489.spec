%define commit0 7564e8b71de31d44913c52a890ef918ef05604ab

Name:    SN76489
Version: 0.0.1
Release: 2%{?dist}
Summary: Sega Master System Sound Chip VST
License: LGPLv2+
URL:     https://github.com/FigBug/SN76489

Vendor:       Audinux
Distribution: Audinux

# ./figbug-source.sh <project> <tag>
# ./figbug-source.sh SN76489 master

Source0: SN76489.tar.gz
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
Sega Master System Sound Chip VST

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
%autosetup -n SN76489

%build

%set_build_flags
export CFLAGS="`pkg-config --cflags gtk+-x11-3.0` $CFLAGS"
export CXXFLAGS="`pkg-config --cflags gtk+-x11-3.0` $CXXFLAGS"

cd plugin
Projucer --resave SN76489.jucer

cd Builds/LinuxMakefile
sed -i -e "s/-Wl,--strip-all/ /g" Makefile
%ifarch aarch64
sed -i -e "s/-m64/ /g" Makefile
%endif
%make_build CONFIG=Release STRIP=true

%install 

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_bindir}/

install -m 755 -p plugin/Builds/LinuxMakefile/build/SN76489 %{buildroot}/%{_bindir}/
cp -ra plugin/Builds/LinuxMakefile/build/SN76489.vst3 %{buildroot}/%{_libdir}/vst3/
cp -ra plugin/Builds/LinuxMakefile/build/SN76489.lv2 %{buildroot}/%{_libdir}/lv2/
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp plugin/Resources/logo.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=SN76489
Exec=SN76489
Icon=/usr/share/pixmaps/%{name}
Comment=Sega Master System Sound Chip
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

* Fri Feb 24 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
