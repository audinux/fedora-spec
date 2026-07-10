# Status: active
# Tag: Devel, Tool
# Type: Standalone
# Category: Tool, Programming

%global commit0 b391626bf570fe1e353fbbe2d7b121469a05468c

Summary: C++ build system 
Name: coddle
Version: 0.0.1
Release: 1%{?dist}
License: MIT
URL: https://github.com/coddle-cpp/coddle
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/coddle-cpp/coddle/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make

%description
Yet another build and package system.
If your project contains only C/C++ source code, Coddle will discover
and install dependencies automatically. No config file or Makefile required.

%prep
%autosetup -n %{name}-%{commit0}

sed -i -e "s|clang++ -Wall -pipe -march=native|g++ -Wall -pipe \$CXXFLAGS|g" build.sh
sed -i -e "s|clang++ |g++ \$(LDFLAGS)|g" build.sh

%build

%set_build_flags
export CXXFLAGS="-fPIC $CXXFLAGS" 

./build.sh

%install

install -m 755 -d %{buildroot}/%{_bindir}/

cp coddle %{buildroot}/%{_bindir}/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%changelog
* Thu Jul 09 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- initial release
