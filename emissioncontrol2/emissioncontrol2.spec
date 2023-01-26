Name:    emissioncontrol2
Version: 1.2
Release: 1%{?dist}
Summary: Granular Scheduler for Arbitrary Sound Files
URL:     https://github.com/EmissionControl2/EmissionControl2
License: GPLv3+

Vendor:       Audinux
Distribution: Audinux

# Usage: ./emissioncontrol2-source.sh <TAG>
#        ./emissioncontrol2-source.sh v1.2

Source0: EmissionControl2.tar.gz
Source1: emissioncontrol2-source.sh
Patch0: emissioncontrol2-0001-add-missing-header.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: libsndfile-devel
BuildRequires: assimp-devel
BuildRequires: fftw-devel
BuildRequires: gtk3-devel
BuildRequires: libvorbis-devel
BuildRequires: libogg-devel
BuildRequires: flac-devel
BuildRequires: libsamplerate-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: desktop-file-utils

%description
EmissionControl2 (EC2) is a standalone interactive real-time
application for granular synthesis and sound file granulation.

%prep
%autosetup -p1 -n EmissionControl2

%ifarch aarch64
cd ecSource/external/nativefiledialog/build/gmake_linux/
sed -i -e "s/-m64//g" nfd.make
sed -i -e "s/-m64//g" test_opendialog.make
sed -i -e "s/-m64//g" test_opendialogmultiple.make
sed -i -e "s/-m64//g" test_pickfolder.make
sed -i -e "s/-m64//g" test_savedialog.make
# Still fail to build!: rror: narrowing conversion of '-1' from 'int' to 'char' [-Wnarrowing]
%endif

%build

cd ecSource/external/nativefiledialog/build/gmake_linux
%make_build
cd ../../../../..

cd ecSource
%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
cp ecSource/bin/EmissionControl2 %{buildroot}/%{_bindir}/emissioncontrol2

install -m 755 -d %{buildroot}/%{_datadir}/emissioncontrol2/samples/
cp -r externalResources/samples/* %{buildroot}/%{_datadir}/emissioncontrol2/samples/

install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp externalResources/icon/EmissionControl2.png %{buildroot}/%{_datadir}/pixmaps/emissioncontrol2.png

install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name
Exec=%{name}
Icon=/usr/share/pixmaps/emissioncontrol2.png
Comment=Granular Scheduler for Arbitrary Sound Files
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_datadir}/emissioncontrol2/samples/*

%changelog
* Thu Jan 26 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2-1
- Initial spec file
