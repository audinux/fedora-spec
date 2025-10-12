# Status: active
# Tag: Tool
# Type: Standalone
# Category: Tool

Name: millisecond
Version: 0.1.1
Release: 1%{?dist}
Summary: Optimize your Linux system for low latency audio
License: GPL-3.0-or-later
URL: https://github.com/gaheldev/Millisecond/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/gaheldev/Millisecond/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: meson
BuildRequires: gettext
BuildRequires: gtk-update-icon-cache
BuildRequires: glib2-devel
BuildRequires: desktop-file-utils

Requires: python3
Requires: python3-gobject-base

%description
Millisecond is a gtk app based on rtcqs.
It provides system diagnostics and offers tips to improve low latency performance
for audio production, with links to detailed documentation from linuxaudio wiki.

In future releases, I intend to allow running fixes from the app whenever possible.

%prep
%autosetup -n Millisecond-%{version}

%meson
%meson_build

%install

%meson_install

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/io.github.gaheldev.Millisecond.desktop

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/io.github.gaheldev.Millisecond.desktop

%files
%doc README.md
%license COPYING
%{_bindir}/*
%{_datadir}/millisecond/*
%{_datadir}/dbus-1/*
%{_datadir}/glib-2.0/*
%{_datadir}/applications/*
%{_datadir}/metainfo/*
%{_datadir}/icons/hicolor/scalable/*
%{_datadir}/icons/hicolor/symbolic/*

%changelog
* Sun Oct 12 2025 Yann Collette <ycollette dot nospam at free.fr> 0.1.1-1
- initial release of the spec file
