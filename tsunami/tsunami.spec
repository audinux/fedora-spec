# Status: active
# Tag: MIDI
# Type: Standalone
# Category: Audio, DAW

%global commit0 f15579ab1239709b289e73c18349044730012179

Name: tsunami
Version: 2024.10
Release: 2%{?dist}
Summary: A simple but powerful audio editor
URL: https://github.com/momentarylapse/tsunami
ExclusiveArch: x86_64 
License: GPL-3.0-only

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/momentarylapse/tsunami/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: 0001-remove-git-call.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: gtk4-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: portaudio-devel
BuildRequires: alsa-lib-devel
BuildRequires: libvorbis-devel
BuildRequires: libogg-devel
BuildRequires: flac-devel
BuildRequires: fftw-devel
BuildRequires: libunwind-devel
BuildRequires: desktop-file-utils

%description
Tsunami is an open-source digital audio workstation (DAW).
It is designed for ease of use and not-looking-crappy™.

%prep
%autosetup -p1 -n %{name}-%{version}

sed -i "/Exec=/c\Exec=tsunami" static/michisoft-tsunami.desktop
sed -i "/Icon=/c\Icon=tsunami" static/michisoft-tsunami.desktop

sed -i -e "s/extern//g" .cmake/git-version.h
sed -i -e "s/GitHash/GitHash=\"%{commit0}\"/g" .cmake/git-version.h
cp .cmake/git-version.h src

%build

%cmake
%cmake_build

%install

%cmake_install

# install desktop file properly.
desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        static/michisoft-tsunami.desktop

# desktop icon
install -Dm 644 static/icons/tsunami.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/tsunami.svg

# mime
install -Dm 644 static/michisoft-nami.xml %{buildroot}%{_datadir}/mime/packages/michisoft-nami.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/michisoft-tsunami.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/tsunami
%{_datadir}/tsunami/
%{_datadir}/applications/michisoft-tsunami.desktop
%{_datadir}/icons/hicolor/scalable/apps/tsunami.svg
%{_datadir}/mime/packages/michisoft-nami.xml

%changelog
* Fri Oct 25 2024 Yann Collette <ycollette.nospam@free.fr> - 2024.10-2
- update to 2024.10-2

* Sun Oct 22 2023 Justin Koh <j@ustink.org> - 0.7.114-2
- update to 0.7.114-2

* Thu Feb 16 2023 Justin Koh <j@ustink.org> - 0.7.111.0-2
- update to 0.7.111.0-2

* Tue Jan 25 2022 Yann Collette <ycollette.nospam@free.fr> - 0.7.90-2
- Initial spec file + fix installation
