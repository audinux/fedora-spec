# Global variables for github repository
%global commit0 38df4d733fff1a9438a89ec8797bc6b6810adfa7
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Tag: Mixer, Alsa, Jack
# Type: Plugin, LV2
# Category: Audio, Tool

Name:    scarlett-mixer
Version: 0.1.0
Release: 1%{?dist}
Summary: A mixer matrix for Scarlett sound card

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/x42/scarlett-mixer
Source0: scarlett-mixer.tar.gz

# git clone git://github.com/x42/scarlett-mixer
# cd scarlett-mixer
# git submodule init
# git submodule update
# find . -name .git -exec rm {} \; -print
# cd ..
# tar cvfz scarlett-mixer.tar.gz scarlett-mixer/*
# rm -rf scarlett-mixer

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: lv2-devel
BuildRequires: cairo-devel
BuildRequires: pango-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel

%description
A mixer matrix for Scarlett sound card by x42

%prep
%setup -qn %{name}

%build

make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags}

%install 

make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags} install

%__install -m 755 -d %{buildroot}/%{_datadir}/icons/scarlett/
cp scarlett-mixer-gui.png %{buildroot}/%{_datadir}/icons/scarlett/

%files
%{_bindir}/*
%{_datadir}/*

%changelog
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.6.7
- Initial build
