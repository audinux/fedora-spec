# Status: active
# Tag: Drum, Presents
# Type: LV2, Presets
# Category: Synthesizer

%global commit0 135e0dde0c81e62567654a2557eee35b2bb59016

Name: drumrox-kits
Version: 0.0.1
Release: 5%{?dist}
Summary: A set of drumrox drum kits
License: GPL-3.0-or-later
URL: https://github.com/psemiletov/drum_sklad
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

BuildArch: noarch

Source0: https://github.com/psemiletov/drumrox-kits/archive/%{commit0}.zip#/%{name}-%{commit0}.zip

%description
Drum kits for Drumrox LV2 drum machine

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation from for %{name}

%package -n %{name}-Lel-DR8
Summary: Lel-DR8 drumkit for %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n %{name}-Lel-DR8
Lel-DR8 drumkit for %{name}

%package -n %{name}-Lel-PSR
Summary:  Lel-PSR drumkit for %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n %{name}-Lel-PSR
Lel-PSR drumkit for %{name}

%package -n %{name}-Rokton-UDS
Summary:  Rokton-UDS drumkit for %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n %{name}-Rokton-UDS
Rokton-UDS drumkit for %{name}

%package -n %{name}-Tamil
Summary:  Tamil drumkit for %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n %{name}-Tamil
Tamil drumkit for %{name}

%package -n %{name}-TamilMultiLayered
Summary:  TamilMultiLayered drumkit for %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n %{name}-TamilMultiLayered
TamilMultiLayered drumkit for %{name}

%package -n %{name}-Wooden
Summary:  Wooden drumkit for %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n %{name}-Wooden
Wooden drumkit for %{name}

%package -n %{name}-Fricke_MFB512
Summary:  Fricke MFB512 drumkit for %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n %{name}-Fricke_MFB512
Fricke MFB512 drumkit for %{name}

%package -n %{name}-Technics_PCM_DP50
Summary:  Technics PCM DP50 drumkit for %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n %{name}-Technics_PCM_DP50
Technics PCM DP50 drumkit for %{name}

%package -n %{name}-SoundMaster_SR-88
Summary:  SoundMaster SR-88 drumkit for %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n %{name}-SoundMaster_SR-88
SoundMaster SR-88 drumkit for %{name}

%package -n %{name}-Ludwig_Sixties
Summary:  Ludwig Sixties drumkit for %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n %{name}-Ludwig_Sixties
Ludwig Sixties drumkit for %{name}

%package -n %{name}-Ludwig_Basic
Summary:  Ludwig Basic drumkit for %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n %{name}-Ludwig_Basic
Ludwig Basic drumkit for %{name}

%package -n %{name}-ELI_CompuRhythm_CR_7030
Summary:  ELI CompuRhythm CR 7030 drumkit for %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n %{name}-ELI_CompuRhythm_CR_7030
ELI CompuRhythm CR 7030 drumkit for %{name}

%package -n %{name}-Cheetah_SpecDrum_Standard
Summary:  Cheetah SpecDrum Standard drumkit for %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n %{name}-Cheetah_SpecDrum_Standard
Cheetah SpecDrum Standard drumkit for %{name}

%package -n %{name}-Cheetah_SpecDrum_Latin
Summary:  Cheetah SpecDrum Latin drumkit for %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n %{name}-Cheetah_SpecDrum_Latin
Cheetah SpecDrum Latin drumkit for %{name}

%package -n %{name}-Cheetah_SpecDrum_Electro
Summary:  Cheetah SpecDrum Electro drumkit for %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n %{name}-Cheetah_SpecDrum_Electro
Cheetah SpecDrum Electro drumkit for %{name}

%package -n %{name}-Cheetah_SpecDrum_Afro
Summary:  Cheetah SpecDrum Afro drumkit for %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n %{name}-Cheetah_SpecDrum_Afro
Cheetah SpecDrum Afro drumkit for %{name}

%package -n %{name}-GEM_Drum15
Summary:  GEM Drum15 drumkit for %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n %{name}-GEM_Drum15
GEM Drum15 drumkit for %{name}

%package -n %{name}-Gretch_Jazzkit
Summary:  Gretch Jazzkit drumkit for %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n %{name}-Gretch_Jazzkit
Gretch Jazzkit drumkit for %{name}

%package -n %{name}-MTI_AO_1
Summary:  MTI AO-1 drumkit for %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n %{name}-MTI_AO_1
MTI AO-1 drumkit for %{name}

%package -n %{name}-The_Almighty_Sound_Drumkit
Summary:  The Almighty Sound drumkit for %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n %{name}-The_Almighty_Sound_Drumkit
The Almighty Sound drumkit for %{name}

%prep
%autosetup -n drum_sklad-%{commit0}

%install

install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Cheetah_SpecDrum_Standard/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Cheetah_SpecDrum_Latin/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Cheetah_SpecDrum_Electro/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Cheetah_SpecDrum_Afro/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/ELI_CompuRhythm_CR_7030/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Fricke_MFB512/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/GEM_Drum15/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Gretch_Jazzkit/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Lel-DR8/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Lel-PSR/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Ludwig_Sixties/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Ludwig_Basic/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/MTI_AO_1/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Rokton-UDS/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/SoundMaster_SR-88/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Tamil/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/TamilMultiLayered/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Technics_PCM_DP50/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/The_Almighty_Sound_Drumkit/
install -m 755 -d %{buildroot}/%{_datadir}/drumrox-kits/Wooden/

cp -ra Cheetah\ SpecDrum\ Standard/* %{buildroot}/%{_datadir}/drumrox-kits/Cheetah_SpecDrum_Standard/
cp -ra Cheetah\ SpecDrum\ Latin/* %{buildroot}/%{_datadir}/drumrox-kits/Cheetah_SpecDrum_Latin/
cp -ra Cheetah\ SpecDrum\ Electro/* %{buildroot}/%{_datadir}/drumrox-kits/Cheetah_SpecDrum_Electro/
cp -ra Cheetah\ SpecDrum\ Afro/* %{buildroot}/%{_datadir}/drumrox-kits/Cheetah_SpecDrum_Afro/
cp -ra ELI\ CompuRhythm\ CR\ 7030/* %{buildroot}/%{_datadir}/drumrox-kits/ELI_CompuRhythm_CR_7030/
cp -ra Fricke\ MFB512/* %{buildroot}/%{_datadir}/drumrox-kits/Fricke_MFB512/
cp -ra GEM\ Drum15/* %{buildroot}/%{_datadir}/drumrox-kits/GEM_Drum15/
cp -ra Gretch\ Jazzkit/* %{buildroot}/%{_datadir}/drumrox-kits/Gretch_Jazzkit/
cp -ra Lel-DR8/* %{buildroot}/%{_datadir}/drumrox-kits/Lel-DR8/
cp -ra Lel-PSR/* %{buildroot}/%{_datadir}/drumrox-kits/Lel-PSR/
cp -ra Ludwig\ Sixties/* %{buildroot}/%{_datadir}/drumrox-kits/Ludwig_Sixties/
cp -ra Ludwig\ Basic/* %{buildroot}/%{_datadir}/drumrox-kits/Ludwig_Basic/
cp -ra MTI\ AO-1/* %{buildroot}/%{_datadir}/drumrox-kits/MTI_AO_1/
cp -ra Rokton\ UDS/* %{buildroot}/%{_datadir}/drumrox-kits/Rokton-UDS/
cp -ra SoundMaster\ SR-88/* %{buildroot}/%{_datadir}/drumrox-kits/SoundMaster_SR-88/
cp -ra Tamil/* %{buildroot}/%{_datadir}/drumrox-kits/Tamil/
cp -ra TamilMultiLayered/* %{buildroot}/%{_datadir}/drumrox-kits/TamilMultiLayered/
cp -ra Technics\ PCM\ DP50/* %{buildroot}/%{_datadir}/drumrox-kits/Technics_PCM_DP50/
cp -ra The\ Almighty\ Sound\ Drumkit/* %{buildroot}/%{_datadir}/drumrox-kits/The_Almighty_Sound_Drumkit/
cp -ra Wooden/* %{buildroot}/%{_datadir}/drumrox-kits/Wooden/

%files -n license-%{name}
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

%files -n %{name}-Technics_PCM_DP50
%{_datadir}/drumrox-kits/Technics_PCM_DP50/*

%files -n %{name}-SoundMaster_SR-88
%{_datadir}/drumrox-kits/SoundMaster_SR-88/*

%files -n %{name}-Ludwig_Sixties
%{_datadir}/drumrox-kits/Ludwig_Sixties/*

%files -n %{name}-Ludwig_Basic
%{_datadir}/drumrox-kits/Ludwig_Basic/*

%files -n %{name}-ELI_CompuRhythm_CR_7030
%{_datadir}/drumrox-kits/ELI_CompuRhythm_CR_7030/*

%files -n %{name}-Cheetah_SpecDrum_Standard
%{_datadir}/drumrox-kits/Cheetah_SpecDrum_Standard/*

%files -n %{name}-Cheetah_SpecDrum_Latin
%{_datadir}/drumrox-kits/Cheetah_SpecDrum_Latin/*

%files -n %{name}-Cheetah_SpecDrum_Electro
%{_datadir}/drumrox-kits/Cheetah_SpecDrum_Electro/*

%files -n %{name}-Cheetah_SpecDrum_Afro
%{_datadir}/drumrox-kits/Cheetah_SpecDrum_Afro/*

%files -n %{name}-GEM_Drum15
%{_datadir}/drumrox-kits/GEM_Drum15/*

%files -n %{name}-Gretch_Jazzkit
%{_datadir}/drumrox-kits/Gretch_Jazzkit/*

%files -n %{name}-MTI_AO_1
%{_datadir}/drumrox-kits/MTI_AO_1/*

%files -n %{name}-The_Almighty_Sound_Drumkit
%{_datadir}/drumrox-kits/The_Almighty_Sound_Drumkit/*

%changelog
* Sat Aug 17 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-5
- update to 135e0dde0c81e62567654a2557eee35b2bb59016 - drumkit fix

* Tue Aug 13 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-4
- update to 0.0.1-4

* Tue Aug 06 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-3
- update to 0.0.1-3

* Tue Apr 09 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to 0.0.1-2

* Sun Jul 02 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial build
