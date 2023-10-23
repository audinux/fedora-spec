Name:    sickbeatbetty
Version: 1.0.3
Release: 1%{?dist}
Summary: An open source MIDI drum machine / generator VST and standalone application
License: GPL-3.0-or-later
URL:     https://github.com/jthwho/SickBeatBetty

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./source-sickbeatbetty.sh v1.0.3

Source0: SickBeatBetty.tar.gz
Source1: source-sickbeatbetty.sh

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
A MIDI VST/AU plugin for generating, well, sick beats.
It uses the JUCE library which makes it cross platform.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n SickBeatBetty

sed -i -e "s|\"-DCMAKE_BUILD_TYPE=Debug\"|\"-DCMAKE_BUILD_TYPE=Debug\" \"-DCMAKE_CXX_FLAGS='-include utility -fPIC'\"|g" JUCE/extras/Build/juceaide/CMakeLists.txt
sed -i -e "s|Sick Beat Betty|SickBeatBetty|g" CMakeLists.txt

%build

%set_build_flags

%cmake -DCMAKE_CXX_FLAGS="$CXXFLAGS -include utility -fPIC"
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_bindir}

cp -ra %{__cmake_builddir}/SICKBEATBETTY_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/SICKBEATBETTY_artefacts/Standalone/* %{buildroot}%{_bindir}/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp icons/sbb.ico %{buildroot}/%{_datadir}/pixmaps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Sick Beat Betty
Exec=%{name}
Icon=sbb
Comment=MIDI drum machine
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

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Fri Mar 03 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.3-1
- Initial spec file
