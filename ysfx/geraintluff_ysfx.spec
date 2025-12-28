# Status: active
# Tag: Audio, Effect
# Type: Plugin, YSFX
# Category: Audio, Effect

%global commit0 e98d64401ba57590b7ea0d3592675accb43667da

Name: geraintluff_ysfx
Version: 0.0.1
Release: 2%{?dist}
Summary: Collection of JSFX effects
URL: https://github.com/geraintluff/jsfx
ExclusiveArch: x86_64 aarch64
License: MIT

BuildArch: noarch

Vendor:       Audinux
Distribution: Audinux

Requires: ysfx

Source0: https://github.com/geraintluff/jsfx/archive/refs/heads/master.zip#/%{name}-%{version}.zip

%description
This is a collection of audio effects I have written in REAPER's JSFX language.

%prep

%autosetup -n jsfx-master

%install

install -m 755 -d %{buildroot}%{_datadir}/%{name}/
cp -ra * %{buildroot}%{_datadir}/%{name}/

%files
%license LICENCE.txt
%{_datadir}/%{name}/*

%changelog
* Sun Oct 19 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to 0.0.1-2 - fix spec

* Fri Nov 10 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
