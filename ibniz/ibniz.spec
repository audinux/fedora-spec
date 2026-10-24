# Status: active
# Tag: Alsa
# Type: Language
# Category: Audio, Video, Synthesizer, Programming

%global commit0 3ba06ae5f2cf5765c0e06874a093f767054b6359

Name: ibniz
Version: 0.0.1
Release: 2%{?dist}
Summary: A virtual machine designed for extremely compact low-level audiovisual programs.
License: Zlib
URL: https://viznut.fi/ibniz/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/viznut/IBNIZ/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz
Source1: ibniz.svg
Patch0: ibniz-fixingmakefile.patch
Patch1: ibniz-manpage.patch
Patch2: ibniz-20.patch
Patch3: ibniz-21.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: perl-interpreter
BuildRequires: python3-docutils
BuildRequires: sdl12-compat-devel
BuildRequires: desktop-file-utils

%description
IBNIZ is a virtual machine designed for extremely compact low-level audiovisual programs.
The leading design goal is usefulness as a platform for demoscene productions, glitch art
and similar projects. Mainsteam software engineering aspects are considered totally irrelevant.
IBNIZ stands for Ideally Bare Numeric Impression giZmo. The name also refers to Gottfried
Leibniz, the 17th-century polymath who, among all, invented binary arithmetic, built the
first four-operation calculating machine, and believed that the world was designed with the
principle that a minimal set of rules should yield a maximal diversity.

%prep
%autosetup -p1 -n IBNIZ-%{commit0}

%build

cd src
%make_build

%install

cd src
%make_install

install -m 755 -d %{buildroot}/%{_datadir}/doc/%{name}/
install -m 644 ibniz.txt %{buildroot}/%{_datadir}/doc/%{name}/

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=%{name}
Icon=%{name}
Comment=A virtual machine designed for extremely compact low-level audiovisual programs
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license src/licence.txt
%{_bindir}/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/applications/*
%{_datadir}/doc/%{name}/%{name}.txt

%changelog
* Sat Oct 24 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to 0.0.1-2 - fix packaging

* Sat Oct 24 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- initial version of the spec
