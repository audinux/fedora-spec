# Status: active
# Tag: MIDI, Sampler
# Type: Standalone, Plugin, CLAP
# Category: Audio, Sampler

Name: smoothir
Version: 0.1
Release: 1%{?dist}
Summary: Creating impulse responses (IRs) through spectral matching of two audio files
License: BSD
URL: https://github.com/brummer10/SmoothIR
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux


# ./brummer10-source.sh <project> <tag>
# ./brummer10-source.sh SmoothIR v0.1

Source0: SmoothIR.tar.gz
Source1: brummer10-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(jack)
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: fluidsynth-devel
BuildRequires: alsa-lib-devel
BuildRequires: libsndfile-devel
BuildRequires: fftw-devel
BuildRequires: vim-common
BuildRequires: desktop-file-utils

%description
SmoothIR is a tool for creating impulse responses (IRs) through spectral matching of two audio files,
with a focus on musically useful results rather than purely technical accuracy.
The idea is simple:
The spectral difference between a Reference and a Source is transformed into an IR,
then deliberately smoothed and band-limited.
The result is an IR that works very well for creative applications (e.g. guitars, reamping, sound design).

%prep
%autosetup -n SmoothIR

sed -i -e "/Version=0.2/d" SmoothIR/smoothir.desktop

%build

%make_build STRIP=true

%install

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra bin/smoothir %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/applications/
cp SmoothIR/smoothir.desktop %{buildroot}/%{_datadir}/applications/

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
cp SmoothIR/smoothir.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/

desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=X-Jack \
        --dir %{buildroot}/%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications/smoothir.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/smoothir.desktop

%files
%doc README.md
%{_bindir}/smoothir
%{_datadir}/applications/smoothir.desktop
%{_datadir}/icons/hicolor/scalable/apps/smoothir.svg

%changelog
* Wed Apr 29 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- update to 0.1-1

* Fri Apr 24 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
