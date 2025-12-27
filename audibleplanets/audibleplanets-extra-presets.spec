# Status: active
# Tag: Presets
# Type: Presets
# Category: Synthesizer

%global commit0 7c78117c018fbbc6d1fb3970662d4a7c1d63a6e4

Name: audibleplanets-extra-presets
Version: 1.0.0
Release: 1%{?dist}
Summary: Extra presets for AudiblePlanets synth 
License: GPL-3.0-or-later
URL: https://github.com/gregrecco67/Audible-Planets-Presets
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

BuildArch: noarch

Source0: https://github.com/gregrecco67/Audible-Planets-Presets/archive/7c78117c018fbbc6d1fb3970662d4a7c1d63a6e4.zip#/%{name}-%{commit0}.zip

%description
Extra presets for AudiblePlanets synth

%prep
%autosetup -n Audible-Planets-Presets-%{commit0}

%install

install -m 755 -d %{buildroot}/%{_datadir}/audibleplanets-extra-presets/

cp *.xml %{buildroot}/%{_datadir}/audibleplanets-extra-presets/

%files
%doc README.md
%{_datadir}/audibleplanets-extra-presets/*

%changelog
* Wed Apr 09 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial build
