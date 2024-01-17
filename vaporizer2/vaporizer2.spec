# Tag: Reverb, Compressor, Equalizer, Overdrive
# Type: Plugin, VST3, Standalone
# Category: Audio, Effect, Synthesizer

Name:    vaporizer2
Version: 3.4.5
Release: 2%{?dist}
Summary: Vaporizer2 hybrid wavetable additive / subtractive VST / AU / AAX synthesizer / sampler workstation plugin
License: GPL-3.0-or-later
URL:     https://github.com/VASTDynamics/Vaporizer2

Vendor:       Audinux
Distribution: Audinux

# To get the sources, use:
# $ ./vaporizer2-source.sh v3.4.5

Source0: Vaporizer2.tar.gz
Source1: vaporizer2-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel
BuildRequires: freetype-devel
BuildRequires: libcurl-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel
BuildRequires: pkgconfig(jack)
BuildRequires: fftw-devel
BuildRequires: desktop-file-utils

%description
PROBABLY THE MOST VERSATILE WAVETABLE SYNTHESIZER.
Vaporizer2 is a hybrid wavetable additive / subtractive VST / AU / AAX / LV2 synthesizer / sampler workstation.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: data-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-3.0-or-later
Requires: data-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n data-%{name}
Summary:  Data and presets for %{name}
License:  GPL-3.0-or-later

%description -n data-%{name}
Data and presets for %{name}

%prep
%autosetup -n Vaporizer2

%build

%set_build_flags

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
install -m 755 -d %{buildroot}/%{_libdir}/vst3/
install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/doc/

cp -ra %{__cmake_builddir}/VASTvaporizer2_artefacts/Release/LV2/* %{buildroot}/%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/VASTvaporizer2_artefacts/Release/VST3/* %{buildroot}/%{_libdir}/vst3/
cp %{__cmake_builddir}/VASTvaporizer2_artefacts/Release/Standalone/* %{buildroot}/%{_bindir}/
cp Documentation/Vaporizer2Manual.pdf %{buildroot}/%{_datadir}/%{name}/doc/

cp -ra VASTvaporizer/Noises %{buildroot}/%{_datadir}/%{name}/
cp -ra VASTvaporizer/Tables %{buildroot}/%{_datadir}/%{name}/
cp -ra VASTvaporizer/Presets %{buildroot}/%{_datadir}/%{name}/

%files
%{_bindir}/*

%files -n data-%{name}
%doc README.md
%license LICENSE
%{_datadir}/%{name}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Mon Dec 25 2023 Yann Collette <ycollette.nospam@free.fr> - 3.4.5-1
- update to 3.4.5-1

* Mon Dec 11 2023 Yann Collette <ycollette.nospam@free.fr> - 3.4.3-1
- update to 3.4.3-1

* Wed Dec 06 2023 Yann Collette <ycollette.nospam@free.fr> - 3.4.1-1
- update to 3.4.1-1

* Mon Dec 04 2023 Yann Collette <ycollette.nospam@free.fr> - 3.4.0-1
- Initial spec file
