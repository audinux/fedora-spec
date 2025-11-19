# Status: active
# Tag: Library, Devel
# Type: Devel
# Category: Programming

%global oname moderngl
%global __python /usr/bin/python3

Name: python3-moderngl
Version: 5.12.0
Release: 1%{?dist}
Summary: Modern OpenGL binding for Python
URL: https://github.com/moderngl/moderngl
License: MIT

Source: https://github.com/moderngl/moderngl/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
BuildRequires: python3-pip
BuildRequires: pyproject-rpm-macros

%description
ModernGL is a Python wrapper over OpenGL Core.
ModernGL simplifies the creation of graphics applications like scientific simulations,
games or user interfaces.
Usually, acquiring in-depth knowledge of OpenGL requires a steep learning curve.
In contrast, ModernGL is easy to learn and use. ModernGL is capable of rendering
with high performance and quality, with less code written.

%prep
%autosetup -n moderngl-%{version}

%build

%pyproject_wheel

%install

%pyproject_install
%pyproject_save_files moderngl

%files -f %{pyproject_files}
%doc README.md CHANGELOG.md
%license LICENSE
%{_libdir}/python%{python3_version}/site-packages/__pycache__/*
%{_libdir}/python%{python3_version}/site-packages/_moderngl.py
%{_libdir}/python%{python3_version}/site-packages/moderngl-stubs/__init__.pyi

%changelog
* Tue Nov 18 2025 Yann Collette <ycollette.nospam@free.fr> - 5.12.0-1
- Initial spec file 

