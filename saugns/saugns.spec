# Status: active
# Tag: Devel, Audio
# Type: Standalone, Language
# Category: Devel, Audio, Tool

Name: saugns
Version: 0.5.3d
Release: 1%{?dist}
Summary: Scriptable AUdio GeNeration System - implements the SAU language.
License: GPL-3.0-only
URL: https://github.com/saugns/saugns
ExclusiveArch: x86_64 aarch64

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

sed -i -e "s/-pedantic -I./-pedantic -I. \$(DEPFLAGS)/g" Makefile
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
* Wed Oct 22 2025 Yann Collette <ycollette.nospam@free.fr> - 0.5.3d-1
- update to 0.5.3d-1

* Fri Oct 17 2025 Yann Collette <ycollette.nospam@free.fr> - 0.5.3c-1
- update to 0.5.3c-1

* Thu Oct 09 2025 Yann Collette <ycollette.nospam@free.fr> - 0.5.3-1
- update to 0.5.3-1

* Wed Aug 27 2025 Yann Collette <ycollette.nospam@free.fr> - 0.5.2-1
- update to 0.5.2-1

* Sun Feb 16 2025 Yann Collette <ycollette.nospam@free.fr> - 0.5.1-1
- update to 0.5.1-1

* Fri Jan 31 2025 Yann Collette <ycollette.nospam@free.fr> - 0.5.0c-1
- update to 0.5.0c-1

* Tue Jan 28 2025 Yann Collette <ycollette.nospam@free.fr> - 0.5.0b-1
- update to 0.5.0b-1

* Mon Jan 06 2025 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-1
- update to 0.5.0-1

* Sat Nov 16 2024 Yann Collette <ycollette.nospam@free.fr> - 0.4.8c-1
- update to 0.4.8c-1

* Tue Nov 12 2024 Yann Collette <ycollette.nospam@free.fr> - 0.4.8b-1
- update to 0.4.8b-1

* Sun Nov 03 2024 Yann Collette <ycollette.nospam@free.fr> - 0.4.8-1
- update to 0.4.8-1

* Wed Oct 30 2024 Yann Collette <ycollette.nospam@free.fr> - 0.4.7c-1
- update to 0.4.7c-1

* Sat Oct 26 2024 Yann Collette <ycollette.nospam@free.fr> - 0.4.7b-1
- update to 0.4.7b-1

* Thu Oct 17 2024 Yann Collette <ycollette.nospam@free.fr> - 0.4.7-1
- update to 0.4.7-1

* Wed Oct 02 2024 Yann Collette <ycollette.nospam@free.fr> - 0.4.6-1
- update to 0.4.6-1

* Sat Aug 10 2024 Yann Collette <ycollette.nospam@free.fr> - 0.4.5-1
- update to 0.4.5-1

* Wed Jul 10 2024 Yann Collette <ycollette.nospam@free.fr> - 0.4.4d-1
- update to 0.4.4d-1

* Sun Jun 02 2024 Yann Collette <ycollette.nospam@free.fr> - 0.4.4c-1
- update to 0.4.4C-1

* Tue Apr 16 2024 Yann Collette <ycollette.nospam@free.fr> - 0.4.4b-1
- update to 0.4.4b-1

* Tue Apr 09 2024 Yann Collette <ycollette.nospam@free.fr> - 0.4.4-1
- update to 0.4.4-1

* Thu Apr 04 2024 Yann Collette <ycollette.nospam@free.fr> - 0.4.3-1
- update to 0.4.3-1

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
