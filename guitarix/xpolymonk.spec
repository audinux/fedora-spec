# Tag: MIDI
# Type: Plugin, LV2
# Category: Audio, Synthesizer

Name:    xpolymonk
Version: 0.6.0
Release: 1%{?dist}
Summary: A LV2 simple polyphonic sound generator to have some fun with
License: GPLv2+
URL:     https://github.com/brummer10/XPolyMonk.lv2

# ./xpolymonk-source.sh <tag>
# ./xpolymonk-source.sh 0.6

Source0: XPolyMonk.lv2.tar.gz
Source1: xpolymonk-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: libsigc++20-devel

%description
A LV2 simple polyphonic sound generator to have some fun with

%prep
%autosetup -n XPolyMonk.lv2

%build

%set_build_flags

%make_build STRIP=true

%install 

%make_install INSTALL_DIR=/usr/%{_lib}/lv2 STRIP=true

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Mon Oct 27 2020 Yann Collette <ycollette.nospam@free.fr> - 0.6.0-1
- Initial spec file
