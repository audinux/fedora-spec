Name:    lv2-gxmrfreeze
Version: 0.5
Release: 1%{?dist}
Summary: An audio, Guitarix compatible, freeze LV2 plugin
License: GPL-2.0-or-later
URL:     https://github.com/ycollet/MrFreezehttps://github.com/romi1502/MrFreeze

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ycollet/MrFreeze/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: fftw-devel
BuildRequires: lv2-devel
BuildRequires: eigen3-devel

%description
An audio, Guitarix compatible, freeze LV2 plugin

%prep
%autosetup -n MrFreeze-%{version}

%build

%set_build_flags
export CFLAGS="-I/usr/include/eigen3 $CFLAGS"
export CXXFLAGS="-I/usr/include/eigen3 $CXXFLAGS"

%ifarch aarch64
%make_build DESTDIR=%{buildroot} INSTALL_PATH=%{_libdir}/lv2/ NOOPT=true
%else
%make_build DESTDIR=%{buildroot} INSTALL_PATH=%{_libdir}/lv2/
%endif

echo "Generating harmonizer.wisdom file, this might take a while..."
fftwf-wisdom -n -x -o mrfreeze.wisdom rof1024 rob1024 rof1536 rob1536 rof2048 rob2048 rof2176 rob2176 rof2304 rob2304 rof2432 rob2432 rof2560 rob2560 rof3072 rob3072 rof4096 rob4096

%install

%make_install DESTDIR=%{buildroot} INSTALL_PATH=%{_libdir}/lv2/

%files
%doc README.md
%{_libdir}/lv2/*

%changelog
* Mon Nov 23 2020 Yann Collette <ycollette.nospam@free.fr> - 0.5-1
- update to 0.5

* Sun Nov 22 2020 Yann Collette <ycollette.nospam@free.fr> - 0.4-1
- Initial build
