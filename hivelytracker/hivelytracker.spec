# Tag: Tracker
# Type: Standalone
# Category: Audio, Sequencer
# LastSourceUpdate: 2020

Name:    hivelytracker
Version: 1.8
Release: 1%{?dist}
Summary: Chip music tracker based on AHX 
License: BSD3
URL:     https://github.com/pete-gordon/hivelytracker

Vendor:       Audinux
Distribution: Audinux

Source0: hivelytracker.tar.gz
Source1: source_hivelytracker.sh
Patch0:  hivelytracker-0001-fix-fonts-path.patch
Patch1:  hivelytracker-0002-add-data-paths.patch

BuildRequires: SDL-devel	
BuildRequires: SDL_image-devel	
BuildRequires: SDL_ttf-devel	
BuildRequires: gcc	
BuildRequires: make
BuildRequires: gtk2-devel

Requires: dejavu-sans-mono-fonts
Requires: dejavu-sans-fonts
Requires: dejavu-serif-fonts

%description
Format created in the mid '90s, AHX was designed to create a very SID-like sound on the Amiga. 
("Sound Interface Device" (SID) was a chip used in Commodore 64 ...)
HivelyTracker offers the following features over AHX:
- Multichannel (4 to 16 channels)
- Per-channel stereo panning
- Two commands per note instead of one
- Ring modulation
- A more feature rich editor

%prep
%autosetup -p1 -n %{name}

sed -i -e "s|\$(PREFIX)|\$(DESTDIR)\$(PREFIX)|g" sdl/Makefile.linux
sed -i -e "s|CFLAGS = -g -D__SDL_WRAPPER__|CFLAGS = -g -D__SDL_WRAPPER__ %{build_cflags}|g" sdl/Makefile.linux

%build

cd sdl
%make_build -f Makefile.linux PREFIX=%{_prefix} DESTDIR=%{buildroot} 

%install
rm -rf $RPM_BUILD_ROOT
cd sdl
%make_install -f Makefile.linux PREFIX=%{_prefix} DESTDIR=%{buildroot}

# Install examples
install -m755 -d %{buildroot}%{_datadir}/%{name}/Songs/
cp -r ../Songs/* %{buildroot}%{_datadir}/%{name}/Songs/

# Cleanup fonts
rm -rf %{buildroot}%{_datadir}/%{name}/ttf

%files
%license LICENSE
%doc ChangeLog.txt
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_mandir}/man1/*

%changelog
* Fri Jun 25 2021 Yann Collette <ycollette.nospam@free.fr> 1.8-1
- initial spec
