# Tag: Synthesizer, Effect
# Type: Plugin, VST3
# Category: Synthesizer, Effect

# Global variables for github repository

Name: uhhyouplugins
Version: 0.61.0
Release: 1%{?dist}
Summary: Uhhyou Plugins VST 3
License: GPL-2.0-or-later
URL: https://github.com/ryukau/VSTPlugins

Vendor:       Audinux
Distribution: Audinux

# ./uhhyouplugins-source.sh <project> <tag>
# ./uhhyouplugins-source.sh UhhyouPlugins 0.61.0

Source0: VSTPlugins.tar.gz
Source1: uhhyouplugins-source.sh

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

sed -i -e "s/other.invoke (false);/other.invoke = false;/g" lib/vst3sdk/vstgui4/vstgui/lib/finally.h

%build

export HOME=`pwd`
mkdir .vst3

%set_build_flags

export CXXFLAGS="-DNDEBUG $CXXFLAGS"
export CFLAGS="-DNDEBUG $CFLAGS"

%cmake -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \
       -DSMTG_RUN_VST_VALIDATOR=OFF

%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/VST3/* %{buildroot}/%{_libdir}/vst3/

%files
%doc README.md
%license LICENSE.txt

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Thu Dec 28 2023 Yann Collette <ycollette.nospam@free.fr> - 0.61.0-1
- update to 0.61.0-1

* Mon Dec 04 2023 Yann Collette <ycollette.nospam@free.fr> - 0.60.0-1
- update to 0.60.0-1

* Sat Dec 02 2023 Yann Collette <ycollette.nospam@free.fr> - 0.59.0-1
- update to 0.59.0-1

* Sun Oct 22 2023 Yann Collette <ycollette.nospam@free.fr> - 0.58.0-1
- update to 0.58.0-1

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
