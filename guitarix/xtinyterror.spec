# Tag: Guitar, Amp Simul
# Type: Plugin, LV2
# Category: Audio, Effect

Name:    xtinyterror
Version: 0.0.1
Release: 1%{?dist}
Summary: Valve amplifier simulation
License: GPLv2+

URL:     https://github.com/brummer10/XTinyTerror.lv2

# git clone https://github.com/brummer10/XTinyTerror.lv2
# cd XTinyTerror.lv2
# git submodule init
# git submodule update
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz XTinyTerror.lv2.tar.gz XTinyTerror.lv2/*
# rm -rf XTinyTerror.lv2

Source0: XTinyTerror.lv2.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: libsigc++20-devel

%description
Valve amplifier simulation

%prep
%autosetup -n XTinyTerror.lv2

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
* Mon Sep 21 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file - master / 714cc15af48290c0191ac23a121f645f5ed1e256
