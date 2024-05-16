# Tag: Jack, Alsa
# Type: Standalone, IDE
# Category: Audio, Programming
# GUIToolkit: Qt5

# Global variables for github repository
%global commit0 af03cba9c166715334c7e3c5263b6505ef16df26
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: faustworks
Version: 0.0.1
Release: 1%{?dist}
Summary: A Faust IDE
URL: https://github.com/grame-cncm/faustworks
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/grame-cncm/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-gui
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-linguist
BuildRequires: desktop-file-utils

%description
FaustWorks is an IDE (Integrated Development Environment) for the
Faust dsp programming language. You must have Faust installed to
be able to use FaustWorks. Platforms supported are Linux and OSX.

%prep
%autosetup -n %{name}-%{commit0}

sed -i -e "s/lrelease/lrelease-qt5/g" FaustWorks.pro

%build

%qmake_qt5 FaustWorks.pro
%make_build

%install

install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 FaustWorks %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
install -m 644 Resources/faustworks.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.svg

# install polyphon.desktop properly.
desktop-file-install --vendor '' \
        --add-category=Graphics \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*

%changelog
* Tue Oct 13 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
