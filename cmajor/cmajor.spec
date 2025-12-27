# Status: active
# Tag: Reverb, Compressor, Equalizer, Overdrive
# Type: Plugin, VST3, Standalone
# Category: Audio, Effect, Synthesizer

%global toolchain clang

Name: cmajor
Version: 1.0.3088
Release: 1%{?dist}
Summary: Cmajor is a programming language for writing fast, portable audio software.
License: GPL-3.0-or-later
URL: https://github.com/cmajor-lang/cmajor
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# To get the sources, use:
# $ ./source-cmajor.sh 1.0.3088

Source0: cmajor.tar.gz
Source1: source-cmajor.sh

BuildRequires: clang
BuildRequires: cmake
BuildRequires: git
BuildRequires: python3
BuildRequires: mold
BuildRequires: alsa-lib-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel
BuildRequires: freetype-devel
BuildRequires: libcurl-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: webkit2gtk4.1-devel
BuildRequires: gtk3-devel
BuildRequires: pkgconfig(jack)
BuildRequires: chrpath

%description
Cmajor is published under a dual GPLv3 (or later)/Commercial license.

All the files in this repository that are marked as being copyright of Cmajor
Software Ltd are covered by these licensing terms, but please note that the
repository also contains some 3rd-party code from other open-source projects.
It is your responsibility when using this codebase to ensure you comply with
the terms of all the code that you use.

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n example-%{name}
Summary: Examples for %{name}
License: GPL-3.0-or-later
Requires: %{name}

%description -n example-%{name}
Examples for %{name}

%package devel
Summary: Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Headers and development files for %{name}

%prep
%autosetup -n cmajor

%build

export CWD=`pwd`

# CMAJ_INCLUDE_SERVER:              FALSE
# CMAJ_INCLUDE_SCRIPTING:           FALSE
# CMAJ_INCLUDE_PLAYBACK:            TRUE
# CMAJ_ENABLE_PERFORMER_LLVM:       TRUE
# CMAJ_ENABLE_PERFORMER_WEBVIEW:    FALSE
# CMAJ_ENABLE_PERFORMER_CPP:        FALSE
# CMAJ_ENABLE_CODEGEN_CPP:          FALSE
# CMAJ_ENABLE_CODEGEN_LLVM_WASM:    FALSE

%set_build_flags

export CXXFLAGS="-Wno-error=use-after-free -fPIC `pkg-config --libs-only-L jack` $CXXFLAGS"
export CFLAGS="`pkg-config --libs-only-L jack` $LDFLAGS"
export LDFLAGS="`pkg-config --libs-only-L jack` $LDFLAGS"

%cmake -DBUILD_PLUGIN=ON \
       -DJUCE_PATH="$CWD/juce" \
       -DWARNINGS_AS_ERRORS=OFF \
       -DCMAKE_EXE_LINKER_FLAGS="-fuse-ld=mold $LDFLAGS" \
       -DCMAKE_SHARED_LINKER_FLAGS="-fuse-ld=mold $LDFLAGS" \
       -DCMAKE_MODULE_LINKER_FLAGS="-fuse-ld=mold $LDFLAGS" \
       -DWEBKIT2_GTK_VERSION="webkit2gtk-4.1"
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 %{__cmake_builddir}/tools/command/cmaj %{buildroot}/%{_bindir}/

install -m 755 %{__cmake_builddir}/examples/native_apps/DiodeClipper %{buildroot}/%{_bindir}/
install -m 755 %{__cmake_builddir}/examples/native_apps/DynamicGain  %{buildroot}/%{_bindir}/
install -m 755 %{__cmake_builddir}/examples/native_apps/HelloCmajor  %{buildroot}/%{_bindir}/
install -m 755 %{__cmake_builddir}/examples/native_apps/RenderPatch  %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_libdir}/
install -m 755 %{__cmake_builddir}/tools/CmajDLL//libCmajPerformer.so %{buildroot}/%{_libdir}/

install -m 755 -d %{buildroot}/%{_includedir}/
cp -rav include/cmajor %{buildroot}/%{_includedir}/

install -m 755 -d %{buildroot}/%{_datadir}/cmajor/examples/
cp -rav examples/* %{buildroot}/%{_datadir}/cmajor/examples/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -rav %{__cmake_builddir}/tools/CmajPlugin/CmajPlugin_artefacts/VST3/*.vst3 %{buildroot}/%{_libdir}/vst3/

# Clean rpath

chrpath --delete %{buildroot}/%{_bindir}/DiodeClipper 
chrpath --delete %{buildroot}/%{_bindir}/DynamicGain
chrpath --delete %{buildroot}/%{_bindir}/HelloCmajor
chrpath --delete %{buildroot}/%{_bindir}/RenderPatch

chrpath --delete %{buildroot}/%{_libdir}/vst3/CmajPlugin.vst3/Contents/%{_target}/CmajPlugin.so
chrpath --delete %{buildroot}/%{_libdir}/libCmajPerformer.so

chrpath --delete %{buildroot}/%{_bindir}/cmaj

%files
%doc README.md docs/*
%license LICENSE.md
%{_bindir}/cmaj

%files devel
%{_libdir}/libCmajPerformer.so
%{_includedir}/cmajor/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n example-%{name}
%{_bindir}/DiodeClipper
%{_bindir}/DynamicGain
%{_bindir}/HelloCmajor
%{_bindir}/RenderPatch
%{_datadir}/cmajor/examples/*

%changelog
* Sat Dec 20 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.3088-1
- Update to 1.0.3088-1

* Sun Nov 23 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.3066-1
- Update to 1.0.3066-1

* Sun Nov 09 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.3029-1
- Update to 1.0.3029-1

* Sat Oct 04 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.3017-1
- Update to 1.0.3017-1

* Fri Oct 03 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.3016-1
- Update to 1.0.3016-1

* Wed Oct 01 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.3014-1
- Update to 1.0.3014-1

* Wed Oct 01 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.3013-1
- Update to 1.0.3013-1

* Tue Sep 30 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.3009-1
- Update to 1.0.3009-1

* Sun Sep 14 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.2997-1
- Update to 1.0.2997-1

* Fri Sep 12 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.2990-1
- Update to 1.0.2990-1

* Sun Aug 17 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.2956-1
- Update to 1.0.2956-1

* Wed Jul 30 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.2945-1
- Update to 1.0.2945-1

* Tue Jul 29 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.2944-1
- Update to 1.0.2944-1

* Thu Jul 24 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.2926-1
- Update to 1.0.2926-1

* Mon Jul 14 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.2921-1
- Update to 1.0.2921-1

* Thu Jun 12 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.2901-1
- Update to 1.0.2901-1

* Wed May 28 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.2893-1
- Update to 1.0.2893-1

* Fri May 02 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.2844-1
- Update to 1.0.2844-1

* Tue Apr 22 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.2829-1
- Update to 1.0.2829-1

* Tue Apr 15 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.2827-1
- Update to 1.0.2827-1

* Thu Mar 06 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.2788-1
- Update to 1.0.2788-1

* Sun Feb 16 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.2771-1
- Update to 1.0.2771-1

* Tue Feb 04 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.2767-1
- Update to 1.0.2767

* Mon Feb 03 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.2764-1
- Update to 1.0.2764

* Mon Jan 27 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.2763-1
- Update to 1.0.2763

* Fri Nov 15 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.2738-1
- Update to 1.0.2738

* Fri Nov 01 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.2724-1
- Update to 1.0.2724-1

* Wed Oct 30 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.2710-1
- Update to 1.0.2710-1

* Fri Oct 18 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.2688-1
- Update to 1.0.2688-1

* Sat Oct 12 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.2677-1
- Update to 1.0.2677-1

* Fri Oct 04 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.2662-1
- Update to 1.0.2662-1

* Fri Oct 04 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.2661-1
- Update to 1.0.2661-1

* Tue Oct 01 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.2658-1
- Update to 1.0.2658-1

* Fri Sep 27 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.2656-1
- Update to 1.0.2656-1

* Sat Sep 21 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.2639-1
- Update to 1.0.2639-1

* Wed Sep 04 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.2634-1
- Update to 1.0.2634-1

* Thu Aug 15 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.2616-1
- Update to 1.0.2616-1

* Sat Jul 27 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.2591-1
- Initial spec file
