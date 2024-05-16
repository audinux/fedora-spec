# Tag: Jack, MIDI
# Type: Plugin, LV2
# Category: Audio, Effect

Summary: Pattern-controlled MIDI amp & time stretch LV2 plugin to produce shuffle / swing effects
Name:    lv2-BSchaffl
Version: 1.4.10
Release: 2%{?dist}
License: GPL
URL:     https://github.com/sjaehn/BSchaffl
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/sjaehn/BSchaffl/archive/%{version}.tar.gz#/BSchaffl-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel

%description
Groove quantizer LV2 MIDI plugin.  B.Schaffl is a slider / shape-controlled MIDI amp & time stretch plugin
to vitalize sequencer-controlled MIDI instruments and to produce shuffle / swing effects.

Key features:
- MIDI velocity amplification and timing manipulation plugin
- Swing and shuffle rhythms
- Pre-generator dynamics
- Tempo rubato
- Pattern (sliders) or shape-controlled
- MIDI filters
- Smart quantization
- Group / link individual instances of B.Schaffl

%prep
%autosetup -n BSchaffl-%{version}

%build

%set_build_flags

%make_build PREFIX=%{_prefix} \
	    LV2DIR=%{_libdir}/lv2 \
	    DESTDIR=%{buildroot} \
	    STRIP=true \
	    CXXFLAGS="$CXXFLAGS -std=c++11 -fvisibility=hidden -fPIC"

%install

%make_install PREFIX=%{_prefix} \
	      LV2DIR=%{_libdir}/lv2 \
	      DESTDIR=%{buildroot} \
	      STRIP=true \
	      CXXFLAGS="$CXXFLAGS -std=c++11 -fvisibility=hidden -fPIC"

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Thu Jun 23 2022 Yann Collette <ycollette dot nospam at free.fr> 1.4.10-2
- update to 1.4.10-2

* Fri Sep 10 2021 Yann Collette <ycollette dot nospam at free.fr> 1.4.6-2
- update to 1.4.6-2 - fix install

* Mon Mar 15 2021 Yann Collette <ycollette dot nospam at free.fr> 1.4.6-1
- update to 1.4.6-1

* Thu Feb 11 2021 Yann Collette <ycollette dot nospam at free.fr> 1.4.4-1
- update to 1.4.4-1

* Mon Jan 11 2021 Yann Collette <ycollette dot nospam at free.fr> 1.4.2-1
- update to 1.4.2-1

* Mon Jan 4 2021 Yann Collette <ycollette dot nospam at free.fr> 1.4.0-1
- update to 1.4.0-1

* Sun Dec 27 2020 Yann Collette <ycollette dot nospam at free.fr> 1.2.2-1
- update to 1.2.2-1

* Sun Aug 23 2020 Yann Collette <ycollette dot nospam at free.fr> 1.2.0-1
- update to 1.2.0-1

* Fri Jul 24 2020 Yann Collette <ycollette dot nospam at free.fr> 0.2.0-1
- update to 0.2.0-1

* Mon May 25 2020 Yann Collette <ycollette dot nospam at free.fr> 0.1.0-1
- initial release
