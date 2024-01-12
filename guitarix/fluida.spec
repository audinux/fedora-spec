# Tag: Sf2
# Type: Plugin, LV2
# Category: Audio, Synthesizer

Name:    fluida
Version: 0.9.2
Release: 1%{?dist}
Summary: Fluidsynth as LV2 plugin
License: BSD
URL: https://github.com/brummer10/Fluida.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/brummer10/Fluida.lv2/releases/download/v%{version}/Fluida.lv2-v%{version}-src.tar.xz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: libsigc++20-devel
BuildRequires: fluidsynth-devel
BuildRequires: vim-common

%description
Fluidsynth as LV2 plugin.

%prep
%autosetup -n Fluida.lv2-v%{version}

%build

%set_build_flags

export CXXFLAGS=`echo $CXXFLAGS | sed -e "s|-Werror=format-security||g"`
export CFLAGS=`echo $CFLAGS | sed -e "s|-Werror=format-security||g"`

%make_build STRIP=true

%install

%make_install INSTALL_DIR=/usr/%{_lib}/lv2 STRIP=true

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Fri Jan 12 2024 Yann Collette <ycollette.nospam@free.fr> - 0.9.2-1
- update to 0.9.2-1

* Wed Jan 10 2024 Yann Collette <ycollette.nospam@free.fr> - 0.9.1-1
- update to 0.9.1-1

* Fri Oct 14 2022 Yann Collette <ycollette.nospam@free.fr> - 0.8-1
- update to 0.8-1

* Sun Apr 18 2021 Yann Collette <ycollette.nospam@free.fr> - 0.7-1
- update to 0.7-1

* Fri Jan 15 2021 Yann Collette <ycollette.nospam@free.fr> - 0.6-1
- update to 0.6-1

* Sat Nov 28 2020 Yann Collette <ycollette.nospam@free.fr> - 0.5-1
- Initial spec file
