# Tag: Synthesizer
# Type: Plugin, VST3, CLAP
# Category: Audio, Synthesizer

%global commit0 75b98515ba51665525dacd545e8e050a8b38bd96

Name: firefly-synth
Version: 0.1
Release: 1%{?dist}
Summary: Semi-modular synthesizer plugin
License: GPL-3.0-or-later
URL: https://github.com/sjoerdvankreel/firefly-synth

Vendor:       Audinux
Distribution: Audinux

# Usage: ./synth-source.sh <PROJECT> <TAG>
#        ./synth-source.sh firefly-synth 75b98515ba51665525dacd545e8e050a8b38bd96

Source0: firefly-synth.tar.gz
Source1: synth-source.sh

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

%description
A semi-modular software synthesizer plugin. It's basically InfernalSynth's big brother.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n %{name}

%build

%cmake -DCMAKE_BUILD_TYPE=RELEASE
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -rav dist/RELEASE/linux/firefly_synth_1.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -rav dist/RELEASE/linux/firefly_synth_1.clap %{buildroot}/%{_libdir}/clap/



%files
%doc README.md FEATURES.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Sat Jan 27 2024 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial spec file
