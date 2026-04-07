# Status: active
# Tag: Guitar, MIDI
# Type: Plugin, LV2
# Category: Audio, Effect, MIDI

%global commit0 dc4565b3827afd34db47d8ecc770a29b1aed61f0

Name: polyphonic-pitch-detector-for-guitars
Version: 0.0.1
Release: 2%{?dist}
Summary: Polyphonic Pitch Detector for guitars
License: GPL-3.0-or-later
URL: https://github.com/luciamarock/Polyphonic-Pitch-Detector-for-guitars
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/luciamarock/Polyphonic-Pitch-Detector-for-guitars/archive/%{commit0}.zip#/%{name}-%{version}.zip
Source1: pdct.svg

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: patchelf
%if 0%{?fedora} <= 38
BuildRequires: wxGTK3-devel
%else
BuildRequires: wxGTK-devel
%endif
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: libsndfile-devel
BuildRequires: desktop-file-utils

%description
This repository hosts a pitch detection application designed for Linux systems,
specifically tailored for guitar input.
The underlying methodology is based on complex resonators and is optimized for
accurate pitch estimation. The theoretical foundation of complex resonators
can be found in the article titled "A Computationally Efficient Method for
 Polyphonic Pitch Estimation" authored by Ruohua Zhou, Joshua D. Reiss,
Marco Mattavelli, and Giorgio Zoia.
The system is currently in a developmental phase to incorporate frequency domain effects.

%prep
%autosetup -n Polyphonic-Pitch-Detector-for-guitars-%{commit0}

sed -i -e "s|cmake_minimum_required (VERSION 2.6)|cmake_minimum_required (VERSION 3.30)|g" CMakeLists.txt
sed -i -e "s|-msse4.2||g" CMakeLists.txt

%build

%set_build_flags
export LDFLAGS="`pkg-config --libs-only-L jack` $LDFLAGS"

%cmake \
%if 0%{?fedora} <= 38
       -DwxWidgets_CONFIG_EXECUTABLE:FILEPATH=/usr/bin/wx-config-3.0 \
%else
       -DwxWidgets_CONFIG_EXECUTABLE:FILEPATH=/usr/bin/wx-config-3.2 \
%endif
       -DCMAKE_EXE_LINKER_FLAGS="-Wl,-rpath,'\$ORIGIN/../%{_lib}/pdct' $LDFLAGS"

%cmake_build

%install

%cmake_install

mkdir -p %{buildroot}/%{_libdir}/pdct/
install -m 755 %{__cmake_builddir}/pdct_lib/libpdct_lib.so %{buildroot}/%{_libdir}/pdct/

# Write the icon
install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
cp %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/pdct.svg

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/pdct.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=pdct
Icon=pdct
Comment=Polyphonic Pitch Detector for guitars
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/pdct.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/pdct.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_libdir}/pdct/*
%{_datadir}/applications/pdct.desktop
%{_datadir}/icons/hicolor/scalable/apps/pdct.svg

%changelog
* Tue Apr 07 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to 0.0.1-2 - fix RPATH change

* Fri Apr 03 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial version - dc4565b3827afd34db47d8ecc770a29b1aed61f0
