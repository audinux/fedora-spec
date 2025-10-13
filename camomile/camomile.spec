# Status: active
# Tag: Tool
# Type: Plugin, VST3, Standalone
# Category: Audio, Tool, Programming

Name: camomile
Version: 1.0.8
Release: 1%{?dist}
Summary: An audio plugin with Pure Data embedded that allows to load and to control patches
URL: https://github.com/pierreguillot/Camomile
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-or-later

Vendor:       Audinux
Distribution: Audinux

# Usage: ./camomile-source.sh <TAG>
#        ./camomile-source.sh dev/v1.0.8

Source0: Camomile.tar.gz
Source3: camomile-source.sh
Patch0: camomile-0001-fix-fsqrt.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: freetype-devel
BuildRequires: libpng-devel
BuildRequires: harfbuzz-devel
BuildRequires: glib2-devel
BuildRequires: alsa-lib-devel
BuildRequires: webkit2gtk4.1-devel
BuildRequires: gtk3-devel
BuildRequires: libcurl-devel
BuildRequires: libsndfile-devel
BuildRequires: desktop-file-utils

Requires: dejavu-sans-mono-fonts

%description
Camomile is a meta plugin with Pure Data embedded that allows creating
audio plugins that load and control Pure Data patches inside digital
audio workstations.
Camomile supports the VST3, LV2 and Audio Unit plugin formats on Windows,
Linux and macOS.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -p1 -n Camomile

%build

%set_build_flags
export CXXFLAGS="`pkg-config --cflags gtk+-3.0 webkit2gtk-4.1` $CXXFLAGS"

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/vst3/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/lv2/

cd Plugins
cp camomile %{buildroot}/%{_bindir}/
cp -rav CamomileFx.vst3 %{buildroot}/%{_libdir}/vst3/
cp -rav Camomile.vst3 %{buildroot}/%{_libdir}/vst3/
cp -rav Examples %{buildroot}/%{_datadir}/%{name}/
cp Camomile_LV2.so lv2_file_generator %{buildroot}/%{_datadir}/%{name}/lv2/

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/%{name}/

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Mon Oct 13 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.8-1
- update to 1.0.8-1

* Wed Feb 15 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.7-1
- Initial spec file
