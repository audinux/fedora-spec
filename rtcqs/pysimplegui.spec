# Tag: Editor
# Type: Standalone, IDE
# Category: Programming, Audio

Name:    PySimpleGUI
Version: 4.60.3
Release: 1%{?dist}
Summary: Super-simple to create custom GUI
License: LGPLv3+
URL: https://github.com/PySimpleGUI/PySimpleGUI
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/PySimpleGUI/PySimpleGUI/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Python3 programming environment providing a fast and user-friendly abstraction to SuperCollider.
It also comes with its own IDE, which means it can be used straight out of the box;
all you need is Python and SuperCollider and you're ready to go!
Note: no longer actively developed.

%prep
%autosetup -n %{name}-%{version}

rm -rf %{py3dir}
cp -a . %{py3dir}

%build

%set_build_flags

python3 setup.py build

%install

python3 setup.py install --root %{buildroot} --optimize=1 --skip-build

%files
%doc readme.md
%license license.txt
%{python3_sitelib}/%{name}-*.egg-info
%{python3_sitelib}/mkdocs_ivory/*
%{python3_sitelib}/rtd_dropdown/*

%changelog
* Sun Nov 20 2022 Yann Collette <ycollette dot nospam at free.fr> 4.60.3-1
- initial release of the spec file
