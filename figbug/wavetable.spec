# Status: active
# Tag: Jack, Synthesizer
# Type: Standalone, VST3, LV2
# Category: Synthesizer

Name: wavetable
Version: 1.0.23
Release: 2%{?dist}
Summary: Wavetable synth
License: BSD-3-Clause
URL: https://github.com/FigBug/Wavetable
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./figbug-source.sh <project> <tag>
# ./figbug-source.sh Wavetable 1.0.23

Source0: Wavetable.tar.gz
Source1: figbug-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: gtk3-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)

%description
Wavetable synth

%package -n license-%{name}
Summary: License and documentation for %{name}
License: BSD-3-Clause

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: BSD-3-Clause
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: BSD-3-Clause
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n Wavetable

sed -i -e "s/-static-libstdc++/-lstdc++/g" CMakeLists.txt

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_bindir}/

install -m 755 -p %{__cmake_builddir}/Wavetable_artefacts/Standalone/Wavetable %{buildroot}/%{_bindir}/
cp -ra %{__cmake_builddir}/Wavetable_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Wavetable_artefacts/LV2/* %{buildroot}/%{_libdir}/lv2/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Sun Aug 31 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.23-2
- update to 1.0.23-2 - remove unused dep

* Fri Feb 14 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.23-1
- update to 1.0.23-1

* Sat Oct 12 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.22-1
- update to 1.0.22-1

* Wed Mar 06 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.21-1
- update to 1.0.21-1

* Tue Jan 23 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.20-1
- update to 1.0.20-1

* Sat Oct 21 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.18-1
- update to 1.0.18-1

* Sun Oct 15 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.17-1
- update to 1.0.17-1

* Wed Oct 11 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.16-1
- update to 1.0.16-1

* Mon Oct 09 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.15-1
- update to 1.0.15-1

* Mon Oct 09 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.14-1
- update to 1.0.14-1

* Sat Oct 07 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.12-1
- update to 1.0.12-1

* Fri Oct 06 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.11-1
- update to 1.0.11-1

* Wed Oct 04 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.9-1
- update to 1.0.9-1

* Tue Oct 03 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.8-1
- update to 1.0.8-1

* Tue Oct 03 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.7-1
- update to 1.0.7-1

* Sun Oct 01 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.6-1
- update to 1.0.6-1

* Sun Oct 01 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.5-1
- update to 1.0.5-1

* Sat Sep 30 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.4-1
- update to 1.0.4-1

* Thu Sep 28 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.3-1
- update to 1.0.3-1

* Mon Sep 25 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-1
- update to 1.0.2-1

* Sun Sep 24 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-1
- update to 1.0.1-1

* Sat Sep 23 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- update to 1.0.0-1

* Thu Sep 21 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.11-1
- update to 0.0.11-1

* Wed Sep 20 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.10-1
- update to 0.0.10-1

* Sun Sep 10 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.8-1
- update to 0.0.8-1

* Thu Sep 07 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.7-1
- update to 0.0.7-1

* Tue Sep 05 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.5-1
- Initial spec file
