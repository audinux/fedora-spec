%global realname yaml-cpp

Name:           yaml-cpp03
Version:        0.3.0
Release:        15%{?dist}
Summary:        A YAML parser and emitter for C++
License:        MIT
URL:            http://code.google.com/p/yaml-cpp/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0:        http://yaml-cpp.googlecode.com/files/%{realname}-%{version}.tar.gz
Patch0:         yaml-cpp03-pkgconf.patch

BuildRequires:  cmake
BuildRequires:  gcc gcc-c++

Provides:       yaml-cpp = %{version}-%{release}
Obsoletes:      yaml-cpp < 0.3.0-5

%description
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.

This is a compatibility package for version 0.3.


%package        devel
Summary:        Development files for %{name}
License:        MIT
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       boost-devel

Provides:       yaml-cpp-devel = %{version}-%{release}
Obsoletes:      yaml-cpp-devel < 0.3.0-5

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

This is a compatibility package for version 3.


%prep
%autosetup -p1 -n %{realname}

# Fix eol
sed -i 's/\r//' license.txt

%build

# ask cmake to not strip binaries
%cmake -DYAML_CPP_BUILD_TOOLS=0
%cmake_build

%install

%cmake_install
#find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Move things as to not conflict with the main package
mv %{buildroot}%{_includedir}/yaml-cpp %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_libdir}/libyaml-cpp.so %{buildroot}%{_libdir}/lib%{name}.so
mv %{buildroot}%{_libdir}/pkgconfig/yaml-cpp.pc \
   %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

# Correct paths in yaml headers
for header in %{buildroot}%{_includedir}/%{name}/*.h; do
    sed -i "s|#include \"yaml-cpp|#include \"%{name}|g" $header
done

%files
%doc license.txt
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

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
