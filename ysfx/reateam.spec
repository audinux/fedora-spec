# Status: active
# Tag: Audio, Effect
# Type: Plugin, YSFX
# Category: Audio, Effect

%global commit0 f7b312c1c5de6356a99ecc30036bb6d174e03e62

Name: ysfx-reateam
Version: 0.0.1
Release: 1%{?dist}
Summary: Community-maintained collection of JS effects for REAPER
URL: https://github.com/ReaTeam/JSFX/
License: MIT

BuildArch: noarch

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ReaTeam/JSFX/archive/%{commit0}.zip#/%{name}-%{version}.zip

%description
Community-maintained collection of JS effects for REAPER.

%prep

%autosetup -n JSFX-%{commit0}

%install

install -m 755 -d %{buildroot}%{_datadir}/%{name}/
cp -ra * %{buildroot}%{_datadir}/%{name}/

%files
%doc README.md
%{_datadir}/%{name}/*

%changelog
* Tue Feb 17 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
