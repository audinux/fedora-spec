# Status: active
# Tag: Jack, Alsa
# Type: Plugin, Standalone, VST3
# Category: Audio, Distortion

Name: drumlabooh
Version: 10.0.1
Release: 2%{?dist}
Summary: LV2/VSTi drum machine that can use Hydrogen, SFZ, and other drumkit formats
License: GPL-3.0-only
URL: https://github.com/psemiletov/drumlabooh
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/psemiletov/drumlabooh/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel

%description
LV2/VSTi drum machine that can use Hydrogen, SFZ, and other drumkit formats

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-3.0-only
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n %{name}-%{version}

%build

%cmake -DINSTALLKITS=OFF
%cmake_build

%install

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_libdir}/vst3/

cp -ra %{__cmake_builddir}/drumlabooh_artefacts/VST3/*   %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/drumlabooh_artefacts/LV2/*    %{buildroot}/%{_libdir}/lv2/
cp %{__cmake_builddir}/drumlabooh_artefacts/Standalone/* %{buildroot}/%{_bindir}/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Wed Aug 13 2025 Yann Collette <ycollette.nospam@free.fr> - 10.0.1-2
- update to 10.0.1-2 - remove an obsolete dependency

* Sat Jun 14 2025 Yann Collette <ycollette.nospam@free.fr> - 10.0.1-1
- update to 10.0.1-1

* Sun Jun 08 2025 Yann Collette <ycollette.nospam@free.fr> - 10.0.0-1
- update to 10.0.0-1

* Tue May 27 2025 Yann Collette <ycollette.nospam@free.fr> - 9.1.0-1
- update to 9.1.0-1

* Thu May 22 2025 Yann Collette <ycollette.nospam@free.fr> - 9.0.0-1
- update to 9.0.0-1

* Sun Apr 27 2025 Yann Collette <ycollette.nospam@free.fr> - 8.0.2-1
- update to 8.0.2-1

* Sun Apr 20 2025 Yann Collette <ycollette.nospam@free.fr> - 8.0.0-1
- update to 8.0.0-1

* Sun Apr 06 2025 Yann Collette <ycollette.nospam@free.fr> - 7.0.1-1
- update to 7.0.1-1

* Sun Mar 30 2025 Yann Collette <ycollette.nospam@free.fr> - 7.0.0-1
- update to 7.0.0-1

* Tue Sep 24 2024 Yann Collette <ycollette.nospam@free.fr> - 6.0.0-1
- update to 6.0.0-1

* Sat Sep 07 2024 Yann Collette <ycollette.nospam@free.fr> - 5.0.0-1
- update to 5.0.0-1

* Tue Aug 13 2024 Yann Collette <ycollette.nospam@free.fr> - 4.0.0-1
- update to 4.0.0-1

* Mon Aug 05 2024 Yann Collette <ycollette.nospam@free.fr> - 3.1.0-1
- update to 3.1.0-1

* Mon Jul 29 2024 Yann Collette <ycollette.nospam@free.fr> - 3.0.1-1
- update to 3.0.1-1

* Thu Jul 25 2024 Yann Collette <ycollette.nospam@free.fr> - 3.0.0-1
- update to 3.0.0-1

* Fri Apr 05 2024 Yann Collette <ycollette.nospam@free.fr> - 2.4.0-1
- update to 2.4.0-1

* Mon Mar 11 2024 Yann Collette <ycollette.nospam@free.fr> - 2.3.0-1
- update to 2.3.0-1

* Wed Jan 24 2024 Yann Collette <ycollette.nospam@free.fr> - 2.2.0-1
- update to 2.2.0-1

* Mon Dec 25 2023 Yann Collette <ycollette.nospam@free.fr> - 2.1.0-1
- update to 2.1.0-1

* Wed Oct 11 2023 Yann Collette <ycollette.nospam@free.fr> - 2.0.2-1
- update to 2.0.2-1

* Mon Oct 09 2023 Yann Collette <ycollette.nospam@free.fr> - 2.0.0-1
- update to 2.0.0-1

* Fri Oct 06 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- update to 1.0.0-1

* Thu Sep 07 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.4-1
- update to 0.0.4-1

* Sat Sep 02 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.2-1
- Initial spec file
