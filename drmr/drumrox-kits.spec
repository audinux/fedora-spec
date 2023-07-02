# Tag: Drum
# Type: LV2
# Category: Synthesizer

%global commit0 ddaebac3bb69327623c7a70e3ca235b49fbb3a25

Name:    drumrox-kits
Version: 0.0.1
Release: 1%{?dist}
Summary: A set of drumrox drum kits
License: GPL-3.0-or-later
URL:     https://github.com/psemiletov/drumrox-kits

Vendor:       Audinux
Distribution: Audinux

BuildArch: noarch

Source0: https://github.com/psemiletov/drumrox-kits/archive/%{commit0}.zip#/%{name}-%{commit0}.zip

%description
Drum kits for Drumrox LV2 drum machine

%package -n %{name}-Lel-DR8
Summary:  Lel-DR8 drumkit for %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n %{name}-Lel-DR8
Lel-DR8 drumkit for %{name}

%package -n %{name}-Lel-PSR
Summary:  Lel-PSR drumkit for %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n %{name}-Lel-PSR
Lel-PSR drumkit for %{name}

%package -n %{name}-Rokton-UDS
Summary:  Rokton-UDS drumkit for %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n %{name}-Rokton-UDS
Rokton-UDS drumkit for %{name}

%package -n %{name}-Tamil
Summary:  Tamil drumkit for %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n %{name}-Tamil
Tamil drumkit for %{name}

%package -n %{name}-TamilMultiLayered
Summary:  TamilMultiLayered drumkit for %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n %{name}-TamilMultiLayered
TamilMultiLayered drumkit for %{name}

%prep
%autosetup -n %{name}-%{commit0}

%install

install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Lel-DR8/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Lel-PSR/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Rokton-UDS/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Tamil/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/TamilMultiLayered/

cp -ra Lel-DR8/* %{buildroot}/%{_datadir}/drumrox-kits/Lel-DR8/
cp -ra Lel-PSR/* %{buildroot}/%{_datadir}/drumrox-kits/Lel-PSR/
cp -ra Rokton\ UDS/* %{buildroot}/%{_datadir}/drumrox-kits/Rokton-UDS/
cp -ra Tamil/* %{buildroot}/%{_datadir}/drumrox-kits/Tamil/
cp -ra TamilMultiLayered/* %{buildroot}/%{_datadir}/drumrox-kits/TamilMultiLayered/

%files
%doc README.md
%license LICENSE

%files -n %{name}-Lel-DR8
%{_datadir}/drumrox-kits/Lel-DR8/*

%files -n %{name}-Lel-PSR
%{_datadir}/drumrox-kits/Lel-PSR/*

%files -n %{name}-Rokton-UDS
%{_datadir}/drumrox-kits/Rokton-UDS/*

%files -n %{name}-Tamil
%{_datadir}/drumrox-kits/Tamil/*

%files -n %{name}-TamilMultiLayered
%{_datadir}/drumrox-kits/TamilMultiLayered/*

%changelog
* Sun Jul 02 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial build
