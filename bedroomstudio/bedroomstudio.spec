# Status: active
# Tag: Effect, Overdrive
# Type: Plugin, LV2
# Category: Audio, Effect

Name: bedroomstudio
Version: 1.0.0
Release: 2%{?dist}
Summary: A set of LV2 plugins
License: MIT
URL: https://github.com/psemiletov/bedroomstudio
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/psemiletov/bedroomstudio/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: lv2-devel

%description
A set of LV2 plugins for bedroom music studio :)
The idea is to provide simple, nice sounding effects those become a legend.

https://psemiletov.github.io/bedroomstudio/

Current plugins list:

Metalluga - the hard and crips distortion with five controls to customize the
effect for your needs: Drive, Level, Weigth, Resonance and Warmth.
The main control here is Level, all other builds around it.
If don't touch too much the distortion stuff, you can use Metalluga in more
soft genres such as blues.

Bronza - the plain fuzz pedal with two parameters - Level and Fuzz. Sounds
like in sixties

Grelka Overdrive - the classic overdrive, has Drive, Level, Lows and Treble
parameters to define the sound.

Charm - the saturation effect, makes sound more "analog".

%prep
%autosetup -n %{name}-%{version}

sed -i -e "s/lib\/lv2/%{_lib}\/lv2/g" CMakeLists.txt

%build

%cmake
%cmake_build

%install

%cmake_install

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Mon Oct 20 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-2
- update to 1.0.0-2 - update description

* Mon Oct 23 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial packaging.
