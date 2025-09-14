# Status: active
# Tag: Reverb
# Type: Plugin, LV2, CLAP, VST3
# Category: Audio, Effect

Name: roomreverb
Version: 1.4.0
Release: 2%{?dist}
Summary: Room Reverb is a mono/stereo to stereo algorithmic reverb audio plugin
License: GPL-3.0-or-later
URL: https://github.com/cvde/RoomReverb
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./roomreverb-source.sh <tag>
# ./roomreverb-source.sh v1.4.0

Source0: RoomReverb.tar.gz
Source1: roomreverb-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: lv2-devel
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel
BuildRequires: libcurl-devel
BuildRequires: gtk3-devel

%description
Room Reverb is a mono/stereo to stereo algorithmic reverb audio
plugin with many presets that lets you add reverberation to your
recordings in your DAW.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n RoomReverb

%build

%cmake
%cmake_build

%install

install -d 755 %{buildroot}/%{_libdir}/vst3/
install -d 755 %{buildroot}/%{_libdir}/lv2/
install -d 755 %{buildroot}/%{_libdir}/clap/

cp -ra %{__cmake_builddir}/RoomReverb_artefacts/Release/CLAP/* %{buildroot}/%{_libdir}/clap/
cp -ra %{__cmake_builddir}/RoomReverb_artefacts/Release/LV2/* %{buildroot}/%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/RoomReverb_artefacts/Release/VST3/* %{buildroot}/%{_libdir}/vst3/

%files
%doc README.md
%license LICENSE

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Fri Sep 12 2025 Yann Collette <ycollette.nospam@free.fr> - 1.4.0-2
- update to 1.4.0-2

* Wed Aug 13 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-2
- update to 1.3.0-2 - remove an obsolete dependency

* Tue Jan 14 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-1
- update to 1.3.0-1

* Sun Aug 04 2024 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-1
- update to 1.2.0-1

* Fri Aug 25 2023 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- update to 1.1.0-1

* Tue Jan 17 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- update to 1.0.0-1

* Sun Jul 17 2022 Yann Collette <ycollette.nospam@free.fr> - 0.6.1-1
- Initial build
