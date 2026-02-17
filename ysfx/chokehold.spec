# Status: active
# Tag: Audio, Effect
# Type: Plugin, YSFX
# Category: Audio, Effect

Name: ysfx-chokehold
Version: 1.8.3
Release: 1%{?dist}
Summary: A free collection of JS (JesuSonic) plugins for Reaper
URL: https://github.com/chkhld/jsfx
License: MIT

BuildArch: noarch

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/chkhld/jsfx/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
A variety of free JSFX plugins I created for use in Reaper.

%prep

%autosetup -n jsfx-%{version}

%install

install -m 755 -d %{buildroot}%{_datadir}/%{name}/
cp -ra * %{buildroot}%{_datadir}/%{name}/

%files
%doc README.md PLUGINS.md
%license LICENSE
%{_datadir}/%{name}/*

%changelog
* Tue Feb 17 2026 Yann Collette <ycollette.nospam@free.fr> - 1.8.3-1
- Initial spec file
