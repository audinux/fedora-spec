Name:    js80p
Version: 1.1.2
Release: 1%{?dist}
Summary: A MIDI driven, performance oriented, versatile synthesizer plugin.
License: GPLv3
URL:     https://github.com/attilammagyar/js80p

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/attilammagyar/js80p/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: libxcb-devel
BuildRequires: cairo-devel
BuildRequires: xcb-util-renderutil-devel

%description
A MIDI driven, performance oriented, versatile synthesizer VST plugin.

%prep
%setup -n %{name}-%{version}

%set_build_flags

sed -i -e "/Werror/d" Makefile
sed -i -e "/Wno-format/d" Makefile
sed -i -e "s/-msse2/\$(CXXFLAGS)/g" Makefile

%build

make TARGET_PLATFORM=x86_64-gpp LIB_PATH=%{_libdir} SYS_LIB_PATH=%{_libdir}

%install 

install -m 755 -d %{buildroot}%{_libdir}/vst3/js80p.vst3/
install -m 755 dist/js80p-dev-linux-64bit-vst3/js80p.vst3 %{buildroot}/%{_libdir}/vst3/js80p.vst3/
cp -ra presets %{buildroot}/%{_libdir}/vst3/js80p.vst3/

%files
%doc README.md
%license LICENSE.txt
%{_libdir}/vst3/*

%changelog
* Sat May 06 2023 Yann Collette <ycollette.nospam@free.fr> - 1.1.2-1
- Initial spec file
