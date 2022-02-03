# Tag: Gate
# Type: Plugin, LV2
# Category: Audio, Effect
# LastSourceUpdate: 2020

# Global variables for github repository
%global commit0 87b4380eae2b69b09bba8a8b181f24153079100d
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    noise-repellent-lv2
Version: 0.1.5.%{shortcommit0}
Release: 3%{?dist}
Summary: A lv2 plug-in for broadband noise reduction.
License: GPLv2+
URL:     https://github.com/lucianodato/noise-repellent	

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/lucianodato/noise-repellent/archive/%{commit0}.tar.gz#/noise-repellent-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: fftw-devel
BuildRequires: meson

%description
Features
* Spectral gating and spectral subtraction suppression rule
* Adaptive and manual noise thresholds estimation
* Adjustable noise floor
* Adjustable offset of thresholds to perform over-subtraction
* Time smoothing and a masking estimation to reduce artifacts
* Basic onset detector to avoid transients suppression
* Whitening of the noise floor to mask artifacts and to recover higher frequencies
* Option to listen to the residual signal
* Soft bypass
* Noise profile saved with the session

Limitations
* The plug-in will introduce latency so it's not appropriate to be used while recording (23 ms for 44.1 kHz)
* It was developed to be used with Ardour however it is known to work with other hosts

%prep
%autosetup -n noise-repellent-%{commit0}

%build

%ifarch x86_64
	VERBOSE=1 meson --prefix=/usr/lib64/lv2 build
%else
	VERBOSE=1 meson --prefix=/usr/lib/lv2 build
%endif

cd build
DESTDIR=%{buildroot} VERBOSE=1 ninja 

%install 
cd build
DESTDIR=%{buildroot} ninja install

%files
%{_libdir}/lv2/*

%changelog
* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.5-3
- update to 0.1.5-3 - fix debug build

* Mon Jan 6 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.5-2
- update to 0.1.5-2

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1.4-2
- update for Fedora 29

* Mon May 14 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1.4-2
- update to latest version + meson build

* Tue Nov 28 2017 Yann Collette <ycollette.nospam@free.fr> - 0.1.4-1
- Initial build
