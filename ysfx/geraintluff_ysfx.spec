# Tag: Audio, Effect
# Type: Plugin
# Category: Audio, Effect

Name: geraintluff_ysfx
Version: 0.0.1
Release: 1%{?dist}
Summary: Collection of JSFX effects
URL: https://github.com/geraintluff/jsfx
License: MIT

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
* Fri Nov 10 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
