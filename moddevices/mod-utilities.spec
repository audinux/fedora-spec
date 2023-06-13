# Global variables for github repository
%global commit0 b8a9d4558efc136c4ce90657a5958064640074f1
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    mod-utilities
Version: 0.1.%{shortcommit0}
Release: 1%{?dist}
Summary: Some utilities lv2 plugins
License: GPL-2.0-or-later
URL:     https://github.com/moddevices/mod-utilities

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/moddevices/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel

%description
Some utilities lv2 plugins developed by mod team

Here you've got some Butterwoth filters, some crossovers based on these filters,
simple gain plugins without zipper noise, two switch box plugins, a switch trigger,
a toogle switch and a peakmeter.

Note2Midi is EXPERIMENTAL and it's NOT WORKING yet.

%prep
%autosetup -n %{name}-%{commit0}

for Files in `find . -name Makefile -exec grep -l "INSTALL_PATH =" {} \;`
do
    sed -i -e "s|INSTALL_PATH = /usr/local/lib/lv2|INSTALL_PATH = /usr/%{_lib}/lv2|g" $Files
    sed -i -e "s|\$(PREFIX)/lib/lv2|\$(PREFIX)/%{_lib}/lv2|g" $Files
done

%build

%set_build_flags

%make_build PREFIX=/usr

%install

%make_install PREFIX=/usr

%files
%doc README.md
%{_libdir}/lv2/*

%changelog
* Wed May 24 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1-b8a9d455-1
- Initial build
