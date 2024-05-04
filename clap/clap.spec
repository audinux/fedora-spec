# Tag: Library
# Type: Devel
# Category: Programming

Summary: CLAP audio plugin API
Name: clap
Version: 1.2.1
Release: 1%{?dist}
License: MIT
URL: https://github.com/free-audio/clap

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/free-audio/clap/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: gcc gcc-c++
BuildRequires: cmake

%description
CLAP stands for CLever Audio Plugin. It is an interface that provides a
stable ABI to define a standard for Digital Audio Workstations and audio
plugins (synthesizers, audio effects, ...) to work together.
The ABI, or Application Binary Interface, serves as a means of
communication between a host and a plugin. It provides backwards compatibility,
that is, a plugin binary compiled with CLAP 1.x can be loaded by any other CLAP 1.y.
To work with CLAP, include clap/clap.h.
The two most important objects are clap_host and clap_plugin.
src/plugin-template.c is a very minimal example which demonstrates how to wire a CLAP plugin.

%package devel
Summary:  Header files for CLAP

%description devel
Header files for CLAP.

%prep
%autosetup -n %{name}-%{version}

%build

%cmake
%cmake_build

%install
%cmake_install

%files devel
%doc README.md
%license LICENSE
%{_includedir}/*
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/*

%changelog
* Sat May 04 2024 Yann Collette <ycollette dot nospam at free.fr> 1.2.1-1
- update to 1.2.1-1

* Mon Jan 22 2024 Yann Collette <ycollette dot nospam at free.fr> 1.2.0-1
- update to 1.2.0-1

* Fri Dec 08 2023 Yann Collette <ycollette dot nospam at free.fr> 1.1.10-1
- initial release
