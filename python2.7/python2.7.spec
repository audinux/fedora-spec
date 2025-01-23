# ======================================================
# Conditionals and other variables controlling the build
# ======================================================

# Note that the bcond macros are named for the CLI option they create.
# "%%bcond_without" means "ENABLE by default and create a --without option"

# Whether to use RPM build wheels from the python-{pip,setuptools}-wheel package
# Uses upstream bundled prebuilt wheels otherwise
# setuptools >= 45.0 no longer support Python 2.7, hence disabled
%bcond_with rpmwheels

# Run the test suite in %%check
%bcond_without tests

# Simplify dependencis for Flatpaks that include Python-2.7
%if 0%{?flatpak}
%bcond_with tkinter
%else
%bcond_without tkinter
%endif

%global unicode ucs4
%global pybasever 2.7
%global pyshortver 27
%global pylibdir %{_libdir}/python%{pybasever}
%global tools_dir %{pylibdir}/Tools
%global demo_dir %{pylibdir}/Demo
%global doc_tools_dir %{pylibdir}/Doc/tools
%global dynload_dir %{pylibdir}/lib-dynload
%global site_packages %{pylibdir}/site-packages

# Python's configure script defines SOVERSION, and this is used in the Makefile
# to determine INSTSONAME, the name of the libpython DSO:
#   LDLIBRARY='libpython$(VERSION).so'
#   INSTSONAME="$LDLIBRARY".$SOVERSION
# We mirror this here in order to make it easier to add the -gdb.py hooks.
# (if these get out of sync, the payload of the libs subpackage will fail
# and halt the build)
%global py_SOVERSION 1.0
%global py_INSTSONAME_optimized libpython%{pybasever}.so.%{py_SOVERSION}
%global py_INSTSONAME_debug     libpython%{pybasever}_d.so.%{py_SOVERSION}

%global with_huntrleaks 0
%global with_gdb_hooks 1
%global with_systemtap 1
%global with_valgrind 0
%global with_gdbm 1

# Disable automatic bytecompilation. The python2.7 binary is not yet
# available in /usr/bin when Python is built. Also, the bytecompilation fails
# on files that test invalid syntax.
%global __brp_python_bytecompile %{nil}
%global regenerate_autotooling_patch 0

# https://fedoraproject.org/wiki/Changes/Package_information_on_ELF_objects
# https://bugzilla.redhat.com/2043092
# The default %%build_ldflags macro contains a reference to a file that only
# exists in the builddir of this very package.
# The flag is stored in distutils/sysconfig and is used to build extension modules.
# As a result, 3rd party extension modules cannot be built,
# because the file does not exist when this package is installed.
# Python 3 solves this by using %%extension_ldflags in LDFLAGS_NODIST,
# however Python 2 does not support LDFLAGS_NODIST, so we opt-out completely.
# The exact opt-out mechanism is still not finalized, so we use all of them:
%undefine _package_note_flags
%undefine _package_note_file
%undefine _generate_package_note_file

# ==================
# Top-level metadata
# ==================
Summary: Version %{pybasever} of the Python interpreter
Name: python%{pybasever}
URL: https://www.python.org/

%global general_version %{pybasever}.18
#global prerel ...
%global upstream_version %{general_version}%{?prerel}
Version: %{general_version}%{?prerel:~%{prerel}}
Release: 43%{?dist}
%if %{with rpmwheels}
License: Python
%else
# Python is Python
# setuptools is MIT and bundles:
#   packaging: BSD or ASL 2.0
#   pyparsing: MIT
#   six: MIT
# pip is MIT and bundles:
#   appdirs: MIT
#   distlib: Python
#   distro: ASL 2.0
#   html5lib: MIT
#   six: MIT
#   colorama: BSD
#   CacheControl: ASL 2.0
#   msgpack-python: ASL 2.0
#   lockfile: MIT
#   progress: ISC
#   ipaddress: Python
#   packaging: ASL 2.0 or BSD
#   pep517: MIT
#   pyparsing: MIT
#   pytoml: MIT
#   retrying: ASL 2.0
#   requests: ASL 2.0
#   chardet: LGPLv2
#   idna: BSD
#   urllib3: MIT
#   certifi: MPLv2.0
#   setuptools: MIT
#   webencodings: BSD
License: Python and MIT and ASL 2.0 and BSD and ISC and LGPLv2 and MPLv2.0 and (ASL 2.0 or BSD)
%endif

# Python 2 is deprecated in Fedora 30+, see:
#   https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal
# This means that new packages MUST NOT depend on python2, even transitively
#   see: https://fedoraproject.org/wiki/Packaging:Deprecating_Packages
# Python 2 will not be supported after 2019. Use the python3 package instead
# if possible.
Provides: deprecated()

# This package was renamed from python27 in Fedora 33
Provides:  python%{pyshortver} = %{version}-%{release}
Obsoletes: python%{pyshortver} < %{version}-%{release}

# People might want to dnf install python2 instead of pythonXY
Provides: python2 = %{version}-%{release}

# We want to be nice for the packages that still remain, so we keep providing this
# TODO stop doing this in undefined future
Provides: python(abi) = %{pybasever}

# To test the python27 without disrupting everything, we keep providing the devel part until mid September 2019
Provides: python2-devel = %{version}-%{release}
%if %{with tkinter}
Provides: python2-tkinter = %{version}-%{release}
%endif


# =======================
# Build-time requirements
# =======================

# (keep this list alphabetized)

BuildRequires: autoconf
BuildRequires: bluez-libs-devel
BuildRequires: bzip2
BuildRequires: bzip2-devel
BuildRequires: expat-devel
BuildRequires: findutils
BuildRequires: gcc-c++
BuildRequires: glibc-all-langpacks
BuildRequires: glibc-devel
BuildRequires: gmp-devel
BuildRequires: libGL-devel
BuildRequires: libX11-devel
BuildRequires: libdb-devel
BuildRequires: libffi-devel
BuildRequires: libnsl2-devel
BuildRequires: libtirpc-devel
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: openssl-devel
BuildRequires: pkgconf-pkg-config
BuildRequires: readline-devel
BuildRequires: sqlite-devel
BuildRequires: tar
%if %{with tkinter}
BuildRequires: tcl-devel
BuildRequires: tix-devel
BuildRequires: tk-devel
%endif
BuildRequires: zlib-devel
BuildRequires: gnupg2
BuildRequires: git-core

%if %{with_gdbm}
# ABI change without soname bump, reverted
BuildRequires: gdbm-devel >= 1:1.13
%endif

%if 0%{?with_systemtap}
BuildRequires: systemtap-sdt-devel
BuildRequires: /usr/bin/dtrace
# (this introduces a circular dependency, in that systemtap-sdt-devel's
# /usr/bin/dtrace is a python script)
%global tapsetdir      /usr/share/systemtap/tapset
%endif # with_systemtap

%if 0%{?with_valgrind}
BuildRequires: valgrind-devel
%endif

%if %{with rpmwheels}
BuildRequires: python-setuptools-wheel < 45
BuildRequires: python-pip-wheel
Requires: python-setuptools-wheel < 45
Requires: python-pip-wheel
%else
Provides: bundled(python2dist(setuptools)) = 41.2.0
Provides: bundled(python2dist(packaging)) = 16.8
Provides: bundled(python2dist(pyparsing)) = 2.2.1
Provides: bundled(python2dist(six)) = 1.10.0

Provides: bundled(python2dist(pip)) = 19.2.3
Provides: bundled(python2dist(appdirs)) = 1.4.3
Provides: bundled(python2dist(CacheControl)) = 0.12.5
Provides: bundled(python2dist(certifi)) = 2019.6.16
Provides: bundled(python2dist(chardet)) = 3.0.4
Provides: bundled(python2dist(colorama)) = 0.4.1
Provides: bundled(python2dist(distlib)) = 0.2.9.post0
Provides: bundled(python2dist(distro)) = 1.4.0
Provides: bundled(python2dist(html5lib)) = 1.0.1
Provides: bundled(python2dist(idna)) = 2.8
Provides: bundled(python2dist(ipaddress)) = 1.0.22
Provides: bundled(python2dist(lockfile)) = 0.12.2
Provides: bundled(python2dist(msgpack)) = 0.6.1
Provides: bundled(python2dist(packaging)) = 19.0
Provides: bundled(python2dist(pep517)) = 0.5.0
Provides: bundled(python2dist(progress)) = 1.5
Provides: bundled(python2dist(pyparsing)) = 2.4.0
Provides: bundled(python2dist(pytoml)) = 0.1.20
Provides: bundled(python2dist(requests)) = 2.22.0
Provides: bundled(python2dist(retrying)) = 1.3.3
Provides: bundled(python2dist(setuptools)) = 41.0.1
Provides: bundled(python2dist(six)) = 1.12.0
Provides: bundled(python2dist(urllib3)) = 1.25.3
Provides: bundled(python2dist(webencodings)) = 0.5.1
%endif

# For /usr/lib64/pkgconfig/
Requires: pkgconf-pkg-config

# The RPM related dependencies bring nothing to a non-RPM Python developer
# But we want them when packages BuildRequire python2-devel
Requires: (python-rpm-macros if rpm-build)
Requires: (python-srpm-macros if rpm-build)
# Remove this no sooner than Fedora 36:
Provides: python2-rpm-macros = 3.9-34
Obsoletes: python2-rpm-macros < 3.9-34

# https://bugzilla.redhat.com/show_bug.cgi?id=1217376
# https://bugzilla.redhat.com/show_bug.cgi?id=1496757
# https://bugzilla.redhat.com/show_bug.cgi?id=1218294
# TODO change to a specific subpackage once available (#1218294)
Requires: (redhat-rpm-config if gcc)

Obsoletes: python2 < %{version}-%{release}
Obsoletes: python2-debug < %{version}-%{release}
Obsoletes: python2-devel < %{version}-%{release}
Obsoletes: python2-libs < %{version}-%{release}
Obsoletes: python2-test < %{version}-%{release}
Obsoletes: python2-tkinter < %{version}-%{release}
Obsoletes: python2-tools < %{version}-%{release}


# =======================
# Source code and patches
# =======================

Source0: %{url}ftp/python/%{general_version}/Python-%{upstream_version}.tar.xz
Source1: %{url}ftp/python/%{general_version}/Python-%{upstream_version}.tar.xz.asc
Source2: %{url}static/files/pubkeys.txt

# Systemtap tapset to make it easier to use the systemtap static probes
# (actually a template; LIBRARY_PATH will get fixed up during install)
# Written by dmalcolm; not yet sent upstream
Source3: libpython.stp

# Example systemtap script using the tapset
# Written by wcohen, mjw, dmalcolm; not yet sent upstream
Source4: systemtap-example.stp

# Another example systemtap script that uses the tapset
# Written by dmalcolm; not yet sent upstream
Source5: pyfuntop.stp

Source6: macros.python2

# Patches for bundled wheels

# Patch for the bundled setuptools wheel for CVE-2024-6345
# Remote code execution via download functions in the package_index module
# Tracking bug: https://bugzilla.redhat.com/show_bug.cgi?id=2297771
# Upstream solution: https://github.com/pypa/setuptools/pull/4332
# Patch simplified because upstream doesn't support SVN anymore.
Source102: setuptools-CVE-2024-6345.patch

# (Patches taken from github.com/fedora-python/cpython)

# 00000 # eb41a89085f19eab30c9e1f22d09102f3dcab7f0
# Modules/Setup.dist is ultimately used by the "makesetup" script to construct
# the Makefile and config.c
#
# Upstream leaves many things disabled by default, to try to make it easy as
# possible to build the code on as many platforms as possible.
#
# TODO: many modules can also now be built by setup.py after the python binary
# has been built; need to assess if we should instead build things there
#
# We patch it downstream as follows:
#   - various modules are built by default by upstream as static libraries;
#   we built them as shared libraries
#   - build the "readline" module (appears to also be handled by setup.py now)
#   - build the nis module (which needs the tirpc library since glibc 2.26)
#   - enable the build of the following modules:
#     - array arraymodule.c     # array objects
#     - cmath cmathmodule.c # -lm # complex math library functions
#     - math mathmodule.c # -lm # math library functions, e.g. sin()
#     - _struct _struct.c       # binary structure packing/unpacking
#     - time timemodule.c # -lm # time operations and variables
#     - operator operator.c     # operator.add() and similar goodies
#     - _weakref _weakref.c     # basic weak reference support
#     - _testcapi _testcapimodule.c    # Python C API test module
#     - _random _randommodule.c # Random number generator
#     - _collections _collectionsmodule.c # Container types
#     - itertools itertoolsmodule.c
#     - strop stropmodule.c
#     - _functools _functoolsmodule.c
#     - _bisect _bisectmodule.c # Bisection algorithms
#     - unicodedata unicodedata.c    # static Unicode character database
#     - _locale _localemodule.c
#     - fcntl fcntlmodule.c     # fcntl(2) and ioctl(2)
#     - spwd spwdmodule.c               # spwd(3)
#     - grp grpmodule.c         # grp(3)
#     - select selectmodule.c   # select(2); not on ancient System V
#     - mmap mmapmodule.c  # Memory-mapped files
#     - _csv _csv.c  # CSV file helper
#     - _socket socketmodule.c  # Socket module helper for socket(2)
#     - _ssl _ssl.c
#     - crypt cryptmodule.c -lcrypt     # crypt(3)
#     - termios termios.c       # Steen Lumholt's termios module
#     - resource resource.c     # Jeremy Hylton's rlimit interface
#     - audioop audioop.c       # Operations on audio samples
#     - imageop imageop.c       # Operations on images
#     - _md5 md5module.c md5.c
#     - _sha shamodule.c
#     - _sha256 sha256module.c
#     - _sha512 sha512module.c
#     - linuxaudiodev linuxaudiodev.c
#     - timing timingmodule.c
#     - _tkinter _tkinter.c tkappinit.c
#     - dl dlmodule.c
#     - gdbm gdbmmodule.c
#     - _bsddb _bsddb.c
#     - binascii binascii.c
#     - parser parsermodule.c
#     - cStringIO cStringIO.c
#     - cPickle cPickle.c
#     - zlib zlibmodule.c
#     - _multibytecodec cjkcodecs/multibytecodec.c
#     - _codecs_cn cjkcodecs/_codecs_cn.c
#     - _codecs_hk cjkcodecs/_codecs_hk.c
#     - _codecs_iso2022 cjkcodecs/_codecs_iso2022.c
#     - _codecs_jp cjkcodecs/_codecs_jp.c
#     - _codecs_kr cjkcodecs/_codecs_kr.c
#     - _codecs_tw cjkcodecs/_codecs_tw.c
Patch0: python-2.7.1-config.patch

# 00001 # 4cc17cbeaa6c5320d44494c14fe4abe479bf186b
# Removes the "-g" option from "pydoc", for some reason; I believe
# (dmalcolm 2010-01-29) that this was introduced in this change:
# - fix pydoc (#68082)
# in 2.2.1-12 as a response to the -g option needing TkInter installed
# (Red Hat Linux 8)
Patch1: 00001-pydocnogui.patch

# 00004 # 81b93bf369d9d67c71beb5449ff0870f8ac15c7d
# Add $(CFLAGS) to the linker arguments when linking the "python" binary
# since some architectures (sparc64) need this (rhbz:199373).
# Not yet filed upstream
Patch4: python-2.5-cflags.patch

# 00006 # bebaf146393db2eb55ea494243a4095ae32eb50d
# Work around a bug in Python' gettext module relating to the "Plural-Forms"
# header (rhbz:252136)
# Related to upstream issues:
#   http://bugs.python.org/issue1448060 and http://bugs.python.org/issue1475523
# though the proposed upstream patches are, alas, different
Patch6: python-2.5.1-plural-fix.patch

# 00007 # 824c01cf0f2ee2f66cdd8373295431c16b809c5c
# This patch was listed in the changelog as:
#  * Fri Sep 14 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-11
#  - fix encoding of sqlite .py files to work around weird encoding problem
#  in Turkish (#283331)
# A traceback attached to rhbz 244016 shows the problem most clearly: a
# traceback on attempting to import the sqlite module, with:
#   "SyntaxError: encoding problem: with BOM (__init__.py, line 1)"
# This seems to come from Parser/tokenizer.c:check_coding_spec
# Our patch changes two source files within sqlite3, removing the
# "coding: ISO-8859-1" specs and character E4 = U+00E4 =
# LATIN SMALL LETTER A WITH DIAERESIS from in ghaering's surname.
#
# It may be that the conversion of "ISO-8859-1" to "iso-8859-1" is thwarted
# by the implementation of "tolower" in the Turkish locale; see:
#   https://bugzilla.redhat.com/show_bug.cgi?id=191096#c9
#
# TODO: Not yet sent upstream, and appears to me (dmalcolm 2010-01-29) that
# it may be papering over a symptom
Patch7: python-2.5.1-sqlite-encoding.patch

# 00010 # 4a21749202ce4e7b8ea716d38c194a997bcf5baa
# FIXME: Lib/ctypes/util.py posix implementation defines a function
# _get_soname(f).  Upstreams's implementation of this uses objdump to read the
# SONAME from a library; we avoid this, apparently to minimize space
# requirements on the live CD:
# (rhbz:307221)
Patch10: 00010-2.7.13-binutils-no-dep.patch

# 00013 # 4f2f7b3152a8c3d28441877567051384f23b3e4b
# Add various constants to the socketmodule (rhbz#436560):
# TODO: these patches were added in 2.5.1-22 and 2.5.1-24 but appear not to
# have been sent upstream yet:
Patch13: python-2.7rc1-socketmodule-constants.patch

# 00014 # 250d635a8481bc3bf729567e135d6d9cb4698199
# Add various constants to the socketmodule (rhbz#436560):
# TODO: these patches were added in 2.5.1-22 and 2.5.1-24 but appear not to
# have been sent upstream yet:
Patch14: python-2.7rc1-socketmodule-constants2.patch

# 00016 # 7ac402c3d2d7f6cd9b98deb0b7138765d31d105a
# Remove an "-rpath $(LIBDIR)" argument from the linkage args in configure.in:
# FIXME: is this for OSF, not Linux?
Patch16: python-2.6-rpath.patch

# 00017 # c30c4e768942a54dd3a5020c820935f9e2e9fa80
# Fixup distutils/unixccompiler.py to remove standard library path from rpath:
# Adapted from Patch0 in ivazquez' python3000 specfile, removing usage of
# super() as it's an old-style class
Patch17: python-2.6.4-distutils-rpath.patch

# 00055 # 4cde34923ef71a8c32f8fae50630c90645170500
# Systemtap support: add statically-defined probe points
# Patch based on upstream bug: http://bugs.python.org/issue4111
# fixed up by mjw and wcohen for 2.6.2, then fixed up by dmalcolm for 2.6.4
# then rewritten by mjw (attachment 390110 of rhbz 545179), then reformatted
# for 2.7rc1 by dmalcolm:
Patch55: 00055-systemtap.patch

# 00102 # 2242f5aa671eb490b5487dc46dcb05266decfe02
# Only used when "%%%%{_lib}" == "lib64"
# Fixup various paths throughout the build and in distutils from "lib" to "lib64",
# and add the /usr/lib64/pythonMAJOR.MINOR/site-packages to sitedirs, in front of
# /usr/lib/pythonMAJOR.MINOR/site-packages
# Not upstream
Patch102: 00102-2.7.13-lib64.patch

# 00103 # ccade12a68954f5bac4d00153ac92e7eee9c2b34
# Python 2.7 split out much of the path-handling from distutils/sysconfig.py to
# a new sysconfig.py (in r77704).
# We need to make equivalent changes to that new file to ensure that the stdlib
# and platform-specific code go to /usr/lib64 not /usr/lib, on 64-bit archs:
Patch103: python-2.7-lib64-sysconfig.patch

# 00104 # dc327f751c4f4ad6c2e7ad338e97a8a1e0650b60
# Only used when "%%%%{_lib}" == "lib64"
# Another lib64 fix, for distutils/tests/test_install.py; not upstream:
Patch104: 00104-lib64-fix-for-test_install.patch

# 00111 # 3dd8cb916b10ea83c0c7d690cf3c7512394a7f66
# Patch the Makefile.pre.in so that the generated Makefile doesn't try to build
# a libpythonMAJOR.MINOR.a (bug 550692):
# Downstream only: not appropriate for upstream
Patch111: 00111-no-static-lib.patch

# 00112 # 1676b155da8dcacc21fd20006105e3c164a6c5de
# Patch to support building both optimized vs debug stacks DSO ABIs, sharing
# the same .py and .pyc files, using "_d.so" to signify a debug build of an
# extension module.
#
# Based on Debian's patch for the same,
#  http://patch-tracker.debian.org/patch/series/view/python2.6/2.6.5-2/debug-build.dpatch
#
# (which was itself based on the upstream Windows build), but with some
# changes:
#
#   * Debian's patch to dynload_shlib.c looks for module_d.so, then module.so,
# but this can potentially find a module built against the wrong DSO ABI.  We
# instead search for just module_d.so in a debug build
#
#   * We remove this change from configure.in's build of the Makefile:
#   SO=$DEBUG_EXT.so
# so that sysconfig.py:customize_compiler stays with shared_lib_extension='.so'
# on debug builds, so that UnixCCompiler.find_library_file can find system
# libraries (otherwise "make sharedlibs" fails to find system libraries,
# erroneously looking e.g. for "libffi_d.so" rather than "libffi.so")
#
#   * We change Lib/distutils/command/build_ext.py:build_ext.get_ext_filename
# to add the _d there, when building an extension.  This way, "make sharedlibs"
# can build ctypes, by finding the sysmtem libffi.so (rather than failing to
# find "libffi_d.so"), and builds the module as _ctypes_d.so
#
#   * Similarly, update build_ext:get_libraries handling of Py_ENABLE_SHARED by
# appending "_d" to the python library's name for the debug configuration
#
#   * We modify Modules/makesetup to add the "_d" to the generated Makefile
# rules for the various Modules/*.so targets
#
# This may introduce issues when building an extension that links directly
# against another extension (e.g. users of NumPy?), but seems more robust when
# searching for external libraries
#
#   * We don't change Lib/distutils/command/build.py: build.build_purelib to
# embed plat_specifier, leaving it as is, as pure python builds should be
# unaffected by these differences (we'll be sharing the .py and .pyc files)
#
#   * We introduce DEBUG_SUFFIX as well as DEBUG_EXT:
#     - DEBUG_EXT is used by ELF files (names and SONAMEs); it will be "_d" for
# a debug build
#     - DEBUG_SUFFIX is used by filesystem paths; it will be "-debug" for a
# debug build
#
#   Both will be empty in an optimized build.  "_d" contains characters that
# are valid ELF metadata, but this leads to various ugly filesystem paths (such
# as the include path), and DEBUG_SUFFIX allows these paths to have more natural
# names.  Changing this requires changes elsewhere in the distutils code.
#
#   * We add DEBUG_SUFFIX to PYTHON in the Makefile, so that the two
# configurations build parallel-installable binaries with different names
# ("python-debug" vs "python").
#
#   * Similarly, we add DEBUG_SUFFIX within python-config and
#  python$(VERSION)-config, so that the two configuration get different paths
#  for these.
#
#  See also patch 130 below
Patch112: 00112-2.7.13-debug-build.patch

# 00113 # 9dd9dbc52d40c76002245bdc718f2d09590615bf
# Add configure-time support for the COUNT_ALLOCS and CALL_PROFILE options
# described at http://svn.python.org/projects/python/trunk/Misc/SpecialBuilds.txt
# so that if they are enabled, they will be in that build's pyconfig.h, so that
# extension modules will reliably use them
# Not yet sent upstream
Patch113: 00113-more-configuration-flags.patch

# 00114 # 3cfc26f24a13732fe602a47e389152714b757fd7
# Add flags for statvfs.f_flag to the constant list in posixmodule (i.e. "os")
# (rhbz:553020); partially upstream as http://bugs.python.org/issue7647
# Not yet sent upstream
Patch114: 00114-statvfs-f_flag-constants.patch

# 00121 # 15d7dd7ccf99e88ddc9d858cef57b1c91f6871b2
# Upstream r79310 removed the "Modules" directory from sys.path when Python is
# running from the build directory on POSIX to fix a unit test (issue #8205).
# This seems to have broken the compileall.py done in "make install": it cannot
# find shared library extension modules at this point in the build (sys.path
# does not contain DESTDIR/usr/lib(64)/python-2.7/lib-dynload for some reason),
# leading to the build failing with:
# Traceback (most recent call last):
#   File "/home/david/rpmbuild/BUILDROOT/python-2.7-0.1.rc2.fc14.x86_64/usr/lib64/python2.7/compileall.py", line 17, in <module>
#     import struct
#   File "/home/david/rpmbuild/BUILDROOT/python-2.7-0.1.rc2.fc14.x86_64/usr/lib64/python2.7/struct.py", line 1, in <module>
#    from _struct import *
# ImportError: No module named _struct
# This patch adds the build Modules directory to build path.
Patch121: 00121-add-Modules-to-build-path.patch

# 00128 # cf4b30b7664a016ba6ee399aad8f65588a7efd79
# 2.7.1 (in r84230) added a test to test_abc which fails if python is
# configured with COUNT_ALLOCS, which is the case for our debug build
# (the COUNT_ALLOCS instrumentation keeps "C" alive).
# Not yet sent upstream
Patch128: python-2.7.1-fix_test_abc_with_COUNT_ALLOCS.patch

# 00130 # a1595a504aa3fc712856b20bd0850a13b5755762
# Add "--extension-suffix" option to python-config and python-debug-config
# (rhbz#732808)
#
# This is adapted from 3.2's PEP-3149 support.
#
# Fedora's debug build has some non-standard features (see also patch 112
# above), though largely shared with Debian/Ubuntu and Windows
#
# In particular, SO in the Makefile is currently always just ".so" for our
# python 2 optimized builds, but for python 2 debug it should be '_d.so', to
# distinguish the debug vs optimized ABI, following the pattern in the above
# patch.
#
# Not yet sent upstream
Patch130: python-2.7.2-add-extension-suffix-to-python-config.patch

# 00131 # aa81f736a8d7cc4315e920bcec3cb5883c67034b
# The four tests in test_io built on top of check_interrupted_write_retry
# fail when built in Koji, for ppc and ppc64; for some reason, the SIGALRM
# handlers are never called, and the call to write runs to completion
# (rhbz#732998)
Patch131: 00131-disable-tests-in-test_io.patch

# 00132 # 1ec40c78e547fc449ee22a4dbc52562b89115f40
# Add non-standard hooks to unittest for use in the "check" phase below, when
# running selftests within the build:
#   @unittest._skipInRpmBuild(reason)
# for tests that hang or fail intermittently within the build environment, and:
#   @unittest._expectedFailureInRpmBuild
# for tests that always fail within the build environment
#
# The hooks only take effect if WITHIN_PYTHON_RPM_BUILD is set in the
# environment, which we set manually in the appropriate portion of the "check"
# phase below (and which potentially other python-* rpms could set, to reuse
# these unittest hooks in their own "check" phases)
Patch132: 00132-add-rpmbuild-hooks-to-unittest.patch

# 00133 # 434fef9eec3c579fd1ecc956136c1b7cc0b2ea3f
# "dl" is deprecated, and test_dl doesn't work on 64-bit builds:
Patch133: 00133-skip-test_dl.patch

# 00136 # 2f7c096e92687ca4ab771802f866588242ba9184
# Some tests try to seek on sys.stdin, but don't work as expected when run
# within Koji/mock; skip them within the rpm build:
Patch136: 00136-skip-tests-of-seeking-stdin-in-rpmbuild.patch

# 00137 # ddb14da3b15a1f6cfda5ab94919f624c91294e00
# Some tests within distutils fail when run in an rpmbuild:
Patch137: 00137-skip-distutils-tests-that-fail-in-rpmbuild.patch

# 00138 # c955cda1742fcfc632c8eaf0b50e4bffb199d33a
# Fixup some tests within distutils to work with how debug builds are set up:
Patch138: 00138-fix-distutils-tests-in-debug-build.patch

# 00139 # 38a2e2222cf61623fa5519a652a28537b5cd005d
# ARM-specific: skip known failure in test_float:
#  http://bugs.python.org/issue8265 (rhbz#706253)
Patch139: 00139-skip-test_float-known-failure-on-arm.patch

# 00140 # e5095acfe56937839f02013f9c46cb188784a5b2
# Sparc-specific: skip known failure in test_ctypes:
#  http://bugs.python.org/issue8314 (rhbz#711584)
# which appears to be a libffi bug
Patch140: 00140-skip-test_ctypes-known-failure-on-sparc.patch

# 00142 # bcd487be7de5823edd0017bf6778d5e2a0b06c8d
# Some pty tests fail when run in mock (rhbz#714627):
Patch142: 00142-skip-failing-pty-tests-in-rpmbuild.patch

# 00143 # 87bf5bbe4f0c89ec249ee9707bc03ccc9103406c
# Fix the --with-tsc option on ppc64, and rework it on 32-bit ppc to avoid
# aliasing violations (rhbz#698726)
# Sent upstream as http://bugs.python.org/issue12872
Patch143: 00143-tsc-on-ppc.patch

# 00144 # 7a99684f18ea9fc4c00cd2235c623658af36fc97
# (Optionally) disable the gdbm module:
Patch144: 00144-no-gdbm.patch

# 00147 # c77e8f43adbfb44f0a843f06869a36a37415d389
# Add a sys._debugmallocstats() function
# Based on patch 202 from RHEL 5's python.spec, with updates from rhbz#737198
# Sent upstream as http://bugs.python.org/issue14785
Patch147: 00147-add-debug-malloc-stats.patch

# 00155 # a154c44f2dfb60419cecaa193ef13e7613dbd488
# Avoid allocating thunks in ctypes unless absolutely necessary, to avoid
# generating SELinux denials on "import ctypes" and "import uuid" when
# embedding Python within httpd (rhbz#814391)
Patch155: 00155-avoid-ctypes-thunks.patch

# 00156 # a8d1c46e2ab627c493fdcea6d6ba752d9a7bfa2e
# Recent builds of gdb will only auto-load scripts from certain safe
# locations.  Turn off this protection when running test_gdb in the selftest
# suite to ensure that it can load our -gdb.py script (rhbz#817072):
# Not yet sent upstream
Patch156: 00156-gdb-autoload-safepath.patch

# 00165 # 38fdabaaa8c5d1576a372a22cdae1f17b65a215f
# Backport to Python 2 from Python 3.3 of improvements to the "crypt" module
# adding precanned ways of salting a password (rhbz#835021)
# Based on r88500 patch to py3k from Python 3.3
# plus 6482dd1c11ed, 0586c699d467, 62994662676a, 74a1110a3b50, plus edits
# to docstrings to note that this additional functionality is not standard
# within 2.7
Patch165: 00165-crypt-module-salt-backport.patch

# 00167 # 76aea104d5c20527ea08936fb6f2edbb52a07a46
# Don't run any of the stack navigation tests in test_gdb when Python is
# optimized, since there appear to be many different ways in which gdb can
# fail to read the PyFrameObject* for arbitrary places in the callstack,
# presumably due to compiler optimization (rhbz#912025)
#
# Not yet sent upstream
Patch167: 00167-disable-stack-navigation-tests-when-optimized-in-test_gdb.patch

# 00169 # 8d99c73e801c185674c7aee473d3466a118b566a
# Use SHA-256 rather than implicitly using MD5 within the challenge handling
# in multiprocessing.connection
#
# Sent upstream as http://bugs.python.org/issue17258
# (rhbz#879695)
Patch169: 00169-avoid-implicit-usage-of-md5-in-multiprocessing.patch

# 00170 # 029de09ec004fb47f8cbd978f68759e7b4267a38
# In debug builds, try to print repr() when a C-level assert fails in the
# garbage collector (typically indicating a reference-counting error
# somewhere else e.g in an extension module)
# Backported to 2.7 from a patch I sent upstream for py3k
#   http://bugs.python.org/issue9263  (rhbz#614680)
# hiding the proposed new macros/functions within gcmodule.c to avoid exposing
# them within the extension API.
# (rhbz#850013)
Patch170: 00170-gc-assertions.patch

# 00174 # 149dca2c7ba69102e681d9834ac13c153ca53afc
# Workaround for failure to set up prefix/exec_prefix when running
# an embededed libpython that sets Py_SetProgramName() to a name not
# on $PATH when run from the root directory due to
#   https://fedoraproject.org/wiki/Features/UsrMove
# e.g. cmpi-bindings under systemd (rhbz#817554):
Patch174: 00174-fix-for-usr-move.patch

# 00180 # 7199dba788cff67117e091f6ea84a8e7a98d39fe
# Enable building on ppc64p7
# Not appropriate for upstream, Fedora-specific naming
Patch180: 00180-python-add-support-for-ppc64p7.patch

# 00181 # 4034653bd9e53ead4d73f263d12acf20497b6155
# Allow arbitrary timeout for Condition.wait, as reported in
# https://bugzilla.redhat.com/show_bug.cgi?id=917709
# Upstream doesn't want this: http://bugs.python.org/issue17748
# But we have no better solution downstream yet, and since there is
# no API breakage, we apply this patch.
# Doesn't apply to Python 3, where this is fixed otherwise and works.
Patch181: 00181-allow-arbitrary-timeout-in-condition-wait.patch

# 00185 # b104ec8a02f122cfc5c1bdfe923dfe94a6b5079e
# Makes urllib2 honor "no_proxy" enviroment variable for "ftp:" URLs
# when ftp_proxy is set
Patch185: 00185-urllib2-honors-noproxy-for-ftp.patch

# 00189 # 038b390c478fe336a8ea350972785d317bdbbd53
# Instead of bundled wheels, use our RPM packaged wheels from
# /usr/share/python-wheels
Patch189: 00189-use-rpm-wheels.patch

# 00191 # d6f8cb42773c48c480e0639cc8a57aebbf3a4c76
# Disabling NOOP test as it fails without internet connection
Patch191: 00191-disable-NOOP.patch

# 00193 # 31a84748ead0945648369d3520369cdd508815e8
# Enable loading sqlite extensions. This patch isn't needed for
# python3.spec, since Python 3 has a configuration option for this.
# rhbz#1066708
# Patch provided by John C. Peterson
Patch193: 00193-enable-loading-sqlite-extensions.patch

# 00289 # a923413277ad6331772a93b9daeb85a842ddfc00
# Disable automatic detection for the nis module
# (we handle it it in Setup.dist, see Patch0)
Patch289: 00289-disable-nis-detection.patch

# 00351 # 2ee72df6cc70c914e55da3017244c59c5d2c872c
# Avoid infinite loop when reading specially crafted TAR files using the tarfile module
# (CVE-2019-20907).
# See: https://bugs.python.org/issue39017
Patch351: 00351-cve-2019-20907-fix-infinite-loop-in-tarfile.patch

# 00354 # 73d8baef9f57f26ba97232d116f7220d1801452c
# Reject control chars in HTTP method in httplib.putrequest to prevent
# HTTP header injection
#
# Backported from Python 3.5-3.10 (and adjusted for py2's single-module httplib):
# - https://bugs.python.org/issue39603
# - https://github.com/python/cpython/pull/18485 (3.10)
# - https://github.com/python/cpython/pull/21946 (3.5)
Patch354: 00354-cve-2020-26116-http-request-method-crlf-injection-in-httplib.patch

# 00355 # fde656e7116767a761720970ee750ecda6774e71
# No longer call eval() on content received via HTTP in the CJK codec tests
# Backported from the python3 branches upstream: https://bugs.python.org/issue41944
# Resolves: https://bugzilla.redhat.com/show_bug.cgi?id=1889886
Patch355: 00355-CVE-2020-27619.patch

# 00357 # c4b8cabe4e772e4b8eea3e4dab5de12a3e9b5bc2
# CVE-2021-3177: Replace snprintf with Python unicode formatting in ctypes param reprs
#
# Backport of Python3 commit 916610ef90a0d0761f08747f7b0905541f0977c7:
# https://bugs.python.org/issue42938
# https://github.com/python/cpython/pull/24239
Patch357: 00357-CVE-2021-3177.patch

# 00359 # 0d63bea395d9ba5e281dfbddddd6843cdfc609e5
# CVE-2021-23336: Add `separator` argument to parse_qs; warn with default
#
# Partially backports https://bugs.python.org/issue42967 : [security] Address a web cache-poisoning issue reported in urllib.parse.parse_qsl().
#
# Backported from the python3 branch.
# However, this solution is different than the upstream solution in Python 3.
#
# Based on the downstream solution for python 3.6.13 by Petr Viktorin.
#
# An optional argument seperator is added to specify the separator.
# It is recommended to set it to '&' or ';' to match the application or proxy in use.
# The default can be set with an env variable of a config file.
# If neither the argument, env var or config file specifies a separator, "&" is used
# but a warning is raised if parse_qs is used on input that contains ';'.
Patch359: 00359-CVE-2021-23336.patch

# 00361 # 67d6979a90e1dddf902dd1dc42fef34b80ca325b
# Make python2.7 compatible with OpenSSL 3.0.0
#
# Backported from python3.
#
# Based on https://github.com/tiran/cpython/tree/2.7.18-openssl3
Patch361: 00361-openssl-3-compat.patch

# 00366 # e76b05ea3313854adf80e290c07d5b38fef606bb
# CVE-2021-3733: Fix ReDoS in urllib AbstractBasicAuthHandler
#
# Fix Regular Expression Denial of Service (ReDoS) vulnerability in
# urllib2.AbstractBasicAuthHandler. The ReDoS-vulnerable regex
# has quadratic worst-case complexity and it allows cause a denial of
# service when identifying crafted invalid RFCs. This ReDoS issue is on
# the client side and needs remote attackers to control the HTTP server.
#
# Backported from Python 3 together with another backward-compatible
# improvement of the regex from fix for CVE-2020-8492.
Patch366: 00366-CVE-2021-3733.patch

# 00368 # 10dcf6732fb101ce89ad506a89365c6b1ff8c4e4
# CVE-2021-3737: http client infinite line reading (DoS) after a HTTP 100 Continue
#
# Fixes http.client potential denial of service where it could get stuck reading
# lines from a malicious server after a 100 Continue response.
#
# Backported from Python 3.
Patch368: 00368-CVE-2021-3737.patch

# 00372 # 0039a5762ac21255d6e4c2421a2159cbecfc95bd
# CVE-2021-4189: ftplib should not use the host from the PASV response
#
# Upstream: https://bugs.python.org/issue43285
#
# Backported from the python3 branch.
Patch372: 00372-CVE-2021-4189.patch

# 00375 # 5488ab84d2447aa8df8b3502e76f151ac2488947
# Fix precision in test_distance (test.test_turtle.TestVec2D).
# See: https://bugzilla.redhat.com/show_bug.cgi?id=2038843
Patch375: 00375-fix-test_distance-to-enable-Python-build-on-i686.patch

# 00377 # 53940f806f5e3451c9b77b44e2fc4d18b243156b
# CVE-2022-0391: urlparse does not sanitize URLs containing ASCII newline and tabs
#
# ASCII newline and tab characters are stripped from the URL.
#
# Upstream: https://bugs.python.org/issue43882
#
# Backported from Python 3.
Patch377: 00377-CVE-2022-0391.patch

# 00378 # 32b7f6200303fb36d104ac8d2afa3afba1789c1b
# Support expat 2.4.5
#
# Curly brackets were never allowed in namespace URIs
# according to RFC 3986, and so-called namespace-validating
# XML parsers have the right to reject them a invalid URIs.
#
# libexpat >=2.4.5 has become strcter in that regard due to
# related security issues; with ET.XML instantiating a
# namespace-aware parser under the hood, this test has no
# future in CPython.
#
# References:
# - https://datatracker.ietf.org/doc/html/rfc3968
# - https://www.w3.org/TR/xml-names/
#
# Also, test_minidom.py: Support Expat >=2.4.5
#
# Upstream: https://bugs.python.org/issue46811
#
# Backported from Python 3.
Patch378: 00378-support-expat-2-4-5.patch

# 00382 # 65796028be4b28aaf027963d6fb2ef4c219e73dc
# Make mailcap refuse to match unsafe filenames/types/params (GH-91993)
#
# Upstream: https://github.com/python/cpython/issues/68966
#
# Tracker bug: https://bugzilla.redhat.com/show_bug.cgi?id=2075390
#
# Backported from python3.
Patch382: 00382-cve-2015-20107.patch

# 00394 # 32a7810526fb88b82f6e2dee6d8367d1264e8fad
# gh-98433: Fix quadratic time idna decoding.
#
# There was an unnecessary quadratic loop in idna decoding. This restores
# the behavior to linear.
#
# Backported from python3.
Patch394: 00394-cve-2022-45061-cpu-denial-of-service-via-inefficient-idna-decoder.patch

# 00399 # 70e14c5e59a39bf5fae54c040d0e1d8b5c06d92c
# * gh-102153: Start stripping C0 control and space chars in `urlsplit` (GH-102508)
#
# `urllib.parse.urlsplit` has already been respecting the WHATWG spec a bit GH-25595.
#
# This adds more sanitizing to respect the "Remove any leading C0 control or space from input" [rule](https://url.spec.whatwg.org/GH-url-parsing:~:text=Remove%%20any%%20leading%%20and%%20trailing%%20C0%%20control%%20or%%20space%%20from%%20input.) in response to [CVE-2023-24329](https://nvd.nist.gov/vuln/detail/CVE-2023-24329).
#
# Backported to Python 2 from Python 3.12.
Patch399: 00399-cve-2023-24329.patch

# 00403 # 1cbe589d7b18cb74b205b9e9d48087c12fa2f6c1
# Fix test suite failure with openssl >= 3.1.0
#
# https://www.openssl.org/news/openssl-3.1-notes.html
#
# > SSL 3, TLS 1.0, TLS 1.1, and DTLS 1.0 only work at security level 0.
#
# This causes a FTBFS in one of the members of the test suite -
# it dies with a SSL internal error rather than the expected error - in detail:
#
# In test_subclass(), SSL_do_handshake() is called with SSL.version unmodified
# from version passed to SSLContext() - but that's an impossible version
# from the config (Fedora's default security level is 2),
# and an internal error is returned.
#
# The assumption of the code is probably that earlier steps will have negotiated
# a version that's allowed by the config, but this test skips them.
# This is fixed by simply using TLSv1_2 to start with.
Patch403: 00403-no-tls-10.patch

# 00405 # 0be039ad8332dded8b1336346a8fa59b84630cbf
# Fix C99 build error: declare functions explicitly
Patch405: 00405-fix-c99-build-error.patch

# 00406 # 33d46d8ceb68210f6234f26f3465c8556c0b6ccb
# Reject XML entity declarations in plist files
# CVE-2022-48565: XML External Entity in XML processing plistlib module
# Backported from https://github.com/python/cpython/commit/a158fb9c5138
# Tracking bug: https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2022-48565
Patch406: 00406-cve-2022-48565.patch

# 00407 # f562db9763f424318fd311e3267d2aed0afadbbe
# gh-99086: Fix implicit int compiler warning in configure check for PTHREAD_SCOPE_SYSTEM
Patch407: 00407-gh-99086-fix-implicit-int-compiler-warning-in-configure-check-for-pthread_scope_system.patch

# 00408 # 7cfb7e151bb64b384c47bfe0dddf5c2d6837772f
# Security fix for CVE-2022-48560: python3: use after free in heappushpop()
# of heapq module
# Resolved upstream: https://github.com/python/cpython/issues/83602
#
# Backported from Python 3.6.11.
Patch408: 00408-cve-2022-48560.patch

# 00410 # ea9f02d63dc0f772362f520967bce90e4f4d3abd
# bpo-42598: Fix implicit function declarations in configure
#
# This is invalid in C99 and later and is an error with some compilers
# (e.g. clang in Xcode 12), and can thus cause configure checks to
# produce incorrect results.
Patch410: 00410-bpo-42598-fix-implicit-function-declarations-in-configure.patch

# 00415 # eb2d53e3e9bd2c708e9387044e8a84f0acda5830
# [CVE-2023-27043] gh-102988: Reject malformed addresses in email.parseaddr() (#111116)
#
# Detect email address parsing errors and return empty tuple to
# indicate the parsing error (old API). Add an optional 'strict'
# parameter to getaddresses() and parseaddr() functions. Patch by
# Thomas Dwyer.
#
#
# Changes for Python 2:
# - Define encoding for test_email
# - Adjust import so we don't need change the tests
# - Do not use f-strings
# - Do not use SubTest
# - KW only function arguments are not supported
Patch415: 00415-cve-2023-27043-gh-102988-reject-malformed-addresses-in-email-parseaddr-111116.patch

# 00417 # 48af248abeac52b6f26f056405170d366ea132ef
# Avoid passing incompatible pointer type in _tkinter
#
# Modules/_tkinter.c:1178:38: error: passing argument 1 of ‘Tcl_NewUnicodeObj’
# from incompatible pointer type [-Wincompatible-pointer-types]
Patch417: 00417-avoid-passing-incompatible-pointer-type-in-_tkinter.patch

# (New patches go here ^^^)
#
# When adding new patches to "python2" and "python3" in Fedora, EL, etc.,
# please try to keep the patch numbers in-sync between all specfiles.
#
# More information, and a patch number catalog, is at:
#
#     https://fedoraproject.org/wiki/SIGs/Python/PythonPatches

# Disable tk, applied conditionally if %%{without tkinter}
Patch4000: 04000-disable-tk.patch

# This is the generated patch to "configure"; see the description of
#   %%{regenerate_autotooling_patch}
# above:

Patch5000: 05000-autotool-intermediates.patch

# ======================================================
# Additional metadata
# ======================================================

%description
Python 2 is an old version of the language that is incompatible with the 3.x
line of releases. The language is mostly the same, but many details, especially
how built-in objects like dictionaries and strings work, have changed
considerably, and a lot of deprecated features have finally been removed in the
3.x line.

Note that Python 2 is not supported upstream after 2020-01-01, please use the
python3 package instead if you can.

This package also provides the "python2" executable.

# ======================================================
# The prep phase of the build:
# ======================================================

%prep
%gpgverify -k2 -s1 -d0
%setup -q -n Python-%{upstream_version}

%if 0%{?with_systemtap}
# Provide an example of usage of the tapset:
cp -a %{SOURCE4} .
cp -a %{SOURCE5} .
%endif # with_systemtap

# Ensure that we're using the system copy of various libraries, rather than
# copies shipped by upstream in the tarball:
#   Remove embedded copy of expat:
rm -r Modules/expat || exit 1

#   Remove embedded copy of libffi:
for SUBDIR in darwin libffi libffi_arm_wince libffi_msvc libffi_osx ; do
  rm -r Modules/_ctypes/$SUBDIR || exit 1 ;
done

#   Remove embedded copy of zlib:
rm -r Modules/zlib || exit 1

## Disabling hashlib patch for now as it needs to be reimplemented
## for OpenSSL 1.1.0.
# Don't build upstream Python's implementation of these crypto algorithms;
# instead rely on _hashlib and OpenSSL.
#
# For example, in our builds md5.py uses always uses hashlib.md5 (rather than
# falling back to _md5 when hashlib.md5 is not available); hashlib.md5 is
# implemented within _hashlib via OpenSSL (and thus respects FIPS mode)
#for f in md5module.c md5.c shamodule.c sha256module.c sha512module.c; do
#    rm Modules/$f
#done

#
# Apply patches:
#
%patch -P0 -p1 -b .rhconfig
%patch -P1 -p1 -b .no_gui
%patch -P4 -p1 -b .cflags
%patch -P6 -p1 -b .plural
%patch -P7 -p1

%if "%{_lib}" == "lib64"
%patch -P102 -p1 -b .lib64
%patch -P103 -p1 -b .lib64-sysconfig
%patch -P104 -p1
%endif

%patch -P10 -p1 -b .binutils-no-dep
%patch -P13 -p1 -b .socketmodule
%patch -P14 -p1 -b .socketmodule2
%patch -P16 -p1 -b .rpath
%patch -P17 -p1 -b .distutils-rpath

%if 0%{?with_systemtap}
%patch -P55 -p1 -b .systemtap
%endif

%patch -P111 -p1 -b .no-static-lib

%patch -P112 -p1 -b .debug-build

%patch -P113 -p1 -b .more-configuration-flags

%patch -P114 -p1 -b .statvfs-f-flag-constants


%patch -P121 -p1
%patch -P128 -p1

%patch -P130 -p1

%ifarch ppc %{power64}
%patch -P131 -p1
%endif

%patch -P132 -p1
%patch -P133 -p1
%patch -P136 -p1 -b .stdin-test
%patch -P137 -p1
%patch -P138 -p1
%ifarch %{arm}
%patch -P139 -p1
%endif
%ifarch %{sparc}
%patch -P140 -p1
%endif
%patch -P142 -p1 -b .tty-fail
%patch -P143 -p1 -b .tsc-on-ppc
%if !%{with_gdbm}
%patch -P144 -p1
%endif
%patch -P147 -p1
%patch -P155 -p1
%patch -P156 -p1
%patch -P165 -p1
mv Modules/cryptmodule.c Modules/_cryptmodule.c
%patch -P167 -p1
%patch -P169 -p1
%patch -P170 -p1
%patch -P174 -p1 -b .fix-for-usr-move
%patch -P180 -p1
%patch -P181 -p1
%patch -P185 -p1

%if %{with rpmwheels}
%patch -P189 -p1
rm Lib/ensurepip/_bundled/*.whl
%else
# Patch the bundled setuptools wheel for CVE-2024-6345
unzip -qq Lib/ensurepip/_bundled/setuptools-41.2.0-py2.py3-none-any.whl
patch -p1 < %{SOURCE102}
zip -rq Lib/ensurepip/_bundled/setuptools-41.2.0-py2.py3-none-any.whl easy_install.py pkg_resources setuptools setuptools-41.2.0.dist-info
rm -rf easy_install.py pkg_resources/ setuptools/ setuptools-41.2.0.dist-info/
%endif

%patch -P191 -p1
%patch -P193 -p1
%patch -P289 -p1

# Patch 351 adds binary file for testing. We need to apply it using Git.
git apply %{PATCH351}

%patch -P354 -p1
%patch -P355 -p1
%patch -P357 -p1
%patch -P359 -p1
%patch -P361 -p1
%patch -P366 -p1
%patch -P368 -p1
%patch -P375 -p1
%patch -P377 -p1
%patch -P378 -p1
%patch -P382 -p1
%patch -P394 -p1
%patch -P399 -p1
%patch -P403 -p1
%patch -P405 -p1
%patch -P406 -p1
%patch -P407 -p1
%patch -P408 -p1
%patch -P410 -p1
%patch -P417 -p1

%if %{without tkinter}
%patch -P4000 -p1
%endif

# This shouldn't be necesarry, but is right now (2.2a3)
find -name "*~" |xargs rm -f

%if ! 0%{regenerate_autotooling_patch}
# Normally we apply the patch to "configure"
# We don't apply the patch if we're working towards regenerating it
%patch -P5000 -p0 -b .autotool-intermediates
%endif


# ======================================================
# Configuring and building the code:
# ======================================================

%build
topdir=$(pwd)
export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC -fwrapv"
export CXXFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC -fwrapv"
export CPPFLAGS="$(pkg-config --cflags-only-I libffi)"
export OPT="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC -fwrapv"
export LINKCC="gcc"
export LDFLAGS="$RPM_LD_FLAGS"
if pkg-config openssl ; then
  export CFLAGS="$CFLAGS $(pkg-config --cflags openssl)"
  export LDFLAGS="$LDFLAGS $(pkg-config --libs-only-L openssl)"
fi
# Force CC
export CC=gcc

%if 0%{regenerate_autotooling_patch}
# If enabled, this code regenerates the patch to "configure", using a
# local copy of autoconf-2.65, then exits the build
#
# The following assumes that the copy is installed to ~/autoconf-2.65/bin
# as per these instructions:
#   http://bugs.python.org/issue7997

for f in pyconfig.h.in configure ; do
    cp $f $f.autotool-intermediates ;
done

# Rerun the autotools:
PATH=~/autoconf-2.65/bin:$PATH autoconf
autoheader

# Regenerate the patch:
gendiff . .autotool-intermediates > %{PATCH5000}


# Exit the build
exit 1
%endif

# Define a function, for how to perform a "build" of python for a given
# configuration:
BuildPython() {
  ConfName=$1
  BinaryName=$2
  SymlinkName=$3
  ExtraConfigArgs=$4
  PathFixWithThisBinary=$5

  ConfDir=build/$ConfName

  echo STARTING: BUILD OF PYTHON FOR CONFIGURATION: $ConfName - %{_bindir}/$BinaryName
  mkdir -p $ConfDir

  pushd $ConfDir

  # Use the freshly created "configure" script, but in the directory two above:
  %global _configure $topdir/configure

%configure \
  --enable-ipv6 \
  --enable-shared \
  --enable-unicode=%{unicode} \
  --with-dbmliborder=gdbm:ndbm:bdb \
  --with-system-expat \
  --with-system-ffi \
%if 0%{?with_systemtap}
  --with-dtrace \
  --with-tapset-install-dir=%{tapsetdir} \
%endif
%if 0%{?with_valgrind}
  --with-valgrind \
%endif
  $ExtraConfigArgs \
  %{nil}

%make_build EXTRA_CFLAGS="$CFLAGS"

# We need to fix shebang lines across the full source tree.
#
# We do this using the pathfix.py script, which requires one of the
# freshly-built Python binaries.
#
# We use the optimized python binary, and make the shebangs point at that same
# optimized python binary:
if $PathFixWithThisBinary
then
  # pathfix.py currently only works with files matching ^[a-zA-Z0-9_]+\.py$
  # when crawling through directories, so we handle the special cases manually
  LD_LIBRARY_PATH="$topdir/$ConfDir" ./$BinaryName \
    $topdir/Tools/scripts/pathfix.py \
      -i "%{_bindir}/python%{pybasever}" \
      $topdir \
      $topdir/Tools/pynche/pynche \
      $topdir/Demo/pdist/{rcvs,rcsbump,rrcs} \
      $topdir/Demo/scripts/find-uname.py \
      $topdir/Tools/scripts/reindent-rst.py
fi

# Rebuild with new python
# We need a link to a versioned python in the build directory
ln -s $BinaryName $SymlinkName
LD_LIBRARY_PATH="$topdir/$ConfDir" PATH=$PATH:$topdir/$ConfDir make -s EXTRA_CFLAGS="$CFLAGS" %{?_smp_mflags}

  popd
  echo FINISHED: BUILD OF PYTHON FOR CONFIGURATION: $ConfDir
}

# Use "BuildPython" to support building with different configurations:

BuildPython optimized \
  python \
  python%{pybasever} \
  "" \
  true


# ======================================================
# Installing the built code:
# ======================================================

%install
topdir=$(pwd)
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix} %{buildroot}%{_mandir}

# Clean up patched .py files that are saved as .lib64
for f in distutils/command/install distutils/sysconfig; do
    rm -f Lib/$f.py.lib64
done

InstallPython() {

  ConfName=$1
  BinaryName=$2
  PyInstSoName=$3

  ConfDir=build/$ConfName

  echo STARTING: INSTALL OF PYTHON FOR CONFIGURATION: $ConfName - %{_bindir}/$BinaryName
  mkdir -p $ConfDir

  pushd $ConfDir

%make_install

# We install a collection of hooks for gdb that make it easier to debug
# executables linked against libpython (such as /usr/lib/python itself)
#
# These hooks are implemented in Python itself
#
# gdb-archer looks for them in the same path as the ELF file, with a -gdb.py suffix.
# We put them in the debuginfo package by installing them to e.g.:
#  /usr/lib/debug/usr/lib/libpython2.6.so.1.0.debug-gdb.py
# (note that the debug path is /usr/lib/debug for both 32/64 bit)
#
# See https://fedoraproject.org/wiki/Features/EasierPythonDebugging for more
# information
#
# Initially I tried:
#  /usr/lib/libpython2.6.so.1.0-gdb.py
# but doing so generated noise when ldconfig was rerun (rhbz:562980)
#
%if 0%{?with_gdb_hooks}
DirHoldingGdbPy=%{_usr}/lib/debug/%{_libdir}
PathOfGdbPy=$DirHoldingGdbPy/$PyInstSoName-%{version}-%{release}.%{_arch}.debug-gdb.py

mkdir -p %{buildroot}$DirHoldingGdbPy
cp $topdir/Tools/gdb/libpython.py %{buildroot}$PathOfGdbPy

# Manually byte-compile the file, in case find-debuginfo.sh is run before
# brp-python-bytecompile, so that the .pyc/.pyo files are properly listed in
# the debuginfo manifest:
# Clamp the source mtime first, see https://fedoraproject.org/wiki/Changes/ReproducibleBuildsClampMtimes
# The clamp_source_mtime module is only guaranteed to exist on Fedoras that enabled this option:
%if 0%{?clamp_mtime_to_source_date_epoch}
LD_LIBRARY_PATH="%{buildroot}%{dynload_dir}/:%{buildroot}%{_libdir}" \
PYTHONPATH="%{_rpmconfigdir}/redhat" \
%{buildroot}%{_bindir}/python%{pybasever} -s -B -m clamp_source_mtime %{buildroot}$DirHoldingGdbPy
%endif
LD_LIBRARY_PATH="$topdir/$ConfDir" $topdir/$ConfDir/$BinaryName \
  -c "import compileall; import sys; compileall.compile_dir('%{buildroot}$DirHoldingGdbPy', ddir='$DirHoldingGdbPy')"

LD_LIBRARY_PATH="$topdir/$ConfDir" $topdir/$ConfDir/$BinaryName -O \
  -c "import compileall; import sys; compileall.compile_dir('%{buildroot}$DirHoldingGdbPy', ddir='$DirHoldingGdbPy')"
%endif # with_gdb_hooks

  popd

  echo FINISHED: INSTALL OF PYTHON FOR CONFIGURATION: $ConfName
}

# Use "InstallPython" to support building with different configurations:

# Now the optimized build:
InstallPython optimized \
  python%{pybasever} \
  %{py_INSTSONAME_optimized}


# Fix the interpreter path in binaries installed by distutils
# (which changes them by itself)
# Make sure we preserve the file permissions
for fixed in %{buildroot}%{_bindir}/pydoc; do
    sed 's,#!.*/python$,#!/usr/bin/env python%{pybasever},' $fixed > $fixed- \
        && cat $fixed- > $fixed && rm -f $fixed-
done

# Junk, no point in putting in -test sub-pkg
rm -f %{buildroot}/%{pylibdir}/idlelib/testcode.py*

# don't include tests that are run at build time in the package
# This is documented, and used: rhbz#387401
if /bin/false; then
 # Move this to -test subpackage.
mkdir save_bits_of_test
for i in test_support.py __init__.py; do
  cp -a %{buildroot}/%{pylibdir}/test/$i save_bits_of_test
done
rm -rf %{buildroot}/%{pylibdir}/test
mkdir %{buildroot}/%{pylibdir}/test
cp -a save_bits_of_test/* %{buildroot}/%{pylibdir}/test
fi

# tools

mkdir -p ${RPM_BUILD_ROOT}%{site_packages}

#pynche
rm -f Tools/pynche/*.pyw
cp -rp Tools/pynche \
  ${RPM_BUILD_ROOT}%{site_packages}/

mv Tools/pynche/README Tools/pynche/README.pynche

#gettext
install -m755  Tools/i18n/pygettext.py %{buildroot}%{_bindir}/
install -m755  Tools/i18n/msgfmt.py %{buildroot}%{_bindir}/

# Useful development tools
install -m755 -d %{buildroot}%{tools_dir}/scripts
install Tools/README %{buildroot}%{tools_dir}/
install Tools/scripts/*py %{buildroot}%{tools_dir}/scripts/

# Documentation tools
install -m755 -d %{buildroot}%{doc_tools_dir}
#install -m755 Doc/tools/mkhowto %{buildroot}%{doc_tools_dir}

# Useful demo scripts
install -m755 -d %{buildroot}%{demo_dir}
cp -ar Demo/* %{buildroot}%{demo_dir}

# Get rid of crap
find %{buildroot}/ -name "*~"|xargs rm -f
find %{buildroot}/ -name ".cvsignore"|xargs rm -f
find %{buildroot}/ -name "*.bat"|xargs rm -f
find . -name "*~"|xargs rm -f
find . -name ".cvsignore"|xargs rm -f


# Provide binaries in the form of bin2 and bin2.7, thus implementing
# (and expanding) the recommendations of PEP 394.
# Do NOT provide unversioned binaries
# https://fedoraproject.org/wiki/Changes/Python_means_Python3
mv %{buildroot}%{_bindir}/idle %{buildroot}%{_bindir}/idle%{pybasever}
ln -s ./idle%{pybasever} %{buildroot}%{_bindir}/idle2

mv %{buildroot}%{_bindir}/pydoc %{buildroot}%{_bindir}/pydoc%{pybasever}
ln -s ./pydoc%{pybasever} %{buildroot}%{_bindir}/pydoc2

mv %{buildroot}%{_bindir}/pygettext.py %{buildroot}%{_bindir}/pygettext%{pybasever}.py
ln -s ./pygettext%{pybasever}.py %{buildroot}%{_bindir}/pygettext2.py

mv %{buildroot}%{_bindir}/msgfmt.py %{buildroot}%{_bindir}/msgfmt%{pybasever}.py
ln -s ./msgfmt%{pybasever}.py %{buildroot}%{_bindir}/msgfmt2.py

mv %{buildroot}%{_bindir}/smtpd.py %{buildroot}%{_bindir}/smtpd%{pybasever}.py
ln -s ./smtpd%{pybasever}.py %{buildroot}%{_bindir}/smtpd2.py

# Fix for bug #136654
rm -f %{buildroot}%{pylibdir}/email/test/data/audiotest.au %{buildroot}%{pylibdir}/test/audiotest.au

# Fix bug #143667: python should own /usr/lib/python2.x on 64-bit machines
%if "%{_lib}" == "lib64"
install -d %{buildroot}/%{_prefix}/lib/python%{pybasever}/site-packages
%endif

# Make python-devel multilib-ready (bug #192747, #139911)
%global _pyconfig32_h pyconfig-32.h
%global _pyconfig64_h pyconfig-64.h

%ifarch %{power64} s390x x86_64 ia64 alpha sparc64 aarch64 %{mips64} riscv64
%global _pyconfig_h %{_pyconfig64_h}
%else
%global _pyconfig_h %{_pyconfig32_h}
%endif

%global PyIncludeDirs python%{pybasever}

for PyIncludeDir in %{PyIncludeDirs} ; do
  mv %{buildroot}%{_includedir}/$PyIncludeDir/pyconfig.h \
     %{buildroot}%{_includedir}/$PyIncludeDir/%{_pyconfig_h}
  cat > %{buildroot}%{_includedir}/$PyIncludeDir/pyconfig.h << EOF
#include <bits/wordsize.h>

#if __WORDSIZE == 32
#include "%{_pyconfig32_h}"
#elif __WORDSIZE == 64
#include "%{_pyconfig64_h}"
#else
#error "Unknown word size"
#endif
EOF
done
ln -s ../../libpython%{pybasever}.so %{buildroot}%{pylibdir}/config/libpython%{pybasever}.so

# Fix for bug 201434: make sure distutils looks at the right pyconfig.h file
# Similar for sysconfig: sysconfig.get_config_h_filename tries to locate
# pyconfig.h so it can be parsed, and needs to do this at runtime in site.py
# when python starts up.
#
# Split this out so it goes directly to the pyconfig-32.h/pyconfig-64.h
# variants:
sed -i -e "s/'pyconfig.h'/'%{_pyconfig_h}'/" \
  %{buildroot}%{pylibdir}/distutils/sysconfig.py \
  %{buildroot}%{pylibdir}/sysconfig.py

# Ensure that the curses module was linked against libncursesw.so, rather than
# libncurses.so (bug 539917)
ldd %{buildroot}/%{dynload_dir}/_curses*.so \
    | grep curses \
    | grep libncurses.so && (echo "_curses.so linked against libncurses.so" ; exit 1)

# Ensure that the debug modules are linked against the debug libpython, and
# likewise for the optimized modules and libpython:
for Module in %{buildroot}/%{dynload_dir}/*.so ; do
    case $Module in
    *_d.so)
        ldd $Module | grep %{py_INSTSONAME_optimized} &&
            (echo Debug module $Module linked against optimized %{py_INSTSONAME_optimized} ; exit 1)

        ;;
    *)
        ldd $Module | grep %{py_INSTSONAME_debug} &&
            (echo Optimized module $Module linked against debug %{py_INSTSONAME_optimized} ; exit 1)
        ;;
    esac
done

#
# Systemtap hooks:
#
%if 0%{?with_systemtap}
# Install a tapset for this libpython into tapsetdir, fixing up the path to the
# library:
mkdir -p %{buildroot}%{tapsetdir}
%ifarch %{power64} s390x x86_64 ia64 alpha sparc64 aarch64 %{mips64}
%global libpython_stp_optimized libpython%{pybasever}-64.stp
%global libpython_stp_debug     libpython%{pybasever}-debug-64.stp
%else
%global libpython_stp_optimized libpython%{pybasever}-32.stp
%global libpython_stp_debug     libpython%{pybasever}-debug-32.stp
%endif

sed \
   -e "s|LIBRARY_PATH|%{_libdir}/%{py_INSTSONAME_optimized}|" \
   %{SOURCE3} \
   > %{buildroot}%{tapsetdir}/%{libpython_stp_optimized}

%endif # with_systemtap

# Do bytecompilation with the newly installed interpreter.
# Clamp the source mtime first, see https://fedoraproject.org/wiki/Changes/ReproducibleBuildsClampMtimes
# The clamp_source_mtime module is only guaranteed to exist on Fedoras that enabled this option:
%if 0%{?clamp_mtime_to_source_date_epoch}
LD_LIBRARY_PATH="%{buildroot}%{dynload_dir}/:%{buildroot}%{_libdir}" \
PYTHONPATH="%{_rpmconfigdir}/redhat" \
%{buildroot}%{_bindir}/python%{pybasever} -s -B -m clamp_source_mtime %{buildroot}%{pylibdir}
%endif
# compile *.pyo
find %{buildroot} -type f -a -name "*.py" -print0 | \
    LD_LIBRARY_PATH="%{buildroot}%{dynload_dir}/:%{buildroot}%{_libdir}" \
    PYTHONPATH="%{buildroot}%{_libdir}/python%{pybasever} %{buildroot}%{_libdir}/python%{pybasever}/site-packages" \
    xargs -0 %{buildroot}%{_bindir}/python%{pybasever} -O -c 'import py_compile, sys; [py_compile.compile(f, dfile=f.partition("%{buildroot}")[2]) for f in sys.argv[1:]]' || :
# compile *.pyc
find %{buildroot} -type f -a -name "*.py" -print0 | \
    LD_LIBRARY_PATH="%{buildroot}%{dynload_dir}/:%{buildroot}%{_libdir}" \
    PYTHONPATH="%{buildroot}%{_libdir}/python%{pybasever} %{buildroot}%{_libdir}/python%{pybasever}/site-packages" \
    xargs -0 %{buildroot}%{_bindir}/python%{pybasever} -c 'import py_compile, sys; [py_compile.compile(f, dfile=f.partition("%{buildroot}")[2]) for f in sys.argv[1:]]' || :


# Make library-files user writable
/usr/bin/chmod 755 %{buildroot}%{dynload_dir}/*.so
/usr/bin/chmod 755 %{buildroot}%{_libdir}/libpython%{pybasever}.so.1.0

# Remove pyc/pyo files from /usr/bin
# They are not needed, and due to them, the resulting RPM is not multilib-clean
# https://bugzilla.redhat.com/show_bug.cgi?id=1703575
rm %{buildroot}%{_bindir}/*.py{c,o}

# Remove all remaining unversioned commands
# https://fedoraproject.org/wiki/Changes/Python_means_Python3
rm %{buildroot}%{_bindir}/python
rm %{buildroot}%{_bindir}/python-config
rm %{buildroot}%{_mandir}/*/python.1*
rm %{buildroot}%{_libdir}/pkgconfig/python.pc

# RPM macros
mkdir -p %{buildroot}%{rpmmacrodir}
cp -a %{SOURCE6} %{buildroot}%{rpmmacrodir}

# ======================================================
# Running the upstream test suite
# ======================================================

%check
topdir=$(pwd)
CheckPython() {
  ConfName=$1
  BinaryName=$2
  ConfDir=$(pwd)/build/$ConfName

  export OPENSSL_CONF=/non-existing-file

  echo STARTING: CHECKING OF PYTHON FOR CONFIGURATION: $ConfName

  # Note that we're running the tests using the version of the code in the
  # builddir, not in the buildroot.

  pushd $ConfDir

  EXTRATESTOPTS="--verbose"

%ifarch s390 s390x %{power64} %{arm} aarch64 %{mips}
    EXTRATESTOPTS="$EXTRATESTOPTS -x test_gdb"
%endif
%ifarch %{mips64}
    EXTRATESTOPTS="$EXTRATESTOPTS -x test_ctypes"
%endif

%if 0%{?with_huntrleaks}
  # Try to detect reference leaks on debug builds.  By default this means
  # running every test 10 times (6 to stabilize, then 4 to watch):
  if [ "$ConfName" = "debug"  ] ; then
    EXTRATESTOPTS="$EXTRATESTOPTS --huntrleaks : "
  fi
%endif

  # Run the upstream test suite, setting "WITHIN_PYTHON_RPM_BUILD" so that the
  # our non-standard decorators take effect on the relevant tests:
  #   @unittest._skipInRpmBuild(reason)
  #   @unittest._expectedFailureInRpmBuild
  WITHIN_PYTHON_RPM_BUILD= EXTRATESTOPTS="$EXTRATESTOPTS" make test

  popd

  echo FINISHED: CHECKING OF PYTHON FOR CONFIGURATION: $ConfName

}

%if %{with tests}

# no locale coercion in python2
# test_ssl:test_load_dh_params shutil.copies into unicode filename
export LC_ALL=C.utf-8

# Check each of the configurations:
CheckPython \
  optimized \
  python%{pybasever}

%endif # with tests


# ======================================================
# Cleaning up
# ======================================================


%files
%doc README
%license %{pylibdir}/LICENSE.txt
%{_bindir}/pydoc2*
%{_bindir}/python2
%{_bindir}/python%{pybasever}
%{_mandir}/*/python2*

%dir %{pylibdir}
%dir %{dynload_dir}

%{dynload_dir}/_md5module.so
%{dynload_dir}/_sha256module.so
%{dynload_dir}/_sha512module.so
%{dynload_dir}/_shamodule.so

%{dynload_dir}/Python-%{upstream_version}-py%{pybasever}.egg-info
%{dynload_dir}/_bisectmodule.so
%{dynload_dir}/_bsddb.so
%{dynload_dir}/_codecs_cn.so
%{dynload_dir}/_codecs_hk.so
%{dynload_dir}/_codecs_iso2022.so
%{dynload_dir}/_codecs_jp.so
%{dynload_dir}/_codecs_kr.so
%{dynload_dir}/_codecs_tw.so
%{dynload_dir}/_collectionsmodule.so
%{dynload_dir}/_csv.so
%{dynload_dir}/_ctypes.so
%{dynload_dir}/_curses.so
%{dynload_dir}/_curses_panel.so
%{dynload_dir}/_elementtree.so
%{dynload_dir}/_functoolsmodule.so
%{dynload_dir}/_hashlib.so
%{dynload_dir}/_heapq.so
%{dynload_dir}/_hotshot.so
%{dynload_dir}/_io.so
%{dynload_dir}/_json.so
%{dynload_dir}/_localemodule.so
%{dynload_dir}/_lsprof.so
%{dynload_dir}/_multibytecodecmodule.so
%{dynload_dir}/_multiprocessing.so
%{dynload_dir}/_randommodule.so
%{dynload_dir}/_socketmodule.so
%{dynload_dir}/_sqlite3.so
%{dynload_dir}/_ssl.so
%{dynload_dir}/_struct.so
%{dynload_dir}/arraymodule.so
%{dynload_dir}/audioop.so
%{dynload_dir}/binascii.so
%{dynload_dir}/bz2.so
%{dynload_dir}/cPickle.so
%{dynload_dir}/cStringIO.so
%{dynload_dir}/cmathmodule.so
%{dynload_dir}/_cryptmodule.so
%{dynload_dir}/datetime.so
%{dynload_dir}/dbm.so
%{dynload_dir}/dlmodule.so
%{dynload_dir}/fcntlmodule.so
%{dynload_dir}/future_builtins.so
%if %{with_gdbm}
%{dynload_dir}/gdbmmodule.so
%endif
%{dynload_dir}/grpmodule.so
%{dynload_dir}/imageop.so
%{dynload_dir}/itertoolsmodule.so
%{dynload_dir}/linuxaudiodev.so
%{dynload_dir}/math.so
%{dynload_dir}/mmapmodule.so
%{dynload_dir}/nismodule.so
%{dynload_dir}/operator.so
%{dynload_dir}/ossaudiodev.so
%{dynload_dir}/parsermodule.so
%{dynload_dir}/pyexpat.so
%{dynload_dir}/readline.so
%{dynload_dir}/resource.so
%{dynload_dir}/selectmodule.so
%{dynload_dir}/spwdmodule.so
%{dynload_dir}/stropmodule.so
%{dynload_dir}/syslog.so
%{dynload_dir}/termios.so
%{dynload_dir}/timemodule.so
%{dynload_dir}/timingmodule.so
%{dynload_dir}/unicodedata.so
%{dynload_dir}/xxsubtype.so
%{dynload_dir}/zlibmodule.so

%dir %{site_packages}
%{site_packages}/README
%{pylibdir}/*.py*
%{pylibdir}/*.doc
%{pylibdir}/wsgiref.egg-info
%dir %{pylibdir}/bsddb
%{pylibdir}/bsddb/*.py*
%{pylibdir}/compiler
%dir %{pylibdir}/ctypes
%{pylibdir}/ctypes/*.py*
%{pylibdir}/ctypes/macholib
%{pylibdir}/curses
%dir %{pylibdir}/distutils
%{pylibdir}/distutils/*.py*
%{pylibdir}/distutils/README
%{pylibdir}/distutils/command
%exclude %{pylibdir}/distutils/command/wininst-*.exe
%dir %{pylibdir}/email
%{pylibdir}/email/*.py*
%{pylibdir}/email/mime
%{pylibdir}/encodings
%{pylibdir}/hotshot
%{pylibdir}/idlelib
%{pylibdir}/importlib
%dir %{pylibdir}/json
%{pylibdir}/json/*.py*
%{pylibdir}/lib2to3
%{pylibdir}/logging
%{pylibdir}/multiprocessing
%{pylibdir}/plat-linux2
%{pylibdir}/pydoc_data
%dir %{pylibdir}/sqlite3
%{pylibdir}/sqlite3/*.py*

%{pylibdir}/unittest
%{pylibdir}/wsgiref
%{pylibdir}/xml
%if "%{_lib}" == "lib64"
%attr(0755,root,root) %dir %{_prefix}/lib/python%{pybasever}
%attr(0755,root,root) %dir %{_prefix}/lib/python%{pybasever}/site-packages
%endif

%{_libdir}/%{py_INSTSONAME_optimized}
%if 0%{?with_systemtap}
%dir %(dirname %{tapsetdir})
%dir %{tapsetdir}
%{tapsetdir}/%{libpython_stp_optimized}
%doc systemtap-example.stp pyfuntop.stp
%endif

%dir %{pylibdir}/ensurepip/
%{pylibdir}/ensurepip/*.py*
%if %{with rpmwheels}
%exclude %{pylibdir}/ensurepip/_bundled
%else
%dir %{pylibdir}/ensurepip/_bundled
%{pylibdir}/ensurepip/_bundled/*.whl
%endif


#files devel
%{_libdir}/pkgconfig/python-%{pybasever}.pc
%{_libdir}/pkgconfig/python2.pc
%{pylibdir}/config/
%{pylibdir}/distutils/command/wininst-*.exe
%dir %{_includedir}/python%{pybasever}/
%{_includedir}/python%{pybasever}/*.h

%doc Misc/README.valgrind Misc/valgrind-python.supp Misc/gdbinit
%{_bindir}/python2-config
%{_bindir}/python%{pybasever}-config
%{_libdir}/libpython%{pybasever}.so

#files tools
%doc Tools/pynche/README.pynche
%{site_packages}/pynche
%{_bindir}/smtpd2*.py

# https://bugzilla.redhat.com/show_bug.cgi?id=1111275
%exclude %{_bindir}/2to3*

%{_bindir}/idle2*
%{_bindir}/pygettext2*.py
%{_bindir}/msgfmt2*.py
%{tools_dir}
%{demo_dir}
%{pylibdir}/Doc

#files tkinter
%{pylibdir}/lib-tk
%if %{with tkinter}
%{dynload_dir}/_tkinter.so
%endif

#files test
%{pylibdir}/bsddb/test
%{pylibdir}/ctypes/test
%{pylibdir}/distutils/tests
%{pylibdir}/email/test
%{pylibdir}/json/tests
%{pylibdir}/sqlite3/test
%{pylibdir}/test/

%{dynload_dir}/_ctypes_test.so
%{dynload_dir}/_testcapimodule.so

# RPM macros, dir co-owned to avoid the dependency
%dir %{rpmmacrodir}
%{rpmmacrodir}/macros.python2

# Workaround for rhbz#1476593
%undefine _debuginfo_subpackages

# ======================================================
# Finally, the changelog:
# ======================================================

%changelog
* Thu Aug 01 2024 Miro Hrončok <mhroncok@redhat.com> - 2.7.18-43
- Security fix for CVE-2024-6345 (in bundled setuptools wheel)

* Mon Jul 22 2024 Lumír Balhar <lbalhar@redhat.com> - 2.7.18-42
- Add /usr/bin/dtrace to build deps

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.18-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.18-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.18-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Miro Hrončok <mhroncok@redhat.com> - 2.7.18-38
- Fix a build failure with GCC 14
- Fix errors in configure script with GCC 14
Resolves: rhbz#2147519

* Fri Dec 22 2023 Lumír Balhar <lbalhar@redhat.com> - 2.7.18-37
- Security fix for CVE-2023-27043
Resolves: rhbz#2196186

* Mon Nov 27 2023 Lumír Balhar <lbalhar@redhat.com> - 2.7.18-36
- Security fix for CVE-2022-48560
Resolves: rhbz#2250592

* Fri Oct 06 2023 Lumír Balhar <lbalhar@redhat.com> - 2.7.18-35
- Fix for CVE-2022-48565
Resolves: rhbz#2240062

* Fri Oct 06 2023 Victor Stinner <vstinner@python.org> - 2.7.18-34
- Fix C99 build error: declare functions explicitly

* Mon Aug 21 2023 Owen Taylor <otaylor@redhat.com> - 2.7.18-33
- Turn off tkinter for Flatpak builds
- Fix test suite failure with openssl >= 3.1.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.18-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 25 2023 Lumír Balhar <lbalhar@redhat.com> - 2.7.18-31
- Fix for CVE-2023-24329
Resolves: rhbz#2174011

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.18-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Miro Hrončok <mhroncok@redhat.com> - 2.7.18-29
- Ensure the source mtime is clamped to $SOURCE_DATE_EPOCH before bytecompilation

* Mon Dec 19 2022 Charalampos Stratakis <cstratak@redhat.com> - 2.7.18-28
- Security fix for CVE-2022-45061: CPU denial of service via inefficient IDNA decoder
  Related: rhbz#2144072

* Thu Nov 03 2022 Orion Poplawski <orion@nwra.com> - 2.7.18-27
- Avoid triggering of %%__python macro by %%py2_shebang_fix

* Wed Oct 26 2022 Lumír Balhar <lbalhar@redhat.com> - 2.7.18-26
- Fix location and invocation of pathfix.py in py2_shebang_fix macro

* Mon Aug 08 2022 Lumír Balhar <lbalhar@redhat.com> - 2.7.18-25
- Fix OpenSSL 3 compatibility (EVP_get_digestbyname -> EVP_MD_fetch)
Resolves: rhbz#2111128

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.18-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Charalampos Stratakis <cstratak@redhat.com> - 2.7.18-23
- Use OpenSSL 3 on Fedora 36+

* Thu Jun 09 2022 Charalampos Stratakis <cstratak@redhat.com> - 2.7.18-22
- Security fix for CVE-2015-20107
Resolves: rhbz#2075390

* Fri Mar 04 2022 Charalampos Stratakis <cstratak@redhat.com> - 2.7.18-21
- Fix the test suite support for Expat >= 2.4.5
Resolves: rhbz#2056970

* Wed Feb 16 2022 Charalampos Stratakis <cstratak@redhat.com> - 2.7.18-20
- Security fixes for CVE-2021-4189 and CVE-2022-0391
Resolves: rhbz#2047376

* Mon Jan 24 2022 Karolina Surma <ksurma@redhat.com> - 2.7.18-19
- Fix test to enable build with i686
Resolves: rhbz#2038843

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.18-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 2.7.18-17
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Fri Nov 12 2021 Björn Esser <besser82@fedoraproject.org> - 2.7.18-16
- Rebuild(libnsl2)

* Fri Sep 17 2021 Lumír Balhar <lbalhar@redhat.com> - 2.7.18-15
- Fix for CVE-2021-3737
Resolves: rhbz#1997671

* Wed Sep 15 2021 Lumír Balhar <lbalhar@redhat.com> - 2.7.18-14
- Fix for CVE-2021-3733
Resolves: rhbz#2000681

* Wed Sep 15 2021 Miro Hrončok <mhroncok@redhat.com> - 2.7.18-13
- Explicitly buildrequire OpenSSL 1.1, as Python 2 is not compatible with OpenSSL 3.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 19 2021 Miro Hrončok <mhroncok@redhat.com> - 2.7.18-11
- Security fix for CVE-2020-27619
- Security fix for CVE-2021-23336
- Fixes rhbz#1928916

* Wed Mar 31 2021 Charalampos Stratakis <cstratak@redhat.com> - 2.7.18-10
- Remove explicit rpath entry from pyexpat

* Wed Feb 03 2021 Miro Hrončok <mhroncok@redhat.com> - 2.7.18-9
- Add python2-rpm-macros content here
- https://fedoraproject.org/wiki/Changes/Disable_Python_2_Dist_RPM_Generators_and_Freeze_Python_2_Macros

* Mon Feb 01 2021 Miro Hrončok <mhroncok@redhat.com> - 2.7.18-8
- Security fix for CVE-2021-3177

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 30 2020 Petr Viktorin <pviktori@redhat.com> - 2.7.18-6
- CVE-2020-26116: Reject control chars in HTTP method in httplib.putrequest

* Tue Sep 29 2020 Petr Viktorin <pviktori@redhat.com> - 2.7.18-5
- Import patches from GitHub tree

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Petr Viktorin <pviktori@redhat.com> - 2.7.18-3
- Avoid infinite loop when reading specially crafted TAR files (CVE-2019-20907)
  Resolves: https://bugzilla.redhat.com/show_bug.cgi?id=1856481

* Thu May 07 2020 Miro Hrončok <mhroncok@redhat.com> - 2.7.18-2
- Rename from python27 to python2.7

* Mon Apr 20 2020 Miro Hrončok <mhroncok@redhat.com> - 2.7.18-1
- Update to 2.7.18
- This is is the last Python 2.7 release and therefore the last Python 2 release

* Thu Apr 09 2020 Marcel Plch <mplch@redhat.com> - 2.7.18~rc1-1
- Update to 2.7.18rc1

* Tue Feb 11 2020 Miro Hrončok <mhroncok@redhat.com> - 2.7.17-3
- Use bundled wheels, to allow updating setuptools in Fedora

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 20 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.17-1
- Update to 2.7.17

* Wed Oct 09 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.17~rc1-1
- Rebase to 2.7.17rc1

* Thu Aug 29 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.16-9
- Restore files %%excluded by accident

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.16-8
- Make the python27 package flat

* Tue Aug 20 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.16-7
- Conditionalize python2-devel runtime dependencies

* Wed Aug 14 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.16-6
- Rebuilt for Python 3.8

* Wed Aug 14 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.16-5
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.16-3
- https://fedoraproject.org/wiki/Changes/Python_means_Python3
- The python-unversioned-command package is no longer Python 2, but 3
- The python, pydoc, python-config, python-debug, idle, pygettext.py and
  msgfmt.py commands are now in python3

* Fri Apr 26 2019 Tomas Orsava <torsava@redhat.com> - 2.7.16-2
- Remove pyc/pyo files from /usr/bin (#1703575)
- Update the macro that disables automatic bytecompilation to the new correct
  form (#1597664)

* Mon Mar 04 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.16-1
- Update to 2.7.16 final

* Tue Feb 19 2019 Charalampos Stratakis <cstratak@redhat.com> - 2.7.16~rc1-1
- Update to 2.7.16rc1

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.7.15-14
- Rebuild for readline 8.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.15-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 2.7.15-12
- Rebuilt for libcrypt.so.2 (#1666033)

* Mon Sep 24 2018 Miro Hrončok <mhroncok@redhat.com> - 2.7.15-11
- Security fix for CVE-2018-14647 (#1631822)

* Thu Sep 20 2018 Miro Hrončok <mhroncok@redhat.com> - 2.7.15-10
- Security fix for CVE-2018-1000802 (#1631662)

* Thu Sep 06 2018 Petr Viktorin <pviktori@redhat.com> - 2.7.15-9
- Deprecate python2 and all subpackages in Fedora 30+ (#1625773)

* Thu Aug 30 2018 Miro Hrončok <mhroncok@redhat.com> - 2.7.15-8
- Require python2-setuptools from python2-devel to prevent packaging errors (#1623922)

* Tue Aug 21 2018 Miro Hrončok <mhroncok@redhat.com> - 2.7.15-7
- Use RPM built wheels of pip and setuptools in ensurepip instead of our rewheel patch

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Miro Hrončok <mhroncok@redhat.com> - 2.7.15-5
- Move /usr/bin/python into a separate package
  https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package
- Revert https://fedoraproject.org/wiki/Changes/Avoid_usr_bin_python_in_RPM_Build

* Wed Jun 13 2018 Miro Hrončok <mhroncok@redhat.com> - 2.7.15-4
- Rebuilt for Python 3.7

* Wed Jun 13 2018 Miro Hrončok <mhroncok@redhat.com> - 2.7.15-3
- Bootstrap for Python 3.7

* Tue May 15 2018 Charalampos Stratakis <cstratak@redhat.com> - 2.7.15-2
- Fix loading of the gdb python plugin (rhbz#1578001)

* Tue May 01 2018 Miro Hrončok <mhroncok@redhat.com> - 2.7.15-1
- Update to version 2.7.15

* Wed Apr 25 2018 Tomas Orsava <torsava@redhat.com> - 2.7.14-17
- Change shebangs to the proper versioned binary
- Bytecompile files manually, disbale brp-python-bytecompile
Resolves: rhbz#1572171

* Fri Apr 13 2018 Miro Hrončok <mhroncok@redhat.com> - 2.7.14-16
- Remove Obsoletes tag from when python was renamed to python2 (Fedora 25 was last)

* Wed Mar 14 2018 Miro Hrončok <mhroncok@redhat.com> - 2.7.14-15
- Fix broken SSL module
Resolves: rhbz#1555081

* Tue Mar 13 2018 Charalampos Stratakis <cstratak@redhat.com> - 2.7.14-14
- Do not send IP addresses in SNI TLS extension

* Mon Feb 26 2018 Petr Viktorin <pviktori@redhat.com> - 2.7.14-13
- Fix -Wint-in-bool-context warnings
Resolves: rhbz#1473425

* Sat Feb 24 2018 Florian Weimer <fweimer@redhat.com> - 2.7.14-12
- Rebuild with new LDFLAGS from redhat-rpm-config

* Thu Feb 15 2018 Miro Hrončok <mhroncok@redhat.com> - 2.7.14-11
- Move test.support and test.script_helper to python2-libs
Resolves: rhbz#1528899

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Petr Viktorin <pviktori@redhat.com> - 2.7.14-9
- Add patch 288: warn/fail if Python 2 is called as /usr/bin/python and
  PYTHON_DISALLOW_AMBIGUOUS_VERSION is set
- Add patch 289: Fix for over-aligned GC info

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.7.14-8
- Rebuilt for switch to libxcrypt

* Wed Jan 17 2018 Petr Viktorin <pviktori@redhat.com> - 2.7.14-7
- Build the nis module with tirpc

* Tue Jan 16 2018 Miro Hrončok <mhroncok@redhat.com> - 2.7.14-6
- Rebuild for reverted gdbm 1.13 on Fedora 27

* Thu Jan 11 2018 Charalampos Stratakis <cstratak@redhat.com> - 2.7.14-5
- Rebuild for gdbm 1.14

* Mon Dec 11 2017 Charalampos Stratakis <cstratak@redhat.com> - 2.7.14-4
- Fix hanging of all threads when trying to access an inaccessible NFS server.

* Thu Nov 09 2017 Miro Hrončok <mhroncok@redhat.com> - 2.7.14-3
- Make the -devel package require redhat-rpm-config
Resolves: rhbz#1496757

* Thu Nov 02 2017 Charalampos Stratakis <cstratak@redhat.com> - 2.7.14-2
- Add a new PYTHONSHOWREFCOUNT environment variable for printing the reference
  count in debug builds.
- Fix nondeterministic read in test_pty.

* Mon Oct 09 2017 Iryna Shcherbina <ishcherb@redhat.com> - 2.7.14-1
- Update to version 2.7.14

* Thu Aug 31 2017 Tomas Orsava <torsava@redhat.com> - 2.7.13-18
- Switch some macros into bconds to facilitate modularity

* Wed Aug 16 2017 Miro Hrončok <mhroncok@redhat.com> - 2.7.13-17
- Exclude /usr/bin/2to3 (rhbz#1111275)

* Mon Aug 14 2017 David "Sanqui" Labský <dlabsky@redhat.com> - 2.7.13-16
- Do not generate debuginfo subpackages (#1476593)

* Wed Aug 09 2017 Michal Cyprian <mcyprian@redhat.com> - 2.7.13-15
- Revert "Add --executable option to install.py command"
  This enhancement is currently not needed and it can possibly
  collide with `pip --editable`option

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Charalampos Stratakis <cstratak@redhat.com> - 2.7.13-11
- Fix test_alpn_protocols from test_ssl

* Wed May 31 2017 Miro Hrončok <mhroncok@redhat.com> - 2.7.13-11
- Change fixed Obsoletes version with a dynamic one (rhbz#1457336)

* Thu May 18 2017 Karsten Hopp <karsten@redhat.com> - 2.7.13-10
- revert logic for modularity patch and enable gdbm for modularity

* Tue May 16 2017 Tomas Orsava <torsava@redhat.com> - 2.7.13-9
- Added a dependency to the devel subpackage on python3-rpm-generators which
  have been excised out of rpm-build
- There is no Python 2 package containing Python RPM generators, therefore
  Python 3 is needed when Python 2 package is to be built, but this was
  decided not to be a problem due to nearing EOL of Python 2
- Involves: rhbz#1410631, rhbz#1444925

* Wed May 10 2017 Charalampos Stratakis <cstratak@redhat.com> - 2.7.13-8
- Enable profile guided optimizations for x86_64 and i686 architectures
- Update description to reflect that Python 2 is not the default Python

* Tue Apr 25 2017 Karsten Hopp <karsten@redhat.com> - 2.7.13-7
- apply modularity patch only during module builds

* Sun Apr 23 2017 Karsten Hopp <karsten@redhat.com> - 2.7.13-6
- add missing patch

* Fri Apr 21 2017 Karsten Hopp <karsten@redhat.com> - 2.7.13-5
- drop a couple of dependencies for Modularity builds

* Tue Feb 21 2017 Michal Cyprian <mcyprian@redhat.com> - 2.7.13-5
- Add --executable option to install.py command

* Fri Feb 17 2017 Charalampos Stratakis <cstratak@redhat.com> - 2.7.13-4
- Fix the upgrade path to F26 due to renaming the package to python2 (rhbz#1420332)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.7.13-2
- Rebuild for readline 7.x

* Wed Jan 11 2017 Charalampos Stratakis <cstratak@redhat.com> - 2.7.13-1
- Update to 2.7.13
- Don't blow up on EL7 kernel (random generator) (rhbz#1410175, rhbz#1410187)
- Require glibc >= 2.24.90-26 (rhbz#1410644)

* Thu Oct 27 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.7.12-9
- Rename package to python2 and also rename the subpackages accordingly
- Provide and obsolete python and the respective subpackages to ensure a clean
upgrade path
- Remove old provides for packages that got into stdlib
- Implement PEP 394

* Wed Oct 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.7.12-8
- Port ssl and hashlib modules to OpenSSL 1.1.0
- Drop hashlib patch for now
- Add riscv64 arch to 64bit and no-valgrind arches

* Thu Sep 29 2016 Miro Hrončok <mhroncok@redhat.com> - 2.7.12-7
- Provide python27

* Fri Sep 02 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.7.12-6
- Remove unversioned Obsoletes

* Thu Sep 01 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.7.12-5
- Rebase rewheel patch so it applies properly (rhbz#1372183)

* Tue Aug 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.7.12-4
- SPEC file cleanup
- Removal of unapplied patches

* Tue Aug 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.7.12-3
- Fix for CVE-2016-1000110 HTTPoxy attack
- SPEC file cleanup

* Mon Aug 01 2016 Michal Toman <mtoman@fedoraproject.org> - 2.7.12-2
- Build properly on MIPS

* Fri Jul 15 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.7.12-1
- Update to 2.7.12
- Refactored patches: 10, 102, 112, 134, 153
- Dropped patches: 166, 209, 210

* Fri Jul 08 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.7.11-8
- Refactor patch for properly fixing CVE-2016-5636

* Fri Jul 08 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.7.11-7
- Fix test_pyexpat failure with Expat version of 2.2.0

* Thu Jun 16 2016 Tomas Orsava <torsava@redhat.com> - 2.7.11-6
- Fix for: CVE-2016-0772 python: smtplib StartTLS stripping attack
- Raise an error when STARTTLS fails
- rhbz#1303647: https://bugzilla.redhat.com/show_bug.cgi?id=1303647
- rhbz#1346344: https://bugzilla.redhat.com/show_bug.cgi?id=1346344
- Fixed upstream: https://hg.python.org/cpython/rev/b3ce713fb9be

* Mon Jun 13 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.7.11-5
- Added patch for fixing possible integer overflow and heap corruption in zipimporter.get_data()

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Orion Poplawski <orion@cora.nwra.com> - 2.7.11-3
- Drop macros, require python/python2-rpm-macros

* Wed Dec 30 2015 Orion Poplawski <orion@cora.nwra.com> - 2.7.11-2
- Get ready for separate python-macros package

* Tue Dec 15 2015 Robert Kuska <rkuska@redhat.com> - 2.7.11-1
- Update to 2.7.11

* Thu Oct 15 2015 Thomas Spura <tomspur@fedoraproject.org> - 2.7.10-11
- provide/obsolete _isa packages in python_provide (#1271776)

* Wed Sep 23 2015 Robert Kuska <rkuska@redhat.com> - 2.7.10-10
- Revert the moving modules to python-tools because distutils uses lib2to3

* Tue Sep 22 2015 Robert Kuska <rkuska@redhat.com> - 2.7.10-9
- Move idlelib and lib2to3 modules to pythont-tools

* Thu Sep 3 2015 Orion Poplawski <orion@cora.nwra.com> - 2.7.10-8
- Fix quoting in %%python_provide macro

* Thu Sep 3 2015 Orion Poplawski <orion@cora.nwra.com> - 2.7.10-7
- Add obsoletes to %%python_provide macro to fix upgrade path
- Fix python2- provides for python- packages in %%python_provide

* Thu Jul 23 2015 Thomas Spura <tomspur@fedoraproject.org> - 2.7.10-6
- python-macros: remove R on python (#1246036)

* Wed Jul 22 2015 Thomas Spura <tomspur@fedoraproject.org> - 2.7.10-5
- Include epoch in the python_provide macro fpc#534 (Slavek Kabrda)

* Mon Jun 29 2015 Thomas Spura <tomspur@fedoraproject.org> - 2.7.10-4
- correct python_provide macro to include version only when emiting provides

* Thu Jun 25 2015 Thomas Spura <tomspur@fedoraproject.org> - 2.7.10-3
- Add unversioned python-macros from fpc#281 and fpc#534
  and require it from python-devel
- Make python-macros noarch

* Wed Jun 17 2015 Matej Stuchlik <mstuchli@redhat.com> - 2.7.10-2
- Make relocating Python by changing _prefix actually work
Resolves: rhbz#1231801

* Mon May 25 2015 Matej Stuchlik <mstuchli@redhat.com> - 2.7.10-1
- Update to 2.7.10

* Tue May  5 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.7.9-11
- Disable test_gdb on aarch64 (rhbz#1196181), it joins all other non x86 arches

* Wed Apr 15 2015 Robert Kuska <rkuska@redhat.com> - 2.7.9-10
- Remove provides/obsolates for unittest2
- Skip test_gdb on arm until rhbz#1196181 is resolved

* Thu Mar 05 2015 Matej Stuchlik <mstuchli@redhat.com> - 2.7.9-9
- Add proper rewheel Requires

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 2.7.9-8
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 2.7.9-7
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Tue Feb 17 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.7.9-6
- Own systemtap dirs (#710733)

* Fri Feb 06 2015 Karsten Hopp <karsten@redhat.com> 2.7.9-5
- disable test_gdb on ppc64* until rhbz#1132488 is really resolved

* Tue Jan 20 2015 Slavek Kabrda <bkabrda@redhat.com> - 2.7.9-4
- We need to provide both arch specific and noarch Provide for python2-devel
in order not to break noarch builds.

* Tue Jan 20 2015 Slavek Kabrda <bkabrda@redhat.com> - 2.7.9-3
- Make python2-devel provide arch specific.
Resolves: rhbz#1183530

* Mon Jan 12 2015 Dan Horák <dan[at]danny.cz> - 2.7.9-2
- build with valgrind on ppc64le
- disable test_gdb on s390(x) until rhbz#1181034 is resolved

* Thu Dec 11 2014 Matej Stuchlik <mstuchli@redhat.com> - 2.7.9-1
- Update to 2.7.9
- Refreshed patches: #55, #137, #146, #153, #156, #198
- Dropped patches: #196, #197
- New patch: #199
- Added the rewheel module

* Mon Nov 24 2014 Matej Stuchlik <mstuchli@redhat.com> - 2.7.8-10
- Improve python2_version macros

* Thu Nov 13 2014 Matej Stuchlik <mstuchli@redhat.com> - 2.7.8-9
- Add python2_version_nodots macro

* Mon Nov 10 2014 Slavek Kabrda <bkabrda@redhat.com> - 2.7.8-8
- Revert previous change, see rhbz#1161166#c6.

* Fri Nov 07 2014 Slavek Kabrda <bkabrda@redhat.com> - 2.7.8-7
- Provide importable unittest2
Resolves: rhbz#1161166

* Thu Aug 21 2014 Robert Kuska <rkuska@redhat.com> - 2.7.8-6
- Update patch 196 (ssl backport)

* Tue Aug 19 2014 Robert Kuska <rkuska@redhat.com> - 2.7.8-5
- Backport ssl module from python3

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 31 2014 Tom Callaway <spot@fedoraproject.org> - 2.7.8-3
- fix license handling

* Fri Jul 18 2014 Robert Kuska <rkuska@redhat.com> - 2.7.8-2
- Enable SSLv2 and SSLv3 when SSLv23_method is used in ssl

* Mon Jul 14 2014 Robert Kuska <rkuska@redhat.com> - 2.7.8-1
- Update to 2.7.8

* Fri Jul 11 2014 Dan Horák <dan[at]danny.cz> - 2.7.7-3
- rebuilt for updated libffi ABI on ppc64le

* Sat Jun  7 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.7.7-2
- aarch64 has valgrind, just list those that don't support it

* Wed Jun 04 2014 Matej Stuchlik <mstuchli@redhat.com> - 2.7.7-1
- Update to 2.7.7
- Refreshed patches: #16, #112, #138, #147, #157, #166, #173, #5000
- Dropped patches: #190, #192, #194

* Tue Jun 03 2014 Dan Horák <dan[at]danny.cz> - 2.7.6-9
- update the arch list where valgrind exists - %%power64 includes also
    ppc64le which is not supported yet

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.7.6-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Fri May 09 2014 Tomas Radej <tradej@redhat.com> - 2.7.6-7
- Fixed obsoletes on ordereddict (bz #1095434)

* Mon Apr 14 2014 Tomas Radej <tradej@redhat.com> - 2.7.6-6
- Obsoletes python-ordereddict (bz #1085593, not precisely 1:1 replacement)

* Mon Apr 07 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 2.7.6-5
- Fix test failure with SQLite > 3.8.4.
- Obsolete/Provide python-unittest2
Related: rhbz#1060426

* Wed Feb 19 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 2.7.6-4
- Enable loading sqlite extensions.
Resolves: rhbz#1066708

* Mon Feb 10 2014 Tomas Radej <tradej@redhat.com> - 2.7.6-3
- Fixed buffer overflow (upstream patch)
Resolves: rhbz#1062375

* Tue Feb 04 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 2.7.6-2
- Install macros in _rpmconfigdir.

* Wed Jan 29 2014 Tomas Radej <tradej@redhat.com> - 2.7.6-1
- Updated to v2.7.6
- Freshened patches 102, 111, 112, 136, and 142
- Dropped patches 186, 188 (both fixed upstream)

* Wed Jan 15 2014 Matej Stuchlik <mstuchli@redhat.com> - 2.7.5-11
- Make library-files user writable to get rid of
  Permission Denied in buildlog from debuginfo-packaging

* Tue Jan 14 2014 Dennis Gilmore <dennis@ausil.us> - 2.7.5-10
- enable valgrind support on 32 bit arm

* Tue Nov 12 2013 Tomas Radej <tradej@redhat.com> - 2.7.5-9
- Import get_python_version in bdist_rpm
Resolves: rhbz#1029082

* Tue Oct 08 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 2.7.5-8
- Fix processing gdb py-bt command in eval calls.
Resolves: rhbz#1008154

* Tue Sep 03 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 2.7.5-7
- Removed ancient Obsolete: python-sqlite2.

* Mon Aug 26 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 2.7.5-6
- Sync back/renumber patches to stay consistent with rhel.

* Mon Aug 19 2013 Matej Stuchlik <mstuchli@redhat.com> - 2.7.5-5
- Added fix for CVE-2013-4238 (rhbz#998430)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 2.7.5-3
- Fix build with libffi containing multilib wrapper for ffi.h (rhbz#979696).

* Mon Jul 08 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 2.7.5-2
- Obsolete PyXML as requested in rhbz#981137.

* Thu May 16 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 2.7.5-1
- Updated to Python 2.7.5.
- Refreshed patches: 0 (config), 102 (lib64), 121 (add Modules to build path),
153 (gdb test noise)
- Dropped patches: 126, 127 (big endian issues, both fixed upstream),
175 (configure -Wformat, fixed upstream)
- Synced patch numbers with python3.spec.

* Tue May 14 2013 David Malcolm <dmalcolm@redhat.com> - 2.7.4-5
- fix multilib issue in python-tools due to /usr/bin/pynche (source 7;
rhbz#831437)

* Thu May 02 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 2.7.4-4
- Add patch that enables building on ppc64p7.

* Mon Apr 22 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 2.7.4-3
- Allow arbitrary timeout in Condition.wait (rhbz#917709).

* Thu Apr 11 2013 Kalev Lember <kalevlember@gmail.com> - 2.7.4-2
- Build with libdb 5.3 instead of libdb4
- Refreshed patches: 0 (config), 102 (lib64)
- Dropped patches: 54 (db4 version), 159 (db4 include path adjustment)

* Mon Apr 08 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 2.7.4-1
- Updated to Python 2.7.4.
- Refreshed patches: 0 (config), 7 (sqlite encoding), 16 (rpath in config),
55 (systemtap), 111 (no static lib), 112 (debug build), 113 (more
configuration flags), 130 (add extension to python config), 134 (fix
COUNT_ALLOCS in test_sys), 146 (haslib FIPS), 147 (add debug malloc stats),
153 (fix gdb test noise), 157 (uid, gid overflow - fixed upstream, just
keeping few more downstream tests), 165 (crypt module salt backport),
175 (fix configure Wformat), 5000 (regenerated autotooling patch)
- Dropped patches: 101 (lib64 regex; merged upstream), 171 (exception on
missing /dev/urandom; merged upstream), 172 (poll for multiprocessing socket
connection; merged upstream)

* Mon Mar 25 2013 David Malcolm <dmalcolm@redhat.com> - 2.7.3-35
- fix gcc 4.8 incompatibility (rhbz#927358); regenerate autotool intermediates

* Wed Mar  6 2013 David Malcolm <dmalcolm@redhat.com> - 2.7.3-34
- restrict scope of workaround for cmpi-bindings issue to avoid breaking
in-tree running of test_sys and test_subprocess (rhbz#817554)

* Wed Mar  6 2013 David Malcolm <dmalcolm@redhat.com> - 2.7.3-33
- add workaround for cmpi-bindings issue (rhbz#817554)

* Mon Mar  4 2013 David Malcolm <dmalcolm@redhat.com> - 2.7.3-32
- add workaround for ENOPROTOOPT seen running selftests in Koji
(rhbz#913732)

* Mon Mar  4 2013 David Malcolm <dmalcolm@redhat.com> - 2.7.3-31
- remove config flag from /etc/rpm/macros.python2

* Fri Feb 22 2013 David Malcolm <dmalcolm@redhat.com> - 2.7.3-30
- remove __debug_package macro from comment

* Fri Feb 22 2013 David Malcolm <dmalcolm@redhat.com> - 2.7.3-29
- drop -b from application of patch 157 (uid/gid overflows)

* Fri Feb 22 2013 David Malcolm <dmalcolm@redhat.com> - 2.7.3-28
- fix bogus dates in changelog

* Thu Feb 21 2013 David Malcolm <dmalcolm@redhat.com> - 2.7.3-27
- port _multiprocessing.Connection.poll() to use the "poll" syscall, rather
than "select", allowing large numbers of subprocesses (patch 172;
rhbz#849992)

* Thu Feb 21 2013 David Malcolm <dmalcolm@redhat.com> - 2.7.3-26
- raise correct exception in os.urandom() when /dev/urandom is missing
(patch 171; rhbz#907383)

* Wed Feb 20 2013 David Malcolm <dmalcolm@redhat.com> - 2.7.3-25
- in debug builds, try to print repr() when a C-level assert fails in the
garbage collector (typically indicating a reference-counting error somewhere
else e.g in an extension module) (patch 170; rhbz#850013)

* Wed Feb 20 2013 David Malcolm <dmalcolm@redhat.com> - 2.7.3-24
- move lib2to3/tests from python-libs to python-test (rhbz#850056)

* Wed Feb 20 2013 David Malcolm <dmalcolm@redhat.com> - 2.7.3-23
- use SHA-256 rather than implicitly using MD5 within the challenge handling
in multiprocessing.connection (patch 169; rhbz#879695)

* Wed Feb 20 2013 David Malcolm <dmalcolm@redhat.com> - 2.7.3-22
- fix a problem with distutils.sysconfig when CFLAGS is defined in the
environment (patch 168; rhbz#849994)

* Wed Feb 20 2013 David Malcolm <dmalcolm@redhat.com> - 2.7.3-21
- don't run any stack navigation tests in test_gdb for optimized builds
(patch 167; rhbz#912025)

* Wed Feb 20 2013 David Malcolm <dmalcolm@redhat.com> - 2.7.3-20
- s/cryptmodule/_cryptmodule/ in package payload (rhbz#835021)

* Tue Feb 19 2013 David Malcolm <dmalcolm@redhat.com> - 2.7.3-19
- bulletproof the gdb debugging hooks against a failure seen in ARM builds
(patch 166; rhbz#912025)
- re-enable make check on ARM (rhbz#912025)

* Tue Feb 19 2013 David Malcolm <dmalcolm@redhat.com> - 2.7.3-18
- backport pre-canned ways of salting a password to the "crypt" module from 3.3
(rhbz#835021)

* Tue Feb 19 2013 David Malcolm <dmalcolm@redhat.com> - 2.7.3-17
- remove "_default_patch_fuzz" directive to avoid patches being silently
misapplied (refresh patch 1, patch 101, patch 102, patch 111, patch 121,
patch 158; rename patch 1, patch 101, patch 121; apply patch 54 before the
lib64 patches to avoid fuzz problems caused by the conditional application
of the lib64 patches)

* Mon Feb 18 2013 Peter Robinson <pbrobinson@fedoraproject.org> 2.7.3-16
- disable make check on ARM for the moment until 912025 is fixed

* Mon Feb 11 2013 David Malcolm <dmalcolm@redhat.com> - 2.7.3-15
- add aarch64 (rhbz#909783)

* Thu Nov 29 2012 David Malcolm <dmalcolm@redhat.com> - 2.7.3-14
- add BR on bluez-libs-devel (rhbz#879720)

* Thu Aug  9 2012 David Malcolm <dmalcolm@redhat.com> - 2.7.3-13
- remove f18 conditional from patch 159

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.7.3-11
- fix memory leak in module _hashlib (patch 158, rhbz#836285)
- fix db4 include path for libdb4 package (f18 and above) (patch 159)

* Tue Jun 26 2012 David Malcolm <dmalcolm@redhat.com> - 2.7.3-10
- fix missing include in uid/gid handling patch (patch 157; rhbz#830405)

* Fri Jun 22 2012 David Malcolm <dmalcolm@redhat.com> - 2.7.3-9
- use rpm macro for power64 (rhbz#834653)

* Tue May 15 2012 David Malcolm <dmalcolm@redhat.com> - 2.7.3-8
- update uid/gid handling to avoid int overflows seen with uid/gid
values >= 2^31 on 32-bit architectures (patch 157; rhbz#697470)

* Fri May  4 2012 David Malcolm <dmalcolm@redhat.com> - 2.7.3-7
- renumber autotools patch from 300 to 5000
- specfile cleanups

* Mon Apr 30 2012 David Malcolm <dmalcolm@redhat.com> - 2.7.3-6
- try again to fix test_gdb.py (patch 156; rhbz#817072)

* Mon Apr 30 2012 David Malcolm <dmalcolm@redhat.com> - 2.7.3-5
- fix test_gdb.py (patch 156; rhbz#817072)

* Fri Apr 20 2012 David Malcolm <dmalcolm@redhat.com> - 2.7.3-4
- avoid allocating thunks in ctypes unless absolutely necessary, to avoid
generating SELinux denials on "import ctypes" and "import uuid" when embedding
Python within httpd (patch 155; rhbz#814391)

* Thu Apr 19 2012 David Malcolm <dmalcolm@redhat.com> - 2.7.3-3
- add explicit version requirements on expat to avoid linkage problems with
XML_SetHashSalt

* Wed Apr 18 2012 David Malcolm <dmalcolm@redhat.com> - 2.7.3-2
- fix -config symlinks (patch 112; rhbz#813836)

* Wed Apr 11 2012 David Malcolm <dmalcolm@redhat.com> - 2.7.3-1
- 2.7.3: refresh patch 102 (lib64); drop upstream patches 11 (ascii-to-lower),
115 (pydoc robustness), 145 (linux2), 148 (gdbm magic values), 151 (deadlock
in fork); refresh patch 112 (debug build); revise patch 127
(test_structmember); fix test_gdb (patch 153); refresh patch 137 (distutils
tests); add python2.pc to python-devel; regenerate the autotool intermediates
patch (patch 300)

* Sat Feb 25 2012 Thomas Spura <tomspur@fedoraproject.org> - 2.7.2-20
- fix deadlock issue (#787712)

* Fri Feb 17 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 2.7.2-19
- Obsolete python-sqlite2

* Thu Nov 24 2011 Ville Skyttä <ville.skytta@iki.fi> - 2.7.2-18
- Build with $RPM_LD_FLAGS (#756862).
- Use xz-compressed source tarball.

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-17
- Rebuilt for glibc bug#747377

* Fri Sep 30 2011 David Malcolm <dmalcolm@redhat.com> - 2.7.2-16
- re-enable gdbm (patch 148; rhbz#742242)

* Fri Sep 16 2011 David Malcolm <dmalcolm@redhat.com> - 2.7.2-15
- add a sys._debugmallocstats() function (patch 147)

* Wed Sep 14 2011 David Malcolm <dmalcolm@redhat.com> - 2.7.2-14
- support OpenSSL FIPS mode in _hashlib and hashlib; don't build the _md5 and
_sha* modules, relying on _hashlib in hashlib, and thus within md5 etc
(rhbz#563986; patch 146)

* Wed Sep 14 2011 David Malcolm <dmalcolm@redhat.com> - 2.7.2-13
- force sys.platform to be "linux2" (patch 145)

* Tue Sep 13 2011 David Malcolm <dmalcolm@redhat.com> - 2.7.2-12
- disable gdbm module to prepare for gdbm soname bump

* Mon Sep 12 2011 David Malcolm <dmalcolm@redhat.com> - 2.7.2-11
- rename and renumber patches for consistency with python3.spec (55, 111, 113,
114, 125, 131, 129 to 143)

* Sat Sep 10 2011 David Malcolm <dmalcolm@redhat.com> - 2.7.2-10
- rewrite of "check", introducing downstream-only hooks for skipping specific
cases in an rpmbuild (patch 132), and fixing/skipping failing tests in a more
fine-grained manner than before (patches 104, 133-142)

* Thu Sep  1 2011 David Malcolm <dmalcolm@redhat.com> - 2.7.2-9
- run selftests with "--verbose"
- disable parts of test_io on ppc (rhbz#732998)

* Tue Aug 23 2011 David Malcolm <dmalcolm@redhat.com> - 2.7.2-8
- add --extension-suffix option to python-config (patch 130; rhbz#732808)

* Tue Aug 23 2011 David Malcolm <dmalcolm@redhat.com> - 2.7.2-7
- re-enable and fix the --with-tsc option on ppc64, and rework it on 32-bit
ppc to avoid aliasing violations (patch 129; rhbz#698726)

* Tue Aug 23 2011 David Malcolm <dmalcolm@redhat.com> - 2.7.2-6
- don't use --with-tsc on ppc64 debug builds (rhbz#698726)

* Thu Aug 18 2011 David Malcolm <dmalcolm@redhat.com> - 2.7.2-5
- add rpm macros file (rhbz#731800)

* Fri Jul  8 2011 David Malcolm <dmalcolm@redhat.com> - 2.7.2-4
- cleanup of BuildRequires; add comment headings to specfile sections

* Wed Jun 22 2011 David Malcolm <dmalcolm@redhat.com> - 2.7.2-3
- reorganize test exclusions (test_openpty and test_pty seem to be failing on
every arch, not just the explicitly-listed ones)

* Mon Jun 13 2011 Dan Horák <dan[at]danny.cz> - 2.7.2-2
- add s390(x) excluded tests

* Mon Jun 13 2011 David Malcolm <dmalcolm@redhat.com> - 2.7.2-1
- 2.7.2; drop upstreamed patches: patch 122 (parallel make fix), patch 124
(test_commands and SELinux), patch 130 (ppc preprocessor macro in debug
build); patch 131 (decimal in Turkish locale); regenerate the autotool
intermediates patch (patch 300)

* Tue Jun 07 2011 Dennis Gilmore <dennis@ausil.us> - 2.7.1-9
- fix sparc building by excluding failing tests RHBZ#711584

* Mon May 23 2011 Peter Robinson <pbrobinson@gmail.com> - 2.7.1-8
- fix compile on ARM by excluding failing tests on arm - RHBZ #706253

* Tue Apr 12 2011 David Malcolm <dmalcolm@redhat.com> - 2.7.1-7
- fix "import decimal" in the Turkish locale (patch 131; rhbz#694928)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan  21 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 2.7.1-5
- Switch from setting OPT to setting EXTRA_CFLAGS so we don't overwrite the
  DNDEBUG flag

* Fri Jan  7 2011 David Malcolm <dmalcolm@redhat.com> - 2.7.1-4
- for now, drop "obsoletes" of python-argparse, since it interracts badly with
multilib (rhbz#667984)

* Fri Jan  7 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.7.1-3
- obsolete/provide python-argparse (new in 2.7)

* Thu Jan  6 2011 David Malcolm <dmalcolm@redhat.com> - 2.7.1-2
- fix the ppc build of the debug configuration (patch 130; rhbz#661510)

* Thu Dec 23 2010 David Malcolm <dmalcolm@redhat.com> - 2.7.1-1
- 2.7.1, reworking patch 0 (config), patch 102 (lib64); drop upstream
patch 56 (cfgparse), patch 110 (ctypes/SELinux/noexecmem), patch 119 (expat
compat), patch 123 (2to3 on "from itertools import *")
- fix test_abc's test_cache_leak in the debug build (patch 128)
- drop _weakref.so from manifest (_weakref became a core module in r84230)

* Wed Sep 29 2010 jkeating - 2.7-13
- Rebuilt for gcc bug 634757

* Mon Sep 27 2010 David Malcolm <dmalcolm@redhat.com> - 2.7-12
- fix test_structmember on 64bit-bigendian (patch 127)

* Fri Sep 24 2010 David Malcolm <dmalcolm@redhat.com> - 2.7-11
- fix dbm_contains on 64bit-bigendian (patch 126; rhbz#626756)

* Thu Sep 16 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 2.7-10
- backport a patch to fix a change in behaviour in configparse.

* Thu Sep  9 2010 David Malcolm <dmalcolm@redhat.com> - 2.7-9
- move most of the payload of the core package to the libs subpackage, given
that the libs aren't meaningfully usable without the standard libraries

* Wed Aug 18 2010 David Malcolm <dmalcolm@redhat.com> - 2.7-8
- add %%check section
- update lib64 patch (patch 102) to fix expected output in test_site.py on
64-bit systems
- patch test_commands.py to work with SELinux (patch 124)
- patch the debug build's usage of COUNT_ALLOCS to be less verbose (patch 125)

* Mon Jul 26 2010 David Malcolm <dmalcolm@redhat.com> - 2.7-7
- fixup missing -lcrypt to "crypt" module in config patch (patch 0)

* Mon Jul 26 2010 David Malcolm <dmalcolm@redhat.com> - 2.7-6
- re-enable systemtap
- cherrypick upstream patch to 2to3 for "from itertools import *"
traceback (patch 123)

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.7-5
- disable systemtap for now (dtrace is failing on startup due to the bug
mentioned in 2.7-4)
- provide relative path to python binary when running pathfix.py
- fix parallel make (patch 122)

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.7-4
- fix reference to pyconfig.h in sysconfig that led to failure on startup if
python-devel was not installed

* Thu Jul  8 2010 David Malcolm <dmalcolm@redhat.com> - 2.7-3
- add patch to fixup the new sysconfig.py for our multilib support on
64-bit (patch 103)

* Thu Jul  8 2010 David Malcolm <dmalcolm@redhat.com> - 2.7-2
- add machinery for regenerating the "configure" script in the face of
mismatching autoconf versions (patch 300)

* Tue Jul  6 2010 David Malcolm <dmalcolm@redhat.com> - 2.7-1
- 2.7 final; drop alphatag
- drop patch 117 (upstream), patch 120 (upstreamed)
- fix the commented-out __python_ver from 26 to 27

* Tue Jun 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.7-0.1.rc2
- 2.7rc2
- revert r79310 (patch 121)
- remove modulator: upstream removed it in r78338
- rename mathmodule(_d).so to math(_d).so in manifests (appears to be changed
by r76861)
- _bytesio(_d).so and _filesio(_d).so were consolidated into _io(_d).so in
r73394 (upstream issue 6215)
- use the gdb hooks from the upstream tarball, rather than keeping our own
copy. The upstream version has some whitespace changes, a new write_repr for
unicode objects, and various bulletproofings for being run on older gdbs

* Tue Jun 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.7-0.1.rc1
- 2.7rc1:
  - rework patches to apply against 2.7 (which among other changes has had a
whitespace cleanup of the .c code): .rhconfig (patch0), .binutils-no-dep
(patch10), .ascii-tolower (patch11), .socketmodule (patch13), .socketmodule2
(patch14), .systemtap (patch55), .lib64 (patch102), .selinux (patch110),
.no-static-lib (patch111), .debug-build (patch112), .statvfs-f-flag-constants
(patch114), ..CVE-2010-2089 (patch117)
  - drop upstream patches: .expat (patch3), .brprpm (patch51), .valgrind
(patch52), .db48 (patch53), .CVE-2010-1634 (patch 116), .CVE-2008-5983 (patch
118)

* Tue Jun 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.5-17
- Stop python bailing out with an assertion failure when UnicodeDecodeErrors
occur on very large buffers (patch 120, upstream issue 9058)

* Mon Jun 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.5-16
- Fix an incompatibility between pyexpat and the system expat-2.0.1 that led to
a segfault running test_pyexpat.py (patch 119; upstream issue 9054)

* Tue Jun  8 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.5-15
- add a flag to make it easy to turn off the debug build when troubleshooting
the rpm build

* Sat Jun  5 2010 Dan Horák <dan[at]danny.cz> - 2.6.5-14
- reading the timestamp counter is available only on some arches (see Python/ceval.c)
- disable --with-valgrind on s390(x) arches

* Fri Jun  4 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.5-13
- ensure that the compiler is invoked with "-fwrapv" (rhbz#594819)
- CVE-2010-1634: fix various integer overflow checks in the audioop
module (patch 116)
- CVE-2010-2089: further checks within the audioop module (patch 117)
- CVE-2008-5983: the new PySys_SetArgvEx entry point from r81399 (patch 118)

* Thu May 27 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.5-12
- make "pydoc -k" more robust in the face of broken modules (rhbz:461419, patch115)

* Wed May 26 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.5-11
- add flags for statvfs.f_flag to the constant list in posixmodule (i.e. "os")
(patch 114)

* Tue May 25 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.5-10
- add configure-time support for COUNT_ALLOCS and CALL_PROFILE debug options
(patch 113); enable them and the WITH_TSC option within the debug build

* Tue May 18 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.5-9
- build and install two different configurations of Python: debug and standard,
packaging the debug build in a new "python-debug" subpackage (patch 112)

* Tue May  4 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.5-8
- don't delete wsgiref.egg-info (rhbz:588426)

* Mon Apr 26 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.5-7
- disable --with-valgrind on sparc arches

* Mon Apr 12 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.5-6
- move the "bdist_wininst" command's template .exe files from the core package
to the devel subpackage, to save space (rhbz:525469)
- fix stray doublelisting of config directory wildcard in devel subpackage

* Wed Mar 31 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.5-5
- update python-gdb.py from v4 to v5 (improving performance and stability,
adding commands)

* Thu Mar 25 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.5-4
- update python-gdb.py from v3 to v4 (fixing infinite recursion on reference
cycles and tracebacks on bytes 0x80-0xff in strings, adding handlers for sets
and exceptions)

* Wed Mar 24 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.5-3
- refresh gdb hooks to v3 (reworking how they are packaged)

* Mon Mar 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.5-2
- remove unnecessary arch-conditionality for patch 101

* Fri Mar 19 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.5-1
- update to 2.6.5: http://www.python.org/download/releases/2.6.5/
- replace our patch to compile against db4.8 with a patch from
upstream (patch 53, from r78974); update patch 54 since part of it is now in
that upstream patch
- update patch 110 so that it still applies in the face of upstream r78380

* Tue Mar 16 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.4-23
- fixup distutils/unixccompiler.py to remove standard library path from
rpath (patch 17)
- delete DOS batch files

* Fri Mar 12 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.4-22
- add pyfuntop.stp; allow systemtap support to be disabled
- remove trailing period from tkinter summary
- don't own /usr/bin/python-config if you're not the main python

* Thu Mar 11 2010 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.4-21
- rebuild with new gdbm

* Thu Feb 11 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.4-20
- avoid having the "test" subdirectory and the files within it that are in the
core subpackage also be owned by the test subpackage (rhbz:467588)

* Wed Feb 10 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.4-19
- revise the systemtap patch (patch 55:python-2.6.4-dtrace.patch) to the
new version by mjw in attachment 390110 of rhbz:545179, as this should
eliminate the performance penalty for the case where the probes aren't in
use, and eliminate all architecture-specific code (rhbz:563541; except on
sparc)

* Tue Feb  9 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.4-18
- add a systemtap tapset defining "python.function.entry" and
"python.function.return" to make it easy to use the static probepoint within
Python; add an example of using the tapset to the docs

* Tue Feb  9 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.4-17
- add systemtap static probes (wcohen; patch 55; rh bug #545179)
- update some comments in specfile relating to gdb work
- manually byte-compile the gdb.py file with the freshly-built python to ensure
that .pyx and .pyo files make it into the debuginfo manifest if they are later
byte-compiled after find-debuginfo.sh is run

* Mon Feb  8 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.4-16
- move the -gdb.py file from %%{_libdir}/INSTSONAME-gdb.py to
%%{_prefix}/lib/debug/%%{_libdir}/INSTSONAME.debug-gdb.py to avoid noise from
ldconfig (bug 562980), and which should also ensure it becomes part of the
debuginfo subpackage, rather than the libs subpackage
- introduce %%{py_SOVERSION} and %%{py_INSTSONAME} to reflect the upstream
configure script, and to avoid fragile scripts that try to figure this out
dynamically (e.g. for the -gdb.py change)

* Mon Feb  8 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.4-15
- work around bug 562906 by supplying a fixed version of pythondeps.sh
- set %%{_python_bytecompile_errors_terminate_build} to 0 to prevent the broken
test files from killing the build on buildroots where python is installed

* Fri Feb  5 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.4-14
- add gdb hooks for easier debugging

* Fri Jan 29 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.4-13
- document all patches, and remove the commented-out ones

* Tue Jan 26 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.4-12
- Address some of the issues identified in package review (bug 226342):
  - update libs requirement on base package to use %%{name} for consistency's
sake
  - convert from backticks to $() syntax throughout
  - wrap value of LD_LIBRARY_PATH in quotes
  - convert "/usr/bin/find" requirement to "findutils"
  - remove trailing periods from summaries of -devel and -tools subpackages
  - fix spelling mistake in description of -test subpackage
  - convert usage of $$RPM_BUILD_ROOT to %%{buildroot} throughout, for
stylistic consistency
  - supply dirmode arguments to defattr directives

* Mon Jan 25 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.4-11
- update python-2.6.2-config.patch to remove downstream customization of build
of pyexpat and elementtree modules
- add patch adapted from upstream (patch 3) to add support for building against
system expat; add --with-system-expat to "configure" invocation
- remove embedded copy of expat from source tree during "prep"

* Mon Jan 25 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.4-10
- introduce macros for 3 directories, replacing expanded references throughout:
%%{pylibdir}, %%{dynload_dir}, %%{site_packages}
- explicitly list all lib-dynload files, rather than dynamically gathering the
payload into a temporary text file, so that we can be sure what we are
shipping; remove now-redundant testing for presence of certain .so files
- remove embedded copy of zlib from source tree before building

* Mon Jan 25 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.4-9
- change python-2.6.2-config.patch to remove our downstream change to curses
configuration in Modules/Setup.dist, so that the curses modules are built using
setup.py with the downstream default (linking against libncursesw.so, rather
than libncurses.so), rather than within the Makefile; add a test to %%install
to verify the dso files that the curses module is linked against the correct
DSO (bug 539917; changes _cursesmodule.so -> _curses.so)

* Fri Jan 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.4-8
- rebuild (bug 556975)

* Wed Jan 20 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.4-7
- move lib2to3 from -tools subpackage to main package (bug 556667)

* Mon Jan 18 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.4-6
- patch Makefile.pre.in to avoid building static library (patch111, bug 556092)
- split up the "configure" invocation flags onto individual lines

* Fri Jan 15 2010 David Malcolm <dmalcolm@redhat.com> - 2.6.4-5
- replace usage of %%define with %%global
- use the %%{_isa} macro to ensure that the python-devel dependency on python
is for the correct multilib arch (#555943)
- delete bundled copy of libffi to make sure we use the system one
- replace references to /usr with %%{_prefix}; replace references to
/usr/include with %%{_includedir}

* Wed Dec 16 2009 David Malcolm <dmalcolm@redhat.com> - 2.6.4-4
- automatically disable arena allocator when run under valgrind (upstream
issue 2422; patch 52)
- add patch from Josh Boyer containing diff against upstream PyBSDDB to make
the bsddb module compile against db-4.8 (patch 53, #544275); bump the necessary
version of db4-devel to 4.8
- patch setup.py so that it searches for db-4.8, and enable debug output for
said search; make Setup.dist use db-4.8 (patch 54)

* Thu Nov 12 2009 David Malcolm <dmalcolm@redhat.com> - 2.6.4-3
- fixup the build when __python_ver is set (Zach Sadecki; bug 533989); use
pybasever in the files section

* Thu Oct 29 2009 David Malcolm <dmalcolm@redhat.com> - 2.6.4-2
- "Makefile" and the config-32/64.h file are needed by distutils/sysconfig.py
_init_posix(), so we include them in the core package, along with their parent
directories (bug 531901)

* Mon Oct 26 2009 David Malcolm <dmalcolm@redhat.com> - 2.6.4-1
- Update to 2.6.4

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.6.2-2
- rebuilt with new openssl

* Mon Jul 27 2009 James Antill <james.antill@redhat.com> - 2.6.2-1
- Update to 2.6.2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 4 2009 Jonathan Steffan <jsteffan@fedoraproject.org> - 2.6-10
- Move python-config to devel subpackage (#506153)
- Update BuildRoot for new standard

* Sun Jun 28 2009 Jonathan Steffan <jsteffan@fedoraproject.org> - 2.6-9
- Update python-tools description (#448940)

* Wed Apr 15 2009 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.6-8
- Replace python-hashlib and python-uuid (#484715)

* Tue Mar 17 2009 James Antill <james@fedoraproject.org> - 2.6-7
- Use system libffi
- Resolves: bug#490573
- Fix SELinux execmem problems
- Resolves: bug#488396

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> - 2.6-4
- rebuild with new openssl

* Tue Jan  6 2009 James Antill <james.antill@redhat.com> - 2.6-3
- Fix distutils generated rpms.
- Resolves: bug#236535

* Wed Dec 10 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.6-2
- Enable -lcrypt for cryptmodule

* Fri Nov 28 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.6-1
- Update to 2.6

* Tue Sep 30 2008 James Antill <james.antill@redhat.com> - 2.5.2-1
- Move to 2.5.2
- Fix CVE-2008-2316 hashlib overflow.

* Thu Jul 17 2008 Jeremy Katz <katzj@redhat.com> - 2.5.1-30
- Fix up the build for new rpm
- And actually build against db4-4.7 (#455170)

* Thu Jul 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.5.1-27
- fix license tag
- enable support for db4-4.7

* Sun Jun 15 2008 James Antill <jantill@redhat.com> - 2.5.1-26
- Fix sporadic listdir problem
- Resolves: bug#451494

* Mon Apr  7 2008 James Antill <jantill@redhat.com> - 2.5.1-25
- Rebuild to re-gen autoconf file due to glibc change.
- Resolves: bug#441003

* Tue Mar 25 2008 James Antill <jantill@redhat.com> - 2.5.1-24
- Add more constants to socketmodule

* Sat Mar  8 2008 James Antill <jantill@redhat.com> - 2.5.1-22
- Add constants to socketmodule
- Resolves: bug#436560

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.5.1-22
- Autorebuild for GCC 4.3

* Sun Jan 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.5.1-21
- rebuild for new tk in rawhide

* Mon Jan  7 2008 James Antill <jantill@redhat.com> - 2.5.1-20
- Add valgrind support files, as doc, to python-devel
- Relates: rhbz#418621
- Add new API from 2.6, set_wakeup_fd ... use at own risk, presumably won't
- change but I have no control to guarantee that.
- Resolves: rhbz#427794
- Add gdbinit support file, as doc, to python-devel

* Fri Jan  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.5.1-19
- rebuild for new tcl/tk in rawhide

* Fri Dec  7 2007 James Antill <jantill@redhat.com> - 2.5.1-18
- Create a python-test sub-module, over 3MB of stuff noone wants.
- Don't remove egginfo files, try this see what happens ... may revert.
- Resolves: rhbz#414711

* Mon Dec  3 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-17
- rebuild for new libssl

* Fri Nov 30 2007 James Antill <jantill@redhat.com> - 2.5.1-16
- Fix pyconfig.h comment typo.
- Add back test_support.py and the __init__.py file.
- Resolves: rhbz#387401

* Tue Oct 30 2007 James Antill <jantill@redhat.com> - 2.5.1-15
- Do codec lowercase in C Locale.
- Resolves: 207134 191096
- Fix stupid namespacing in pysqlite, minimal upgrade to 2.3.3 pysqlite
- Resolves: 263221

* Wed Oct 24 2007 James Antill <jantill@redhat.com> - 2.5.1-14
- Remove bintuils dep. for live CD ... add work around for ctypes

* Mon Oct 22 2007 James Antill <jantill@redhat.com> - 2.5.1-13
- Add tix buildprereq
- Add tkinter patch
- Resolves: #281751
- Fix ctypes loading of libraries, add requires on binutils
- Resolves: #307221
- Possible fix for CVE-2007-4965 possible exploitable integer overflow
- Resolves: #295971

* Tue Oct 16 2007 Mike Bonnet <mikeb@redhat.com> - 2.5.1-12
- fix marshalling of objects in xmlrpclib (python bug #1739842)

* Fri Sep 14 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-11
- fix encoding of sqlite .py files to work around weird encoding problem
  in Turkish (#283331)

* Mon Sep 10 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-10
- work around problems with multi-line plural specification (#252136)

* Tue Aug 28 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-9
- rebuild against new expat

* Tue Aug 14 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-8
- build against db4.6

* Tue Aug 14 2007 Dennis Gilmore <dennis@ausil.us> - 2.5.1-7
- add sparc64 to the list of archs for _pyconfig64_h

* Fri Aug 10 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-6
- fix ctypes again on some arches (Hans de Goede, #251637)

* Fri Jul  6 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-5
- link curses modules with ncursesw (#246385)

* Wed Jun 27 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-4
- fix _elementtree.so build (#245703)
- ensure that extension modules we expect are actually built rather than
  having them silently fall out of the package

* Tue Jun 26 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-3
- link with system expat (#245703)

* Thu Jun 21 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-2
- rebuild to take advantage of hardlinking between identical pyc/pyo files

* Thu May 31 2007 Jeremy Katz <katzj@redhat.com> - 2.5.1-1
- update to python 2.5.1

* Mon Mar 19 2007 Jeremy Katz <katzj@redhat.com> - 2.5.3-12
- fix alpha build (#231961)

* Tue Feb 13 2007 Jeremy Katz <katzj@redhat.com> - 2.5.3-11
- tcl/tk was reverted; rebuild again

* Thu Feb  1 2007 Jeremy Katz <katzj@redhat.com> - 2.5.3-10
- rebuild for new tcl/tk

* Tue Jan 16 2007 Miroslav Lichvar <mlichvar@redhat.com> - 2.5.3-9
- link with ncurses

* Sat Jan  6 2007 Jeremy Katz <katzj@redhat.com> - 2.5.3-8
- fix extensions to use shared libpython (#219564)
- all 64bit platforms need the regex fix (#122304)

* Wed Jan  3 2007 Jeremy Katz <katzj@redhat.com> - 2.5.3-7
- fix ctypes to not require execstack (#220669)

* Fri Dec 15 2006 Jeremy Katz <katzj@redhat.com> - 2.5.3-6
- don't link against compat-db (Robert Scheck)

* Wed Dec 13 2006 Jarod Wilson <jwilson@redhat.com> - 2.5.3-5
- fix invalid assert in debug mode (upstream changeset 52622)

* Tue Dec 12 2006 Jeremy Katz <katzj@redhat.com> - 2.5.3-4
- obsolete/provide python-ctypes (#219256)

* Mon Dec 11 2006 Jeremy Katz <katzj@redhat.com> - 2.5.3-3
- fix atexit traceback with failed syslog logger (#218214)
- split libpython into python-libs subpackage for multilib apps
  embedding python interpreters

* Wed Dec  6 2006 Jeremy Katz <katzj@redhat.com> - 2.5.3-2
- disable installation of .egg-info files for now

* Tue Dec  5 2006 Jeremy Katz <katzj@redhat.com>
- support db 4.5
- obsolete python-elementtree; since it requires some code tweaks, don't
  provide it
- obsolete old python-sqlite; provide the version that's actually included

* Mon Oct 30 2006 Jeremy Katz <katzj@redhat.com>
- fix _md5 and _sha modules (Robert Sheck)
- no longer provide optik compat; it's been a couple of years now
- no longer provide the old shm module; if this is still needed, let's
  build it separately
- no longer provide japanese codecs; should be a separate package

* Mon Oct 23 2006 Jeremy Katz <katzj@redhat.com> - 2.5-0
- update to 2.5.0 final

* Fri Aug 18 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.99.c1
- Updated to 2.5c1. Merged fixes from FC6 too:
- Fixed bug #199373 (on some platforms CFLAGS is needed when linking)
- Fixed bug #198971 (case conversion not locale safe in logging library)
- Verified bug #201434 (distutils.sysconfig is confused by the change to make
  python-devel multilib friendly) is fixed upstream

* Sun Jul 16 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.99.b2
- Updated to 2.5b2 (which for comparison reasons is re-labeled 2.4.99.b2)

* Fri Jun 23 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.99.b1
- Updated to 2.5b1 (which for comparison reasons is re-labeled 2.4.99.b1)

* Tue Jun 13 2006 Jeremy Katz <katzj@redhat.com> - 2.4.3-11.FC6
- and fix it for real

* Tue Jun 13 2006 Jeremy Katz <katzj@redhat.com> - 2.4.3-10.FC6
- fix python-devel on ia64

* Tue Jun 13 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.3-9
- Fixed python-devel to be multilib friendly (bug #192747, #139911)

* Tue Jun 13 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.3-8
- Only copying mkhowto from the Docs - we don't need perl dependencies from
  python-tools.

* Mon Jun 12 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.3-7
- Fixed bug #121198 (webbrowser.py should use the user's preferences first)

* Mon Jun 12 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.3-6
- Fixed bug #192592 (too aggressive assertion fails) - SF#1257960
- Fixed bug #167468 (Doc/tools not included) - added in the python-tools package

* Thu Jun  8 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.3-5
- Fixed bug #193484 (added pydoc in the main package)

* Mon Jun  5 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.3-4
- Added dist in the release

* Mon May 15 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.3-3
- rebuilt to fix broken libX11 dependency

* Wed Apr 12 2006 Jeremy Katz <katzj@redhat.com> - 2.4.3-2
- rebuild with new gcc to fix #188649

* Thu Apr  6 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.3-1
- Updated to 2.4.3

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.4.2-3.2.1
- bump again for double-long bug on ppc(64)

* Fri Feb 10 2006 Mihai Ibanescu <misa@redhat.com> - 2.4.3-3.2
- rebuilt for newer tix

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.4.2-3.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Jan 20 2006 Mihai Ibanescu <misa@redhat.com> 2.4.2-3
- fixed #136654 for another instance of audiotest.au

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sat Nov 19 2005 Bill Nottingham <notting@redhat.com> 2.4.2-2
- fix build for modular X, remove X11R6 path references

* Tue Nov 15 2005 Mihai Ibanescu <misa@redhat.com> 2.4.2-1
- Upgraded to 2.4.2
- BuildRequires autoconf

* Wed Nov  9 2005 Mihai Ibanescu <misa@redhat.com> 2.4.1-16
- Rebuilding against newer openssl.
- XFree86-devel no longer exists

* Mon Sep 26 2005 Peter Jones <pjones@redhat.com> 2.4.1-14
- Once more -- this time, to fix -EPERM when you run it in a directory
  you can't read from.

* Mon Sep 26 2005 Peter Jones <pjones@redhat.com> 2.4.1-13
- So, 5 or 6 people have said it works for them with this patch...

* Sun Sep 25 2005 Peter Jones <pjones@redhat.com> 2.4.1-12
- Fixed bug #169159 (check for argc>0 and argv[0] == NULL, not just
    argv[0][0]='\0')
  Reworked the patch from -8 a bit more.

* Fri Sep 23 2005 Mihai Ibanescu <misa@redhat.com> 2.4.1-10
- Fixed bug #169159 (don't let python core dump if no arguments are passed in)
  Reworked the patch from -8 a bit more.

* Thu Sep 22 2005 Peter Jones <pjones@redhat.com> 2.4.1-8
- Fix bug #169046 more correctly.

* Thu Sep 22 2005 Mihai Ibanescu <misa@redhat.com> 2.4.1-7
- Fixed bug #169046 (realpath is unsafe); thanks to
  Peter Jones <pjones@redhat.com> and Arjan van de Ven <arjanv@redhat.com> for
  diagnosing and the patch.

* Tue Sep 20 2005 Mihai Ibanescu <misa@redhat.com> 2.4.1-4
- Fixed bug #168655 (fixes for building as python24)

* Tue Jul 26 2005 Mihai Ibanescu <misa@redhat.com> 2.4.1-3
- Fixed bug #163435 (pynche doesn't start))

* Wed Apr 20 2005 Mihai Ibanescu <misa@redhat.com> 2.4.1-2
- Fixed bug #143667 (python should own /usr/lib/python* on 64-bit systems, for
  noarch packages)
- Fixed bug #143419 (BuildRequires db4 is not versioned)

* Wed Apr  6 2005 Mihai Ibanescu <misa@redhat.com> 2.4.1-1
- updated to 2.4.1

* Mon Mar 14 2005 Mihai Ibanescu <misa@redhat.com> 2.4-6
- building the docs from a different source rpm, to decouple bootstrapping
  python from having tetex installed

* Fri Mar 11 2005 Dan Williams <dcbw@redhat.com> 2.4-5
- Rebuild to pick up new libssl.so.5

* Wed Feb  2 2005 Mihai Ibanescu <misa@redhat.com> 2.4-4
- Fixed security issue in SimpleXMLRPCServer.py (#146647)

* Wed Jan 12 2005 Tim Waugh <twaugh@redhat.com> 2.4-3
- Rebuilt for new readline.

* Mon Dec  6 2004 Jeff Johnson <jbj@jbj.org> 2.4-2
- db-4.3.21 returns DB_BUFFER_SMALL rather than ENOMEM (#141994).
- add Provide: python(abi) = 2.4
- include msgfmt/pygettext *.pyc and *.pyo from brp-python-bytecompile.

* Fri Dec  3 2004 Mihai Ibanescu <misa@redhat.com> 2.4-1
- Python-2.4.tar.bz2 (final)

* Fri Nov 19 2004 Mihai Ibanescu <misa@redhat.com> 2.4-0.c1.1
- Python-2.4c1.tar.bz2 (release candidate 1)

* Thu Nov 11 2004 Jeff Johnson <jbj@jbj.org> 2.4-0.b2.4
- rebuild against db-4.3.21.

* Mon Nov  8 2004 Jeremy Katz <katzj@redhat.com> - 2.4-0.b2.3
- fix the lib64 patch so that 64bit arches still look in /usr/lib/python...

* Mon Nov  8 2004 Jeremy Katz <katzj@redhat.com> - 2.4-0.b2.2
- cryptmodule still needs -lcrypt (again)

* Thu Nov  4 2004 Mihai Ibanescu <misa@redhat.com> 2.4-0.b2.1
- Updated to python 2.4b2 (and labeled it 2.4-0.b2.1 to avoid breaking rpm's
  version comparison)

* Thu Nov  4 2004 Mihai Ibanescu <misa@redhat.com> 2.3.4-13
- Fixed bug #138112 (python overflows stack buffer) - SF bug 105470

* Tue Nov  2 2004 Mihai Ibanescu <misa@redhat.com> 2.3.4-12
- Fixed bugs #131439 #136023 #137863 (.pyc/.pyo files had the buildroot added)

* Tue Oct 26 2004 Mihai Ibanescu <misa@redhat.com> 2.3.4-11
- Fixed bug #136654 (python has sketchy audio clip)

* Tue Aug 31 2004 Mihai Ibanescu <misa@redhat.com> 2.3.4-10
- Fixed bug #77418 (Demo dir not packaged)
- More tweaking on #19347 (Moved Tools/ under /usr/lib/python2.3/Tools)

* Fri Aug 13 2004 Mihai Ibanescu <misa@redhat.com> 2.3.4-8
- Fixed bug #129769: Makefile in new python conflicts with older version found
  in old python-devel
- Reorganized the spec file to get rid of the aspython2 define; __python_ver
  is more powerful.

* Tue Aug  3 2004 Mihai Ibanescu <misa@redhat.com> 2.3.4-7
- Including html documentation for non-i386 arches
- Fixed #125362 (python-doc html files have japanese character encoding)
- Fixed #128923 (missing dependency between python and python-devel)

* Fri Jul 30 2004 Mihai Ibanescu <misa@redhat.com> 2.3.4-6
- Fixed #128030 (help() not printing anything)
- Fixed #125472 (distutils.sysconfig.get_python_lib() not returning the right
  path on 64-bit systems)
- Fixed #127357 (building python as a shared library)
- Fixed  #19347 (including the contents of Tools/scripts/ in python-tools)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  8 2004 Mihai Ibanescu <misa@redhat.com> 2.3.4-3
- Added an optik.py that provides the same interface from optparse for
  backward compatibility; obsoleting python-optik

* Mon Jun  7 2004 Mihai Ibanescu <misa@redhat.com> 2.3.4-2
- Patched bdist_rpm to allow for builds of multiple binary rpms (bug #123598)

* Fri Jun  4 2004 Mihai Ibanescu <misa@redhat.com> 2.3.4-1
- Updated to 2.3.4-1 with Robert Scheck's help (bug #124764)
- Added BuildRequires: tix-devel (bug #124918)

* Fri May  7 2004 Mihai Ibanescu <misa@redhat.com> 2.3.3-6
- Correct fix for #122304 from upstream:
  http://sourceforge.net/tracker/?func=detail&atid=105470&aid=931848&group_id=5470

* Thu May  6 2004 Mihai Ibanescu <misa@redhat.com> 2.3.3-4
- Fix for bug #122304 : splitting the domain name fails on 64-bit arches
- Fix for bug #120879 : including Makefile into the main package

- Requires XFree86-devel instead of -libs (see bug #118442)

* Tue Mar 16 2004 Mihai Ibanescu <misa@redhat.com> 2.3.3-3
- Requires XFree86-devel instead of -libs (see bug #118442)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Dec 19 2003 Jeff Johnson <jbj@jbj.org> 2.3.3-1
- upgrade to 2.3.3.

* Sat Dec 13 2003 Jeff Johnson <jbj@jbj.org> 2.3.2-9
- rebuild against db-4.2.52.

* Fri Dec 12 2003 Jeremy Katz <katzj@redhat.com> 2.3.2-8
- more rebuilding for new tcl/tk

* Wed Dec  3 2003 Jeff Johnson <jbj@jbj.org> 2.3.2-7.1
- rebuild against db-4.2.42.

* Fri Nov 28 2003 Mihai Ibanescu <misa@redhat.com> 2.3.2-7
- rebuilt against newer tcl/tk

* Mon Nov 24 2003 Mihai Ibanescu <misa@redhat.com> 2.3.2-6
- added a Provides: python-abi

* Wed Nov 12 2003 Mihai Ibanescu <misa@redhat.com> 2.3.2-5
- force CC (#109268)

* Sun Nov  9 2003 Jeremy Katz <katzj@redhat.com> 2.3.2-4
- cryptmodule still needs -lcrypt

* Wed Nov  5 2003 Mihai Ibanescu <misa@redhat.com> 2.3.2-2
- Added patch for missing mkhowto

* Thu Oct 16 2003 Mihai Ibanescu <misa@redhat.com> 2.3.2-1
- Updated to 2.3.2

* Thu Sep 25 2003 Mihai Ibanescu <misa@redhat.com> 2.3.1-1
- 2.3.1 final

* Tue Sep 23 2003 Mihai Ibanescu <misa@redhat.com> 2.3.1-0.8.RC1
- Building the python 2.3.1 release candidate
- Updated the lib64 patch

* Wed Jul 30 2003 Mihai Ibanescu <misa@redhat.com> 2.3-0.2
- Building python 2.3
- Added more BuildRequires
- Updated the startup files for modulator and pynche; idle installs its own
  now.

* Thu Jul  3 2003 Mihai Ibanescu <misa@redhat.com> 2.2.3-4
- Rebuilt against newer db4 packages (bug #98539)

* Mon Jun 9 2003 Elliot Lee <sopwith@redhat.com> 2.2.3-3
- rebuilt

* Sat Jun  7 2003 Mihai Ibanescu <misa@redhat.com> 2.2.3-2
- Rebuilt

* Fri Jun  6 2003 Mihai Ibanescu <misa@redhat.com> 2.2.3-1
- Upgraded to 2.2.3

* Wed Apr  2 2003 Mihai Ibanescu <misa@redhat.com> 2.2.2-28
- Rebuilt

* Wed Apr  2 2003 Mihai Ibanescu <misa@redhat.com> 2.2.2-27
- Modified the ftpuri patch conforming to http://ietf.org/rfc/rfc1738.txt

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 24 2003 Mihai Ibanescu <misa@redhat.com> 2.2.2-25
- Fixed bug #84886: pydoc dies when run w/o arguments
- Fixed bug #84205: add python shm module back (used to be shipped with 1.5.2)
- Fixed bug #84966: path in byte-compiled code still wrong

* Thu Feb 20 2003 Jeremy Katz <katzj@redhat.com> 2.2.2-23
- ftp uri's should be able to specify being rooted at the root instead of
  where you login via ftp (#84692)

* Mon Feb 10 2003 Mihai Ibanescu <misa@redhat.com> 2.2.2-22
- Using newer Japanese codecs (1.4.9). Thanks to
  Peter Bowen <pzb@datastacks.com> for pointing this out.

* Thu Feb  6 2003 Mihai Ibanescu <misa@redhat.com> 2.2.2-21
- Rebuild

* Wed Feb  5 2003 Mihai Ibanescu <misa@redhat.com> 2.2.2-20
- Release number bumped really high: turning on UCS4 (ABI compatibility
  breakage)

* Fri Jan 31 2003 Mihai Ibanescu <misa@redhat.com> 2.2.2-13
- Attempt to look both in /usr/lib64 and /usr/lib/python2.2/site-packages/:
  some work on python-2.2.2-lib64.patch

* Thu Jan 30 2003 Mihai Ibanescu <misa@redhat.com> 2.2.2-12
- Rebuild to incorporate the removal of .lib64 and - files.

* Thu Jan 30 2003 Mihai Ibanescu <misa@redhat.com> 2.2.2-11.7.3
- Fixed bug #82544: Errata removes most tools
- Fixed bug #82435: Python 2.2.2 errata breaks redhat-config-users
- Removed .lib64 and - files that get installed after we fix the multilib
  .py files.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Jan 15 2003 Jens Petersen <petersen@redhat.com> 2.2.2-10
- rebuild to update tkinter's tcltk deps
- convert changelog to utf-8

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 2.2.2-9
- rebuild

* Fri Jan  3 2003 Nalin Dahyabhai <nalin@redhat.com>
- pick up OpenSSL cflags and ldflags from pkgconfig if available

* Thu Jan  2 2003 Jeremy Katz <katzj@redhat.com> 2.2.2-8
- urllib2 didn't support non-anonymous ftp.  add support based on how
  urllib did it (#80676, #78168)

* Mon Dec 16 2002 Mihai Ibanescu <misa@redhat.com> 2.2.2-7
- Fix bug #79647 (Rebuild of SRPM fails if python isn't installed)
- Added a bunch of missing BuildRequires found while fixing the
  above-mentioned bug

* Tue Dec 10 2002 Tim Powers <timp@redhat.com> 2.2.2-6
- rebuild to fix broken tcltk deps for tkinter

* Fri Nov 22 2002 Mihai Ibanescu <misa@redhat.com>
2.2.2-3.7.3
- Recompiled for 7.3 (to fix the -lcrypt bug)
- Fix for the spurious error message at the end of the build (build-requires
  gets confused by executable files starting with """"): make the tests
  non-executable.

* Wed Nov 20 2002 Mihai Ibanescu <misa@redhat.com>
2.2.2-5
- Fixed configuration patch to add -lcrypt when compiling cryptmodule.c

2.2.2-4
- Spec file change from Matt Wilson <msw@redhat.com> to disable linking
  with the C++ compiler.

* Mon Nov 11 2002 Mihai Ibanescu <misa@redhat.com>
2.2.2-3.*
- Merged patch from Karsten Hopp <karsten@redhat.de> from 2.2.1-17hammer to
  use %%{_libdir}
- Added XFree86-libs as BuildRequires (because of tkinter)
- Fixed duplicate listing of plat-linux2
- Fixed exclusion of lib-dynload/japanese
- Added lib64 patch for the japanese codecs
- Use setup magic instead of using tar directly on JapaneseCodecs

* Tue Nov  5 2002 Mihai Ibanescu <misa@redhat.com>
2.2.2-2
- Fix #76912 (python-tools contains idle, which uses tkinter, but there is no
  requirement of tkinter from python-tools).
- Fix #74013 (rpm is missing the /usr/lib/python2.2/test directory)

* Mon Nov  4 2002 Mihai Ibanescu <misa@redhat.com>
- builds as python2 require a different libdb
- changed the buildroot name of python to match python2 builds

* Fri Nov  1 2002 Mihai Ibanescu <misa@redhat.com>
- updated python to 2.2.2 and adjusted the patches accordingly

* Mon Oct 21 2002 Mihai Ibanescu <misa@redhat.com>
- Fix #53930 (Python-2.2.1-buildroot-bytecode.patch)
- Added BuildPrereq dependency on gcc-c++

* Fri Aug 30 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-17
- security fix for _execvpe

* Tue Aug 13 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-16
- Fix  #71011,#71134, #58157

* Wed Aug  7 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-15
- Resurrect tkinter
- Fix for distutils (#67671)
- Fix #69962

* Thu Jul 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-14
- Obsolete tkinter/tkinter2 (#69838)

* Tue Jul 23 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-13
- Doc fixes (#53951) - not on alpha at the momemt

* Mon Jul  8 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-12
- fix pydoc (#68082)

* Mon Jul  8 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-11
- Add db4-devel as a BuildPrereq

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 2.2.1-10
- automated rebuild

* Mon Jun 17 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-9
- Add Japanese codecs (#66352)

* Tue Jun 11 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-8
- No more tkinter...

* Wed May 29 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-7
- Rebuild

* Tue May 21 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-6
- Add the email subcomponent (#65301)

* Fri May 10 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-5
- Rebuild

* Thu May 02 2002 Than Ngo <than@redhat.com> 2.2.1-4
- rebuild i new enviroment

* Tue Apr 23 2002 Trond Eivind Glomsrød <teg@redhat.com>
- Use ucs2, not ucs4, to avoid breaking tkinter (#63965)

* Mon Apr 22 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-2
- Make it use db4

* Fri Apr 12 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1-1
- 2.2.1 - a bugfix-only release

* Fri Apr 12 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-16
- the same, but in builddirs - this will remove them from the
  docs package, which doesn't look in the buildroot for files.

* Fri Apr 12 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-15
- Get rid of temporary files and .cvsignores included
  in the tarball and make install

* Fri Apr  5 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-14
- Don't own lib-tk in main package, only in tkinter (#62753)

* Mon Mar 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-13
- rebuild

* Mon Mar 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-12
- rebuild

* Fri Mar  1 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-11
- Add a not to the Distutils obsoletes test (doh!)

* Fri Mar  1 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-10
- Rebuild

* Mon Feb 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-9
- Only obsolete Distutils when built as python

* Thu Feb 21 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-8
- Make files in /usr/bin install side by side with python 1.5 when
- Drop explicit requirement of db4
  built as python2

* Thu Jan 31 2002 Elliot Lee <sopwith@redhat.com> 2.2-7
- Use version and pybasever macros to make updating easy
- Use _smp_mflags macro

* Tue Jan 29 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-6
- Add db4-devel to BuildPrereq

* Fri Jan 25 2002 Nalin Dahyabhai <nalin@redhat.com> 2.2-5
- disable ndbm support, which is db2 in disguise (really interesting things
  can happen when you mix db2 and db4 in a single application)

* Thu Jan 24 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-4
- Obsolete subpackages if necesarry
- provide versioned python2
- build with db4

* Wed Jan 16 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2-3
- Alpha toolchain broken. Disable build on alpha.
- New openssl

* Wed Dec 26 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2-1
- 2.2 final

* Fri Dec 14 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2-0.11c1
- 2.2 RC 1
- Don't include the _tkinter module in the main package - it's
  already in the tkiter packace
- Turn off the mpzmodule, something broke in the buildroot

* Wed Nov 28 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2-0.10b2
- Use -fPIC for OPT as well, in lack of a proper libpython.so

* Mon Nov 26 2001 Matt Wilson <msw@redhat.com> 2.2-0.9b2
- changed DESTDIR to point to / so that distutils will install dynload
  modules properly in the installroot

* Fri Nov 16 2001 Matt Wilson <msw@redhat.com> 2.2-0.8b2
- 2.2b2

* Fri Oct 26 2001 Matt Wilson <msw@redhat.com> 2.2-0.7b1
- python2ify

* Fri Oct 19 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2-0.5b1
- 2.2b1

* Sun Sep 30 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2-0.4a4
- 2.2a4
- Enable UCS4 support
- Enable IPv6
- Provide distutils
- Include msgfmt.py and pygettext.py

* Fri Sep 14 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2-0.3a3
- Obsolete Distutils, which is now part of the main package
- Obsolete python2

* Thu Sep 13 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2-0.2a3
- Add docs, tools and tkinter subpackages, to match the 1.5 layout

* Wed Sep 12 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2-0.1a3
- 2.2a3
- don't build tix and blt extensions

* Mon Aug 13 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Add tk and tix to build dependencies

* Sat Jul 21 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 2.1.1 bugfix release - with a GPL compatible license

* Fri Jul 20 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Add new build dependencies (#49753)

* Tue Jun 26 2001 Nalin Dahyabhai <nalin@redhat.com>
- build with -fPIC

* Fri Jun  1 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 2.1
- reorganization of file includes

* Wed Dec 20 2000 Trond Eivind Glomsrød <teg@redhat.com>
- fix the "requires" clause, it lacked a space causing problems
- use %%{_tmppath}
- don't define name, version etc
- add the available patches from the Python home page

* Fri Dec 15 2000 Matt Wilson <msw@redhat.com>
- added devel subpackage

* Fri Dec 15 2000 Matt Wilson <msw@redhat.com>
- modify all files to use "python2.0" as the intrepter
- don't build the Expat bindings
- build against db1

* Mon Oct 16 2000 Jeremy Hylton <jeremy@beopen.com>
- updated for 2.0 final

* Mon Oct  9 2000 Jeremy Hylton <jeremy@beopen.com>
- updated for 2.0c1
- build audioop, imageop, and rgbimg extension modules
- include xml.parsers subpackage
- add test.xml.out to files list

* Thu Oct  5 2000 Jeremy Hylton <jeremy@beopen.com>
- added bin/python2.0 to files list (suggested by Martin v. L?)

* Tue Sep 26 2000 Jeremy Hylton <jeremy@beopen.com>
- updated for release 1 of 2.0b2
- use .bz2 version of Python source

* Tue Sep 12 2000 Jeremy Hylton <jeremy@beopen.com>
- Version 2 of 2.0b1
- Make the package relocatable.  Thanks to Suchandra Thapa.
- Exclude Tkinter from main RPM.  If it is in a separate RPM, it is
  easier to track Tk releases.
