%global commit0 ebaba6375f2de68222a853c01427e44eabea2896

Name: imogen
Version: 0.0.1
Release: 1%{?dist}
Summary: Ultimate vocal harmonizer
License: MIT
URL: https://github.com/benthevining/imogen

Source0: https://github.com/benthevining/imogen/archive/%{commit0}.zip#/%{name}-%{commit0}.zip

BuildRequires: gcc gcc-c++ gcc-objc
BuildRequires: cmake
BuildRequires: libsamplerate-devel
BuildRequires: fftw-devel
BuildRequires: libcurl
BuildRequires: freetype-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel
BuildRequires: alsa-lib-devel
BuildRequires: JUCE

%description
Imogen is a low-latency pitch shifter designed to function as an instrument
that is dynamic to play, and as a lead vocals mixing workstation:
Imogen also includes pitch correction for the lead vocals, as well as a
suite of built-in mixing effects.

%prep
%autosetup -n %{name}-%{commit0}

%build

# AllLemonsModules missing
# BVBrandFlags missing

%cmake
%cmake_build

%install

%cmake_install

%files
%license LICENSE.md
%doc README.md

%changelog
* Wed Aug 03 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
-  Initial version of the spec
