# Tag: Jack, Alsa
# Type: Standalone, Language
# Category: Audio, Programming

Name:    bipscript
Version: 0.18
Release: 1%{?dist}
Summary: Audio language
URL:     https://www.bipscript.org/
License: GPLv2+

Vendor:       Audinux
Distribution: Audinux

# original tarfile can be found here:
Source0: https://gitlab.domainepublic.net/bipscript/bipscript/-/archive/v%{version}/bipscript-v%{version}.tar.gz
Source1: https://gitlab.domainepublic.net/bipscript/examples/-/archive/v%{version}/examples-%{version}.tar.gz
Source2: https://gitlab.domainepublic.net/bipscript/apidocs/-/archive/v%{version}/apidocs-v%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: lilv-devel
BuildRequires: lv2-devel
BuildRequires: fftw-devel
BuildRequires: liblo-devel
BuildRequires: portsmf-devel
BuildRequires: libsndfile-devel
BuildRequires: boost-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel
BuildRequires: libatomic

%description
Bipscript is a scripting language for creating music.

%package doc
Summary: Documentation for %{name}
License: GPLv2+
Requires: %{name}

%description doc
Documentation for %{name}

%package examples
Summary: Examples for %{name}
License: GPLv2+
Requires: %{name}

%description examples
Examples for %{name}

%prep
%autosetup -n %{name}-v%{version}

mkdir examples && tar xvfz %{SOURCE1} -C examples --strip-components 1
mkdir apidocs && tar xvfz %{SOURCE2} -C apidocs --strip-components 1

%build

%set_build_flags
export CFLAGS="$CFLAGS -fPIC"
export CXXFLAGS="$CXXFLAGS -include cstdint -include map -fPIC"

%cmake
%cmake_build

%install

%cmake_install

install -m 755 -d %{buildroot}/%{_datadir}/bipscript/examples/
cp -ra examples/src/* %{buildroot}/%{_datadir}/bipscript/examples/

install -m 755 -d %{buildroot}/%{_datadir}/bipscript/apidocs/
cp -ra apidocs/en %{buildroot}/%{_datadir}/bipscript/apidocs/

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%dir %{_datadir}/bipscript/

%files doc
%{_datadir}/bipscript/apidocs/

%files examples
%{_datadir}/bipscript/examples/

%changelog
* Fri Mar 31 2023 Yann Collette <ycollette.nospam@free.fr> - 0.18-1
- update to 0.18-1

* Mon Mar 14 2022 Yann Collette <ycollette.nospam@free.fr> - 0.16-1
- update to 0.16-1

* Sat Jan 15 2022 Yann Collette <ycollette.nospam@free.fr> - 0.15-1
- update to 0.15-1

* Wed Oct 13 2021 Yann Collette <ycollette.nospam@free.fr> - 0.14-1
- update to 0.14-1

* Sat Jul 17 2021 Yann Collette <ycollette.nospam@free.fr> - 0.13-1
- update to 0.13-1

* Sat Apr 17 2021 Yann Collette <ycollette.nospam@free.fr> - 0.12-1
- Initial build
