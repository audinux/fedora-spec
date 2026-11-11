# Status: active
# Tag: Editor
# Type: Standalone
# Category: Audio

%global pypi_name leggio

Name: python-%{pypi_name}
Version: 0.4.4
Release: 1%{?dist}
Summary: Sheet music viewer for Linux: read your PDF scores from a screen on your music stand
License: GPL-3.0-or-later
URL: https://github.com/MrGilfy/leggio

Source0: https://github.com/MrGilfy/leggio/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3dist(pytest)
BuildRequires: pyproject-rpm-macros
BuildRequires: python3-gobject
BuildRequires: python3-gobject-base
BuildRequires: poppler-glib

Requires: python3-gobject
Requires: python3-gobject-base
Requires: python3-cairo
Requires: gtk4
Requires: libadwaita
Requires: poppler-glib
Requires: hicolor-icon-theme

%description
Leggio keeps a library of your sheet music PDFs, with search, tags and setlists.
Scores open fullscreen with the white margins cut off, and pages turn instantly
by tap, swipe, keyboard or Bluetooth pedal. You can draw on a score, jump to a
D.S. or coda with one tap, bookmark long scores and export them as PDFs, and your
PDF files are never changed.

%package -n python3-%{pypi_name}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Leggio keeps a library of your sheet music PDFs, with search, tags and setlists.
Scores open fullscreen with the white margins cut off, and pages turn instantly
by tap, swipe, keyboard or Bluetooth pedal. You can draw on a score, jump to a
D.S. or coda with one tap, bookmark long scores and export them as PDFs, and your
PDF files are never changed.

%generate_buildrequires
%pyproject_buildrequires -r

%prep
%autosetup -n leggio-%{version}

%build

%pyproject_wheel

%install

%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/leggio

%changelog
* Wed Nov 11 2026 Yann Collette <ycollette.nospam@free.fr> - 0.4.4-1
- initial version of the spec
