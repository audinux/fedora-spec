# Kernel major version
%define kmaj  5
# Kernel minor version
%define kmin  10
# Kernel patch version
%define kpat  56
# RT patch version
%define krt   49
# package version
%define krel  11

%define kver  %{kmaj}.%{kmin}.%{kpat}
%define fcver %{dist}.%{_arch}

Name:    kernel-rt-mao
Summary: The Linux Real Time Kernel
Version: %{kver}.rt%{krt}
Release: %{krel}%{?dist}
License: GPL
Group:   System Environment/Kernel
URL:     http://www.kernel.org

Vendor:       Audinux
Distribution: Audinux

Source0: https://cdn.kernel.org/pub/linux/kernel/v%{kmaj}.x/linux-%{kver}.tar.gz
Source1: kernel-config-%{kmaj}.%{kmin}

Patch0: https://mirrors.edge.kernel.org/pub/linux/kernel/projects/rt/%{kmaj}.%{kmin}/older/patch-%{kver}-rt%{krt}.patch.gz

BuildRequires: openssl-devel
BuildRequires: openssl
BuildRequires: kmod
BuildRequires: patch
BuildRequires: bash
BuildRequires: tar
BuildRequires: bzip2
BuildRequires: xz
BuildRequires: findutils
BuildRequires: gzip
BuildRequires: m4
BuildRequires: perl-interpreter
BuildRequires: perl-Carp
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: make
BuildRequires: diffutils
BuildRequires: gawk
BuildRequires: gcc
BuildRequires: binutils
BuildRequires: redhat-rpm-config
BuildRequires: bison
BuildRequires: flex
BuildRequires: net-tools
BuildRequires: hostname
BuildRequires: bc
BuildRequires: elfutils-devel
BuildRequires: rpm-build
BuildRequires: rpm
BuildRequires: elfutils
BuildRequires: elfutils-libelf-devel
BuildRequires: grub2-tools
BuildRequires: sed
BuildRequires: rsync
BuildRequires: dwarves

Provides: kernel = %{version}
Provides: kernel-rt-mao = %{version}

%define __spec_install_post /usr/lib/rpm/brp-compress || :
%define debug_package %{nil}

%description
The Linux Real Time Kernel, the operating system core itself

%package headers
Summary: Header files for the Linux real time kernel for use by glibc
Group: Development/System

%description headers
Kernel-headers includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.  The
header files define structures and constants that are needed for
building most standard programs and are also needed for rebuilding the
glibc package.

%package devel
Summary: Development package for building real time kernel modules to match the %{version} kernel
Group: System Environment/Kernel
AutoReqProv: no

%description devel
This package provides real time kernel headers and makefiles sufficient to build modules
against the %{version} kernel package.

%prep
%autosetup -p1 -n linux-%{kver}

cp %{SOURCE1} .config
sed -i -e "s/EXTRAVERSION =/EXTRAVERSION = -rt%{krt}%{fcver}/g" Makefile
echo "" > localversion-rt

make oldconfig

%build

make clean && make %{?_smp_mflags}

%install

KBUILD_IMAGE=$(make image_name)

%ifarch ia64
  mkdir -p $RPM_BUILD_ROOT/boot/efi $RPM_BUILD_ROOT/lib/modules
%else
  mkdir -p $RPM_BUILD_ROOT/boot     $RPM_BUILD_ROOT/lib/modules
%endif

make %{?_smp_mflags} INSTALL_MOD_PATH=$RPM_BUILD_ROOT KBUILD_SRC= mod-fw= INSTALL_MOD_STRIP=1 CONFIG_MODULE_COMPRESS=1 CONFIG_MODULE_COMPRESS_XZ=1 modules_install

# We estimate the size of the initramfs because rpm needs to take this size
# into consideration when performing disk space calculations. (See bz #530778)
dd if=/dev/zero of=$RPM_BUILD_ROOT/boot/initramfs-%{kver}-rt%{krt}%{fcver}.img bs=1M count=20

%ifarch ia64
  cp $KBUILD_IMAGE $RPM_BUILD_ROOT/boot/efi/vmlinuz-%{kver}-rt%{krt}%{fcver}
  chmod a+x $RPM_BUILD_ROOT/boot/efi/vmlinuz-%{kver}-rt%{krt}%{fcver}
  ln -s efi/vmlinuz-%{kver}-%{krt}%{fcver} $RPM_BUILD_ROOT/boot/
%else
  cp $KBUILD_IMAGE $RPM_BUILD_ROOT/boot/vmlinuz-%{kver}-rt%{krt}%{fcver}
  chmod a+x $RPM_BUILD_ROOT/boot/vmlinuz-%{kver}-rt%{krt}%{fcver}
%endif

make %{?_smp_mflags} INSTALL_HDR_PATH=$RPM_BUILD_ROOT/usr KBUILD_SRC= headers_install
cp System.map $RPM_BUILD_ROOT/boot/System.map-%{kver}-rt%{krt}%{fcver}
cp .config    $RPM_BUILD_ROOT/boot/config-%{kver}-rt%{krt}%{fcver}

cp $RPM_BUILD_ROOT/boot/vmlinuz-%{kver}-rt%{krt}%{fcver} $RPM_BUILD_ROOT/lib/modules/%{kver}-rt%{krt}%{fcver}/vmlinuz

rm -f $RPM_BUILD_ROOT/lib/modules/%{kver}-rt%{krt}%{fcver}/build
rm -f $RPM_BUILD_ROOT/lib/modules/%{kver}-rt%{krt}%{fcver}/source

mkdir -p $RPM_BUILD_ROOT/lib/modules/%{kver}-rt%{krt}%{fcver}/build
(cd $RPM_BUILD_ROOT/lib/modules/%{kver}-rt%{krt}%{fcver} ; ln -s build source)

# dirs for additional modules per module-init-tools, kbuild/modules.txt
mkdir -p $RPM_BUILD_ROOT/lib/modules/%{kver}-rt%{krt}%{fcver}/extra
mkdir -p $RPM_BUILD_ROOT/lib/modules/%{kver}-rt%{krt}%{fcver}/internal
mkdir -p $RPM_BUILD_ROOT/lib/modules/%{kver}-rt%{krt}%{fcver}/updates

# CONFIG_KERNEL_HEADER_TEST generates some extra files in the process of
# testing so just delete
find . -name *.h.s -delete

# first copy everything
cp --parents `find  -type f -name "Makefile*" -o -name "Kconfig*"` $RPM_BUILD_ROOT/lib/modules/%{kver}-rt%{krt}%{fcver}/build
cp Module.symvers $RPM_BUILD_ROOT/lib/modules/%{kver}-rt%{krt}%{fcver}/build
cp System.map $RPM_BUILD_ROOT/lib/modules/%{kver}-rt%{krt}%{fcver}/build
if [ -s Module.markers ]; then
  cp Module.markers $RPM_BUILD_ROOT/lib/modules/%{kver}-rt%{krt}%{fcver}/build
fi

# Move the devel headers out of the root file system

DevelDir=/usr/src/kernels/%{kver}-rt%{krt}%{fcver}

mkdir -p $RPM_BUILD_ROOT/usr/src/kernels/%{kver}-rt%{krt}%{fcver}
mv $RPM_BUILD_ROOT/lib/modules/%{kver}-rt%{krt}%{fcver}/build $RPM_BUILD_ROOT/$DevelDir

# This is going to create a broken link during the build, but we don't use
# it after this point.  We need the link to actually point to something
# when kernel-devel is installed, and a relative link doesn't work across
# the F17 UsrMove feature.

ln -sf $DevelDir $RPM_BUILD_ROOT/lib/modules/%{kver}-rt%{krt}%{fcver}/build

# prune junk from kernel-devel

find $RPM_BUILD_ROOT/usr/src/kernels -name ".*.cmd" -delete

EXCLUDES="--exclude SCCS --exclude BitKeeper --exclude .svn --exclude CVS --exclude .pc --exclude .hg --exclude .git --exclude .tmp_versions --exclude=*vmlinux* --exclude=*.o --exclude=*.ko --exclude=*.ko.xz --exclude=*.cmd --exclude=Documentation --exclude=firmware --exclude .config.old --exclude .missing-syscalls.d"
tar $EXCLUDES -cf- . | (cd $RPM_BUILD_ROOT/usr/src/kernels/%{kver}-rt%{krt}%{fcver}; tar xvf -)

%clean
rm -rf $RPM_BUILD_ROOT

%post
# Create the initramfs file
/bin/kernel-install add %{kver}-rt%{krt}%{fcver} /lib/modules/%{kver}-rt%{krt}%{fcver}/vmlinuz
grub2-mkconfig -o /boot/grub2/grub.cfg

%postun
/bin/kernel-install remove %{kver}-rt%{krt}%{fcver} /lib/modules/%{kver}-rt%{krt}%{fcver}/vmlinuz
grub2-mkconfig -o /boot/grub2/grub.cfg

%files
%defattr (-, root, root)
/lib/modules/%{kver}-rt%{krt}%{fcver}
/boot/*
%ghost /boot/initramfs-%{kver}-rt%{krt}%{fcver}

%files headers
%defattr (-, root, root)
/usr/include

%files devel
%defattr (-, root, root)
/usr/src/kernels/%{kver}-rt%{krt}%{fcver}

%changelog
* Mon Aug 16 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.56-rt49-11
- update to 5.10.56-rt49-11 - vanilla RT kernel

* Sat Aug 07 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.56-rt48-11
- update to 5.10.56-rt48-11 - vanilla RT kernel

* Fri Jul 23 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.52-rt47-11
- update to 5.10.52-rt47-11 - vanilla RT kernel

* Fri Jul 16 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.47-rt46-11
- update to 5.10.47-rt46-11 - vanilla RT kernel

* Sat Jul 03 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.47-rt45-11
- update to 5.10.47-rt45-11 - vanilla RT kernel

* Sat Jun 05 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.41-rt42-11
- update to 5.10.41-rt42-11 - vanilla RT kernel

* Wed May 12 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.35-rt39-11
- update to 5.10.35-rt39-11 - vanilla RT kernel

* Sat May 08 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.30-rt38-11
- update to 5.10.30-rt38-11 - vanilla RT kernel

* Tue Apr 20 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.30-rt37-11
- update to 5.10.30-rt37-11 - vanilla RT kernel

* Thu Apr 08 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.27-rt36-11
- update to 5.10.27-rt36-11 - vanilla RT kernel

* Wed Mar 24 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.25-rt35-11
- update to 5.10.25-rt35-11 - vanilla RT kernel

* Tue Mar 09 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.21-rt34-11
- update to 5.10.21-rt34-11 - vanilla RT kernel

* Fri Feb 19 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.17-rt32-11
- update to 5.10.17-rt32-11 - vanilla RT kernel

* Tue Feb 16 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.16-rt30-11
- update to 5.10.16-rt30-11 - vanilla RT kernel

* Tue Feb 9 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.14-rt28-11
- update to 5.10.14-rt28-11 - vanilla RT kernel

* Tue Feb 2 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.12-rt26-11
- update to 5.10.12-rt26-11 - vanilla RT kernel

* Tue Jan 19 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.8-rt24-11
- update to 5.10.8-rt24-11 - vanilla RT kernel

* Sat Jan 16 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.4-rt22-11
- update to 5.10.4-rt22-11 - vanilla RT kernel

* Sun Aug 23 2020 Yann Collette <ycollette.nospam@free.fr> - 5.6.19-rt12-11
- update to 5.6.19-rt12-11 - vanilla RT kernel

* Sun Jul 26 2020 Yann Collette <ycollette.nospam@free.fr> - 5.6.19-rt11-11
- update to 5.6.19-rt11-11 - vanilla RT kernel

* Fri Jun 19 2020 Yann Collette <ycollette.nospam@free.fr> - 5.6.17-rt10-11
- update to 5.6.17-rt10-11 - fix preempt option ...

* Tue Jun 16 2020 Yann Collette <ycollette.nospam@free.fr> - 5.6.17-rt10-10
- update to 5.6.17-rt10-10

* Wed Jun 10 2020 Yann Collette <ycollette.nospam@free.fr> - 5.6.17-rt9-10
- update to 5.6.17-rt9-10

* Wed May 27 2020 Yann Collette <ycollette.nospam@free.fr> - 5.6.14-rt7-10
- update to 5.6.14-rt7-10

* Thu May 14 2020 Yann Collette <ycollette.nospam@free.fr> - 5.6.10-rt5-10
- update to 5.6.10-rt5-10

* Sun May 10 2020 Yann Collette <ycollette.nospam@free.fr> - 5.4.39-rt23-10
- update to 5.4.39-rt23-10

* Sun May 10 2020 Yann Collette <ycollette.nospam@free.fr> - 5.4.34-rt21-10
- update to 5.4.34-rt21-10

* Mon Mar 30 2020 Yann Collette <ycollette.nospam@free.fr> - 5.4.28-rt19-10
- update to 5.4.28-rt19-10

* Sat Mar 21 2020 Yann Collette <ycollette.nospam@free.fr> - 5.4.26-rt17-10
- update to 5.4.26-rt17-10

* Sun Mar 8 2020 Yann Collette <ycollette.nospam@free.fr> - 5.4.24-rt15-10
- update to 5.4.24-rt15-10

* Sat Feb 29 2020 Yann Collette <ycollette.nospam@free.fr> - 5.4.22-rt13-10
- update to 5.4.22-rt13-10

* Sat Feb 15 2020 Yann Collette <ycollette.nospam@free.fr> - 5.4.19-rt11-10
- update to 5.4.19-rt11-10

* Fri Feb 7 2020 Yann Collette <ycollette.nospam@free.fr> - 5.4.17-rt9-10
- update to 5.4.17-rt9-10

* Mon Dec 16 2019 Yann Collette <ycollette.nospam@free.fr> - 5.2.21-rt15-9
- update to 5.2.21-rt15-9

* Wed Dec 4 2019 Yann Collette <ycollette.nospam@free.fr> - 5.2.21-rt14-9
- update to 5.2.21-rt14-9

* Sat Oct 19 2019 Yann Collette <ycollette.nospam@free.fr> - 5.2.21-rt13-9
- update to 5.2.21-rt13-9

* Tue Oct 8 2019 Yann Collette <ycollette.nospam@free.fr> - 5.2.19-rt11-9
- update to 5.2.19-rt11-9

* Mon Sep 30 2019 Yann Collette <ycollette.nospam@free.fr> - 5.2.17-rt9-9
- update to 5.2.17-rt9-9

* Sat Sep 14 2019 Yann Collette <ycollette.nospam@free.fr> - 5.2.14-rt7-9
- update to 5.2.14-rt7-9

* Tue Aug 27 2019 Yann Collette <ycollette.nospam@free.fr> - 5.2.10-rt5-9
- update to 5.2.10-rt5-9

* Sun Aug 18 2019 Yann Collette <ycollette.nospam@free.fr> - 5.2.9-rt3-9
- update to 5.2.9-rt3-9

* Sat Aug 17 2019 Yann Collette <ycollette.nospam@free.fr> - 5.0.21-rt16-9
- update to 5.0.21-rt16-9 - fix a radeon / dma bug

* Thu Jul 4 2019 Yann Collette <ycollette.nospam@free.fr> - 5.0.21-rt15-8
- update to 5.0.21-rt15-8

* Wed Jun 26 2019 Yann Collette <ycollette.nospam@free.fr> - 5.0.21-rt14-8
- update to 5.0.21-rt14-8 - buggy - doesn't boot

* Wed Jun 19 2019 Yann Collette <ycollette.nospam@free.fr> - 5.0.21-rt12-8
- update to 5.0.21-rt12-8

* Sun Jun 9 2019 Yann Collette <ycollette.nospam@free.fr> - 5.0.19-rt11-8
- update to 5.0.19-rt11-8

* Sat May 11 2019 Yann Collette <ycollette.nospam@free.fr> - 5.0.14-rt9-8
- update to 5.0.14-rt9-8

* Mon Apr 29 2019 Yann Collette <ycollette.nospam@free.fr> - 4.19.37-rt19-8
- update to 4.19.37-rt19-8

* Thu Mar 28 2019 Yann Collette <ycollette.nospam@free.fr> - 4.19.31-rt18-8
- update to 4.19.31-rt18-8

* Thu Mar 28 2019 Yann Collette <ycollette.nospam@free.fr> - 4.19.25-rt16-8
- update to 4.19.25-rt16-8

* Fri Mar 1 2019 Yann Collette <ycollette.nospam@free.fr> - 4.19.25-rt16-7
- update to 4.19.25-rt16-7

* Tue Jan 15 2019 Yann Collette <ycollette.nospam@free.fr> - 4.19.15-rt12-7
- update to 4.19.15-rt12-7

* Tue Jan 15 2019 Yann Collette <ycollette.nospam@free.fr> - 4.19.13-rt10-7
- update to 4.19.13-rt10-7 - fix package version

* Thu Jan 10 2019 Yann Collette <ycollette.nospam@free.fr> - 4.19.13-rt10-6
- update to 4.19.13-rt10-6

* Wed Jan 9 2019 Yann Collette <ycollette.nospam@free.fr> - 4.19.13-rt10-5
- update to 4.19.13-rt10-5

* Sun Oct 28 2018 Yann Collette <ycollette.nospam@free.fr> - 4.18.16-rt8-5
- fix kernel install

* Sat Oct 27 2018 Yann Collette <ycollette.nospam@free.fr> - 4.18.16-rt8-4
- add 4.18.16-rt8 kernel

* Wed Oct 10 2018 Yann Collette <ycollette.nospam@free.fr> - 4.18.12-rt7-3
- add 4.18.12-rt7 kernel

* Tue Sep 18 2018 Yann Collette <ycollette.nospam@free.fr> - 4.18.7-rt5-3
- add 4.18.7-rt5 kernel

* Sat Sep 8 2018 Yann Collette <ycollette.nospam@free.fr> - 4.16.18-rt11-3
- add 4.16.18-rt11 kernel

* Sun Jul 22 2018 Yann Collette <ycollette.nospam@free.fr> - 4.16.18-rt10-3
- add 4.16.18-rt10 kernel

* Sat Jun 23 2018 Yann Collette <ycollette.nospam@free.fr> - 4.16.15-rt7-3
- add 4.16.15-rt7 kernel

* Wed Jun 13 2018 Yann Collette <ycollette.nospam@free.fr> - 4.16.12-rt5-3
- fix a huge config problem

* Sun Jun 10 2018 Yann Collette <ycollette.nospam@free.fr> - 4.14.40-2
- add 4.14.40-rt30 kernel (4.16 kernels are xrunning)

* Sun Jun 10 2018 Yann Collette <ycollette.nospam@free.fr> - 4.16.12-rt5-2
- add 4.16.12-rt5 kernel

* Sun Jun 10 2018 Yann Collette <ycollette.nospam@free.fr> - 4.16.8-rt2-2
- add 4.16.8-rt2 kernel
