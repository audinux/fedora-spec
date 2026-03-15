# Status: active
# Tag: Devel
# Type: Devel
# Category: Programming

Name: yaml-cpp03
Version: 0.9.0
Release: 15%{?dist}
Summary: A YAML parser and emitter for C++
License: MIT
URL: https://github.com/jbeder/yaml-cpp/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/jbeder/yaml-cpp/releases/download/yaml-cpp-%{version}/yaml-cpp-yaml-cpp-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc gcc-c++

Provides: yaml-cpp = %{version}-%{release}
Obsoletes: yaml-cpp < 0.3.0-5

%description
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.

This is a compatibility package for version 0.3.


%package devel
Summary: Development files for %{name}
License: MIT
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Requires: boost-devel

Provides: yaml-cpp-devel = %{version}-%{release}
Obsoletes: yaml-cpp-devel < 0.3.0-5

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

This is a compatibility package for version 3.

%prep
%autosetup -c -p1 -n yaml-cpp

%build

# ask cmake to not strip binaries
%cmake -DYAML_CPP_BUILD_TOOLS=0 \
       -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install

%cmake_install

%files
%doc README.md SECURITY.md CONTRIBUTING.md
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/yaml-cpp/*
%{_libdir}/libyaml-cpp.so
%{_libdir}/pkgconfig/yaml-cpp.pc
%{_libdir}/cmake/yaml-cpp/*.cmake

%changelog
* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 0.7.0-15
- update for Fedora 33

* Tue Apr 30 2019 Yann Collette <ycollette.nospam@free.fr> - 0.7.0-14
- update for Fedora 30

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.3.0-12
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 0.3.0-11
- Rebuilt for Boost 1.64

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.0-7
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 30 2013 Richard Shaw <hobbes1069@gmail.com> - 0.3.0-4
- Change package name to yaml-cpp03 per reviewer input.

* Wed Sep  4 2013 Richard Shaw <hobbes1069@gmail.com> - 0.3.0-3
- Add obsoletes/provides for proper upgrade path.
- Fix internal header references to yaml-cpp3.
- Fix pkg-config file to reference yaml-cpp3.

* Mon Aug 26 2013 Richard Shaw <hobbes1069@gmail.com> - 0.3.0-1
- Initial packaging.
