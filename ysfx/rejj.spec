# Status: active
# Tag: Audio, Effect
# Type: Plugin, YSFX
# Category: Audio, Effect

Name: ysfx-rejj
Version: 1.2.0
Release: 2%{?dist}
Summary: Reaper JSFX Plugins
URL: https://github.com/Justin-Johnson/ReJJ
License: MIT

BuildArch: noarch

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/Justin-Johnson/ReJJ/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Obsoletes:  rejj <= 1.2.0-1

%description
This is a collection of audio effects I have written in REAPER's JSFX language.

%prep

%autosetup -n ReJJ-%{version}

%install

install -m 755 -d %{buildroot}%{_datadir}/%{name}/
cp -ra * %{buildroot}%{_datadir}/%{name}/

%files
%doc README.md
%license LICENSE
%{_datadir}/%{name}/*

%changelog
* Tue Feb 17 2026 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-2
- update to 1.2.0-2 - rename spec

* Fri Nov 10 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-1
- Initial spec file
