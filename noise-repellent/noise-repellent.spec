# Tag: Gate
# Type: Plugin, LV2
# Category: Audio, Effect
# LastSourceUpdate: 2020

Name: lv2-noise-repellent
Version: 0.2.3
Release: 5%{?dist}
Summary: A lv2 plug-in for broadband noise reduction.
License: GPL-2.0-or-later
URL: https://github.com/lucianodato/noise-repellent

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/lucianodato/noise-repellent/archive/refs/tags/v%{version}.tar.gz#/noise-repellent-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: meson
BuildRequires: git
BuildRequires: lv2-devel
BuildRequires: fftw-devel

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
%autosetup -n noise-repellent-%{version}

%build

%meson --buildtype=release --libdir=%{_lib} --wrap-mode forcefallback
%meson_build

%install
%meson_install

# Cleanup
rm -f %{buildroot}/%{_libdir}/libspecbleach.a
rm -rf %{buildroot}/%{_libdir}/pkgconfig/libspecbleach.pc

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*
%exclude %{_includedir}/

%changelog
* Tue Mar 07 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2.3-5
- update to 0.2.3-5 - fixes

* Fri May 20 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2.3-4
- update to 0.2.3-4

* Sun May 15 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2.2-4
- update to 0.2.2-4

* Sun Apr 24 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2.1-4
- update to 0.2.1-4  - obsoletes noie-repellent in favor of lv2-noise-repellent

* Sun Apr 24 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2.1-3
- update to 0.2.1-3

* Sat Apr 23 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-3
- update to 0.2.0-3

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
