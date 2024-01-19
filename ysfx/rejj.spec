# Tag: Audio, Effect
# Type: Plugin
# Category: Audio, Effect

Name: rejj
Version: 1.2.0
Release: 1%{?dist}
Summary: Reaper JSFX Plugins
URL: https://github.com/Justin-Johnson/ReJJ
License: MIT

Vendor:       Audinux
Distribution: Audinux

Requires: ysfx

Source0: https://github.com/Justin-Johnson/ReJJ/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
* Fri Nov 10 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-1
- Initial spec file
