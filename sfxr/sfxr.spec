# Tag: Alsa
# Type: Standalone
# Category: Synthesizer

Name: sfxr
Version: 1.2.1
Release: 1%{?dist}
Summary: Create sound effects
License: GPL-2.0-only
URL: http://www.drpetter.se/project_sfxr.html
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: sfxr-sdl-1.2.1.tar.gz
Source1: sfxr-share.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: SDL-devel
BuildRequires: gtk3-devel
BuildRequires: portaudio-devel
BuildRequires: desktop-file-utils

%description
sfxr's original purpose was to provide a simple means of getting
basic sound effects into a game for those people who were working
hard to get their entries done for the Ludum Dare gaming contest
within the 48 hours and didn't have time to spend looking for
suitable ways of doing this.

The idea was that they could just hit a few buttons in this
application and get some largely randomized effects that were custom
in the sense that the user could accept/reject each proposed sound.

%prep
%autosetup -n sfxr-sdl-%{version}

tar xvfz %{SOURCE1}

%build
%set_build_flags
%make_build

%install
%make_install

cp -r share/* %{buildroot}%{_datadir}/

# install sfxr.desktop properly.
desktop-file-install --vendor '' \
        --add-category=AudioVideo \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc ChangeLog readme.txt
%{_bindir}/*
%{_datadir}/*

%changelog
* Tue Dec 14 2021 Yann Collette <ycollette.nospam@free.fr>
-
