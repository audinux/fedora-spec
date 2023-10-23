# Tag: Keyboard
# Type: Plugin, LV2
# Category: Audio, MIDI

Name:    xkeyboard
Version: 0.0.1
Release: 1%{?dist}
Summary:  simple LV2 MIDI keyboard
License: GPL-2.0-or-later
URL:     https://github.com/brummer10/XKeyboard.lv2

Vendor:       Audinux
Distribution: Audinux

# git clone https://github.com/brummer10/XKeyboard.lv2
# cd XKeyboard.lv2
# #git checkout main
# git submodule init
# git submodule update
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz XKeyboard.lv2.tar.gz XKeyboard.lv2/*
# rm -rf XKeyboard.lv2

Source0: XKeyboard.lv2.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: lilv-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: libsigc++20-devel
BuildRequires: vim-common

%description
A simple 4 in 1 Mixer

%prep
%autosetup -n XKeyboard.lv2

%build

%set_build_flags

export CXXFLAGS="-std=c++11 -fPIC -I/usr/include/cairo $CXXFLAGS"
%make_build STRIP=true

%install

%make_install INSTALL_DIR=/usr/%{_lib}/lv2 STRIP=true

%files
%doc README.md
%{_libdir}/lv2/*

%changelog
* Sun May 23 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
