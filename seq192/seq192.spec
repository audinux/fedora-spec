# Tag: Sequencer, MIDI
# Type: Standalone
# Category: Audio, Sequencer, MIDI

Name: seq192
Version: 1.5.1
Release: 1%{?dist}
Summary: MIDI sequencer based on seq24 with less features and more swag
License: GPL
URL: https://github.com/jean-emmanuel/seq192

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/jean-emmanuel/seq192/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: seq192-0001-update-makefile.patch

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: gtkmm30-devel
BuildRequires: liblo-devel
BuildRequires: json-devel
BuildRequires: desktop-file-utils

%description
MIDI sequencer based on seq24 with less features and more swag.

%prep
%autosetup -p1 -n %{name}-%{version}

%build

%set_build_flags

export EXTRA_CXXFLAGS="$CXXFLAGS"
export EXTRA_LDFLAGS="$LDCFLAGS"

%make_build USE_GTK=1 USE_JACK=1 PREFIX=/usr

%install

%make_install PREFIX=/usr

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man1/*

%changelog
* Tue Jan 30 2024 Yann Collette <ycollette.nospam@free.fr> - 1.5.1-1
- initial version
