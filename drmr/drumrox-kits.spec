# Tag: Drum, Presents
# Type: LV2, Presets
# Category: Synthesizer

%global commit0 cecd0845bcf3aebe562e2cfa5231916301668d44

Name: drumrox-kits
Version: 0.0.1
Release: 2%{?dist}
Summary: A set of drumrox drum kits
License: GPL-3.0-or-later
URL: https://github.com/psemiletov/drum_sklad

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

%package -n %{name}-Wooden
Summary:  Wooden drumkit for %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n %{name}-Wooden
Wooden drumkit for %{name}

%package -n %{name}-Fricke_MFB512
Summary:  Fricke MFB512 drumkit for %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n %{name}-Fricke_MFB512
Fricke MFB512 drumkit for %{name}

%prep
%autosetup -n drum_sklad-%{commit0}

%install

install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Lel-DR8/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Lel-PSR/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Rokton-UDS/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Tamil/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/TamilMultiLayered/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Wooden/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Fricke_MFB512/

cp -ra Lel-DR8/* %{buildroot}/%{_datadir}/drumrox-kits/Lel-DR8/
cp -ra Lel-PSR/* %{buildroot}/%{_datadir}/drumrox-kits/Lel-PSR/
cp -ra Rokton\ UDS/* %{buildroot}/%{_datadir}/drumrox-kits/Rokton-UDS/
cp -ra Tamil/* %{buildroot}/%{_datadir}/drumrox-kits/Tamil/
cp -ra TamilMultiLayered/* %{buildroot}/%{_datadir}/drumrox-kits/TamilMultiLayered/
cp -ra Wooden/* %{buildroot}/%{_datadir}/drumrox-kits/Wooden/
cp -ra Fricke\ MFB512/* %{buildroot}/%{_datadir}/drumrox-kits/Fricke_MFB512/

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

%files -n %{name}-Wooden
%{_datadir}/drumrox-kits/Wooden/*

%files -n %{name}-Fricke_MFB512
%{_datadir}/drumrox-kits/Fricke_MFB512/*

%changelog
* Tue Apr 09 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to 0.0.1-2

* Sun Jul 02 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial build
