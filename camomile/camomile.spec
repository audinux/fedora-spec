# Tag: Tool
# Type: Plugin, VST3, Standalone
# Category: Audio, Tool, Programming

Name:    camomile
Version: 1.0.7
Release: 1%{?dist}
Summary: An audio plugin with Pure Data embedded that allows to load and to control patches
URL:     https://github.com/pierreguillot/Camomile
License: GPLv3+

Vendor:       Audinux
Distribution: Audinux

# Usage: ./camomile-source.sh <TAG>
# ./camomile-source.sh v1.0.7

Source0: Camomile.tar.gz
Source3: camomile-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: freetype-devel
BuildRequires: libpng-devel
BuildRequires: harfbuzz-devel
BuildRequires: glib2-devel
BuildRequires: alsa-lib-devel
BuildRequires: webkit2gtk3-devel
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
License:  GPLv2+
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n Camomile

%build

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
* Wed Feb 15 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.7-1
- Initial spec file
