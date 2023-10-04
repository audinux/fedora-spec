Name: rt-tests
Version: 2.5
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
%if 0%{?fedora} >= 39
BuildRequires:  python3.10
%endif

%description
Suite of real-time tests

%prep
%autosetup

%if 0%{?fedora} >= 39
sed -i -e "s/python3/python3.10/g" Makefile
%endif

%build
%make_build prefix=%{_prefix}

%install
%make_install prefix=%{_prefix}

%if 0%{?fedora} >= 39
mkdir -p %buildroot/%{python3_sitelib}/
mv %buildroot/%{_usr}/lib/python3.10/site-packages/* %buildroot/%{python3_sitelib}/
%endif

%files
%license COPYING
%doc README.markdown
%{_bindir}/*
%{_mandir}/*
%{python3_sitelib}/*

%changelog
* Fri Jan 20 2023 Yann Collette <ycollette.nospam@free.fr> - 2.5-1
- update to 2.5-1

* Sun Jul 10 2022 Yann Collette <ycollette.nospam@free.fr> - 2.4-1
- update to 2.4-1

* Tue Mar 01 2022 Yann Collette <ycollette.nospam@free.fr> - 2.3-1
- initial release of the spec file
