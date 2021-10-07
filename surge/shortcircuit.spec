%global debug_package %{nil}

Name:    shortcircuit
Version: 0.0.1
Release: 1%{?dist}
Summary: A VST3 / LV2 Synthesizer
License: GPLv2+
URL:     https://github.com/surge-synthesizer/shortcircuit3

Vendor:       Audinux
Distribution: Audinux

# To get the sources, use:
# $ ./source-shortcircuit.sh main

Source0: shortcircuit.tar.gz
Source1: source-shortcircuit.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: rsync
BuildRequires: git
BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: libX11-devel
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libcurl-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel

%description
A VST3 / LV2 Synthesizer

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n shortcircuit3

# Fix a compilation problem on Fedora 35 (variable size list)
sed -i -e "s| >= MINSIGSTKSZ ? 32768 : MINSIGSTKSZ||g" libs/catch2/include/catch2/catch2.hpp

%build

mkdir -p build
cd build
cmake -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON -DCMAKE_INSTALL_PREFIX:PATH=/usr -DINCLUDE_INSTALL_DIR:PATH=/usr/include -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DSYSCONF_INSTALL_DIR:PATH=/etc -DSHARE_INSTALL_PREFIX:PATH=/usr/share -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RELEASE ..

%make_build 

%install 

install -m 755 -d %{buildroot}%{_libdir}/vst3/ShortcircuitXT.vst3/
cp -r build/ShortcircuitXT_artefacts/RELEASE/VST3/Shortcircuit\ XT.vst3/* %{buildroot}/%{_libdir}/vst3/ShortcircuitXT.vst3/

install -m 755 -d %{buildroot}%{_bindir}/
cp -r build/ShortcircuitXT_artefacts/RELEASE/Standalone/* %{buildroot}/%{_bindir}/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Thu Oct 07 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- Fix for Fedora 35

* Sun Feb 07 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
