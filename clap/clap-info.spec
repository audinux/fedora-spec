# Tag: Tool
# Type: Devel
# Category: Tool

Summary: An automatic CLAP validation and testing tool
Name: clap-info
Version: 1.2.0
Release: 1%{?dist}
License: MIT
URL: https://github.com/free-audio/clap-info
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./clap-source.sh <project> <tag>
# ./clap-source.sh clap-info v1.2.0

Source0: clap-info.tar.gz
Source1: clap-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: chrpath

%description
This is a CLAP information tool which simply loads a clap and allows you to print
a variety of information about the plugin. It prints the information in machine-readable (JSON) format.

%prep
%autosetup -n %{name}

sed -i -e "s/add_library(jsoncpp/add_library(jsoncpp STATIC/g" libs/CMakeLists.txt

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
cp %{__cmake_builddir}/clap-info %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_libdir}/
cp %{__cmake_builddir}/libclap-scanner.so %{buildroot}/%{_libdir}/

# chrpath --delete %{buildroot}/%{_libdir}/libclap-scanner.so
chrpath --delete %{buildroot}/%{_bindir}/clap-info

%files
%doc README.md
%license LICENSE.md
%{_bindir}/*
%{_libdir}/*

%changelog
* Sat Feb 10 2024 Yann Collette <ycollette dot nospam at free.fr> 1.2.0-1
- update to 1.2.0-1

* Mon Jan 22 2024 Yann Collette <ycollette dot nospam at free.fr> 1.0.0-1
- initial release
