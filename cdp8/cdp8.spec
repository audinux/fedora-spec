# Status: active
# Tag: Tool
# Type: Standalone
# Category: Tool

%global commit0 9cd1c6bf883fd104e494ca4f7ed1fd346483c3c5

Name: cdp
Version: 8.0
Release: 1%{?dist}
Summary: New version of CDP software 
License: LGPL-2.1
URL: https://composersdesktop.com/index.html
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ComposersDesktop/CDP8/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz
Source1: https://www.composersdesktop.com/pdf/CDPWorkshop1infopg.pdf
Source2: https://www.composersdesktop.com/pdf/CDPWorkshop2infopg.pdf
Source3: https://www.composersdesktop.com/pdf/CDPWorkshop3infopg.pdf
Source4: https://www.composersdesktop.com/downloads/CDPDocs_PDF.zip
Source5: https://www.composersdesktop.com/downloads/cdpguide.zip
Patch0: cdp8-0001-fix-cmake-flags.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: unzip

%description
New version of CDP software.
Discover new musical possibilities with CDP, a mature and wide-ranging suite of sound-manipulation programs:
- CDP has hundreds of processes covering nearly every aspect of creative sound design.
- CDP's emphasis is on transforming existing sounds to create new ones in the tradition of musique concrète.

%package doc
Summary: Documentation for %{name}
License: LGPL-2.1

%description doc
Documentation for %{name}

%prep
%autosetup -p1 -n CDP8-%{commit0}

%build

%set_build_flags
export CFLAGS=`echo $CFLAGS | sed -e "s/-Werror=format-security//g"`
export CXXFLAGS=`echo $CXXFLAGS | sed -e "s/-Werror=format-security//g"`

%cmake -DCMAKE_CXX_FLAGS="-fPIC $CXXFLAGS" \
       -DCMAKE_C_FLAGS="-fPIC $CFLAGS" \
       -DUSE_COMPILER_OPTIMIZATIONS=OFF \
       -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install

%cmake_install

# Install documentation
mkdir -p %{buildroot}/%{_datadir}/%{name}/docs/pdf/
install -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/%{name}/docs/pdf/
install -m 644 %{SOURCE2} %{buildroot}/%{_datadir}/%{name}/docs/pdf/
install -m 644 %{SOURCE3} %{buildroot}/%{_datadir}/%{name}/docs/pdf/

install -m 644 %{SOURCE4} %{buildroot}/%{_datadir}/%{name}/docs/pdf/
install -m 644 %{SOURCE5} %{buildroot}/%{_datadir}/%{name}/docs/pdf/
pushd %{buildroot}/%{_datadir}/%{name}/docs/pdf/
unzip %{SOURCE4}
unzip %{SOURCE5}
popd

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files doc
%{_datadir}/%{name}/docs/pdf/*

%changelog
* Mon May 18 2026 Yann Collette <ycollette.nospam@free.fr> - 8.0-1
- initial version of the spec
