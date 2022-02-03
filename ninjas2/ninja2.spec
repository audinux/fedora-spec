# Global variables for github repository
%global commit0 a767a9eea4e543061993290168a321d10c08b03c
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: A sample slicer audio plugin
Name:    ninjas2
Version: 0.2.0
Release: 2%{?dist}
License: GPL
URL:     https://github.com/clearly-broken-software/ninjas2

Vendor:       Audinux
Distribution: Audinux

# git clone https://github.com/clearly-broken-software/ninjas2
# cd ninjas2
# git checkout v0.2.0
# git submodule init
# git submodule update
# rm -rf .git dpf/.git
# cd ..
# tar cvfz ninjas2.tar.gz ninjas2/*

Source0: ninjas2.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel

%description
A sample slicer audio plugin

%prep
%autosetup -n %{name}

%build

make PREFIX=%{_prefix}r LV2DIR=%{_libdir}/lv2 DESTDIR=%{buildroot} SKIP_STRIPPING=true CXXFLAGS="%{build_cxxflags} -std=c++11 -fvisibility=hidden -fPIC"

%install

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 755 -d %{buildroot}/%{_libdir}/lv2/ninjas2.lv2
%__install -m 755 -d %{buildroot}/%{_libdir}/vst

cp bin/ninjas2 %{buildroot}/%{_bindir}/
cp -r bin/ninjas2.lv2/* %{buildroot}/%{_libdir}/lv2/ninjas2.lv2/
cp bin/ninjas2-vst.so %{buildroot}/%{_libdir}/vst/

%files
%doc AUTHORS LICENSE README.md
%{_bindir}/*
%{_libdir}/lv2/*
%{_libdir}/vst/*

%changelog
* Sun Oct 4 2020 Yann Collette <ycollette dot nospam at free.fr> 0.2.0-2
- debug fixes 

* Mon Jan 20 2020 Yann Collette <ycollette dot nospam at free.fr> 0.2.0-1
- initial release 
