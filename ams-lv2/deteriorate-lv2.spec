# Tag: Live
# Type: Plugin, LV2
# Category: Audio, Effect

Name:    deteriorate-lv2
Version: 1.0.7
Release: 2%{?dist}
Summary: Set of plugins to destroy and deteriorate the sound quality of a live input
License: GPL-2.0-or-later
URL:     https://github.com/blablack/deteriorate-lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/blablack/deteriorate-lv2/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: gtkmm24-devel
BuildRequires: gtk2-devel
BuildRequires: cairo-devel
BuildRequires: lvtk
BuildRequires: sed
BuildRequires: python2

%description
deteriorate-lv2 is a set of plugins to destroy and
deteriorate the sound quality of a live input.
The set contains:
 * DownSampler
 * Granulator

%prep
%autosetup -n %{name}-%{version}

%build

sed -i -e "s/lvtk-plugin-1/lvtk-plugin-2/g" wscript
sed -i -e "s/lvtk-ui-1/lvtk-ui-2/g" wscript
sed -i -e "s/lvtk-gtkui-1/lvtk-gtkui-2/g" wscript

# For Fedora 29
%if 0%{?fedora} >= 29
  for Files in `grep -lr "/usr/bin/env.*python"`; do sed -ie "s/env python/python2/g" $Files; done
%endif

for Files in src/*.cpp ; do sed -i -e "s/lvtk-1/lvtk-2/g" $Files; done
for Files in src/*.hpp ; do sed -i -e "s/lvtk-1/lvtk-2/g" $Files; done

%set_build_flags

./waf configure --destdir=%{buildroot} --libdir=%{_libdir}
./waf

%install
./waf -j1 install --destdir=%{buildroot}

%files
%doc README.md THANKS
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.7-3
- fix debug build

* Wed Apr 22 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.7-2
- update to 1.0.7-2

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 1.0.7-1
- update to 1.0.7-1

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.6-1
- update for Fedora 29

* Mon Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 1.0.6-1
- update to 1.0.6-1

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial build
