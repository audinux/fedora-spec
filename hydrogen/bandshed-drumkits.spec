# Tag: Drum
# Type: Presets
# Category: Sequencer

Summary: Bandshed DrumKits for Hydrogen
Name:    bandshed-drumkits
Version: 0.0.1
Release: 1%{?dist}
License: GPL-2.0-or-later AND GPL-3.0-only AND LicenseRef-OpenMusic-green
URL:     http://www.bandshed.net/avldrumkits/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: http://www.bandshed.net/sounds/AVLDrumkits_H2/AVLDrumkits-BlackPearl-H2-repack.h2drumkit
Source1: http://www.bandshed.net/sounds/AVLDrumkits_H2/AVLDrumkits-BlondeBop-HotRod.h2drumkit
Source2: http://www.bandshed.net/sounds/AVLDrumkits_H2/AVLDrumkits-BlondeBop.h2drumkit
Source3: http://www.bandshed.net/sounds/AVLDrumkits_H2/AVLDrumkits-BuskmansHoliday.h2drumkit
Source4: http://www.bandshed.net/sounds/AVLDrumkits_H2/AVLDrumkits-RedZeppelin-H2-repack.h2drumkit

BuildArch: noarch

Requires: hydrogen >= 0.9.5

%description
A collection of bandshed drumkits for the
Hydrogen advanced drum machine for GNU/Linux.

%package -n AVLDrumkits-BlackPearl-H2-repack
Summary: Hydrogen drumkit

%description -n AVLDrumkits-BlackPearl-H2-repack
Hydrogen drumkit

%package -n AVLDrumkits-BlondeBop-HotRod.h2d
Summary: Hydrogen drumkit

%description -n AVLDrumkits-BlondeBop-HotRod.h2d
Hydrogen drumkit

%package -n AVLDrumkits-BlondeBop.h2d
Summary: Hydrogen drumkit

%description -n AVLDrumkits-BlondeBop.h2d
Hydrogen drumkit

%package -n AVLDrumkits-BuskmansHoliday
Summary: Hydrogen drumkit

%description -n AVLDrumkits-BuskmansHoliday
Hydrogen drumkit

%package -n AVLDrumkits-RedZeppelin-H2-repack.h2d
Summary: Hydrogen drumkit

%description -n AVLDrumkits-RedZeppelin-H2-repack.h2d
Hydrogen drumkit

%prep

%install

# These directories are owned by hydrogen:
mkdir -p %{buildroot}/%{_datadir}/hydrogen/data/drumkits/

# Now copy everything into the %{buildroot}
CURRENT_DIR=`pwd`

cp %{SOURCE0} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/tmp.h2drumkit
cd %{buildroot}/%{_datadir}/hydrogen/data/drumkits/; tar xvfz tmp.h2drumkit; rm tmp.h2drumkit; cd $CURRENT_DIR

cp %{SOURCE1} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/tmp.h2drumkit
cd %{buildroot}/%{_datadir}/hydrogen/data/drumkits/; tar xvfz tmp.h2drumkit; rm tmp.h2drumkit; cd $CURRENT_DIR

cp %{SOURCE2} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/tmp.h2drumkit
cd %{buildroot}/%{_datadir}/hydrogen/data/drumkits/; tar xvfz tmp.h2drumkit; rm tmp.h2drumkit; cd $CURRENT_DIR

cp %{SOURCE3} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/tmp.h2drumkit
cd %{buildroot}/%{_datadir}/hydrogen/data/drumkits/; tar xvfz tmp.h2drumkit; rm tmp.h2drumkit; cd $CURRENT_DIR

cp %{SOURCE4} %{buildroot}/%{_datadir}/hydrogen/data/drumkits/tmp.h2drumkit
cd %{buildroot}/%{_datadir}/hydrogen/data/drumkits/; tar xvfz tmp.h2drumkit; rm tmp.h2drumkit; cd $CURRENT_DIR

%files -n AVLDrumkits-BlackPearl-H2-repack
%{_datadir}/hydrogen/data/drumkits/AVLDrumkits-BlackPearl-H2-repack/*

%files -n AVLDrumkits-BlondeBop-HotRod.h2d
%{_datadir}/hydrogen/data/drumkits/AVLDrumkits-BlondeBop-HotRod/*

%files -n AVLDrumkits-BlondeBop.h2d
%{_datadir}/hydrogen/data/drumkits/AVLDrumkits-BlondeBop/*

%files -n  AVLDrumkits-BuskmansHoliday
%{_datadir}/hydrogen/data/drumkits/AVLDrumkits-BuskmansHoliday-BETA/*

%files -n AVLDrumkits-RedZeppelin-H2-repack.h2d
%{_datadir}/hydrogen/data/drumkits/AVLDrumkits-RedZeppelin-H2-repack/*

%changelog
* Wed Aug 23 2023 Yann Collette <ycollette dot nospam at free.fr> 0.0.1-1
- initial spec
