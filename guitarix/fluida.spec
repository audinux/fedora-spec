# Tag: SF2
# Type: Plugin, LV2
# Category: Audio, Synthesizer

Name:    fluida
Version: 0.7
Release: 1%{?dist}
Summary: Fluidsynth as LV2 plugin 
License: BSD

URL: https://github.com/brummer10/Fluida.lv2

Source0: https://github.com/brummer10/Fluida.lv2/files/6329806/Fluida_%{version}.tar.gz

BuildRequires: gcc gcc-c++
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
%autosetup -n Fluida_%{version}

%build

%set_build_flags

%make_build STRIP=true CXXFLAGS="%build_cxxflags -fPIC -I/usr/include/cairo -I/usr/include/sigc++-2.0/ -I/usr/%{_lib}/sigc++-2.0/include" 

%install 

%make_install INSTALL_DIR=/usr/%{_lib}/lv2 STRIP=true

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Sun Apr 18 2021 Yann Collette <ycollette.nospam@free.fr> - 0.7-1
- update to 0.7-1

* Fri Jan 15 2021 Yann Collette <ycollette.nospam@free.fr> - 0.6-1
- update to 0.6-1

* Sat Nov 28 2020 Yann Collette <ycollette.nospam@free.fr> - 0.5-1
- Initial spec file
