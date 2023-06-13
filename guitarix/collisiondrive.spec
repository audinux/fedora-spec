# Tag: Guitar, Overdrive
# Type: Plugin, LV2
# Category: Audio, Effect

Name:    lv2-collisiondrive
Version: 0.1
Release: 1%{?dist}
Summary: Overdrive / Distortion
License: GPL-2.0-or-later
URL:     https://github.com/brummer10/CollisionDrive

Vendor:       Audinux
Distribution: Audinux

# To get the sources
# ./brummer10-source.sh CollisionDrive v0.1

Source0: CollisionDrive.tar.gz
Source1: brummer10-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: libsigc++20-devel
BuildRequires: vim-common

%description
CollisionDrive is modeled after the Horizon Devices Precision Drive(*),
a modern overdrive pedal with a built-in noise gate.
Besides the usual Volume and Drive controls, the CollisionDrive features
Attack and Bright controls.
The Attack control manipulates the response of the pedal, turning it down
simultaneously softens the overdrive attack and increases the sustain.
The Bright control gives you even more flexibility. It can add presence
to darker sounding amps, or remove buzzing when needed.
The Gate control sets the noise gate threshold. In the plugin interface,
this control lights up to indicate that the noise gate is active.

(*) 'Other product names modeled in this software are trademarks of their
respective companies that do not endorse and are not associated or affiliated
with this software.
Horizon Devices Precision Drive is a trademark or trade name of another
manufacturer and was used merely to identify the product whose sound was
reviewed in the creation of this product. All other trademarks are the property
of their respective holders.'

%prep
%autosetup -n CollisionDrive

%build

%set_build_flags

%make_build STRIP=true

%install 

%make_install INSTALL_DIR=/usr/%{_lib}/lv2 STRIP=true

%files
%doc README.md
%{_libdir}/lv2/*

%changelog
* Sat Apr 23 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial spec file
