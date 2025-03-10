# Status: active
# Tag: Tool
# Type: Devel, Plugin, CLAP
# Category: Tool

%global debug_package %{nil}

Summary: An automatic CLAP validation and testing tool
Name: clap-validator
Version: 0.3.2
Release: 1%{?dist}
License: MIT
URL: https://github.com/free-audio/clap-validator
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/free-audio/clap-validator/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: rustup

%description
A validator and automatic test suite for CLAP plugins.
Clap-validator can automatically test one or more plugins for common bugs and incorrect behavior.

%prep
%autosetup -n %{name}-%{version}

%build

export RUSTFLAGS="-g -O"

export CWD=`pwd`
export RUSTUP_HOME="$CWD/rustup"
export CARGO_HOME="$CWD/cargo"

#%ifarch x86_64
#rustup-init -y --no-modify-path --default-toolchain nightly-x86_64-unknown-linux-gnu
#%endif
#%ifarch aarch64
#rustup-init -y --no-modify-path --default-toolchain nightly-aarch64-unknown-linux-gnu
#%endif

%ifarch x86_64
rustup-init -y --no-modify-path --default-toolchain 1.76.0-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --no-modify-path --default-toolchain 1.76.0-aarch64-unknown-linux-gnu
%endif

source cargo/env

cargo build --release

%install

install -m 755 -d %{buildroot}/%{_bindir}/
cp target/release/clap-validator %{buildroot}/%{_bindir}/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%changelog
* Mon Jan 22 2024 Yann Collette <ycollette dot nospam at free.fr> 0.3.2-1
- initial release
