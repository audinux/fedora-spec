Name:    soundux
Version: 0.2.7
Release: 1%{?dist}
Summary: A cross-platform soundboard 
License: GPLv3+
URL:     https://github.com/Soundux/Soundux

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/Soundux/Soundux/releases/download/%{version}/soundux-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: pipewire-devel
BuildRequires: libX11-devel
BuildRequires: libwnck3-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: libappindicator-devel
BuildRequires: libappindicator-gtk3-devel
BuildRequires: libdwarf-devel
BuildRequires: openssl-devel
BuildRequires: binutils-devel
BuildRequires: elfutils-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: chrpath

Requires: ffmpeg
Requires: youtube-dl

%description
Soundux is a cross-platform soundboard that features a simple user interface.
With Soundux you can play audio to a specific application on Linux.

%prep
%autosetup -n Soundux

sed -i -e "s/-Werror/ /g" CMakeLists.txt
#-Wno-gnu
#-Wno-unused-lambda-capture

%build

%cmake -DEMBED_PATH=ON
%cmake_build

%install 

%cmake_install	

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/
cp %{__cmake_builddir}/lib/tiny-process-library/libtiny-process-library.so %{buildroot}/%{_libdir}/
cp %{__cmake_builddir}/soundux-%{version} %{buildroot}/%{_bindir}/%{name}
rm -rf %{buildroot}/opt

chrpath --delete %{buildroot}/%{_bindir}/%{name}

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/io.github.Soundux.metainfo.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_libdir}/*
%{_datadir}/applications/soundux.desktop
%{_datadir}/metainfo/io.github.Soundux.metainfo.xml
%{_datadir}/pixmaps/soundux.png

%changelog
* Fri Jan 13 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2.7-1
- Initial spec file
