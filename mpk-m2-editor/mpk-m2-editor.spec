# Tag: MIDI, Editor
# Type: Standalone
# Category: Audio

# Global variables for github repository
%global commit0 36b5571c7530a224c71c640610f3e9622b989087
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%define libname mpk_m2_editor

Name:    mpk-m2-editor
Version: 0.0.1
Release: 1%{?dist}
Summary: Alternative to the official AKAI MPKMini MkII Editor
URL:     https://github.com/PiOverFour/MPK-M2-editor
License: GPLv3

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/PiOverFour/MPK-M2-editor/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildArch: noarch

BuildRequires: desktop-file-utils
BuildRequires: python3-devel
BuildRequires: python3-rtmidi
BuildRequires: python3-qt5-base
BuildRequires: python3-setuptools

%description
A Linux editor for the Akai LPD8 pad controller.

%prep
%autosetup -n MPK-M2-editor-%{commit0}

%build

%{__python3} setup.py build

%install

%{__python3} setup.py install --root %{buildroot}

install -m 755 -d %{buildroot}%{_datadir}/applications/
cp ressources/%{name}.desktop %{buildroot}%{_datadir}/applications/

install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/128x128/
cp ressources/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/128x128/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/doc/
cp -r docs/* %{buildroot}/%{_datadir}/%{name}/doc/

desktop-file-install --vendor '' \
        --add-category=Midi \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE_GPL3.md LICENSE_OTHERS.md
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*
%{_datadir}/%{name}/*
%{python3_sitelib}/ui/*
%{python3_sitelib}/%{libname}-*.egg-info/

%changelog
* Mon Nov 22 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
