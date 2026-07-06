# Status: active
# Tag: Controller, Keyboard, MIDI
# Type: Standalone
# Category: Audio, Tool

%global commit0 ea5dab84a6cf87d8b9f76076242106471212c4b9

Name: jmidiracc
Version: 0.0.1
Release: 1%{?dist}
Summary: A customizable MIDI control panel for Jack
URL: https://codeberg.org/zynskeyfolf/jmidiracc
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://codeberg.org/zynskeyfolf/jmidiracc/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: qt6-qtbase-devel
BuildRequires: pkgconfig(jack)
BuildRequires: desktop-file-utils

%description
A customizable MIDI control panel for Jack.

Features as of writing:
- Standard CC controllers (double precision mode too)
- NRPN and RPN controllers
- Display as knobs or buttons with adjustable range
- Program change and bank selection
- User-defined instrument and bank lists
- User-defined SysEx macros
Presets for a few synths are included, but you can save your own layouts as well.
Currently only the Jack MIDI backend is supported, but I'm planning to implement
ALSA Sequencer support too in the future.

%prep
%autosetup -n %{name}

%build

%set_build_flags
export LDFLAGS="`pkg-config --libs-only-L jack` $LDFLAGS"

%cmake
%cmake_build

%install

%cmake_install

desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/*.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*
%{_datadir}/%{name}/Casio\ CTK-601-611.jmrc

%changelog
* Mon Jul 06 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
