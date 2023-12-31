Name:    saugns
Version: 0.4.2d
Release: 1%{?dist}
Summary: Scriptable AUdio GeNeration System - implements the SAU language.
License: GPL-3.0-only
URL:     https://github.com/saugns/saugns

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/saugns/saugns/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: alsa-lib-devel

%description
saugns is the Scriptable AUdio GeNeration System, the implementation
of the SAU language (Scriptable AUdio). The project website has more on them.

SAU is a simple language for mathematical audio synthesis, without support
for using pre-recorded samples. See the README.SAU for the current details,
or a more how-to language web page covering the main features.
Example scripts under examples/ also use most of the features.

While the language is still primitive relative to the goal (a useful
language for writing electronic music), it makes it simple to experiment
with sounds. A collection of basic wave types are supported, as well as AM/RM,
FM, and PM (the "FM" of most commercial synthesizers). An arbitrary number
of oscillators can be used.

The program reads SAU (Scriptable AUdio) files or strings, and can output
to system audio, a 16-bit PCM WAV file, and/or stdout (raw or AU, for
interfacing with other programs). Basic usage information is provided with
the -h option. More can be found in the man page and on the usage web page.

%prep
%autosetup -p1 -n %{name}-%{version}

sed -i -e "s/-Wall -I./-Wall -I. \$(DEPFLAGS)/g" Makefile
sed -i -e "s/-s / /g" Makefile

%build

%set_build_flags
export DEPFLAGS="$CFLAGS"

%make_build

%install

%make_install PREFIX=/usr

install -m 755 -d %{buildroot}/%{_datadir}/%{name}

mv %{buildroot}/%{_datadir}/doc/%{name}/ %{buildroot}/%{_datadir}/%{name}/doc/

%files
%doc README.md
%license COPYING
%{_bindir}/*
%{_mandir}/*
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/doc/*
%{_datadir}/%{name}/examples/*

%changelog
* Sat Dec 30 2023 Yann Collette <ycollette.nospam@free.fr> - 0.4.2d-1
- update to 0.4.2d-1

* Tue Oct 03 2023 Yann Collette <ycollette.nospam@free.fr> - 0.4.2c-1
- update to 0.4.2c-1

* Fri Sep 08 2023 Yann Collette <ycollette.nospam@free.fr> - 0.4.2b-1
- update to 0.4.2b-1

* Tue Aug 29 2023 Yann Collette <ycollette.nospam@free.fr> - 0.4.2-1
- update to 0.4.2-1

* Tue Jul 04 2023 Yann Collette <ycollette.nospam@free.fr> - 0.4.1-1
- update to 0.4.1-1

* Sun Mar 19 2023 Yann Collette <ycollette.nospam@free.fr> - 0.4.0d-1
- update to 0.4.0d-1

* Sun Jan 29 2023 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-1
- Initial build
