# Tag: Audio, Effect
# Type: Plugin
# Category: Audio, Effect

Name: joepvanlier_ysfx
Version: 0.1.0
Release: 1%{?dist}
Summary: A bundle of JSFX and scripts for reaper.
URL: https://github.com/JoepVanlier/JSFX
ExclusiveArch: x86_64 aarch64
License: MIT

Vendor:       Audinux
Distribution: Audinux

Requires: ysfx

Source0: https://github.com/JoepVanlier/JSFX/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
* Sun Dec 17 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- update to 0.1.0-1

* Fri Nov 10 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
