# Tag: Effect, Plugin, Audio
# Type: Standalone, Plugin, VST3
# Category: Audio, Effect

%global debug_package %{nil}

Name: paulxstretch
Version: 1.6.0
Release: 1%{?dist}
Summary: A Paulstretch VST3/Standalone plugin
License: MIT
URL: https://github.com/essej/paulxstretch
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/essej/paulxstretch/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: fftw-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libX11-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: mesa-libGL-devel
BuildRequires: freetype-devel
BuildRequires: libcurl-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel
BuildRequires: desktop-file-utils

%description
A PaulStretch VST3Standalone plugin

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n %{name}-%{version}

#sed -i -e "s/--config Debug/--config Debug --verbose/g" deps/juce/extras/Build/juceaide/CMakeLists.txt
#sed -i -e "/OUTPUT_VARIABLE/d" deps/juce/extras/Build/juceaide/CMakeLists.txt
sed -i -e "s/\"-DJUCE_BUILD_HELPER_TOOLS=ON\"/\"-DJUCE_BUILD_HELPER_TOOLS=ON\" \"-DCMAKE_CXX_FLAGS='-include utility -fPIC'\"/g" deps/juce/extras/Build/juceaide/CMakeLists.txt

%build

%set_build_flags

%cmake -DCMAKE_CXX_FLAGS="-include utility"
%cmake_build

%install

%cmake_install

install -m 755 -d %{buildroot}%{_libdir}/vst/
install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_bindir}/

install -m 755 %{__cmake_builddir}/PaulXStretch_artefacts/Standalone/paulxstretch %{buildroot}/%{_bindir}/
cp -ra  %{__cmake_builddir}/PaulXStretch_artefacts/VST3/PaulXStretch.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/1024x1024/apps/
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -m 755 -d %{buildroot}%{_datadir}/applications/
install -m 644 images/paulxstretch_icon_1024.png %{buildroot}/%{_datadir}/icons/hicolor/1024x1024/apps/
install -m 644 images/paulxstretch_icon_1024_rounded.png %{buildroot}/%{_datadir}/icons/hicolor/1024x1024/apps/
install -m 644 images/paulxstretch_icon_256.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/
install -m 644 images/paulxstretch_icon_256_rounded.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/
install -m 644 images/paulxstretch_icon.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 linux/%{name}.desktop %{buildroot}%{_datadir}/applications/

desktop-file-install --vendor '' \
        --add-category=AudioVideo \
        --add-category=X-Midi \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md CHANGES.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Wed Jan 18 2023 Yann Collette <ycollette.nospam@free.fr> - 1.6.0-1
- update to 1.6.0-1

* Sun May 01 2022 Yann Collette <ycollette.nospam@free.fr> - 1.5.3-1
- Initial spec file
