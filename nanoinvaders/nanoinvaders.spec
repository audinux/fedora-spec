# Tag: Tool, Graphic
# Type: Standalone, Plugin, LV2, VST
# Category: Tool, Graphic

Name: nanoinvaders
Version: 0.1
Release: 2%{?dist}
Summary: Play space invaders in an audio plugin
License: GPL-2.0-or-later
URL: https://github.com/clearly-broken-software/nanoinvaders

Vendor:       Audinux
Distribution: Audinux

# git clone https://github.com/clearly-broken-software/nanoinvaders
# git submodule init
# git submodule update
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz nanoinvaders.tar.gz nanoinvaders/
# rm -rf nanoinvaders

Source0: nanoinvaders.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: pkgconfig(jack)
BuildRequires: liblo-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libsamplerate-devel

%description
Play space invaders in an audio plugin

%prep
%autosetup -n %{name}

%build

%set_build_flags

%make_build PREFIX=/usr LIBDIR=%{_lib} SKIP_STRIPPING=true all

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/
install -m 755 -d %{buildroot}/%{_libdir}/vst/

cp bin/%{name} %{buildroot}/%{_bindir}/
cp bin/%{name}-vst.so %{buildroot}/%{_libdir}/vst/
cp -r bin/%{name}.lv2 %{buildroot}/%{_libdir}/lv2/

%files
%doc README.md
%license LICENSE.md
%{_bindir}/*
%{_libdir}/lv2/*
%{_libdir}/vst/*

%changelog
* Tue Oct 6 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1-2
- fix debug package

* Fri May 8 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial spec file
