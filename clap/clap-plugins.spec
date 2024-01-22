# Tag: Tool
# Type: Devel, Plugin, CLAP
# Category: Tool

Summary: An automatic CLAP validation and testing tool
Name: clap-validator
Version: 0.3.2
Release: 1%{?dist}
License: MIT
URL: https://github.com/free-audio/clap-validator

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/free-audio/clap-validator/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake

%description
A validator and automatic test suite for CLAP plugins.
Clap-validator can automatically test one or more plugins for
common bugs and incorrect behavior.

%prep
%autosetup -n %{name}-%{version}

%build

%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%changelog
* Mon Jan 22 2024 Yann Collette <ycollette dot nospam at free.fr> 0.3.2-1
- initial release
