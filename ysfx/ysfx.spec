# Status: active
# Tag: Audio, Tool
# Type: Plugin, VST3; CLAP
# Category: Audio, Tool

Name: ysfx
Version: 0.0.31
Release: 1%{?dist}
Summary: Hosting library for JSFX
URL: https://github.com/JoepVanlier/ysfx
ExclusiveArch: x86_64 aarch64
License: Apache-2.0

Vendor:       Audinux
Distribution: Audinux

# ./ysfx-source.sh v0.0.31

Source0: ysfx.tar.gz
Source1: ysfx-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel
BuildRequires: libcurl-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel

%description
This package provides support for audio and MIDI effects developed with the
JSFX language. These effects exist in source code form, and they are compiled
and ran natively by hosting software.
This contains a hosting library, providing a JSFX compiler and runtime.
In addition, there is an audio plugin which can act as a JSFX host in a
digital audio workstation.

%package -n license-%{name}
Summary: License and documentations for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentations for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep

%autosetup -n ysfx

sed -i -e "s/set(SUFFIX \" FX\")/set(SUFFIX \"_FX\")/g" cmake.plugin.txt
sed -i -e "s/set(SUFFIX \" instrument/set(SUFFIX \"_instrument/g" cmake.plugin.txt

%build

%cmake 
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/ysfx_plugin_artefacts/RelWithDebInfo/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/ysfx_plugin_instrument_artefacts/RelWithDebInfo/VST3/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra %{__cmake_builddir}/ysfx_plugin_artefacts/RelWithDebInfo/CLAP/* %{buildroot}/%{_libdir}/clap/
cp -ra %{__cmake_builddir}/ysfx_plugin_instrument_artefacts/RelWithDebInfo/CLAP/* %{buildroot}/%{_libdir}/clap/

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Thu Dec 26 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.31-1
- update to 0.0.31-1

* Mon Dec 16 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.30-1
- update to 0.0.30-1

* Sun Dec 08 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.29-1
- update to 0.0.29-1

* Tue Dec 03 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.28-1
- update to 0.0.28-1

* Sat Nov 16 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.27-1
- update to 0.0.27-1

* Wed Oct 09 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.26-1
- update to 0.0.26-1

* Fri Sep 27 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.25-1
- update to 0.0.25-1

* Sat Sep 21 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.24-1
- update to 0.0.24-1

* Tue Sep 17 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.23-1
- update to 0.0.23-1 - move to https://github.com/JoepVanlier/ysfx

* Fri Nov 10 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
