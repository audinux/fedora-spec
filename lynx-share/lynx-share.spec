# Status: active
# Tag: Jack, Alsa, Distortion
# Type: Plugin, Standalone, VST3
# Category: Effect

Name: lynx-share
Version: 0.1.27
Release: 1%{?dist}
Summary: Lightweight open-source DAW with the FL Studio workflow: Channel Rack, Piano Roll, Playlist, Mixer and .flp import
License: AGPL-3.0-or-later
URL: https://github.com/Ka1-S/LYNX-SHARE
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/Ka1-S/LYNX-SHARE/archive/refs/tags/v%{version}-alpha.tar.gz#/%{name}-%{version}.tar.gz

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

%description
Lightweight open-source DAW with the FL Studio workflow: Channel Rack, Piano Roll, Playlist, Mixer and .flp import.

%prep
%autosetup -n LYNX-SHARE-%{version}-alpha

# Remove the use of static libs
sed -i -e "/-static-libgcc/d" CMakeLists.txt

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/LYNX_artefacts/LYNX %{buildroot}/%{_bindir}/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp resources/LYNX.ico %{buildroot}/%{_datadir}/pixmaps/lynx.ico

# Write appdata file
install -m 755 -d %{buildroot}/%{_metainfodir}/
install -m 644 resources/linux/com.lynx_share.LYNX.appdata.xml %{buildroot}/%{_metainfodir}/

# Write mime file
install -m 755 -d %{buildroot}/%{_datadir}/mime/applications/
install -m 644 resources/linux/lynx-mime.xml %{buildroot}/%{_datadir}/mime/applications/

# Write desktop file
install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 resources/linux/lynx.desktop %{buildroot}/%{_datadir}/applications/

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/lynx.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/lynx.desktop

%files
%doc README.md CONTRIBUTING.md PRIVACY.md SECURITY.md THIRD_PARTY.md CODE_OF_CONDUCT.md docs/*
%license LICENSE
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_metainfodir}/*
%{_datadir}/mime/applications/*
%{_datadir}/applications/*

%changelog
* Fri Nov 13 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.27-1
- update to 0.1.27-1

* Thu Nov 12 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.26-1
- update to 0.1.26-1

* Mon Nov 09 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.25-1
- update to 0.1.25-1

* Fri Nov 06 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.24-1
- Initial spec file
