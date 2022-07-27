# Tag: Guitar, Overdrive
# Type: Plugin, LV2
# Category: Audio, Effect

Name:    neothesia
Version: 0.0.13
Release: 1%{?dist}
Summary: Flashy Synthesia Like Software
License: GPLv3+
URL:     https://github.com/PolyMeilex/Neothesia

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/PolyMeilex/Neothesia/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: rust cargo
# BuildRequires: ffmpeg-deve
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
%{_datadir}/neothesia/sf2/*
%{_datadir}/neothesia/midi/*
%{_datadir}/applications/com.github.polymeilex.neothesia.desktop
%{_datadir}/icons/neothesia/com.github.polymeilex.neothesia.png
%{_datadir}/metainfo/com.github.polymeilex.neothesia.metainfo.xml

%changelog
* Mon Jul 25 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.13-1
- Initial spec file
