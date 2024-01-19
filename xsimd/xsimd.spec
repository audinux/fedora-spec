# Tag: Library
# Type: Devel
# Category: Programming

%global github  https://github.com/xtensor-stack/xsimd

Name: xsimd8
Version: 8.1.0
Release: 2%{?dist}
Summary: C++ wrappers for SIMD intrinsics
License: BSD
URL: https://xsimd.readthedocs.io/

Source0: %{github}/archive/%{version}/xsimd-%{version}.tar.gz

# Do not run tests on unsupported architectures
Patch:          %{github}/pull/742.patch

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gtest-devel

%ifarch %{arm}
# Only used for testing, as it's a header-only package.
%global optflags %(echo %{optflags} -mfpu=neon)
%endif

# there is no actual arched content - this is a header only library
%global debug_package %{nil}

# Get Fedora 33++ behavior on anything older
%undefine __cmake_in_source_build

%global _description \
SIMD (Single Instruction, Multiple Data) is a feature of microprocessors that \
has been available for many years. SIMD instructions perform a single operation \
on a batch of values at once, and thus provide a way to significantly \
accelerate code execution. However, these instructions differ between \
microprocessor vendors and compilers. \
 \
xsimd provides a unified means for using these features for library authors. \
Namely, it enables manipulation of batches of numbers with the same arithmetic \
operators as for single values. It also provides accelerated implementation \
of common mathematical functions operating on batches. \

%description %_description

%package devel
Summary: %{summary}
Provides: %{name} = %{version}-%{release}
Provides: %{name}-static = %{version}-%{release}
%description devel %_description

%prep
%autosetup -p1 -n xsimd-%{version}

%build
%cmake -DBUILD_TESTS=ON -DCMAKE_CXX_STANDARD=14
%cmake_build

%install
%cmake_install

%check
# Explicitly not supported upstream for simd mode. Still valuable for scalar mode layer.
%ifnarch ppc64le s390x
%cmake_build -- xtest
%endif

%files devel
%doc README.md
%license LICENSE
%{_includedir}/xsimd/
%{_libdir}/cmake/xsimd/
%{_libdir}/pkgconfig/xsimd.pc

%changelog
* Fri Sep 09 2022 Yann Collette <ycollette dot nospam at free.fr> - 8.1.0-2
- rename this package xsimd8 to ship version 9 of xsimd

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 11 2022 sguelton@redhat.com - 8.1.0-1
- Update to 8.1.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 08 2021 Miro Hrončok <mhroncok@redhat.com> - 8.0.5-1
- Update to 8.0.5
- Fixes rhbz#1997274

* Wed Dec 08 2021 Miro Hrončok <mhroncok@redhat.com> - 8.0.4-1
- Update to 8.0.4

* Mon Aug 09 2021 Miro Hrončok <mhroncok@redhat.com> - 7.6.0-1
- Update to 7.6.0
- Fixes rhbz#1988647

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 23 2021 sguelton@redhat.com - 7.5.0-1
- Update to latest version

* Tue Apr 6 2021 sguelton@redhat.com - 7.4.10-1
- Update to latest version

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 sguelton@redhat.com - 7.4.9-1
- Update to latest version

* Sat Oct 17 2020 sguelton@redhat.com - 7.4.8-2
- Fix missing #include for gcc-11

* Sat Oct 3 2020 sguelton@redhat.com - 7.4.8-1
- Update to latest version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 16 2020 sguelton@redhat.com - 7.4.6-1
- Update to latest version

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 04 2019 Miro Hrončok <mhroncok@redhat.com> - 7.2.3-3
- Allow all architectures

* Wed Jul 03 2019 Miro Hrončok <mhroncok@redhat.com> - 7.2.3-2
- Apply upstream workaround for armv7
- Reenable tests (commented out by mistake)

* Fri Jun 28 2019 Miro Hrončok <mhroncok@redhat.com> - 7.2.3-1
- Initial package
