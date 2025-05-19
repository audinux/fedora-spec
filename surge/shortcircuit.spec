# Status: active
# Tag: Synthesizer
# Type: Plugin, VST3
# Category: Synthesizer

%global commit0 4bd459d5ad8ee3091d35b1a5f2d812c8a8912bd6

Name: shortcircuit
Version: 0.0.1
Release: 6%{?dist}
Summary: A VST3 Synthesizer
License: GPL-2.0-or-later
URL: https://github.com/surge-synthesizer/shortcircuit-xt
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# To get the sources, use:
# $ ./source-shortcircuit.sh main

Source0: shortcircuit-xt.tar.gz
Source1: source-shortcircuit.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: rsync
BuildRequires: git
BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: libX11-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libcurl-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: pybind11-devel
BuildRequires: simde-devel
BuildRequires: desktop-file-utils

%description
A VST3  Synthesizer

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n shortcircuit-xt

sed -i -e "s|Shortcircuit XT|Shortcircuit_XT|g" CMakeLists.txt
sed -i -e "s| >= MINSIGSTKSZ ? 32768 : MINSIGSTKSZ||g" libs/catch2/include/catch2/catch2.hpp

sed -i -e "/-Werror/d" cmake/compiler-options.cmake
sed -i -e "/-march=nehalem/d" cmake/compiler-options.cmake

%build

%set_build_flags

export CXXFLAGS=`echo $CXXFLAGS | sed -e "s/-Werror=format-security//g"`

%cmake -DBUILD_SHARED_LIBS=OFF
%cmake_build

%install

install -m 755 -d %{buildroot}%{_bindir}/
cp build/ShortcircuitXT_artefacts/DEBUG/Standalone/Shortcircuit_XT %{buildroot}/%{_bindir}/ShortcitcuitXT

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -rav build/ShortcircuitXT_artefacts/DEBUG/VST3/Shortcircuit_XT.vst3 %{buildroot}/%{_libdir}/vst3/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp resources/shortcircuit.ico %{buildroot}/%{_datadir}/pixmaps/%{name}.ico

install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=ShortCircuit XT
Exec=Shortcircuit_XT
Icon=shortcircuit
Comment=Synthesizer
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
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Mon May 19 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-6
- update to last nightly - 4bd459d5ad8ee3091d35b1a5f2d812c8a8912bd6

* Tue Mar 21 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-5
- update to last nightly - 15b969b8ac1151c9c9a81665738ef9f81511136c

* Wed Feb 22 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-4
- update to last nightly

* Mon May 23 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-3
- Fix for Fedora 36

* Thu Oct 07 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- Fix for Fedora 35

* Sun Feb 07 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
