%define _lto_cflags %{nil}

Name:    vmpc
Version: 0.5.1
Release: 1%{?dist}
Summary: JUCE implementation of VMPC2000XL
License: GPL-3.0-only
URL:     https://github.com/izzyreal/vmpc-juce

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/izzyreal/vmpc-juce/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: vmpc-0001-fix-build.patch

BuildRequires: gcc gcc-c++
BuildRequires: git
BuildRequires: cmake
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: libudisks2-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: libcurl-devel
BuildRequires: freetype-devel
BuildRequires: rapidjson-devel

%description
a JUCE implementation of VMPC2000XL, the Akai MPC2000XL emulator

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%setup -n vmpc-juce-%{version}

%build

%set_build_flags

%if 0%{?fedora} >= 38
%cmake -DCMAKE_CXX_FLAGS="-include cstdint $CXXFLAGS"
%else
%cmake
%endif

sed -i -e "/mpc-tests/d" editables/mpc/CMakeLists.txt
%cmake_build --target vmpc2000xl_Standalone vmpc2000xl_VST3 
# vmpc2000xl_LV2

%install 

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_bindir}

cp -ra %{__cmake_builddir}/vmpc2000xl_artefacts/RelWithDebInfo/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/vmpc2000xl_artefacts/RelWithDebInfo/Standalone/* %{buildroot}%{_bindir}/

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
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
