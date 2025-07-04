# Status: active
# Tag: Audio, AI, Amp Simul
# Type: Plugin, LV2
# Category: Audio, Tool

Name: lv2-neural-amp-modeler
Version: 0.1.9
Release: 1%{?dist}
Summary: Neural Amp Modeler LV2 plugin implementation
License: MIT
URL: https://github.com/mikeoliphant/neural-amp-modeler-lv2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./neural-amp-modeler-source.sh <TAG>
#        ./neural-amp-modeler-source.sh v0.1.9

Source0: neural-amp-modeler-lv2.tar.gz
Source1: neural-amp-modeler-source.sh

BuildRequires: gcc-c++
BuildRequires: cmake

%description
Bare-bones implementation of Neural Amp Modeler (NAM) models in an LV2 plugin.
There is no user interface. Setting the model to use requires that your LV2 host
supports atom:Path parameters. Reaper does not. Carla and Ardour do.

To get the intended behavior, you must run your audio host at the same sample
rate the model was trained at (usually 48kHz) - no resampling is done by the plugin.

For amp-only models (the most typical), you will need to run an impulse reponse
after this plugin to model the cabinet.

Some nam model can be found on https://tonehunt.org

%prep
%autosetup -n neural-amp-modeler-lv2

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -rav %{__cmake_builddir}/neural_amp_modeler.lv2 %{buildroot}/%{_libdir}/lv2/

%files
%doc README.md CREDITS.md
%license LICENCE.md
%{_libdir}/lv2/*

%changelog
* Mon Jun 09 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.9.1
- update to 0.1.9-1

* Wed May 28 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.8.1
- update to 0.1.8-1

* Mon Feb 10 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.7.1
- update to 0.1.7-1

* Mon Dec 02 2024 Yann Collette <ycollette.nospam@free.fr> - 0.1.6.1
- update to 0.1.6-1

* Mon Nov 04 2024 Yann Collette <ycollette.nospam@free.fr> - 0.1.5.1
- update to 0.1.5-1

* Sat Aug 17 2024 Yann Collette <ycollette.nospam@free.fr> - 0.1.4.1
- update to 0.1.4-1

* Mon Oct 16 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.3.1
- update to 0.1.3-1

* Wed Sep 13 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.2.1
- update to 0.1.2-1

* Fri Jul 07 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.1.1
- update to 0.1.1-1

* Thu Jun 22 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.0.1
- update to 0.1.0-1

* Sun Feb 19 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1.1
- Initial development
