Name:    infernal-synth
Version: 1.2p4
Release: 1%{?dist}
Summary: An open source VST3 synthesizer and effect plugin.
License: GPL-3.0-or-later
URL:     https://sjoerdvankreel.github.io/infernal-synth/

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/sjoerdvankreel/infernal-synth/archive/refs/tags/v1.2-preview4.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
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

%description
InfernalSynth is a semi-modular software synthesizer and effect plugin.
For system requirements, download and installation, see the project website.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n infernal-synth-1.2-preview4

sed -i -e "/-Werror/d" CMakeLists.txt

%build

%cmake -DCMAKE_BUILD_TYPE=RELEASE
%cmake_build

%install 

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -rav dist/linux_/RELEASE/* %{buildroot}/%{_libdir}/vst3/

%files
%doc README.md MANUAL.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Sun Jul 23 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2p4-1
- Initial spec file
