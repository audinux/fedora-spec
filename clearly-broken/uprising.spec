# Tag: Synthesizer
# Type: Plugin, LV2, VST3
# Category: Synthesizer

%global commit0 89f5b49d90cd47611da7e7dc2009061768716b4c

Name: uprising
Version: 0.0.1
Release: 1%{?dist}
Summary: A transition Designer Synth
License: GPL-2.0-only
URL: https://github.com/clearly-broken-software/Uprising

# Usage: ./clearly-broken-source.sh <PROJECT> <TAG>
#        ./clearly-broken-source.sh Uprising 89f5b49d90cd47611da7e7dc2009061768716b4c

Source0: Uprising.tar.gz
Source1: clearly-broken-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: mesa-libGL-devel
BuildRequires: libsndfile-devel
BuildRequires: rubberband-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libX11-devel
BuildRequires: lv2-devel

%description
A transition Designer Synth

%package -n vst-%{name}
Summary:  VST version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst-%{name}
VST version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n Uprising

%build
%set_build_flags
%make_build SKIP_STRIPPING=true

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/uprising.lv2/
install -m 755 -d %{buildroot}/%{_libdir}/vst/

install -m 755 -p bin/uprising %{buildroot}%{_bindir}/
install -m 755 -p bin/uprising-vst.so %{buildroot}%{_libdir}/vst/
cp -ra bin/uprising.lv2/* %{buildroot}%{_libdir}/lv2/uprising.lv2/

%files
%{_bindir}/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Tue Aug 02 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- initial spec file
