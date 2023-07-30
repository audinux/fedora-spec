Name:    js80p
Version: 1.9.8
Release: 1%{?dist}
Summary: A MIDI driven, performance oriented, versatile synthesizer plugin.
License: GPL-3.0-only
URL:     https://github.com/attilammagyar/js80p

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/attilammagyar/js80p/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: libxcb-devel
BuildRequires: cairo-devel
BuildRequires: xcb-util-renderutil-devel
BuildRequires: vst3sdk

%description
A MIDI driven, performance oriented, versatile synthesizer VST plugin.

%prep
%setup -n %{name}-%{version}

%set_build_flags

sed -i -e "/Werror/d" Makefile
sed -i -e "/Wno-format/d" Makefile
sed -i -e "s/-Wall/-Wall \$(CXXFLAGS)/g" Makefile

%build

make SYS_LIB_PATH=%{_libdir} INSTRUCTION_SET=sse2

%install 

install -m 755 -d %{buildroot}%{_libdir}/vst3/js80p.vst3/Contents/%{_target}/
install -m 755 dist/js80p-dev-linux-64bit-sse2-vst3_single_file/js80p.vst3 %{buildroot}/%{_libdir}/vst3/js80p.vst3/Contents/%{_target}/js80p.so
cp -ra presets %{buildroot}/%{_libdir}/vst3/js80p.vst3/

%check
validator %{buildroot}/%{_libdir}/vst3/js80p.vst3

%files
%doc README.md
%license LICENSE.txt
%{_libdir}/vst3/*

%changelog
* Sun Jul 30 2023 Yann Collette <ycollette.nospam@free.fr> - 1.9.8-1
- update to 1.9.8-1

* Wed Jul 26 2023 Yann Collette <ycollette.nospam@free.fr> - 1.9.7-1
- update to 1.9.7-1

* Sat May 06 2023 Yann Collette <ycollette.nospam@free.fr> - 1.1.2-1
- Initial spec file
