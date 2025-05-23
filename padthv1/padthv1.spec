# Status: active
# Tag: MIDI
# Type: Plugin, LV2
# Category: Audio, Synthesizer
# LastSourceUpdate: 2021

Summary: Old-school all-digital 4-oscillator subtractive polyphonic synthesizer with stereo fx.
Name: padthv1
Version: 1.3.1
Release: 4%{?dist}
URL: https://sourceforge.net/projects/%{name}
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/rncbc/padthv1/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: https://www.linuxsynths.com/Padthv1PatchesDemos/67Padthv1Patches.tar.gz
Patch0:  padthv1-0001-disable-strip.patch

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: lv2-devel >= 1.2.0
BuildRequires: libsndfile-devel
BuildRequires: fftw-devel
BuildRequires: liblo-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

Requires: hicolor-icon-theme

%description
Based on the PADsynth algorithm, by Paul Nasca (ZynAddSubFX),
as a special variant of additive synthesis.

%package -n lv2-%{name}
Summary:  An LV2 port of synthv1
Requires: lv2
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n lv2-%{name}
An LV2 plugin of the padthv1 synthesizer

%prep
%autosetup -p1 -n %{name}-%{version}

%build

%cmake -DCONFIG_QT6=OFF \
       -DCONFIG_JACK=ON \
       -DCMAKE_LIBRARY_PATH="`pkg-config --libs-only-L jack | sed -e 's/-L//g'`"

%cmake_build

%install

%cmake_install

install -m 755 -d %{buildroot}/%{_datadir}/mime/packages/
install -m 755 -d %{buildroot}/%{_datadir}/metainfo/
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/presets/

install -m 644 src/mimetypes/org.rncbc.padthv1.xml %{buildroot}%{_datadir}/mime/packages/padthv1.xml
install -m 644 src/appdata/org.rncbc.padthv1.metainfo.xml %{buildroot}%{_datadir}//metainfo/org.rncbc.padthv1.xml

pushd %{buildroot}/%{_datadir}/%{name}/presets
tar xvfz %{SOURCE1}
popd

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/org.rncbc.padthv1.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.rncbc.padthv1.desktop
#appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.rncbc.padthv1.xml

%files
%doc README
%license LICENSE
%{_datadir}/applications/org.rncbc.padthv1.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_bindir}/%{name}_jack
%{_datadir}/man/man1/%{name}*
%{_datadir}/man/*/man1/%{name}*
%{_datadir}/mime/packages/*.xml
%{_datadir}/metainfo/*.xml
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/presets/*
%{_datadir}/%{name}/palette/*

%files -n lv2-%{name}
%{_libdir}/lv2/%{name}.lv2/

%changelog
* Fri May 09 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.1-4
- update to 1.3.1-4

* Thu Jan 16 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-4
- update to 1.3.0-4

* Mon Dec 16 2024 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-4
- update to 1.2.0-4

* Thu Oct 31 2024 Yann Collette <ycollette.nospam@free.fr> - 1.1.3-4
- update to 1.1.3-4

* Wed Oct 02 2024 Yann Collette <ycollette.nospam@free.fr> - 1.1.2-4
- update to 1.1.2-4

* Sat Sep 21 2024 Yann Collette <ycollette.nospam@free.fr> - 1.1.1-4
- update to 1.1.1-4

* Wed Jun 19 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-4
- update to 1.0.0-4

* Thu May 02 2024 Yann Collette <ycollette.nospam@free.fr> - 0.9.91-4
- update to 0.9.91-4

* Tue Apr 09 2024 Yann Collette <ycollette.nospam@free.fr> - 0.9.90-4
- update to 0.9.90-4

* Fri Jan 26 2024 Yann Collette <ycollette.nospam@free.fr> - 0.9.34-4
- update to 0.9.34-4

* Wed Dec 20 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.33-4
- update to 0.9.33-4

* Tue Sep 12 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.32-4
- update to 0.9.32-4

* Thu Jun 08 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.31-4
- update to 0.9.31-4 - install desktop file

* Thu Jun 08 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.31-3
- update to 0.9.31-3

* Fri Mar 24 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.30-2
- update to 0.9.30-2

* Thu Jan 26 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.29-2
- update to 0.9.29-2 - add some presets

* Wed Jan 25 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.29-1
- update to 0.9.29-1

* Thu Dec 29 2022 Yann Collette <ycollette.nospam@free.fr> - 0.9.28-1
- update to 0.9.28-1

* Tue Jun 07 2022 Yann Collette <ycollette.nospam@free.fr> - 0.9.26-1
- update to 0.9.26-1

* Wed Jan 26 2022 Yann Collette <ycollette.nospam@free.fr> - 0.9.24-1
- update to 0.9.24-1

* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9.17-1
- update to 0.9.17-1 + fix debug build

* Fri Mar 27 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9.13-1
- update to 0.9.13-1

* Sun Mar 15 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9.12-1
- Initial spec file
