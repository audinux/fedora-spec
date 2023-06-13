# Tag: Reverb, Convolution
# Type: Plugin, LV2, Standalone
# Category: Audio, Effect

Name:    hybridreverb2
Version: 2.1.2
Release: 1%{?dist}
Summary: Reverb effect using hybrid impulse convolution
URL:     https://github.com/jpcima/HybridReverb2
License: BSL-1.0

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/jpcima/HybridReverb2/releases/download/v%{version}/HybridReverb2-%{version}.tar.gz
Source1: https://github.com/jpcima/HybridReverb2-impulse-response-database/archive/v1.0.0.zip#/impulse-response-database.zip
Patch0:  hybridreverb-0001-fix-JUCE-compilation.patch

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: freetype-devel
BuildRequires: libcurl-devel
BuildRequires: fftw-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: unzip

%description
HybridReverb2 is a convolution-based reverberation effect which combines the
superior sound quality of a convolution reverb with the tuning capability of
a feedback delay network. The sound quality of a convolution reverb depends
on the quality of the used room impulse responses. HybridReverb2 comes with
a set of room impulse responses which were synthesized with tinyAVE, an
auralization software which was developed at the Institute of Communication
Acoustics, Ruhr-Universität Bochum (Borß and Martin, 2009; Borß, 2009a).
These room impulse responses are designed for a speaker setup with two front
and two rear speakers (Borß, 2009b). For a full surround sound effect, you
will need two plugins, one plugin which uses a "front" preset for the front
channels and a second plugin which uses the corresponding "rear" preset
for the rear channels.

%package -n %{name}-common
Summary:   Impulse response files for %{name}
License:   GPL-2.0-or-later
Requires:  %{name}-common
BuildArch: noarch

%description -n %{name}-common
Impulse response files for %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}-common

%description -n lv2-%{name}
LV2 version of %{name}

Requires: %{name}-common

%prep

%autosetup -p1 -n HybridReverb2-%{version}

%build

%cmake -DHybridReverb2_VST2=OFF \
       -DHybridReverb2_LV2=ON \
       -DHybridReverb2_Standalone=ON \
       -DHybridReverb2_AdvancedJackStandalone=ON \
       -DHybridReverb2_UseLocalDatabase=ON \
       -DHybridReverb2_Assertions=OFF

%cmake_build

%install

%cmake_install

desktop-file-install --vendor '' \
        --add-category=AudioVideo \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/hybridreverb2.desktop

unzip %{SOURCE1}
install -m 755 -d %{buildroot}/%{_datadir}/HybridReverb2/
cp -ra HybridReverb2-impulse-response-database-1.0.0/* %{buildroot}/%{_datadir}/HybridReverb2/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/hybridreverb2.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/32x32/apps/HybridReverb2.png
%{_datadir}/icons/hicolor/96x96/apps/HybridReverb2.png
%{_datadir}/pixmaps/HybridReverb2.png
%{_datadir}/man/fr/man1/hybridreverb2.1.gz
%{_datadir}/man/man1/hybridreverb2.1.gz

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n %{name}-common
%{_datadir}/HybridReverb2/

%changelog
* Thu Nov 26 2020 Yann Collette <ycollette.nospam@free.fr> - 2.1.2-1
- Initial spec file
