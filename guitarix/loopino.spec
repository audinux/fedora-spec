# Status: active
# Tag: MIDI, Sampler
# Type: Standalone, Plugin, CLAP
# Category: Audio, Sampler

Name: loopino
Version: 0.9.6
Release: 2%{?dist}
Summary: A Minimalist Sampler for Linux
License: BSD
URL: https://github.com/brummer10/Loopino
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux


# ./brummer10-source.sh <project> <tag>
# ./brummer10-source.sh Loopino v0.9.6

Source0: Loopino.tar.gz

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

Requires: license-%{name}

%description
Loopino is a lightweight audio sampler designed for Linux systems,
built around the JACK Audio Connection Kit. It allows you to load,
trim, and loop audio files with precision, making it ideal for
crafting seamless sample loops.
With a clean, minimal interface and smooth JACK integration, Loopino
fits perfectly into any Linux-based audio workflow — whether for sound
design, live performance, or creative sampling experiments

%package -n license-%{name}
Summary: License and documentation for %{name}
License: BSD

%description -n license-%{name}
License and documentation for %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: BSD
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n Loopino

sed -i -e "/$Version=0.2/d" Loopino/loopino.desktop
sed -i -e "/SSE_CFLAGS =/d" Loopino/Makefile

%build

%make_build STRIP=true all clap

%install

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra bin/*.clap %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra bin/loopino %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/applications/
cp Loopino/loopino.desktop %{buildroot}/%{_datadir}/applications/

install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp Loopino/loopino.svg %{buildroot}/%{_datadir}/pixmaps/

desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=X-Jack \
        --dir %{buildroot}/%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications/loopino.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/loopino.desktop

%files
%{_bindir}/*
%{_datadir}/applications/loopino.desktop
%{_datadir}/pixmaps/loopino.svg

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Sun Feb 01 2026 Yann Collette <ycollette.nospam@free.fr> - 0.9.6-2
- update to 0.9.6-2

* Thu Jan 29 2026 Yann Collette <ycollette.nospam@free.fr> - 0.9.5-2
- update to 0.9.5-2

* Thu Jan 22 2026 Yann Collette <ycollette.nospam@free.fr> - 0.9.2-2
- update to 0.9.2-2

* Wed Jan 21 2026 Yann Collette <ycollette.nospam@free.fr> - 0.9.1-2
- update to 0.9.1-2

* Thu Jan 08 2026 Yann Collette <ycollette.nospam@free.fr> - 0.8.1-2
- update to 0.8.1-2

* Wed Jan 07 2026 Yann Collette <ycollette.nospam@free.fr> - 0.8.0-2
- update to 0.8.0-2

* Sat Jan 03 2026 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-2
- update to 0.5.0-2

* Wed Dec 24 2025 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-2
- update to 0.2.0-2

* Thu Dec 18 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-2
- update to 0.1.0-2

* Sun Dec 07 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.2-2
- update to 0.0.2-2

* Wed Nov 26 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to 0.0.1-2 - real 0.0.1 release

* Sat Nov 22 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
