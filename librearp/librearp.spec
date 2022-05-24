# Tag: Jack, Alsa
# Type: Plugin, Standalone, VST3
# Category: Audio, Synthesizer

Name:    librearp
Version: 2.4
Release: 2%{?dist}
Summary: A pattern-based arpeggio generator plugin
License: GPLv3
URL:     https://gitlab.com/LibreArp/LibreArp

Vendor:       Audinux
Distribution: Audinux

# Usage: ./librearp-source.sh <TAG>
# ./librearp-source.sh 2.4

Source0: LibreArpLV2.tar.gz
Source1: LibreArpVST3.tar.gz
Source2: librearp-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: lv2-devel
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

%description
A pattern-based arpeggio generator plugin

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n lv2-%{name}
VST3 version of %{name}

%prep

tar xvfz %{SOURCE1}

%autosetup -n LibreArpLV2

%build

%cmake
%cmake_build

cd ../LibreArpVST3
%cmake
%cmake_build

%install 

install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/LibreArp_artefacts/LV2/* %{buildroot}/%{_libdir}/lv2/

cd ../LibreArpVST3
install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/LibreArp_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

%files -n lv2-%{name}
%doc README.md CHANGELOG.md
%license LICENSE.md
%{_libdir}/lv2/*

%files -n vst3-%{name}
%doc README.md CHANGELOG.md
%license LICENSE.md
%{_libdir}/vst3/*

%changelog
* Tue May 24 2022 Yann Collette <ycollette.nospam@free.fr> - 2.4-2
- update to 2.4-2

* Thu Mar 10 2022 Yann Collette <ycollette.nospam@free.fr> - 2.3-2
- update to 2.3-2 - fix for Fedora 35

* Sun Oct 03 2021 Yann Collette <ycollette.nospam@free.fr> - 2.2-2
- update to 2.2-2 - fix for Fedora 35

* Tue Sep 07 2021 Yann Collette <ycollette.nospam@free.fr> - 2.2-1
- update to 2.2-1

* Wed Aug 18 2021 Yann Collette <ycollette.nospam@free.fr> - 2.1-1
- Initial spec file
