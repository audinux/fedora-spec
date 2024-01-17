# Tag: MIDI, Jack
# Type: Standalone
# Category: Synthesizer

# Global variables for github repository
%global commit0 0f4ef66ad46d3a1e542ea160487b1a3fe3b76031
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: Software Synthesizer
Name: horgand
Version: 1.15.0
Release: 1%{?dist}
License: GPL
URL: https://github.com/ycollet/horgand

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ycollet/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: alsa-lib-devel
BuildRequires: alsa-utils
BuildRequires: fltk-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libsndfile-devel
BuildRequires: libxcb-devel
BuildRequires: libXpm-devel
BuildRequires: zlib-devel
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: desktop-file-utils

%description
Horgand is a organ ... generates sound like a FM sinthesizer in real time,
good reason for use a fast computer, there are many others programs who emulate a organ and sure
their sound is better, but i program what i need, and just for fun.

%prep
%autosetup -n %{name}-%{commit0}

%build

./autogen.sh
%configure --libdir=%{_libdir}

%make_build CFLAGS="-fPIC %{__global_cflags}" CXXFLAGS="-fPIC %{__global_cflags}"

%install

%make_install
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/
cp src/horgand128.xpm %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/horgand.xpm

mkdir -p %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Name=Horgand
Comment=Organ
Exec=horgand
Icon=horgand
Terminal=false
Type=Application
Categories=Audio;
EOF

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS ChangeLog INSTALL NEWS README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/man/*
%{_datadir}/horgand/
%{_datadir}/applications/*
%{_datadir}/icons/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free.fr> 1.15.0-1
- update for Fedora 29

* Thu May 12 2016 Yann Collette <ycollette dot nospam at free.fr> 1.15.0-1
- Initial release of spec fil to 1.15.0
