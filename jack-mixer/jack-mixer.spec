# Tag: Jack
# Type: Standalone
# Category: Audio, Tool

Name: jack_mixer
Version: 18
Release: 1%{?dist}
Summary: jack_mixer is GTK (2.x) JACK audio mixer with look similar to it\`s hardware counterparts
URL: https://github.com/jack-mixer/jack_mixer
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/jack-mixer/jack_mixer/archive/release-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: meson
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: glib2-devel
BuildRequires: gettext
BuildRequires: python3-devel
BuildRequires: python3-cairo
BuildRequires: python3-gobject-base
BuildRequires: python3-pyxdg
BuildRequires: python3-Cython
BuildRequires: python3-docutils
BuildRequires: python3-appdirs
BuildRequires: desktop-file-utils

Requires: python3-cairo
Requires: python3-gobject-base
Requires: python3-appdirs

%description
jack_mixer is Gtk Jack audio mixer with look similar to it`s hardware counterparts.
It has lot of useful features, apart from being able to mix multiple Jack audio streams.

%prep
%autosetup -n %{name}-release-%{version}

# Remove unsupported desktop Categories
sed -i -e "s/GTK;GNOME;//g" data/jack_mixer.desktop
sed -i -e "s/Player;//g"    data/jack_mixer.desktop

%build

%set_build_flags

export CFLAGS="$CFLAGS -Wno-error=format-security"

%meson
%meson_build

%install

%meson_install

desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/jack_mixer.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/jack_mixer.desktop

%files
%doc CHANGELOG.md AUTHORS README.md
%license COPYING
%{_bindir}/*
%{_usr}/lib/*
%{_libdir}/*
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/man/*
%{_datadir}/locale/*
%{_sysconfdir}/xdg/raysession/client_templates/*

%changelog
* Fri Nov 10 2023 Yann Collette <ycollette.nospam@free.fr> - 18-1
- update to 18-1

* Sat Oct 16 2021 Yann Collette <ycollette.nospam@free.fr> - 17-1
- update to 17-1

* Thu Apr 15 2021 Yann Collette <ycollette.nospam@free.fr> - 16-1
- update to 16-1

* Thu Mar 18 2021 Yann Collette <ycollette.nospam@free.fr> - 15.1-1
- update to 15.1-1

* Fri Feb 26 2021 Yann Collette <ycollette.nospam@free.fr> - 15-1
- update to 15-1

* Fri Jul 17 2020 Yann Collette <ycollette.nospam@free.fr> - 13-1
- Initial spec file
