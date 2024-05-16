# Kernel major version
%define kmaj  5
# Kernel minor version
%define kmin  15
# Kernel patch version
%define kpat  85
# RT patch version
%define krt   55
# package version
%define krel  1

%define kver  %{kmaj}.%{kmin}.%{kpat}
%define fcver %{dist}.%{_arch}

Name:    kernel-rt-stable-mao
Summary: The Linux Real Time Kernel
Version: %{kver}.rt%{krt}
Release: %{krel}%{?dist}
License: GPL
URL:     http://www.kernel.org
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://cdn.kernel.org/pub/linux/kernel/v%{kmaj}.x/linux-%{kver}.tar.gz
Source1: kernel-config-%{kmaj}.%{kmin}
Patch0:  https://mirrors.edge.kernel.org/pub/linux/kernel/projects/rt/%{kmaj}.%{kmin}/older/patch-%{kver}-rt%{krt}.patch.gz

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
BuildRequires: zlib-devel
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

%description headers
Kernel-headers includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.  The
header files define structures and constants that are needed for
building most standard programs and are also needed for rebuilding the
glibc package.

%package devel
Summary: Development package for building real time kernel modules to match the %{version} kernel
AutoReqProv: no

%description devel
This package provides real time kernel headers and makefiles sufficient to build modules
against the %{version} kernel package.

%prep
%autosetup -p1 -n linux-%{kver}

cp %{SOURCE1} .config
sed -i -e "s/EXTRAVERSION =/EXTRAVERSION = -rt-stable%{krt}%{fcver}/g" Makefile
echo "" > localversion-rt

make oldconfig

%build

make clean && make %{?_smp_mflags}

%install

KBUILD_IMAGE=$(make image_name)

%ifarch ia64
  mkdir -p %{buildroot}/boot/efi %{buildroot}/lib/modules
%else
  mkdir -p %{buildroot}/boot     %{buildroot}/lib/modules
%endif

make %{?_smp_mflags} INSTALL_MOD_PATH=%{buildroot} KBUILD_SRC= mod-fw= INSTALL_MOD_STRIP=1 CONFIG_MODULE_COMPRESS=1 CONFIG_MODULE_COMPRESS_XZ=1 modules_install

# We estimate the size of the initramfs because rpm needs to take this size
# into consideration when performing disk space calculations. (See bz #530778)
dd if=/dev/zero of=%{buildroot}/boot/initramfs-%{kver}-rt-stable%{krt}%{fcver}.img bs=1M count=20

%ifarch ia64
  cp $KBUILD_IMAGE %{buildroot}/boot/efi/vmlinuz-%{kver}-rt-stable%{krt}%{fcver}
  chmod a+x %{buildroot}/boot/efi/vmlinuz-%{kver}-rt-stable%{krt}%{fcver}
  ln -s efi/vmlinuz-%{kver}-stable-%{krt}%{fcver} %{buildroot}/boot/
%else
  cp $KBUILD_IMAGE %{buildroot}/boot/vmlinuz-%{kver}-rt-stable%{krt}%{fcver}
  chmod a+x %{buildroot}/boot/vmlinuz-%{kver}-rt-stable%{krt}%{fcver}
%endif

make %{?_smp_mflags} INSTALL_HDR_PATH=%{buildroot}/usr KBUILD_SRC= headers_install
cp System.map %{buildroot}/boot/System.map-%{kver}-rt-stable%{krt}%{fcver}
cp .config    %{buildroot}/boot/config-%{kver}-rt-stable%{krt}%{fcver}

cp %{buildroot}/boot/vmlinuz-%{kver}-rt-stable%{krt}%{fcver} %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/vmlinuz

rm -f %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/build
rm -f %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/source

mkdir -p %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/build
(cd %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver} ; ln -s build source)

# dirs for additional modules per module-init-tools, kbuild/modules.txt
mkdir -p %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/extra
mkdir -p %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/internal
mkdir -p %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/updates

# CONFIG_KERNEL_HEADER_TEST generates some extra files in the process of
# testing so just delete
find . -name *.h.s -delete

# first copy everything
cp --parents `find  -type f -name "Makefile*" -o -name "Kconfig*"` %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/build
cp Module.symvers %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/build
cp System.map %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/build
if [ -s Module.markers ]; then
  cp Module.markers %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/build
fi

# Move the devel headers out of the root file system

DevelDir=/usr/src/kernels/%{kver}-rt-stable%{krt}%{fcver}

mkdir -p %{buildroot}/usr/src/kernels/%{kver}-rt-stable%{krt}%{fcver}
mv %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/build %{buildroot}/$DevelDir

# This is going to create a broken link during the build, but we don't use
# it after this point.  We need the link to actually point to something
# when kernel-devel is installed, and a relative link doesn't work across
# the F17 UsrMove feature.

ln -sf $DevelDir %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/build

# prune junk from kernel-devel

find %{buildroot}/usr/src/kernels -name ".*.cmd" -delete

EXCLUDES="--exclude SCCS --exclude BitKeeper --exclude .svn --exclude CVS --exclude .pc --exclude .hg --exclude .git --exclude .tmp_versions --exclude=*vmlinux* --exclude=*.o --exclude=*.ko --exclude=*.ko.xz --exclude=*.cmd --exclude=Documentation --exclude=firmware --exclude .config.old --exclude .missing-syscalls.d"
tar $EXCLUDES -cf- . | (cd %{buildroot}/usr/src/kernels/%{kver}-rt-stable%{krt}%{fcver}; tar xvf -)

%post
# Create the initramfs file
/bin/kernel-install add %{kver}-rt-stable%{krt}%{fcver} /lib/modules/%{kver}-rt-stable%{krt}%{fcver}/vmlinuz
grub2-mkconfig -o /boot/grub2/grub.cfg

%postun
/bin/kernel-install remove %{kver}-rt-stable%{krt}%{fcver} /lib/modules/%{kver}-rt-stable%{krt}%{fcver}/vmlinuz
grub2-mkconfig -o /boot/grub2/grub.cfg

%files
%defattr (-, root, root)
/lib/modules/%{kver}-rt-stable%{krt}%{fcver}
/boot/*
%ghost /boot/initramfs-%{kver}-rt-stable%{krt}%{fcver}

%files headers
%defattr (-, root, root)
/usr/include

%files devel
%defattr (-, root, root)
/usr/src/kernels/%{kver}-rt-stable%{krt}%{fcver}

%changelog
* Thu Dec 29 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.85-rt55-1
- update to 5.15.85-rt55-1 - vanilla RT kernel
