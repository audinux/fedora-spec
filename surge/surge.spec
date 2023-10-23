Name:    surge
Version: 1.9.0
Release: 8%{?dist}
Summary: A VST3 / LV2 Synthesizer
License: GPL-2.0-or-later
URL:     https://github.com/surge-synthesizer/surge

Vendor:       Audinux
Distribution: Audinux

# To get the sources, use:
# $ ./source-surge.sh 1.9.0

Source0: surge.tar.gz
Source1: source-surge.sh

BuildRequires: gcc gcc-c++
BuildRequires: libX11-devel
BuildRequires: cmake
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: rsync
BuildRequires: git
BuildRequires: python3
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel

%description
A VST3 / LV2 Synthesizer

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n %{name}

%ifarch x86_64
  sed -i -e "s/lib\/vst/lib64\/vst/g" build-linux.sh
%endif

sed -i -e "s/find_package/#find_package/g" cmake/versiontools.cmake

# manage python
sed -i -e "s/COMMAND python /COMMAND python2 /g" CMakeLists.txt
for Files in `find . -name "*.py" -exec grep -l "bin/python$" {} \;`
do
  sed -i -e "s/env python$/env python3/g" $Files
done
for Files in `find . -type f -executable -exec grep -l "env python$" {} \;`
do
  sed -i -e "s/env python$/env python3/g" $Files
done

# Fix a compilation problem on Fedora 35 (variable size list)
sed -i -e "s| >= MINSIGSTKSZ ? 32768 : MINSIGSTKSZ||g" libs/catch2/include/catch2/catch2.hpp

%build

%set_build_flags

./build-linux.sh cmake

cd buildlin
cmake -DCMAKE_C_FLAGS="-Wno-error -O2 -g -fPIC" -DCMAKE_CXX_FLAGS="-include limits -std=c++14 -Wno-error -O2 -g -fPIC" .
cd ..

./build-linux.sh build

%install

export HOME=`pwd`
mkdir .vst3
mkdir .lv2
mkdir -p .local/share/Surge

./build-linux.sh -l install

install -m 755 -d %{buildroot}%{_libdir}/vst3/Surge.vst3/
cp -r .vst3/Surge.vst3/* %{buildroot}/%{_libdir}/vst3/Surge.vst3/

install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -r .lv2/* %{buildroot}/%{_libdir}/lv2/

install -m 755 -d %{buildroot}%{_datadir}/Surge/
rsync -rav .local/share/surge/* %{buildroot}/%{_datadir}/Surge/

%files
%{_datadir}/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Sun Oct 03 2021 Yann Collette <ycollette.nospam@free.fr> - 1.9.0-8
- update to 1.9.0-8 - fixes for Fedora 35

* Wed Apr 21 2021 Yann Collette <ycollette.nospam@free.fr> - 1.9.0-7
- update to 1.9.0-7

* Wed Jan 27 2021 Yann Collette <ycollette.nospam@free.fr> - 1.8.1-7
- update to 1.8.1-7

* Sun Jan 17 2021 Yann Collette <ycollette.nospam@free.fr> - 1.8.0-7
- update to 1.8.0-7

* Sun Dec 13 2020 Yann Collette <ycollette.nospam@free.fr> - 1.7.1-7
- fix install

* Sat Oct 24 2020 Yann Collette <ycollette.nospam@free.fr> - 1.7.1-6
- fix permissions on vst3

* Sun Aug 2 2020 Yann Collette <ycollette.nospam@free.fr> - 1.7.1-5
- update to 1.7.1-5

* Thu Jul 2 2020 Yann Collette <ycollette.nospam@free.fr> - 1.6.6-5
- update to 1.6.6-5 - fix package

* Wed Jun 24 2020 Yann Collette <ycollette.nospam@free.fr> - 1.6.6-4
- update to 1.6.6-4 - fix debug build

* Wed Jun 24 2020 Yann Collette <ycollette.nospam@free.fr> - 1.6.6-3
- update to 1.6.6-3 - fix requires for subpackage

* Mon Jun 22 2020 Yann Collette <ycollette.nospam@free.fr> - 1.6.6-2
- update to 1.6.6-2

* Sat Feb 29 2020 Yann Collette <ycollette.nospam@free.fr> - 1.6.6-1
- update to 1.6.6-1

* Tue Feb 4 2020 Yann Collette <ycollette.nospam@free.fr> - 1.6.5-1
- update to 1.6.5-1

* Sun Nov 3 2019 Yann Collette <ycollette.nospam@free.fr> - 1.6.3-1
- update to 1.6.3-1

* Thu Sep 26 2019 Yann Collette <ycollette.nospam@free.fr> - 1.6.2.1
- update to 1.6.2.1

* Fri May 3 2019 Yann Collette <ycollette.nospam@free.fr> - 1.6.0.b9
- update to beta9

* Mon Apr 29 2019 Yann Collette <ycollette.nospam@free.fr> - 1.6.0.b3
- Initial spec file
