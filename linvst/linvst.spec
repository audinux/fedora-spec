%global debug_package %{nil}

Name:    LinVst
Version: 4.78
Release: 3%{?dist}
Summary: Linux Windows vst wrapper/bridge
License: GPLv3
URL:     https://github.com/osxmidi/linvst

Source0: %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: glibc-devel(x86-32)
BuildRequires: gtk3-devel
BuildRequires: libX11-devel
BuildRequires: libX11-devel(x86-32)
BuildRequires: libstdc++-devel(x86-32)
BuildRequires: wine-devel
BuildRequires: wine-devel(x86-32)

Requires: wine
Requires: python3

%description
LinVst adds support for Windows vst's to be used in Linux vst capable DAW's.

%prep
%autosetup

sed -i "s/LINK_WINE = .* -l/LINK_WINE = -L\/usr\/lib64\/wine -l/g" Makefile
sed -i "s/LINK_WINE32 = .* -l/LINK_WINE32 = -L\/usr\/lib\/wine -l/g" Makefile

%build

export LDFLAGS="-lX11 -lrt"

make
make -f Makefile-convert

%install

%make_install
%make_install -f Makefile-convert

mkdir -p %{buildroot}/%{_datadir}/%{name}/64bit-32bit
install -m 755 linvst.so %{buildroot}/%{_datadir}/%{name}/64bit-32bit

mkdir -p %{buildroot}/%{_datadir}/%{name}/doc
cp -ra Detailed-Guide %{buildroot}/%{_datadir}/%{name}/doc
cp -ra Realtime-Audio-Config %{buildroot}/%{_datadir}/%{name}/doc

mkdir -p %{buildroot}/%{_datadir}/%{name}/manage/
cp manage/linvstmanage-cli %{buildroot}/%{_bindir}/
cp manage/linvstmanage.ini %{buildroot}/%{_datadir}/%{name}/manage/
cp manage/README.md %{buildroot}/%{_datadir}/%{name}/manage/

%files
%license COPYING
%doc README.md
%{_bindir}/linvstmanage-cli
%{_bindir}/lin-vst-servertrack.exe
%{_bindir}/lin-vst-servertrack.exe.so
%{_bindir}/lin-vst-servertrack32.exe
%{_bindir}/lin-vst-servertrack32.exe.so
%{_bindir}/linvstconvert
%{_datadir}/%{name}/64bit-32bit/linvst.so
%{_datadir}/%{name}/doc/*
%{_datadir}/%{name}/manage/*

%changelog
* Thu Feb 09 2023 Yann Collette <ycollette.nospam@free.fr> - 4.78-3
- update to version 4.78-3 - rebuild with wine 8.

* Tue Dec 06 2022 Yann Collette <ycollette.nospam@free.fr> - 4.78-2
- update to version 4.78-1

* Sun May 15 2022 Yann Collette <ycollette.nospam@free.fr> - 4.77-1
- update to version 4.77-1

* Tue Aug 03 2021 Yann Collette <ycollette.nospam@free.fr> - 4.76-1
- update to version 4.76-1

* Sun May 02 2021 Tony James - 4.2-1
- Initial build of LinVst 4.2
