Name:    monique-monosynth
Version: 01122021
Release: 1%{?dist}
Summary: Monique is a monophonic synth from Thomas Arndt
License: GPLv3+
URL:     https://github.com/surge-synthesizer/monique-mpnosynth

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

%description
Monique is a monophonic synth from Thomas Arndt which,
in December 2021 became open source as part of the surge-synth-team family of products.
We are thrilled Thomas chose to combine efforts with the rest of the team.
A VST3 Synthesizer

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv3+
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n %{name}

sed -i -e "s/find_package/#find_package/g" cmake/versiontools.cmake
sed -i -e "/Werror/d" CMakeLists.txt

%build

%cmake
%cmake_build

%install 

export HOME=`pwd`
mkdir .vst3
mkdir -p .local/share/Surge

install -m 755 -d %{buildroot}%{_libdir}/
cp -r %{__cmake_builddir}/libs/oddsound-mts/liboddsound-mts.so %{buildroot}/%{_libdir}/

install -m 755 -d %{buildroot}%{_bindir}/
cp -r %{__cmake_builddir}/MoniqueMonosynth_artefacts/Standalone/* %{buildroot}/%{_bindir}/
chrpath --delete %{buildroot}/%{_bindir}/MoniqueMonosynth

install -m 755 -d %{buildroot}%{_libdir}/vst3/MoniqueMonosynth.vst3/
cp -r %{__cmake_builddir}/MoniqueMonosynth_artefacts/VST3/MoniqueMonosynth.vst3/* %{buildroot}/%{_libdir}/vst3/MoniqueMonosynth.vst3/
chrpath --delete %{buildroot}/%{_libdir}/vst3/MoniqueMonosynth.vst3/Contents/%{_target}/MoniqueMonosynth.so

%files
%doc README.md
%license LICENSE LICENSE-gpl3
%{_bindir}/*
%{_libdir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Sun Dec 26 2021 Yann Collette <ycollette.nospam@free.fr> - 01122021-1
- Initial spec file
