# Status: active
# Tag: Audio, Effect
# Type: Plugin, YSFX
# Category: Audio, Effect

Name: ysfx-joepvanlier
Version: 0.2.0
Release: 2%{?dist}
Summary: A bundle of JSFX and scripts for reaper.
URL: https://github.com/JoepVanlier/JSFX
License: MIT

BuildArch: noarch

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/JoepVanlier/JSFX/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Obsoletes:  joepvanlier_ysfx <= 0.2.0-1

%description
This is a bundle of JSFX and scripts for reaper.

%prep

%autosetup -n JSFX-%{version}

%install

install -m 755 -d %{buildroot}%{_datadir}/%{name}/
cp -ra * %{buildroot}%{_datadir}/%{name}/

%files
%doc README.md
%license LICENSE
%{_datadir}/%{name}/*

%changelog
* Tue Feb 17 2026 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-2
- update to 0.2.0-2 - rename spec

* Sun Sep 29 2024 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- update to 0.2.0-1

* Sun Dec 17 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- update to 0.1.0-1

* Fri Nov 10 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
