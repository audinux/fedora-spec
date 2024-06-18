# Tag: Drum, Synthesizer
# Type: Standalone, Plugin, LV2, VST3
# Category: Synthesizer

Name: vmpc
Version: 0.6.0
Release: 1%{?dist}
Summary: JUCE implementation of VMPC2000XL
License: GPL-3.0-only
URL: https://github.com/izzyreal/vmpc-juce
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/izzyreal/vmpc-juce/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: vmpc-0001-fix-build.patch

BuildRequires: gcc gcc-c++
BuildRequires: git
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: libudisks2-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libcurl-devel
BuildRequires: freetype-devel
BuildRequires: rapidjson-devel

%description
A JUCE implementation of VMPC2000XL, the Akai MPC2000XL emulator

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n standalone-%{name}
Summary:  Standalone version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n standalone-%{name}
Standalone version of %{name}

%prep
%setup -n vmpc-juce-%{version}

%build

%set_build_flags

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_bindir}/

cp -ra %{__cmake_builddir}/vmpc2000xl_artefacts/RelWithDebInfo/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/vmpc2000xl_artefacts/RelWithDebInfo/LV2/* %{buildroot}/%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/vmpc2000xl_artefacts/RelWithDebInfo/Standalone/* %{buildroot}/%{_bindir}/

%files
%doc README.md
%license LICENSE.txt

%files -n standalone-%{name}
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
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
