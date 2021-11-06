Summary: Software Synthesizer
Name:    dgedit
Version: 0.10.0
Release: 2%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     http://git.drumgizmo.org/dgedit.git

Vendor:       Audinux
Distribution: Audinux

# To get dgedit source code: ./dgedit-source.sh v0.10.0
Source0: dgedit.tar.gz
Source1: dgedit-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: qtchooser
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsndfile-devel
BuildRequires: libao-devel

%description
The DrumGizmo drumkit editor DGEdit is currently in a functioning,
but very early phase of development. All of the essentials for
importing, editing and exporting the raw drumkit recordings are
there - but it is not exactly user friendly. 

%prep
%autosetup -n %{name}

%build

sed -i -e "s/lupdate/lupdate-qt5/g" src/Makefile.am
sed -i -e "s/lrelease/lrelease-qt5/g" src/Makefile.am

export QT_SELECT=5

./autogen.sh
%configure
%make_build

%install

%make_install

%files
%doc AUTHORS ChangeLog INSTALL NEWS README
%license COPYING
%{_bindir}/dgedit
%{_datadir}/locale/*

%changelog
* Wed Jul 14 2021 Yann Collette <ycollette dot nospam at free.fr> 0.10.0-2
- update to 0.10.0-2

* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free.fr> 0.1-2
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette dot nospam at free.fr> 0.1-2
- update to eeef75b159369a6441641c2c14c217c29b02a3ff

* Thu Jun 04 2015 Yann Collette <ycollette dot nospam at free.fr> 0.1-1
- Initial release of spec file for 0.1
