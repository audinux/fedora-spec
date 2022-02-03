Name:    context-free
Summary: Context Free is a program that generates images from written instructions called a grammar.
Version: 3.3
Release: 1%{?dist}
License: GPL
URL:     https://github.com/MtnViewJohn/context-free

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/MtnViewJohn/context-free/archive/Version%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:  context-free-01_enable_ffmpeg.patch

BuildRequires: gcc gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: ffmpeg-devel
BuildRequires: x264-devel
BuildRequires: libpng-devel
BuildRequires: libicu-devel
BuildRequires: libatomic
BuildRequires: bison
BuildRequires: flex
BuildRequires: python3

%description
Context Free is a program that generates images from written instructions called a grammar.
The program follows the instructions in a few seconds to create images that can contain
millions of shapes. 

%prep
%autosetup -p1 -n context-free-Version%{version}

sed -i -r "/strip $@/d" Makefile

%build

%set_build_flags

export CXXFLAGS="-I/usr/include/ffmpeg $CXXFLAGS"

%make_build prefix=/usr

%install

%make_install prefix=/usr

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/examples/
cp -ra input/* %{buildroot}/%{_datadir}/%{name}/examples/

%files
%doc README
%license LICENSE.txt
%{_bindir}/*
%{_datadir}/*

%changelog
* Wed Oct 28 2020 Yann Collette <ycollette dot nospam at free.fr> 3.3-1
- initial build
