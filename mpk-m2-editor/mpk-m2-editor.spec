# Tag: MIDI, Editor
# Type: Standalone
# Category: Audio

# Global variables for github repository
%global commit0 78410346fce152d7ef6cadf1ab0588068e5bf387
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%define libname mpk_m2_editor
%define _python_dist_allow_version_zero %{nil}

Name: mpk-m2-editor
Version: 0.0.1
Release: 3%{?dist}
Summary: Alternative to the official AKAI MPKMini MkII Editor
URL: https://github.com/PiOverFour/MPK-M2-editor
License: GPL-3.0-only

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/PiOverFour/MPK-M2-editor/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: desktop-file-utils

Requires: python3-rtmidi
Requires: python3-qt5-base

%description
A Linux editor for the Akai LPD8 pad controller.

%prep
%autosetup -n MPK-M2-editor-%{commit0}

sed -i -e "s/'ui'/'mpk_m2_editor_ui'/g" setup.py
rm -f mpk_m2_editor_ui
ln -s ui mpk_m2_editor_ui
sed -i -e "s/from ui/from mpk_m2_editor_ui/g" mpk-m2-editor

%build

%{py3_build}

%install

%{py3_install}

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
%{_datadir}/%{name}/
%{python3_sitelib}/mpk_m2_editor_ui/*
%{python3_sitelib}/%{libname}-*.egg-info/

%changelog
* Mon Nov 22 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
