# Status: active
# Tag: Effect
# Type: LADSPA
# Category: Audio, Effects

# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments to toni@links2linux.de

%global commit0 085bff5aba2e4f4b8467e9e3596686e6aa68debf

Name: ladspa-wubflip
Summary: WubFlip ladspa effect plugin
Version: 1
Release: 1%{?dist}
License: GPL-2.0
URL: http://www.alexs.org/ladspa/

Source0: https://github.com/ycollet/ladspa-wubflip/archive/%{commit0}.tar.gz#/ladspa-wubflip-%{commit0}.tar.gz

BuildRequires: gcc-c++
BuildRequires: ladspa-devel

%description
I am not an expert on effects algorithms. I just thought I'd mess
around with the audio data and see what happens. WubFlip was the
result.

It sort of flips high or low values beyond a threshold making a
dirty distorted mess of the sound that might be useful for people
making wanting big dirty breaks or synths or something like that.

Play around with the sliders. The upper threshold slider needs to
be higher (to the right of) than the lower threshold slider
otherwise you'll get no sound. The difference between them
effects the sound. Then the multiplier slider effects how much
"flipping" gets done.

%prep
%autosetup -n ladspa-wubflip-%{commit0}

%build

%set_build_flags
export CFLAGS="-fPIC $CFLAGS"
export CXXFLAGS="-fPIC $CXXFLAGS"

%make_build

%install

install -m755 -d %{buildroot}/%{_libdir}/ladspa/
install -m755 wubflip.so %{buildroot}/%{_libdir}/ladspa/

%files
%doc README
%{_libdir}/ladspa/wubflip.so

%changelog
* Thu May 07 2026 Yann Collette <ycollette dot nospam at free.fr> 1-1
- update to 1-1 - first Fedora release

* Wed May 20 2009 Toni Graffy <toni@links2linux.de> - 1-0.pm.1
- initial build 1
