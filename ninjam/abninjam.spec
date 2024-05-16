# Tag: Audio, Live, Session
# Type: Plugin, LV2, VST
# Category: Audio, Tool, Session Mngmt

Name: abNinjam
Version: 0.0.8
Release: 3%{?dist}
Summary: Ninjam LV2 / VST plugin
URL: https://github.com/antanasbruzas/abNinjam
ExclusiveArch: x86_64 aarch64
License: MIT

Vendor:       Audinux
Distribution: Audinux

#./abninjam-source.sh <tag>
#./abninjam-source.sh v0.0.8

Source0: abNinjam.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: freetype-devel
BuildRequires: xcb-util-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libvorbis-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel

%description
Ninjam LV2 / VST plugin.

%prep
%autosetup -n %{name}

# Don't try to create /usr/lib64/{vst,lv2} directories
sed -i -e "/MAKE_DIRECTORY/d" cmake/VSTConfig.cmake

%build

%set_build_flags

%cmake -DCMAKE_BUILD_TYPE=RELEASE \
       -DVSTPLUGIN_INSTALL_DIR=%{_libdir}/vst \
       -DLV2PLUGIN_INSTALL_DIR=%{_libdir}/lv2

%cmake_build

%install

%cmake_install

chmod a+x %{buildroot}%{_libdir}/vst/abNinjam.vst3/Contents/x86_64-linux/*.so
chmod a+x %{buildroot}%{_libdir}/lv2/abNinjam.lv2/*.so

%files
%doc README.md
%license LICENSE
%{_libdir}/vst/*
%{_libdir}/lv2/*

%changelog
* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.8-3
- fix debug build

* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.8-2
- update to 0.0.8-2 - fix for fedora 33

* Fri Jun 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.8-1
- update to 0.0.8-1

* Sun Jun 7 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.7-1
- update to 0.0.7-1

* Sun May 31 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.5-1
- update to 0.0.5-1

* Sat May 16 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.2-1
- initial version of the spec file
