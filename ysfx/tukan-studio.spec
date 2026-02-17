# Status: active
# Tag: Audio, Effect
# Type: Plugin, YSFX
# Category: Audio, Effect

%global commit0 b10f54490e87ab63df886b0b1bd828ab27b2a6bf

Name: ysfx-tukan-studio
Version: 0.0.1
Release: 1%{?dist}
Summary: JSFX Plugins for Reaper
URL: https://github.com/TukanStudios/TUKAN_STUDIOS_PLUGINS/
License: MIT

BuildArch: noarch

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/TukanStudios/TUKAN_STUDIOS_PLUGINS/archive/%{commit0}.zip#/%{name}-%{version}.zip

%description
JSFX Plugins for Reaper.

%prep

%autosetup -n TUKAN_STUDIOS_PLUGINS-%{commit0}

%install

install -m 755 -d %{buildroot}%{_datadir}/%{name}/
cp -ra * %{buildroot}%{_datadir}/%{name}/

%files
%{_datadir}/%{name}/*

%changelog
* Tue Feb 17 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
