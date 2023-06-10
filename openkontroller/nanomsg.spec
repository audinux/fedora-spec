Name:    nanomsg
Version: 1.1.5
Release: 2%{?dist}
Summary: The nanomsg library is a simple high-performance implementation of several "scalability protocols"
URL:     https://github.com/nanomsg/nanomsg
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/nanomsg/nanomsg/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake

%description
The nanomsg library is a simple high-performance implementation of several "scalability protocols". These scalability protocols are light-weight messaging protocols which can be used to solve a number of very common messaging patterns, such as request/reply, publish/subscribe, surveyor/respondent, and so forth. These protocols can run over a variety of transports such as TCP, UNIX sockets, and even WebSocket.
For more information check the http://nanomsg.org.

%package devel
Summary:  Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%autosetup -n %{name}-%{version}

%build

%cmake -DNN_ENABLE_DOC=OFF -DNN_TESTS=OFF
%cmake_build

%install

%cmake_install

%files
%{_bindir}/*
%{_libdir}/*

%files devel
%{_includedir}/*

%changelog
* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.5-2
- fix for fedora 33

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 1.1.5
- update to 1.1.5

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.1.2
- update for Fedora 29

* Sat May 12 2017 Yann Collette <ycollette.nospam@free.fr> - 1.1.2
- update to 1.1.2

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.0.0
- Initial build
