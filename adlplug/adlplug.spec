# Tag: MIDI, FM, Emulator
# Type: Plugin, VST, LV2
# Category: Audio, Synthesizer

Name:    adlplug
Version: 1.0.2
Release: 6%{?dist}
Summary: Synthesizer plugin for ADLMIDI (VST/LV2)
URL:     https://github.com/jpcima/ADLplug
ExclusiveArch: x86_64 aarch64
License: BSL-1.0

Vendor:       Audinux
Distribution: Audinux

# ./adlplug-source.sh v1.0.2

Source0: ADLplug.tar.gz
Source1: adlplug-source.sh
Patch0:  adlplug-0001-fix-JUCE-compilation.patch

BuildRequires: gcc gcc-c++
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel

%description
FM synthesizer plugins, based on OPL3 and OPN2 sound chip emulations.

%package -n opnplug
Summary:    Synthesizer plugin for OPNMIDI (VST/LV2)
Requires:   %{name}%{?_isa} = %{version}-%{release}, pkgconfig

%description -n opnplug
Synthesizer plugin for OPNMIDI (VST/LV2)

%prep

%autosetup -p1 -n ADLplug

%build

%set_build_flags

mkdir -p build_adl
cd build_adl

cmake -DCMAKE_INSTALL_PREFIX=/usr \
      -DCMAKE_INSTALL_LIBDIR=%{_lib} \
      -DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
      ..

%make_build

cd ..

mkdir -p build_opn
cd build_opn

cmake -DCMAKE_INSTALL_PREFIX=/usr \
      -DCMAKE_INSTALL_LIBDIR=%{_lib} \
      -DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
      -DADLplug_CHIP=OPN2 \
      ..

%make_build

%install

cd build_adl

%make_install

desktop-file-install --vendor '' \
        --add-category=Midi \
        --add-category=Audio \
        --add-category=AudioVideo \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/ADLplug.desktop

cd ..
cd build_opn

%make_install

desktop-file-install --vendor '' \
        --add-category=Midi \
        --add-category=Audio \
        --add-category=AudioVideo \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/OPNplug.desktop

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/ADLplug.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/OPNplug.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/ADLplug
%{_libdir}/lv2/ADLplug.lv2/*
%{_libdir}/vst/ADLplug.so
%{_datadir}/applications/ADLplug.desktop
%{_datadir}/pixmaps/ADLplug.png
%{_datadir}/icons/hicolor/32x32/apps/ADLplug.png
%{_datadir}/icons/hicolor/96x96/apps/ADLplug.png

%files -n opnplug
%doc README.md
%license LICENSE
%{_bindir}/OPNplug
%{_libdir}/lv2/OPNplug.lv2/*
%{_libdir}/vst/OPNplug.so
%{_datadir}/applications/OPNplug.desktop
%{_datadir}/pixmaps/OPNplug.png
%{_datadir}/icons/hicolor/32x32/apps/OPNplug.png
%{_datadir}/icons/hicolor/96x96/apps/OPNplug.png

%changelog
* Mon Oct 5 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-5
- fix for fedora 33

* Wed Aug 5 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-4
- update to 1.0.2-4

* Wed Apr 22 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-4
- update for Fedora 32

* Mon Apr 15 2019 Yann Collette <ycollette.nospam@free.fr> - 1.0.1
- update to 1.0.1

* Mon Mar 18 2019 Yann Collette <ycollette.nospam@free.fr> - 1.0.0
- update to 1.0.0

* Sun Nov 11 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-beta.4-3
- update to 1.0.0-beta.4.3

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-beta.3-3
- update for Fedora 29

* Thu Oct 11 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-beta.3-3
- update to 1.0.0-beta.3-3

* Thu Oct 04 2018 Jean Pierre Cimalando <jp-dev.nospam@inbox.ru> - 1.0.0-beta.2-1
- update to latest master version
- update package summary
- remove a libcurl-devel dependency which became unnecessary

* Fri Sep 28 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-beta.1-2
- update to latest master version

* Sat Sep 22 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-beta.1-1
- Initial spec file
