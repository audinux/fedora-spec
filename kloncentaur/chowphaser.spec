# Tag: Guitar, Phaser
# Type: Plugin, VST3
# Category: Audio, Effect

Name: ChowPhaser
Version: 1.1.1
Release: 1%{?dist}
Summary: Phaser effect based loosely on the Schulte Compact Phasing 'A'
License: BSD-3-Clause
URL: https://github.com/jatinchowdhury18/ChowPhaser

Vendor:       Audinux
Distribution: Audinux

# to generater code archive:
# ./source_chowphaser.sh <tag>
# ./source_chowphaser.sh 1.1.1

Source0: ChowPhaser.tar.gz
Source1: source_chowphaser.sh

BuildRequires: gcc-c++
BuildRequires: JUCE
BuildRequires: cmake
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(webkit2gtk-4.0)
BuildRequires: pkgconfig(gtk+-x11-3.0)
BuildRequires: pkgconfig(jack)
BuildRequires: libcurl-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: xsimd-devel
BuildRequires: lv2-devel

%description
CHOW Phaser is an open-source phaser effect, based very loosely on the classic Shulte Compact Phasing "A".

%package -n vst3-%{name}
Summary: CHOW Phaser plugin (VST3)

%description -n vst3-%{name}
CHOW Phaser is an open-source phaser effect, based very loosely on the classic Shulte Compact Phasing "A".

%prep
%autosetup -n ChowPhaser

%build
%set_build_flags

%cmake -B cmake-build -DCMAKE_BUILD_TYPE=Release -DRTNEURAL_XSIMD=ON -DCMAKE_PREFIX_PATH=/usr/lib64/juce
touch cmake-build/ChowPhaserMono_artefacts/JuceLibraryCode/AppConfig.h
touch cmake-build/ChowPhaserStereo_artefacts/JuceLibraryCode/AppConfig.h
cmake --build cmake-build %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
install cmake-build/ChowPhaserMono_artefacts/Release/Standalone/* %{buildroot}%{_bindir}/
install cmake-build/ChowPhaserStereo_artefacts/Release/Standalone/* %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_libdir}/vst3
cp -r cmake-build/ChowPhaserMono_artefacts/Release/VST3/*.vst3 %{buildroot}%{_libdir}/vst3/
cp -r cmake-build/ChowPhaserStereo_artefacts/Release/VST3/*.vst3 %{buildroot}%{_libdir}/vst3/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n vst3-%{name}
%doc README.md
%license LICENSE
%{_libdir}/vst3/

%changelog
* Mon Jun 07 2021 Yann Collette <ycollette.nospam@free.fr> - 1.1.1-1
- Initial spec file
