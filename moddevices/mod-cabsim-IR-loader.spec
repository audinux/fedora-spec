# Status: active
# Tag: IR
# Type: LV2
# Category: Plugin, Effect

%global debug_package %{nil}
%global commit0 6fcc59f57f19b93db94cf74a5f529421a7fb4c16

Name: mod-cabsim-IR-loader
Version: 0.0.1
Release: 1%{?dist}
Summary: Cabsim that can load Impulse Responses
License: GPL-2.0-or-later
URL: https://github.com/mod-audio/mod-cabsim-IR-loader
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/mod-audio/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: fftw-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel

%description
An LV2 cabinet simulator plugin that loads impulse response (IR) files.
This plugin is specifically created for handling speaker cabinet IRs,
this plugin is not optimized for handling larger files like reverb IRs.
Currently it only uses the first 42.7 ms (2048 samples at 48 kHz sampling
rate) of the loaded IR file. IR files at different sample rates are
resampled to 48 kHz by the plugin. It is recommended to trim any silence
at the start of the IR file for optimal results.
Default IR file provided by forward audio.

%prep
%autosetup -n %{name}-%{commit0}

sed -i -e "s|lib/lv2|%{_lib}/lv2|g" source/Makefile

%build

cd source

%set_build_flags

%make_build DEBUG=true PREFIX=%{_prefix}

%install

cd source

%make_install DEBUG=true PREFIX=%{_prefix}

%files
%doc README.md
%{_libdir}/lv2/*

%changelog
* Tue Jan 13 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial build
