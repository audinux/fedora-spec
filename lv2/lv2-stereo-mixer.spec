# Status: active
# Tag: Mixer
# Type: Plugin, LV2
# Category: Effect

Name: lv2-stereo-mixer
Version: 0.1
Release: 1%{?dist}
Summary: An LV2 audio plug-in for stereo-signal manipulation
License: GPL-3.0-or-later
URL: https://github.com/unclechu/lv2-stereo-mixer/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/unclechu/lv2-stereo-mixer/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: lv2-stereo-mixer-0001-add-missing-headers.patch
Patch1: lv2-stereo-mixer-0001-add-fedora-cflags.patch

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: lv2-devel

%description
An LV2 audio plug-in for stereo-signal manipulation.
Features:
* Input/Output gain independent for each channel alongwith combined
* Wide
  * Wideness percent
  * Wide law
* Panning
  * Pan (percent of shifting between -100 and +100)
  * Pan law
  * Optional gain compensation for "pan law"

%prep
%autosetup -p1 -n %{name}-%{version}

%build

%make_build

%install

mkdir -p %{buildroot}%{_libdir}/lv2/
cp -ra stereo-mixer.lv2 %{buildroot}%{_libdir}/lv2/

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Tue Mar 17 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial development
