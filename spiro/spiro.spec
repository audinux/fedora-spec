# Status: active
# Tag: Synthesizer, Modular
# Type: Plugin, Standalone, VST3, CLAP
# Category: Synthesizer

%global commit0 bf86749dd255c11ce4470c0e3a855ad55568b468

Name: spiro
Version: 0.0.1
Release: 1%{?dist}
Summary: Semi-modular synthesizer
License: MIT
URL: https://github.com/p-o-l-e/spiro
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/p-o-l-e/spiro/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz

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
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: gtk3-devel
BuildRequires: desktop-file-utils

Requires: license-%{name}

%description
Semi-modular synthesizer

%package -n license-%{name}
Summary: License and documentation for %{name}
License: MIT

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: MIT
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: MIT
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n %{name}-%{commit0}

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Spiro_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra %{__cmake_builddir}/Spiro_artefacts/CLAP/* %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/Spiro_artefacts/Standalone/* %{buildroot}/%{_bindir}/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/apps/512x512/
install -m 744 packaging/icon.png %{buildroot}/%{_datadir}/icons/hicolor/apps/512x512/%{name}.png

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=%{name}-jack
Icon=%{name}
Comment=Semimodular synthesizer
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
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/apps/512x512/*

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Fri May 15 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
