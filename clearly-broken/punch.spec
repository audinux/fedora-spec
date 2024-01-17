# Tag: Compressor
# Type: Plugin, LV2, VST3
# Category: Audio, Effect

%global commit0 3969dc2fda5afe856a2a515de5c14b345f6891d1

Name: punch
Version: 0.0.1
Release: 1%{?dist}
Summary: A punchy compressor plugin with character
License: GPL-2.0-only
URL: https://github.com/clearly-broken-software/Punch

# Usage: ./clearly-broken-source.sh <PROJECT> <TAG>
#        ./clearly-broken-source.sh Punch 3969dc2fda5afe856a2a515de5c14b345f6891d1

Source0: Punch.tar.gz
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
A punchy compressor plugin with character

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
%autosetup -n Punch

%build
%set_build_flags
%make_build SKIP_STRIPPING=true

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/Punch.lv2/
install -m 755 -d %{buildroot}/%{_libdir}/vst/

install -m 755 -p bin/Punch %{buildroot}%{_bindir}/
install -m 755 -p bin/Punch-vst.so %{buildroot}%{_libdir}/vst/
cp -ra bin/Punch.lv2/* %{buildroot}%{_libdir}/lv2/Punch.lv2/

%files
%doc README.md
%{_bindir}/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Tue Aug 02 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- initial spec file
