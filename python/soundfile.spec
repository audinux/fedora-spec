# Tag: Library, Devel
# Type: Devel
# Category: Programming

%global __python /usr/bin/python3

Name: python3-soundfile
Version: 0.12.1
Release: 1%{?dist}
Summary: SoundFile is an audio library based on libsndfile, CFFI, and NumPy
License: BSD-3-Clause
URL: https://github.com/bastibe/python-soundfile

BuildArch: noarch

Source0: %{pypi_source soundfile}

BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: libsndfile-devel
BuildRequires: python3-cffi
BuildRequires: python3-numpy
BuildRequires: python3-pip
BuildRequires: python3-pytest
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
BuildRequires: pyproject-rpm-macros

Requires: libsndfile
Requires: python3-cffi

Recommends: python3-numpy

%description
PySoundFile is an audio library based on libsndfile, CFFI and NumPy.
Full documentation is available on http://pysoundfile.readthedocs.org/.

PySoundFile can read and write sound files. File reading/writing is
supported through libsndfile, which itself is accessed through CFFI,
a foreign function interface for Python calling C code. PySoundFile
represents audio data as NumPy arrays.

%prep
%autosetup -n soundfile-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files soundfile

%check
%pytest

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/_soundfile.py
%{python_sitelib}/__pycache__/*

%changelog
* Sat Jul 13 2024 Yann Collette <ycollette.nospam@free.fr> - 0.12.1-1
- Initial release
