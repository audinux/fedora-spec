# Tag: Tool
# Type: Standalone
# Category: Tool

# Global variables for github repository
%global commit0 cf9f324a16751812105f1f7613b799e65e43b91f
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: sfArk tool
Name: sfarkxtc
Version: 0.1.%{shortcommit0}
Release: 2%{?dist}
License: GPL
URL: https://github.com/raboof/sfarkxtc
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/raboof/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0: sfark-0001-fix-install-path.patch

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: sfArkLib-devel
BuildRequires: zlib-devel

%description
sfArk extractor, console version

Converts soundfonts in the legacy sfArk v2 file format to sf2

%prep
%autosetup -p1 -n %{name}-%{commit0}

%build

%set_build_flags

%make_build BIN_PATH=%{_bindir}

%install

%make_install BIN_PATH=%{_bindir}

%files
%doc README.md
%license COPYING
%{_bindir}/*

%changelog
* Fri Oct 22 2020 Yann Collette <ycollette dot nospam at free.fr> 0.1-2
- fix debug build

* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free.fr> 0.1-1
- update for Fedora 29

* Thu Jun 04 2015 Yann Collette <ycollette dot nospam at free.fr> 0.1-1
- Initial release of spec file for 0.1
