%define commit0 5a829b37904914c2d547c52959679754e84ca66d

Name:    organ
Version: 0.0.1
Release: 1%{?dist}
Summary: Organ VST / LV2 plugin
License: GPLv2+
URL:     https://github.com/FigBug/Organ

Vendor:       Audinux
Distribution: Audinux

# ./figbug-source.sh <project> <tag>
# ./figbug-source.sh Organ master

Source0: Organ.tar.gz
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
Organ VST / LV2 plugin

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPLv2+
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPLv2+
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n Organ

%build

%set_build_flags
export CFLAGS="`pkg-config --cflags gtk+-x11-3.0` $CFLAGS"
export CXXFLAGS="`pkg-config --cflags gtk+-x11-3.0` $CXXFLAGS"

cd plugin
Projucer --resave Organ.jucer

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

install -m 755 -p plugin/Builds/LinuxMakefile/build/Organ %{buildroot}/%{_bindir}/
cp -ra plugin/Builds/LinuxMakefile/build/Organ.vst3/* %{buildroot}/%{_libdir}/vst3/
cp -ra plugin/Builds/LinuxMakefile/build/Organ.lv2/* %{buildroot}/%{_libdir}/lv2/
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
%license LICENSE
%{_bindir}/*
%{_datadir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Thu Jan 12 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
