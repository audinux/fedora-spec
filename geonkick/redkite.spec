# Tag: Library
# Type: Devel
# Category: Programming

Name: redkite
Version: 1.3.0
Release: 3%{?dist}
Summary: A cross-platform GUI toolkit in C++.
URL: https://gitlab.com/iurie-sw/redkite
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-only

Vendor:       Audinux
Distribution: Audinux

Source0: https://gitlab.com/iurie-sw/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: cairo-devel

%description
Redkite is a small free software and cross-platform GUI toolkit.
It is developed in C++11&14 and inspired from other well known GUI toolkits.

%prep
%autosetup -n %{name}-v%{version}

sed -i -e "s/${CMAKE_INSTALL_PREFIX}\/lib/${CMAKE_INSTALL_PREFIX}\/%{_lib}/g" CMakeLists.txt

%build

%cmake -DCMAKE_BUILD_TYPE=RELEASE \
       -DCMAKE_INSTALL_LIBDIR=%{_lib}

%cmake_build

%install

%cmake_install

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_mandir}/*

%changelog
* Fri Dec 18 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-3
- update to 1.3.0-3

* Mon Oct 26 2020 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-3
- update to 1.2.0-3

* Sat Oct 24 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-3
- update to 1.1.0-3

* Wed Sep 30 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.3-3
- update to 1.0.3-3 - fix for fedora 33

* Thu Aug 13 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.3-1
- update to 1.0.3-1

* Sun Aug 9 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-1
- update to 1.0.2-1

* Fri Jul 24 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-1
- update to 1.0.1-1

* Fri Jun 12 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- update to 1.0.0-1

* Sat May 09 2020 Bruno Vernay <brunovern.a@gmail.com> - 0.8.1-2
- Update the URL, add make dependency, change licence to GPLv3

* Fri Apr 17 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.1-1
- update to 0.8.1-1

* Sun Apr 5 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.0-1
- update to 0.8.0

* Sat Dec 28 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.3-1
- update to 0.6.3

* Wed Oct 16 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.2-1
- update to 0.6.2

* Thu Aug 8 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.1-1
- update to 0.6.1

* Mon May 27 2019 Yann Collette <ycollette.nospam@free.fr> - 0.5.2-1
- switch to 0.5.2

* Tue May 21 2019 Yann Collette <ycollette.nospam@free.fr> - 0.5.1-1
- switch to 0.5.1

* Mon May 20 2019 Yann Collette <ycollette.nospam@free.fr> - 0.5-1
- initial version of the spec file
