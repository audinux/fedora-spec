Name:    shortcircuit
Version: 0.0.1
Release: 4%{?dist}
Summary: A VST3 / LV2 Synthesizer
License: GPLv2+
URL:     https://github.com/surge-synthesizer/shortcircuit3

Vendor:       Audinux
Distribution: Audinux

# To get the sources, use:
# $ ./source-shortcircuit.sh main

Source0: shortcircuit.tar.gz
Source1: source-shortcircuit.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: rsync
BuildRequires: git
BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: libX11-devel
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
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

%description
A VST3 / CLAP Synthesizer

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n clap-%{name}
CLAP version of %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n shortcircuit3

sed -i -e "s|Shortcircuit XT|Shortcircuit_XT|g" wrappers/juce/CMakeLists.txt

%build

# export CXXFLAGS="-Wno-error=format-security -include utility"

mkdir -p build
cd build
cmake -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
      -DCMAKE_INSTALL_PREFIX:PATH=/usr \
      -DINCLUDE_INSTALL_DIR:PATH=/usr/include \
      -DLIB_INSTALL_DIR:PATH=/usr/lib64 \
      -DSYSCONF_INSTALL_DIR:PATH=/etc \
      -DSHARE_INSTALL_PREFIX:PATH=/usr/share \
      -DLIB_SUFFIX=64 \
      -DCMAKE_BUILD_TYPE=DEBUG ..

%make_build 

%install 

install -m 755 -d %{buildroot}%{_bindir}/
cp build/shortcircuit-products/Shortcircuit_XT %{buildroot}/%{_bindir}/ShortcitcuitXT

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -rav build/shortcircuit-products/Shortcircuit_XT.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp build/shortcircuit-products/Shortcircuit_XT.clap %{buildroot}/%{_libdir}/clap/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp resources/images/SCAppIcon.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

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

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Wed Feb 22 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-4
- update to last nightly

* Mon May 23 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-3
- Fix for Fedora 36    

* Thu Oct 07 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- Fix for Fedora 35

* Sun Feb 07 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
