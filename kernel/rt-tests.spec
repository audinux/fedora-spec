Name: rt-tests
Version: 2.6
Release: 1%{?dist}
Summary: Various programs that test various rt-linux features
License: GPL2
URL: https://git.kernel.org/pub/scm/utils/rt-tests/rt-tests

Vendor:       Audinux
Distribution: Audinux

Source0: https://git.kernel.org/pub/scm/utils/rt-tests/rt-tests.git/snapshot/rt-tests-%{version}.tar.gz

BuildRequires: gcc make
BuildRequires: numactl-devel
BuildRequires: python3
BuildRequires: python3-rpm-macros

%description
Suite of real-time tests

%prep
%autosetup

%build
%make_build prefix=%{_prefix}

%install
%make_install prefix=%{_prefix}

%files
%license COPYING
%doc README.markdown
%{_bindir}/*
%{_mandir}/*
%{python3_sitelib}/*

%changelog
* Fri Oct 06 2023 Yann Collette <ycollette.nospam@free.fr> - 2.6-1
- update to 2.6-1

* Fri Jan 20 2023 Yann Collette <ycollette.nospam@free.fr> - 2.5-1
- update to 2.5-1

* Sun Jul 10 2022 Yann Collette <ycollette.nospam@free.fr> - 2.4-1
- update to 2.4-1

* Tue Mar 01 2022 Yann Collette <ycollette.nospam@free.fr> - 2.3-1
- initial release of the spec file
