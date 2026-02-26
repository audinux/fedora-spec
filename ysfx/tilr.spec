# Status: active
# Tag: Audio, Effect
# Type: Plugin, YSFX
# Category: Audio, Effect

%global commit0 9cc5cd9e09846c9a1f9711db3bb42639546b0730

Name: ysfx-tilr
Version: 0.0.1
Release: 1%{?dist}
Summary: TiagoLR collection of JSFX effects
URL: https://github.com/tiagolr/tilr_jsfx
License: MIT

BuildArch: noarch

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/tiagolr/tilr_jsfx/archive/refs/heads/master.zip#/%{name}-%{version}.zip

%description
TiagoLR collection of JSFX effects.

%prep

%autosetup -n tilr_jsfx-master

%install

install -m 755 -d %{buildroot}%{_datadir}/%{name}/
cp -ra * %{buildroot}%{_datadir}/%{name}/

%files
%doc README.md
%license LICENSE
%{_datadir}/%{name}/*

%changelog
* Thu Feb 26 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
