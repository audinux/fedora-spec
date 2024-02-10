# Tag: Effect
# Type: Plugin, CLAP
# Category: Audio, Effect

%define commit0 3782ff63dd11ac7cba13bd642cd222e8000877b5
%define _lto_cflags %{nil}

Summary: Example clap plugins
Name: clap-plugins
Version: 1.0.1
Release: 1%{?dist}
License: MIT
URL: https://github.com/free-audio/clap-plugins

Vendor:       Audinux
Distribution: Audinux

# ./clap-source.sh <project> <tag>
# ./clap-source.sh clap-plugins 3782ff63dd11ac7cba13bd642cd222e8000877b5

Source0: clap-plugins.tar.gz
Source1: clap-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake

%description
Example Clap Plugins

%prep
%autosetup -n %{name}

%build

%set_build_flags
export CXXFLAGS="-fPIC $CXXFLAGS"
export CFLAGS="-fPIC $CFLAGS"

%cmake
%cmake_build -- -j1

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_libndir}/clap/*

%changelog
* Mon Jan 22 2024 Yann Collette <ycollette dot nospam at free.fr> 1.0.1-1
- initial release
