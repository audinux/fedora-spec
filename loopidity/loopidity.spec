Name:    loopidity
Version: 0.14.026
Release: 1%{?dist}
Summary: A multi-track, multi-channel, looping audio recorder designed for live handsfree use
License: GPL-3.0-or-later
URL:     https://github.com/bill-auger/loopidity

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/bill-auger/loopidity/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: loopidity.jpg

BuildRequires: gcc-c++ gcc
BuildRequires: autoconf automake
BuildRequires: SDL-devel
BuildRequires: SDL_gfx-devel
BuildRequires: SDL_ttf-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: desktop-file-utils

%description
A multi-track, multi-channel, looping audio recorder designed
for live handsfree use.

%prep
%autosetup -n %{name}-%{version}

%build

autoreconf --install

%configure
%make_build

%install

%make_install

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp %{SOURCE1} %{buildroot}/%{_datadir}/pixmaps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=%{name}
Icon=%{name}
Comment=A multi-track, multi-channel, looping audio recorder designed for live handsfree use
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/doc/%{name}/
%{_datadir}/pixmaps/*
%{_mandir}/man1/*

%changelog
* Thu Mar 09 2023 Yann Collette <ycollette.nospam@free.fr> - 0.14.026-1
- Initial development
