# Tag: MIDI, FM, Tracker
# Type: Standalone
# Category: Audio, Synthesizer, Sequencer

Name:    protrekkr2
Version: 2.6.3
Release: 1%{?dist}
Summary: A jack tracker
License: GPLv2+
URL:     https://github.com/hitchhikr/protrekkr

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/hitchhikr/protrekkr/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:  protrekkr2-0001-set-config-file-paths.patch

BuildRequires: gcc gcc-c++ make
BuildRequires: alsa-lib-devel
BuildRequires: SDL-devel
BuildRequires: zlib-devel
BuildRequires: desktop-file-utils

%description
An ALSA tracker

%prep
%autosetup -p1 -n protrekkr-%{version}

sed -i -e "s/-O3/-O2/g" makefile.linux
sed -i -e "s/-g/-g \$(CFLAGS)/g" makefile.linux
sed -i -e "/strip/d" makefile.linux

%build

%set_build_flags

export CFLAGS=`echo $CFLAGS | sed -e "s/-Werror=format-security//g"`
export LDFLAGS=`echo $LDFLAGS | sed -e "s/-Werror=format-security//g"`
export CXXFLAGS=`echo $CXXFLAGS | sed -e "s/-Werror=format-security//g"`

cd src/extralibs/sdl_draw
%make_build -f makefile.linux
cd ../../..
	
%make_build -f makefile.linux

%install

install -m 755 -d %{buildroot}/%{_datadir}/applications/
cat > %{buildroot}/%{_datadir}/applications/protrekkr2.desktop <<EOF
[Desktop Entry]
Version=1.0
Name=protrekkr2
Comment=Mod tracker
Exec=protrekkr2
Icon=protrekkr2
Terminal=false
Type=Application
Categories=AudioVideo;Audio;
EOF

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 release/distrib/ptk_linux %{buildroot}%{_bindir}/protrekkr2

install -m 755 -d %{buildroot}/%{_datadir}/protrekkr2/instruments/
install -m 644 release/distrib/instruments/* %{buildroot}%{_datadir}/protrekkr2/instruments/
install -m 755 -d %{buildroot}/%{_datadir}/protrekkr2/modules/
cp -ra release/distrib/modules/* %{buildroot}%{_datadir}/protrekkr2/modules/
install -m 755 -d %{buildroot}/%{_datadir}/protrekkr2/presets/
install -m 644 release/distrib/presets/* %{buildroot}%{_datadir}/protrekkr2/presets/
install -m 755 -d %{buildroot}/%{_datadir}/protrekkr2/reverbs/
install -m 644 release/distrib/reverbs/* %{buildroot}%{_datadir}/protrekkr2/reverbs/
install -m 755 -d %{buildroot}/%{_datadir}/protrekkr2/skins/
install -m 644 release/distrib/skins/* %{buildroot}%{_datadir}/protrekkr2/skins/

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
install -m 644 ./src/support/project.ico %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/protrekkr2.ico

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/protrekkr2.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/protrekkr2.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/*

%changelog
* Thu Jan 27 2022 Yann Collette <ycollette.nospam@free.fr> - 2.6.3-1
- Update to 2.6.3-1

* Thu Dec 16 2021 Yann Collette <ycollette.nospam@free.fr> - 2.6.2-1
- Initial build
