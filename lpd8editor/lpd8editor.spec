# Tag: MIDI, Editor
# Type: Standalone
# Category: Audio

Name:    lpd8editor
Version: 0.0.14
Release: 1%{?dist}
Summary: A linux editor for the Akai LPD8
URL:     https://github.com/charlesfleche/lpd8editor
License: GPLv2+

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/charlesfleche/lpd8editor/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: alsa-lib-devel

%description
A Linux editor for the Akai LPD8 pad controller.

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags

%qmake_qt5 CONFIG+=nostrip lpd8editor.pro
%make_build

%install

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/doc/
cp -r doc/* %{buildroot}/%{_datadir}/%{name}/doc/

install -m 755 -d %{buildroot}%{_datadir}/applications/
cp debian/%{name}.desktop %{buildroot}%{_datadir}/applications/

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 src/%{name} %{buildroot}%{_bindir}/%{name}

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 %{name}.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

desktop-file-install --vendor '' \
        --add-category=Midi \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc NOTES.md README.md
%license LICENSE.md
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*
%{_datadir}/%{name}/*

%changelog
* Sun Nov 21 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.14-1
- Initial spec file
