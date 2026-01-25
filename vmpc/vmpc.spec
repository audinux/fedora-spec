# Status: active
# Tag: Drum, Synthesizer
# Type: Standalone, Plugin, VST3
# Category: Synthesizer

Name: vmpc
Version: 0.9.0.18
Release: 1%{?dist}
Summary: JUCE implementation of VMPC2000XL
License: GPL-3.0-only
URL: https://github.com/izzyreal/vmpc-juce
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/izzyreal/vmpc-juce/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: vmpc-0001-force-shared.patch

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
A JUCE implementation of VMPC2000XL, the Akai MPC2000XL emulator

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%prep
%autosetup -n vmpc-juce-%{version}

# Remove LV2 plugin ... Segfault during build
sed -i -e "s/FORMATS LV2 VST3 AU AUv3 Standalone/FORMATS VST3 AU AUv3 Standalone/g" CMakeLists.txt

%build

%set_build_flags
export LDFLAGS="`pkg-config --libs-only-L jack` $LDFLAGS"

%cmake -DCMAKE_LIBRARY_PATH="`pkg-config --libs-only-L jack | sed -e 's/-L//g'`" \
       -DBUILD_SHARED_LIBS=OFF

%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_bindir}/

cp -ra %{__cmake_builddir}/vmpc2000xl_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/vmpc2000xl_artefacts/Standalone/* %{buildroot}/%{_bindir}/

%files -n license-%{name}
%doc README.md
%license LICENSE.txt

%files
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Sun Jan 25 2026 Yann Collette <ycollette.nospam@free.fr> - 0.9.0.18-1
- update to 0.9.0.18-1

* Fri Jan 23 2026 Yann Collette <ycollette.nospam@free.fr> - 0.9.0.17-1
- update to 0.9.0.17-1

* Sun Sep 28 2025 Yann Collette <ycollette.nospam@free.fr> - 0.9.0.16-1
- update to 0.9.0.16-1

* Thu Sep 11 2025 Yann Collette <ycollette.nospam@free.fr> - 0.9.0.12-1
- update to 0.9.0.12-1

* Sat Sep 06 2025 Yann Collette <ycollette.nospam@free.fr> - 0.9.0.9-1
- update to 0.9.0.9-1

* Wed Sep 03 2025 Yann Collette <ycollette.nospam@free.fr> - 0.9.0.8-1
- update to 0.9.0.8-1

* Mon Aug 25 2025 Yann Collette <ycollette.nospam@free.fr> - 0.9.0.6-1
- update to 0.9.0.6-1

* Wed Jul 30 2025 Yann Collette <ycollette.nospam@free.fr> - 0.9.0.4-1
- update to 0.9.0.4-1

* Fri Feb 28 2025 Yann Collette <ycollette.nospam@free.fr> - 0.9.0.0-1
- update to 0.9.0.0-1

* Wed Oct 30 2024 Yann Collette <ycollette.nospam@free.fr> - 0.6.4-1
- update to 0.6.4-1

* Tue Aug 13 2024 Yann Collette <ycollette.nospam@free.fr> - 0.6.1-1
- update to 0.6.1-1

* Sat Jun 15 2024 Yann Collette <ycollette.nospam@free.fr> - 0.6.0-1
- update to 0.6.0-1

* Mon Jan 29 2024 Yann Collette <ycollette.nospam@free.fr> - 0.5.14.3-1
- update to 0.5.14.3-1

* Fri Jan 05 2024 Yann Collette <ycollette.nospam@free.fr> - 0.5.14.3-1
- update to 0.5.14.3-1

* Sun Dec 31 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.14.2-1
- update to 0.5.14.2-1

* Sun Dec 31 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.14.1-1
- update to 0.5.14.1-1

* Fri Dec 29 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.14-1
- update to 0.5.14-1

* Thu Dec 28 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.13-1
- update to 0.5.13-1

* Sun Dec 24 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.12-1
- update to 0.5.12-1

* Mon Dec 18 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.11-1
- update to 0.5.11-1

* Sat Dec 16 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.10-1
- update to 0.5.10-1

* Tue Dec 05 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.9-1
- update to 0.5.9-1

* Sun Dec 03 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.8-1
- update to 0.5.8-1

* Tue Oct 03 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.7-1
- update to 0.5.7-1

* Wed Sep 20 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.6-1
- update to 0.5.6-1

* Tue Sep 19 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.5-1
- update to 0.5.5-1

* Sat Aug 19 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.3-1
- update to 0.5.3-1

* Tue Aug 15 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.2-1
- update to 0.5.2-1

* Sun Jul 30 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.1-1
- update to 0.5.1-1

* Mon Jul 10 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.0.6-1
- update to 0.5.0.6-1

* Thu Jul 06 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.0.5-1
- update to 0.5.0.5-1

* Sat Jun 24 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.0.4-1
- update to 0.5.0.4-1

* Sun Mar 12 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.0.3-1
- update to 0.5.0.3-1

* Tue Jan 31 2023 Yann Collette <ycollette.nospam@free.fr> - 0.4.4-1
- Initial spec file
