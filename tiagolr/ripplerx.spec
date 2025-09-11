# Status: active
# Tag: Synthesizer
# Type: Plugin, LV2, VST3
# Category: Synthesizer

Name: ripplerx
Version: 1.5.16
Release: 1%{?dist}
Summary: A physically modeled synth
License: GPL-3.0-only
URL: https://github.com/tiagolr/ripplerx
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./ripplerx-source.sh <PROJECT> <TAG>
#        ./ripplerx-source.sh ripplerx v1.5.16

Source0: ripplerx.tar.gz
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
RipplerX is a physically modeled synth, capable of sounds similar
to AAS Chromaphone and Ableton Collision.

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
%autosetup -n ripplerx

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/

cp -ra %{__cmake_builddir}/RipplerX_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/RipplerX_artefacts/LV2/* %{buildroot}/%{_libdir}/lv2/

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Thu Sep 11 2025 Yann Collette <ycollette.nospam@free.fr> - 1.5.16-1
- update to 1.5.16-1

* Wed Sep 10 2025 Yann Collette <ycollette.nospam@free.fr> - 1.5.15-1
- update to 1.5.15-1

* Tue Sep 09 2025 Yann Collette <ycollette.nospam@free.fr> - 1.5.14-1
- update to 1.5.14-1

* Tue Sep 09 2025 Yann Collette <ycollette.nospam@free.fr> - 1.5.10-1
- update to 1.5.10-1

* Sun Sep 07 2025 Yann Collette <ycollette.nospam@free.fr> - 1.5.8-1
- update to 1.5.8-1

* Sat Sep 06 2025 Yann Collette <ycollette.nospam@free.fr> - 1.5.7-1
- update to 1.5.7-1

* Fri Sep 05 2025 Yann Collette <ycollette.nospam@free.fr> - 1.5.6-1
- update to 1.5.6-1

* Fri Sep 05 2025 Yann Collette <ycollette.nospam@free.fr> - 1.5.3-1
- update to 1.5.3-1

* Thu Sep 04 2025 Yann Collette <ycollette.nospam@free.fr> - 1.5.2-1
- update to 1.5.2-1

* Thu Sep 04 2025 Yann Collette <ycollette.nospam@free.fr> - 1.5.1-1
- update to 1.5.1-1

* Wed Sep 03 2025 Yann Collette <ycollette.nospam@free.fr> - 1.5.0-1
- update to 1.5.0-1

* Fri Mar 14 2025 Yann Collette <ycollette.nospam@free.fr> - 1.4.3-1
- update to 1.4.3-1

* Mon Feb 24 2025 Yann Collette <ycollette.nospam@free.fr> - 1.4.2-1
- update to 1.4.2-1

* Thu Feb 20 2025 Yann Collette <ycollette.nospam@free.fr> - 1.4.1-1
- update to 1.4.1-1

* Tue Feb 18 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.5-1
- update to 1.3.5-1

* Tue Feb 18 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.1-1
- update to 1.3.1-1

* Mon Feb 17 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.3-1
- update to 1.2.3-1

* Sat Feb 15 2025 Yann Collette <ycollette.nospam@free.fr> - 1.1.1-1
- Initial spec file
