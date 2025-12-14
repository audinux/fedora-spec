# Status: active
# Tag: Reverb, Effect
# Type: Plugin, LV2, VST3
# Category: Effect

Name: reevr
Version: 1.2.0
Release: 2%{?dist}
Summary: Convolution reverb with pre and post modulation
License: GPL-3.0-only
URL: https://github.com/tiagolr/reevr
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./ripplerx-source.sh <PROJECT> <TAG>
#        ./ripplerx-source.sh reevr v1.2.0

Source0: reevr.tar.gz
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
REEV-R is a cross-platform convolution reverb with modulation for pre/send and post/volume signals.

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
%autosetup -n reevr

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/

cp -ra %{__cmake_builddir}/REEVR_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/REEVR_artefacts/LV2/* %{buildroot}/%{_libdir}/lv2/

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Sat Dec 13 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-2
- update to 1.2.0-2

* Fri Dec 12 2025 Yann Collette <ycollette.nospam@free.fr> - 1.1.1-2
- update to 1.1.1-2

* Fri Nov 07 2025 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-2
- update to 1.1.0-2

* Wed Sep 03 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-2
- update to 1.0.2-2 - remove unused dep

* Tue Jun 17 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-1
- update to 1.0.2-1

* Thu Jun 12 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
