# Tag: Synthesizer
# Type: Plugin, CLAP
# Category: Synthesizer

%global debug_package %{nil}

Summary: Frequency modulation synthesizer plugin
Name: octasine
Version: 0.9.0
Release: 1%{?dist}
License: AGPL-3.0-only
URL: https://github.com/greatest-ape/OctaSine
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/greatest-ape/OctaSine/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: rust cargo
BuildRequires: python3
BuildRequires: libglvnd-devel
BuildRequires: libXcursor-devel
BuildRequires: xcb-util-wm-devel

%description
Frequency modulation synthesizer plugin

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  AGPL-3.0-only
Requires: %{name}

%description -n vst-%{name}
VST2 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  AGPL-3.0-only
Requires: %{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n OctaSine-%{version}

%build

export RUSTFLAGS="-g -O"
export RUST_BACKTRACE=1

cargo xtask bundle octasine --release --features clap
cargo xtask bundle octasine --release --features vst2

%install

install -m 755 -d %{buildroot}/%{_libdir}/vst/
cp target/bundled/octasine.so %{buildroot}/%{_libdir}/vst/

install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp target/bundled/octasine.clap %{buildroot}/%{_libdir}/clap/

%files
%doc README.md
%license LICENSE

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Tue Jan 23 2024 Yann Collette <ycollette dot nospam at free.fr> 0.9.0-1
- initial release
