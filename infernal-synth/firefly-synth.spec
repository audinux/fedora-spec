# Tag: Synthesizer
# Type: Plugin, VST3, CLAP
# Category: Audio, Synthesizer

Name: firefly-synth
Version: 1.04
Release: 1%{?dist}
Summary: Semi-modular synthesizer plugin
License: GPL-3.0-or-later
URL: https://github.com/sjoerdvankreel/firefly-synth

Vendor:       Audinux
Distribution: Audinux

# Usage: ./synth-source.sh <PROJECT> <TAG>
#        ./synth-source.sh firefly-synth v1.04

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
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Sat Feb 09 2024 Yann Collette <ycollette.nospam@free.fr> - 1.04-1
- update to 1.04-1

* Sat Feb 03 2024 Yann Collette <ycollette.nospam@free.fr> - 1.03-1
- update to 1.03-1

* Sat Feb 03 2024 Yann Collette <ycollette.nospam@free.fr> - 1.02-1
- update to 1.02-1

* Thu Feb 01 2024 Yann Collette <ycollette.nospam@free.fr> - 1.01-1
- update to 1.01-1

* Sun Jan 28 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- update to 1.0-1

* Sat Jan 27 2024 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial spec file
