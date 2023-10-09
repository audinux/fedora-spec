# Tag: Synthesizer
# Type: LV2
# Category: Synthesizer

# Global variables for github repository

Name:    uhhyouplugins
Version: 0.57.0
Release: 1%{?dist}
Summary: Uhhyou Plugins VST 3
License: GPL-2.0-or-later
URL:     https://github.com/ryukau/VSTPlugins

Vendor:       Audinux
Distribution: Audinux

# ./uhhyouplugins-source.sh <tag>
# ./uhhyouplugins-source.sh UhhyouPlugins 0.57.0
# ./vst3sdk-source.sh v3.7.8_build_34

Source0: VSTPlugins.tar.gz
Source1: vst3sdk.tar.gz
Source2: vst3-source.sh
Source3: uhhyouplugins-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: sqlite-devel
BuildRequires: gtkmm30-devel
BuildRequires: xcb-util-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: libxkbcommon-x11-devel

%description
Uhhyou Plugins VST 3

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n VSTPlugins

tar xvfz %{SOURCE1}
cp ci/linux_patch/cairocontext.cpp vst3sdk/vstgui4/vstgui/lib/platform/linux/cairocontext.cpp

%build

export HOME=`pwd`
mkdir .vst3

%set_build_flags

export CXXFLAGS="-O2 -flto=auto -ffat-lto-objects -fexceptions -g -grecord-gcc-switches -pipe -Wall -Werror=format-security -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 -mtune=generic -fasynchronous-unwind-tables"

export CXXFLAGS="-include cstdint $CXXFLAGS"

mkdir vst3sdk/build
cd vst3sdk/build

cmake -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_CXX_FLAGS="$CXXFLAGS -include limits" \
      -DSMTG_MYPLUGINS_SRC_PATH="../.." \
      -DSMTG_ADD_VST3_HOSTING_SAMPLES=FALSE \
      -DSMTG_ADD_VST3_PLUGINS_SAMPLES=FALSE \
      -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \
      -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
      -DCMAKE_INSTALL_DO_STRIP:BOOL=OFF \
      -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
      -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
      -DLIB_INSTALL_DIR:PATH=%{_libdir} \
      -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \
      -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \
      -DCMAKE_STRIP=/usr/bin/true \
      ..

cmake --build . %{?_smp_mflags}

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra vst3sdk/build/VST3/Release/* %{buildroot}/%{_libdir}/vst3/

%files
%doc README.md
%license LICENSE.txt

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Mon Oct 09 2023 Yann Collette <ycollette.nospam@free.fr> - 0.57.0-1
- update to 0.57.0-1

* Thu Jun 08 2023 Yann Collette <ycollette.nospam@free.fr> - 0.56.0-1
- update to 0.56.0-1

* Sat May 06 2023 Yann Collette <ycollette.nospam@free.fr> - 0.55.0-1
- update to 0.55.0-1

* Thu Mar 30 2023 Yann Collette <ycollette.nospam@free.fr> - 0.54.2-1
- update to 0.54.2-1

* Sun Oct 09 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-e5eee4c3-4
- update to e5eee4c3

* Sun May 01 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-df67460f-3
- update to df67460f

* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-fae2ad4b-2
- fix debug build and update to fae2ad4b

* Wed Feb 26 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-6bcd263e-1
- Initial spec file for 6bcd263e
