# Tag: MIDI, Tool, Video
# Type: Standalone
# Category: MIDI, Tool

Name: neothesia
Version: 0.2.1
Release: 1%{?dist}
Summary: Flashy Synthesia Like Software
License: GPL-3.0-or-later
URL: https://github.com/PolyMeilex/Neothesia

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/PolyMeilex/Neothesia/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: rust
BuildRequires: cargo
BuildRequires: alsa-lib-devel
BuildRequires: glib2-devel
BuildRequires: atk-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: gtk3-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

%description
Flashy Synthesia Like Software

%prep
%autosetup -n Neothesia-%{version}

%build

%set_build_flags
export RUSTFLAGS="-g -O"
export RUST_BACKTRACE=1

%make_build build-app
# %make_build build-recorder

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_datadir}/neothesia/sf2/
install -m 755 -d %{buildroot}/%{_datadir}/neothesia/midi/

install -m 755 target/release/neothesia %{buildroot}/%{_bindir}/
install -m 644 default.sf2 %{buildroot}/%{_datadir}/neothesia/sf2/
install -m 644 sin_wave.sf2 %{buildroot}/%{_datadir}/neothesia/sf2/
install -m 644 test.mid %{buildroot}/%{_datadir}/neothesia/midi/

install -m 755 -d %{buildroot}/%{_datadir}/icons/%{name}/
install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 755 -d %{buildroot}%{_datadir}/metainfo/

install -m 644 flatpak/com.github.polymeilex.neothesia.desktop %{buildroot}/%{_datadir}/applications/
install -m 644 flatpak/com.github.polymeilex.neothesia.png %{buildroot}/%{_datadir}/icons/%{name}/
install -m 644 flatpak/com.github.polymeilex.neothesia.metainfo.xml %{buildroot}%{_datadir}/metainfo/

desktop-file-install --vendor '' \
        --add-category=Midi \
        --add-category=Sequencer \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/com.github.polymeilex.neothesia.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/com.github.polymeilex.neothesia.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.github.polymeilex.neothesia.metainfo.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%dir %{_datadir}/neothesia/
%{_datadir}/neothesia/sf2/*
%{_datadir}/neothesia/midi/*
%{_datadir}/applications/com.github.polymeilex.neothesia.desktop
%{_datadir}/icons/neothesia/com.github.polymeilex.neothesia.png
%{_datadir}/metainfo/com.github.polymeilex.neothesia.metainfo.xml

%changelog
* Mon Mar 11 2024 Yann Collette <ycollette.nospam@free.fr> - 0.2.1-1
- update to 0.2.1-1

* Sun Jan 14 2024 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- update to 0.2.0-1

* Sun Jul 02 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- update to 0.1.0-1

* Fri Feb 17 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.16-1
- update to 0.0.16-1

* Fri Jan 27 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.15-1
- update to 0.0.15-1

* Mon Jul 25 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.13-1
- Initial spec file
