# Tag: MIDI, Editor
# Type: Standalone
# Category: Audio

Name:    lpd8editor
Version: 0.0.16
Release: 1%{?dist}
Summary: A linux editor for the Akai LPD8
URL:     https://github.com/charlesfleche/lpd8editor
License: GPLv2+

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/charlesfleche/lpd8editor/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: qt5-linguist
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils

%description
A Linux editor for the Akai LPD8 pad controller.

%prep
%autosetup -n %{name}-%{version}

%build

%cmake
%cmake_build

%install

%cmake_install

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/doc/
cp -r doc/* %{buildroot}/%{_datadir}/%{name}/doc/

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 %{name}.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name
Exec=%{name}
Icon=%{name}
Comment=LPD8Editor
Terminal=false
Type=Application
Categories=AudioVideo;Audio;
EOF

desktop-file-install --vendor '' \
        --add-category=Midi \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/%{name}/

%changelog
* Sun Apr 17 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.16-1
- Update to 0.0.16-1

* Sun Nov 21 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.14-1
- Initial spec file
