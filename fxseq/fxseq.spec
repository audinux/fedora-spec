%define commit0 1cefe703884950c161d2b6777cec47a0020b6d6b

Name:    fxseq
Version: 0.1
Release: 1%{?dist}
Summary: A step sequencer based multi effect plugin using JUCE.
License: GPL-2.0-or-later
URL:     https://github.com/ssabug/fxseq

Vendor:       Audinux
Distribution: Audinux

# Usage: ./fxseq-source.sh <TAG>
# ./fxseq-source.sh master

Source0: fxseq.tar.gz
Source1: fxseq-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
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
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel

%description
Fxseq is a step sequencer-based multi effect like dblue glitch or effectrix.

%prep
%autosetup -n %{name}

%build

%cmake
# LV2 tests are failing for now
cd %{__cmake_builddir}
%make_build fxseq-VST3_All

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -rav %{__cmake_builddir}/fxseq-VST3_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/

%files
%doc README.md
%{_libdir}/vst3/*

%changelog
* Thu Nov 02 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial spec file
