# Status: active
# Tag: Audio, Effect
# Type: Plugin, YSFX
# Category: Audio, Effect

%global commit0 663735021e59d788e8ebacc4b9678569378deec9

Name: ysfx-sonic-anomaly
Version: 0.0.1
Release: 1%{?dist}
Summary: Sonic Anomaly JSFX scripts for Reaper
URL: https://github.com/Sonic-Anomaly/Sonic-Anomaly-JSFX/
License: MIT

BuildArch: noarch

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/Sonic-Anomaly/Sonic-Anomaly-JSFX/archive/%{commit0}.zip#/%{name}-%{version}.zip

%description
Sonic Anomaly JSFX scripts for Reaper.

%prep

%autosetup -n Sonic-Anomaly-JSFX-%{commit0}

%install

install -m 755 -d %{buildroot}%{_datadir}/%{name}/
cp -ra * %{buildroot}%{_datadir}/%{name}/

%files
%{_datadir}/%{name}/*

%changelog
* Tue Feb 17 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
