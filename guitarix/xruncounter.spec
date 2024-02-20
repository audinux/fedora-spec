# Tag: Jack
# Type: Standalone
# Category: Audio, Tool

%global commit0 4c234ddf154b5ea656a90ad77a440d4e2893d7a7

Name: xruncounter
Version: 0.1
Release: 1%{?dist}
Summary: Small linux tool to measure jack xruns and evaluate the overall performance of a system for realtime audio.
License: GPL-2.0-or-later
URL: https://github.com/Gimmeapill/xruncounter

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/Gimmeapill/xruncounter/archive/%{commit0}.zip#/%{name}-%{commit0}.zip

BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconfig(jack)

%description
Small linux tool to measure jack xruns and evaluate the overall performance of a system for realtime audio. 

%prep
%autosetup -n %{name}-%{commit0}

%build

%set_build_flags

gcc $CFLAGS $LDFLAGS xruncounter.c -lm `pkg-config --cflags --libs jack` -o xruncounter

%install

install -m 755 -d %{buildroot}%{_bindir}/
cp xruncounter %{buildroot}%{_bindir}/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%changelog
* Tue Feb 20 2024 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial spec file
