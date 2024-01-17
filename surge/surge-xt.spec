%define _lto_cflags %{nil}

# Tag: Reverb, Compressor, Equalizer, Overdrive
# Type: Plugin, VST3, Standalone
# Category: Audio, Effect, Synthesizer

Name:    surge-xt
Version: 1.3.0
Release: 2%{?dist}
Summary: A VST3 Synthesizer and Effects, including Airwindows
License: GPL-2.0-or-later
URL:     https://github.com/surge-synthesizer/surge

Vendor:       Audinux
Distribution: Audinux

# To get the sources, use:
# $ ./source-surge.sh release_xt_1.3.0

Source0: surge.tar.gz
Source1: source-surge.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: rsync
BuildRequires: git
BuildRequires: python3
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
BuildRequires: pkgconfig(jack)
BuildRequires: desktop-file-utils

%description
A VST3 Synthesizer and Effects, including Airwindows

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -p1 -n surge

sed -i -e "/Werror=/d" CMakeLists.txt
sed -i -e "/:-Werror/d" CMakeLists.txt

sed -i -e "s/Surge XT/Surge_XT/g" CMakeLists.txt
sed -i -e "s/Surge XT/Surge_XT/g" resources/CMakeLists.txt
sed -i -e "s/Surge XT/Surge_XT/g" src/surge-fx/CMakeLists.txt
sed -i -e "s/Surge XT/Surge_XT/g" src/CMakeLists.txt
sed -i -e "s/Surge XT/Surge_XT/g" src/surge-xt/CMakeLists.txt

sed -i -e "s/Surge_XT Effects/Surge_XT_Effects/g" src/surge-fx/CMakeLists.txt

%build

%set_build_flags

%cmake \
%if 0%{?fedora} >= 38
       -DCMAKE_CXX_FLAGS="-include cstdint -fPIC $CXXFLAGS" \
%endif
       -DBUILD_SHARED_LIBS=OFF
%cmake_build

%install

%cmake_install

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/Surge-XT.desktop <<EOF
[Desktop Entry]
Categories=AudioVideo;Audio;
Comment=Free Open Source Hybrid Synthesizer
Exec="/usr/bin/Surge_XT"
GenericName=Surge XT
Icon=surge-xt
MimeType=
Name=Surge XT
NoDisplay=false
Path=
StartupNotify=true
Terminal=false
TerminalOptions=
Type=Application
EOF

cat > %{buildroot}%{_datadir}/applications/Surge-XT-FX.desktop <<EOF
[Desktop Entry]
Categories=AudioVideo;Audio;
Comment=Surge XT Effects
Exec="/usr/bin/Surge_XT_Effects"
GenericName=Surge XT Effects
Icon=surge-xt-fx
MimeType=
Name=Surge XT Effects
NoDisplay=false
Path=
StartupNotify=true
Terminal=false
TerminalOptions=
Type=Application
EOF

# Write icons files
install -m 755 -d %{buildroot}/%{_datadir}/icons/
cp -rav scripts/installer_linux/assets/icons/* %{buildroot}/%{_datadir}/icons/

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/Surge-XT-FX.desktop

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/Surge-XT.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/Surge-XT.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/Surge-XT-FX.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/surge-xt/fx_presets/*
%{_datadir}/surge-xt/modulator_presets/*
%{_datadir}/surge-xt/patches_3rdparty/*
%{_datadir}/surge-xt/patches_factory/*
%{_datadir}/surge-xt/skins/*
%{_datadir}/surge-xt/tuning_library/*
%{_datadir}/surge-xt/wavetables/*
%{_datadir}/surge-xt/wavetables_3rdparty/*
%{_datadir}/surge-xt/*.txt

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Fri Dec 08 2023 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-2
- update to 1.3.0-2

* Fri May 05 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.3-2
- update to 1.2.3-2

* Mon May 01 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.2-2
- update to 1.2.2-2

* Sun Apr 30 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.1-2
- update to 1.2.1-2

* Mon Apr 10 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-2
- update to 1.2.0-2

* Tue Nov 01 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1.2-2
- update to 1.1.2-2

* Fri Sep 23 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1.1-2
- add patch to fix an out-of-bounds array access

* Fri Aug 26 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1.1-1
- update to 1.1.1-1

* Thu Aug 04 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- update to 1.1.0-1

* Tue Jan 18 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
