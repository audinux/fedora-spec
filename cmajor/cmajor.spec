# Tag: Reverb, Compressor, Equalizer, Overdrive
# Type: Plugin, VST3, CLAP, Standalone
# Category: Audio, Effect, Synthesizer

Name: cmajor
Version: 1.0.2591
Release: 1%{?dist}
Summary: Cmajor is a programming language for writing fast, portable audio software.
License: GPL-3.0-or-later
URL: https://github.com/cmajor-lang/cmajor
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# To get the sources, use:
# $ ./source-cmajor.sh 1.0.2562

Source0: cmajor.tar.gz
Source1: source-cmajor.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: python3
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
BuildRequires: webkit2gtk3-devel
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

export CXXFLAGS="-Wno-error=use-after-free -fPIC $CXXFLAGS"

%cmake -DBUILD_PLUGIN=ON -DJUCE_PATH="$CWD/juce"
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
* Sat Jul 27 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.2591-1
- Initial spec file
