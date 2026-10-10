# Status: active
# Tag: Tool, Rack
# Type: Plugin, VST3, Standalone
# Category: Audio, Effect, Tool

Name: open-riff-box
Version: 0.9.1
Release: 2%{?dist}
Summary: Free, open-source, lightweight guitar effects processor for Linux
License: GPL-3.0-or-later
URL: https://github.com/dlujic/open-riff-box
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./open-riff-box-source.sh <TAG>
#        ./open-riff-box-source.sh v0.9.1

Source0: open-riff-box.tar.gz
Source1: open-riff-box-source.sh
Patch0: open-riff-box-0001-fix-preset-dir.patch

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
Free, open-source, lightweight guitar effects processor for Linux.
Plug in your guitar, choose your effects, and play.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -p1 -n %{name}

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/OpenRiffBox_artefacts/Standalone/* %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/OpenRiffBox_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

# Install icon

mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/apps/16x16
install -m 644 resources/icon_16.png %{buildroot}/%{_datadir}/icons/hicolor/apps/16x16/%{name}.png

mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/apps/32x32
install -m 644 resources/icon_32.png %{buildroot}/%{_datadir}/icons/hicolor/apps/32x32/%{name}.png

mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/apps/48x48
install -m 644 resources/icon_48.png %{buildroot}/%{_datadir}/icons/hicolor/apps/48x48/%{name}.png

mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/apps/256x256
install -m 644 resources/icon_256.png %{buildroot}/%{_datadir}/icons/hicolor/apps/256x256/%{name}.png

# Install IRS
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/IR/
cp -ra resources/irs/* %{buildroot}/%{_datadir}/%{name}/IR/

# Install Presets
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/presets/
cp -ra presets/* %{buildroot}/%{_datadir}/%{name}/presets/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=OpenRiffBox
Icon=%{name}
Comment=Free, open-source, lightweight guitar effects processor for Linux
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
%{_datadir}/icons/hicolor/apps/16x16/*
%{_datadir}/icons/hicolor/apps/32x32/*
%{_datadir}/icons/hicolor/apps/48x48/*
%{_datadir}/icons/hicolor/apps/256x256/*
%{_datadir}/applications/*
%{_datadir}/%{name}/presets/*

%files -n license-%{name}
%doc README.md docs/*
%license LICENSE
%{_datadir}/%{name}/IR/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Sat Oct 10 2026 Yann Collette <ycollette.nospam@free.fr> - 0.9.1-2
- update to 0.9.1-2 - fix desktop file

* Sat Oct 10 2026 Yann Collette <ycollette.nospam@free.fr> - 0.9.1-1
- Initial spec file
