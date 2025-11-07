# Status: active
# Tag: Effect
# Type: Plugin, LV2, VST3
# Category: Effect

Name: gate12
Version: 1.2.1
Release: 2%{?dist}
Summary: Trance gate / volume shaper
License: GPL-3.0-only
URL: https://github.com/tiagolr/gate12
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./ripplerx-source.sh <PROJECT> <TAG>
#        ./ripplerx-source.sh gate12 v1.2.1

Source0: gate12.tar.gz
Source1: ripplerx-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: git
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: libudisks2-devel
BuildRequires: gtk3-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libcurl-devel
BuildRequires: freetype-devel
BuildRequires: rapidjson-devel
BuildRequires: libudisks2-devel

Requires: license-%{name}

%description
GATE-12 is a cross-platform envelope generator for gate/volume control inspired by plugins
like GrossBeat and ShaperBox.

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%prep
%autosetup -n gate12

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/

cp -ra %{__cmake_builddir}/GATE12_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/GATE12_artefacts/LV2/* %{buildroot}/%{_libdir}/lv2/

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Fri Nov 07 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.1-2
- update to 1.2.1-2

* Wed Sep 03 2025 Yann Collette <ycollette.nospam@free.fr> - 1.1.7-2
- update to 1.1.7-2 - remove unused dep

* Sat Jun 14 2025 Yann Collette <ycollette.nospam@free.fr> - 1.1.7-1
- Initial spec file
