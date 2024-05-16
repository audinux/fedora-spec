# Tag: Guitar
# Type: Plugin, LV2, VST3, CLAP
# Category: Audio, Effect

Name: ToneTwistPlugs
Version: 0.7
Release: 1%{?dist}
Summary: Multi-format LV2|VST2|VST3|CLAP audio effect plugs using the DISTRHO Plugin Framework
License: GPL-2.0-or-later
URL: https://github.com/brummer10/ToneTwistPlugs
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./brummer10-source.sh ToneTwistPlugs v0.7

Source0: ToneTwistPlugs.tar.gz
Source1: brummer10-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: git
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: libsigc++20-devel
BuildRequires: vim-common

%description
Multi-format LV2|VST2|VST3|CLAP audio effect plugs using the DISTRHO Plugin Framework

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n ToneTwistPlugs

%build

%set_build_flags

%make_build SKIP_STRIPPING=true

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_libdir}/clap/
install -m 755 -d %{buildroot}%{_bindir}/

install -m 755 bin/boobtube %{buildroot}/%{_bindir}/
install -m 755 bin/collisiondrive %{buildroot}/%{_bindir}/
install -m 755 bin/metaltone %{buildroot}/%{_bindir}/
install -m 755 bin/rumor %{buildroot}/%{_bindir}/
install -m 755 bin/tubescreamer %{buildroot}/%{_bindir}/

cp -ra bin/*.clap %{buildroot}%{_libdir}/clap/
cp -ra bin/*.lv2 %{buildroot}%{_libdir}/lv2/
cp -ra bin/*.vst3 %{buildroot}%{_libdir}/vst3/

%files
%doc README.md
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Mon Nov 27 2023 Yann Collette <ycollette.nospam@free.fr> - 0.7-1
- update to 0.7-1

* Sun Oct 08 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6-1
- Initial spec file
