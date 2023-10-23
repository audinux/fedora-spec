%global debug_package %{nil}

Name:    monique-monosynth
Version: 23102022
Release: 1%{?dist}
Summary: Monique is a monophonic synth from Thomas Arndt
License: GPL-3.0-or-later
URL:     https://github.com/surge-synthesizer/monique-monosynth

Vendor:       Audinux
Distribution: Audinux

# To get the sources, use:
# $ ./source-monique-monosynth.sh main

Source0: monique-monosynth.tar.gz
Source1: source-monique-monosynth.sh

BuildRequires: gcc gcc-c++
BuildRequires: libX11-devel
BuildRequires: cmake
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: rsync
BuildRequires: git
BuildRequires: python3
BuildRequires: chrpath
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libcurl-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: pkgconfig(webkit2gtk-4.0)
BuildRequires: patchelf

%description
Monique is a monophonic synth from Thomas Arndt which,
in December 2021 became open source as part of the surge-synth-team family of products.
We are thrilled Thomas chose to combine efforts with the rest of the team.
A VST3 Synthesizer

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n %{name}

sed -i -e "s/find_package/#find_package/g" cmake/versiontools.cmake
sed -i -e "/Werror/d" CMakeLists.txt

# Fix build of juceaide on f36
sed -i -e "s/\"-DJUCE_BUILD_HELPER_TOOLS=ON\"/\"-DJUCE_BUILD_HELPER_TOOLS=ON\" \"-DCMAKE_CXX_FLAGS='-include utility -fPIC'\"/g" libs/JUCE/extras/Build/juceaide/CMakeLists.txt

%build

%set_build_flags

%cmake -DCMAKE_CXX_FLAGS="-include utility -fPIC $CXXFLAGS"
%cmake_build

%install

export HOME=`pwd`
mkdir .vst3
mkdir -p .local/share/Surge

install -m 755 -d %{buildroot}/%{_libdir}/moniquemonosynth
cp -rav %{__cmake_builddir}/libs/oddsound-mts/liboddsound-mts.so %{buildroot}/%{_libdir}/moniquemonosynth/

install -m 755 -d %{buildroot}/%{_bindir}/
cp -rav %{__cmake_builddir}/MoniqueMonosynth_artefacts/Standalone/MoniqueMonosynth %{buildroot}/%{_bindir}/
chrpath --delete %{buildroot}/%{_bindir}/MoniqueMonosynth
patchelf --set-rpath '$ORIGIN/../%{_lib}/moniquemonosynth/' %{buildroot}/%{_bindir}/MoniqueMonosynth

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -rav %{__cmake_builddir}/MoniqueMonosynth_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/
chrpath --delete %{buildroot}/%{_libdir}/vst3/MoniqueMonosynth.vst3/Contents/%{_target}/MoniqueMonosynth.so
patchelf --set-rpath '$ORIGIN/../../../../../%{_lib}/moniquemonosynth/' %{buildroot}/%{_libdir}/vst3/MoniqueMonosynth.vst3/Contents/%{_target}/MoniqueMonosynth.so

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra %{__cmake_builddir}/MoniqueMonosynth_artefacts/CLAP/* %{buildroot}/%{_libdir}/clap/
chrpath --delete %{buildroot}/%{_libdir}/clap/MoniqueMonosynth.clap
patchelf --set-rpath '$ORIGIN/../../../%{_lib}/moniquemonosynth/' %{buildroot}/%{_libdir}/clap/MoniqueMonosynth.clap

%files
%doc README.md
%license LICENSE LICENSE-gpl3
%{_bindir}/*
%{_libdir}/moniquemonosynth/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Sun Dec 26 2021 Yann Collette <ycollette.nospam@free.fr> - 01122021-1
- Initial spec file
