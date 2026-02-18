# Status: active
# Tag: Audio, Effect
# Type: Plugin, YSFX
# Category: Audio, Effect

Name: ysfx-lms
Version: 2.0
Release: 2%{?dist}
Summary: LMS Plugin Suite - Open source JSFX audio plugins
URL: https://github.com/LMSBAND/LMS
License: MIT

BuildArch: noarch

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/LMSBAND/LMS/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Obsoletes:  lms <= 0.0.1-1

%description
LMS Plugin Suite - Open source JSFX audio plugins.

%prep

%autosetup -n LMS-%{version}

%install

install -m 755 -d %{buildroot}%{_datadir}/%{name}/
cp -ra * %{buildroot}%{_datadir}/%{name}/

%files
%doc README.md NOTICE.TXT
%{_datadir}/%{name}/*

%changelog
* Wed Feb 18 2026 Yann Collette <ycollette.nospam@free.fr> - 2.0-2
- update to 2.0-2

* Tue Feb 17 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to 0.0.1-2 - rename spec

* Tue Feb 17 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
