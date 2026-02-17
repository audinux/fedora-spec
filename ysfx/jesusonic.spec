# Status: active
# Tag: Audio, Effect
# Type: Plugin, YSFX
# Category: Audio, Effect

Name: ysfx-jesusonic
Version: 0.991
Release: 1%{?dist}
Summary: Some JSFX effects from Cockos
URL: https://www.cockos.com/jsfx/
License: JESUSONIC-SOFTWARE-LICENSE-AGREEMENT

BuildArch: noarch

Vendor:       Audinux
Distribution: Audinux

Source0: https://www.cockos.com/jsfx/software/jesusonic-0.991-linux-x86.tar.gz

%description
Some JSFX effects from Cockos.

%prep

%autosetup -n jesusonic-%{version}-linux-x86

%install

install -m 755 -d %{buildroot}%{_datadir}/%{name}/
cp -ra data effects %{buildroot}%{_datadir}/%{name}/

%files
%doc whatsnew.txt
%license license.txt
%{_datadir}/%{name}/*

%changelog
* Tue Feb 17 2026 Yann Collette <ycollette.nospam@free.fr> - 0.991-1
- Initial spec file
