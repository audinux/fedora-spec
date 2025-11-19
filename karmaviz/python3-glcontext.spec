# Status: active
# Tag: Library, Devel
# Type: Devel
# Category: Programming

%global oname glcontext
%global __python /usr/bin/python3

Name: python3-glcontext
Version: 3.0.0
Release: 1%{?dist}
Summary: Connects moderngl to your window or create headless contexts
URL: https://github.com/moderngl/glcontext
License: MIT

Source: https://github.com/moderngl/glcontext/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
BuildRequires: python3-pip
BuildRequires: libX11-devel
BuildRequires: pyproject-rpm-macros

%description
glcontext is a library providing OpenGL implementation for ModernGL on multiple platforms.

%prep
%autosetup -n glcontext-%{version}

%build

%pyproject_wheel

%install

%pyproject_install
%pyproject_save_files glcontext

%files -f %{pyproject_files}
%doc README.md CHANGELOG.md
%license LICENSE

%changelog
* Tue Nov 18 2025 Yann Collette <ycollette.nospam@free.fr> - 3.0.0-1
- Initial spec file 

