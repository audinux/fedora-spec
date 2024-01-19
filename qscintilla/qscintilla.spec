# Tag: Library, Devel
# Type: Devel
# Category: Programming

%global scintilla_ver 3.10.1
# sip_ver for Fedora 31: 4.19.19, for Fedora 33: 4.19.24.
%global sip_ver 4.19.19

%global py3 1
%global qt4 1
# global qt5 1 # add a % before global

## f29+ no longer using separate sipdir for python3
%global py3_sipdir %{_datadir}/sip
%global py3_sip %{_bindir}/sip

Summary: A Scintilla port to Qt
Name: qscintilla
Version: 2.11.5
Release: 10%{?dist}
License: GPL-3.0-only
URL: http://www.riverbankcomputing.com/software/qscintilla/

Vendor:       Audinux
Distribution: Audinux

%if 0%{?snap:1}
Source0: https://www.riverbankcomputing.com/static/Downloads/QScintilla/%{version}/QScintilla-%{version}-snapshot-%{snap}.tar.gz
%else
Source0: https://www.riverbankcomputing.com/static/Downloads/QScintilla/%{version}/QScintilla-%{version}.tar.gz
%endif

## upstreamable patches
# make runtime sip check informative, not fatal
Patch100: QScintilla_gpl-2.10.7-sip_check.patch
Patch101: QScintilla_gpl-2.11-QUrl.patch

BuildRequires: gcc-c++
%if 0%{?qt4}
BuildRequires: pkgconfig(QtDesigner) pkgconfig(QtGui) pkgconfig(QtScript) pkgconfig(QtXml)
%endif
%if 0%{?qt5}
BuildRequires: pkgconfig(Qt5Designer) pkgconfig(Qt5Gui) pkgconfig(Qt5Widgets)
%endif

Provides: bundled(scintilla) = %{scintilla_ver}

%description
QScintilla is a port of Scintilla to the Qt GUI toolkit.

%{?scintilla_ver:This version of QScintilla is based on Scintilla v%{scintilla_ver}.}

%package devel
Summary:  QScintilla Development Files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt4-devel
%description devel
%{summary}.

%if 0%{?qt5}
%package qt5
Summary: A Scintilla port to Qt5
Provides: bundled(scintilla) = %{scintilla_ver}
%description qt5
%{summary}.

%package qt5-devel
Summary:  QScintilla Development Files
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel
%description qt5-devel
%{summary}.
%endif

%if 0%{?py2}
%if 0%{?qt4}
%package -n python2-qscintilla
Summary:  QScintilla python2 bindings
BuildRequires: python2-devel
BuildRequires: PyQt4-devel
BuildRequires: python2-sip-devel >= %{sip_ver}
Obsoletes: qscintilla-python < 2.9.2-2
Provides:  qscintilla-python = %{version}-%{release}
Provides:  python2-PyQt4-Qsci = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python2-qt4
%{?_sip_api:Requires: python2-pyqt4-sip-api(%{_sip_api_major}) >= %{_sip_api}}
%description -n python2-qscintilla
%{summary}.

%package -n python2-qscintilla-devel
Summary:  Development files for QScintilla python2 bindings
Obsoletes: qscintilla-python-devel < 2.9.2-2
Provides:  qscintilla-python-devel = %{version}-%{release}
Requires: PyQt4-devel
BuildArch: noarch
%description -n python2-qscintilla-devel
%{summary}.
%endif

%if 0%{?qt5}
%package -n python2-qscintilla-qt5
Summary:  QScintilla-qt5 python2 bindings
BuildRequires: python2-qt5
BuildRequires: python2-qt5-devel
BuildRequires: python2-sip-devel >= %{sip_ver}
Provides: %{name}-qt5-python2 = %{version}-%{release}
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
Requires: python2-qt5%{?pyqt5_version: >= %{pyqt5_version}}
%{?_sip_api:Requires: python2-pyqt5-sip-api(%{_sip_api_major}) >= %{_sip_api}}
%description -n python2-qscintilla-qt5
%{summary}.

%package -n python2-qscintilla-qt5-devel
Summary:  Development files for QScintilla-qt5 python2 bindings
Provides: %{name}-qt5-python2-devel = %{version}-%{release}
Requires: python2-qt5-devel
BuildArch: noarch
%description -n python2-qscintilla-qt5-devel
%{summary}.
%endif
%endif

%if 0%{?py3}
%if 0%{?qt4}
%package -n python3-qscintilla
Summary:  QScintilla python3 bindings
BuildRequires: python3-devel
BuildRequires: python3-PyQt4-devel
BuildRequires: python3-sip-devel >= %{sip_ver}
Provides: %{name}-python3 = %{version}-%{release}
Provides: python3-PyQt5-Qsci = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python3-PyQt4
%{?_sip_api:Requires: python3-pyqt4-sip-api(%{_sip_api_major}) >= %{_sip_api}}
%description -n python3-qscintilla
%{summary}.

%package -n python3-qscintilla-devel
Summary:  Development files for QScintilla python3 bindings
Provides: %{name}-python3-devel = %{version}-%{release}
Requires: python3-PyQt4-devel
BuildArch: noarch
%description -n python3-qscintilla-devel
%{summary}.
%endif

%if 0%{?qt5}
%package -n python3-qscintilla-qt5
Summary:  QScintilla-qt5 python3 bindings
BuildRequires: python3-qt5
BuildRequires: python3-qt5-devel
BuildRequires: python3-sip-devel >= %{sip_ver}
Provides: %{name}-qt5-python3 = %{version}-%{release}
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
Requires: python3-qt5%{?pyqt5_version: >= %{pyqt5_version}}
%{?_sip_api:Requires: python3-pyqt5-sip-api(%{_sip_api_major}) >= %{_sip_api}}
%description -n python3-qscintilla-qt5
%{summary}.

%package -n python3-qscintilla-qt5-devel
Summary:  Development files for QScintilla-qt5 python3 bindings
Provides: %{name}-qt5-python3-devel = %{version}-%{release}
Requires: python3-qt5-devel
BuildArch: noarch
%description -n python3-qscintilla-qt5-devel
%{summary}.
%endif
%endif

%prep
%autosetup -n QScintilla-%{version}%{?snap:-snapshot-%{snap}}

%patch100 -p1 -b .sip_check
%patch101 -p1 -b .qurl


%build
PATH=%{_qt4_bindir}:$PATH; export PATH

%if 0%{?qt4}
cp -a Qt4Qt5 Qt4/
pushd Qt4
%{qmake_qt4} qscintilla.pro
%make_build
popd

# set QMAKEFEATURES to ensure just built lib/feature is found
QMAKEFEATURES=`pwd`/Qt4/features; export QMAKEFEATURES

cp -a designer-Qt4Qt5 designer-Qt4/
pushd designer-Qt4
%{qmake_qt4} designer.pro INCLUDEPATH+=../Qt4 LIBS+=-L../Qt4
%make_build
popd

%if 0%{?py2}
cp -a Python Python2-qt4
pushd Python2-qt4
%{__python2} \
  configure.py --verbose \
    --sip=/usr/bin/sip-pyqt4 \
    --pyqt=PyQt4 \
    --qsci-incdir=../Qt4 --qsci-libdir=../Qt4 \
    --no-dist-info

%make_build
popd
%endif

%if 0%{?py3}
cp -a Python Python3-qt4
pushd Python3-qt4
%{__python3} \
  configure.py --verbose \
    --sip=/usr/bin/sip-pyqt4 \
    --pyqt=PyQt4 \
    --qsci-incdir=../Qt4 --qsci-libdir=../Qt4 \
    --no-dist-info

%make_build
popd
%endif
%endif

%if 0%{?qt5}
PATH=%{_qt5_bindir}:$PATH; export PATH

cp -a Qt4Qt5 Qt5/
pushd Qt5
%{qmake_qt5} qscintilla.pro
%make_build
popd

# set QMAKEFEATURES to ensure just built lib/feature is found
QMAKEFEATURES=`pwd`/Qt5/features; export QMAKEFEATURES

cp -a designer-Qt4Qt5 designer-Qt5/
pushd designer-Qt5
%{qmake_qt5} designer.pro INCLUDEPATH+=../Qt5 LIBS+=-L../Qt5
%make_build
popd

%if 0%{?py2}
cp -a Python Python2-qt5
pushd Python2-qt5
%{__python2} \
  configure.py --verbose \
    --pyqt=PyQt5 \
    --sip=/usr/bin/sip-pyqt5 \
    --qsci-incdir=../Qt5 --qsci-libdir=../Qt5 \

%make_build
popd
%endif

%if 0%{?py3}
cp -a Python Python3-qt5
pushd Python3-qt5
%{__python3} \
  configure.py --verbose \
    --pyqt=PyQt5 \
    --sip=/usr/bin/sip%{!?el8:-pyqt5} \
    --qsci-incdir=../Qt5 --qsci-libdir=../Qt5

%make_build
popd
%endif

%endif


%install
%if 0%{?qt4}
make -C Qt4 install INSTALL_ROOT=%{buildroot}
# compat symlink
ln -s libqscintilla2_qt4.so %{buildroot}%{_qt4_libdir}/libqscintilla2.so
make -C designer-Qt4 install INSTALL_ROOT=%{buildroot}
%if 0%{?py2}
make -C Python2-qt4 install DESTDIR=%{buildroot} INSTALL_ROOT=%{buildroot}
test -x   %{buildroot}%{python2_sitearch}/PyQt4/Qsci.so || \
chmod a+x %{buildroot}%{python2_sitearch}/PyQt4/Qsci.so
%endif
%if 0%{?py3}
make -C Python3-qt4 install DESTDIR=%{buildroot} INSTALL_ROOT=%{buildroot}
test -x   %{buildroot}%{python3_sitearch}/PyQt4/Qsci.so || \
chmod a+x %{buildroot}%{python3_sitearch}/PyQt4/Qsci.so
%endif
%endif

%if 0%{?qt5}
make -C Qt5 install INSTALL_ROOT=%{buildroot}
# compat symlink
ln -s libqscintilla2_qt5.so %{buildroot}%{_qt5_libdir}/libqscintilla2-qt5.so
make -C designer-Qt5 install INSTALL_ROOT=%{buildroot}
%if 0%{?py2}
make -C Python2-qt5 install DESTDIR=%{buildroot} INSTALL_ROOT=%{buildroot}
test -x   %{buildroot}%{python2_sitearch}/PyQt5/Qsci.so || \
chmod a+x %{buildroot}%{python2_sitearch}/PyQt5/Qsci.so
%endif
%if 0%{?py3}
make -C Python3-qt5 install DESTDIR=%{buildroot} INSTALL_ROOT=%{buildroot}
test -x   %{buildroot}%{python3_sitearch}/PyQt5/Qsci.so || \
chmod a+x %{buildroot}%{python3_sitearch}/PyQt5/Qsci.so
%endif
%endif

%find_lang qscintilla --with-qt
%if 0%{?qt4}
grep "%{_qt4_translationdir}" qscintilla.lang > qscintilla-qt4.lang
%endif
%if 0%{?qt5}
grep "%{_qt5_translationdir}" qscintilla.lang > qscintilla-qt5.lang
%endif

# unpackaged files
%if  ! ( 0%{?qt4} && (0%{?py2} || 0%{?py3}))
rm -rfv %{buildroot}%{_qt4_datadir}/qsci/
%endif
%if  ! ( 0%{?qt5} && (0%{?py2} || 0%{?py3}))
rm -rfv %{buildroot}%{_qt5_datadir}/qsci/
%endif


%check
# verify python module(s) permissions and libqscintilla2 linkage
# https://bugzilla.redhat.com/show_bug.cgi?id=1104559
%if 0%{?qt4}
%if 0%{?py2}
ldd     %{buildroot}%{python2_sitearch}/PyQt4/Qsci.so | grep libqscintilla2 || exit 1
test -x %{buildroot}%{python2_sitearch}/PyQt4/Qsci.so
%endif
%if 0%{?py3}
ldd     %{buildroot}%{python3_sitearch}/PyQt4/Qsci.so | grep libqscintilla2 || exit 1
test -x %{buildroot}%{python3_sitearch}/PyQt4/Qsci.so
%endif
%endif


%if 0%{?qt4}
%ldconfig_scriptlets

%files -f qscintilla-qt4.lang
%doc NEWS Python3-qt4/README
%license LICENSE
%{_qt4_libdir}/libqscintilla2_qt4.so.15*
%{_qt4_plugindir}/designer/libqscintillaplugin.so

%files devel
%doc doc/html-Qt4Qt5 doc/Scintilla example-Qt4Qt5
%{_qt4_headerdir}/Qsci/
%{_qt4_libdir}/libqscintilla2_qt4.so
%{_qt4_datadir}/mkspecs/features/qscintilla2.prf
# compat symlink
%{_qt4_libdir}/libqscintilla2.so

%if 0%{?py2}
%files -n python2-qscintilla
%{python2_sitearch}/PyQt4/Qsci.*
%{_qt4_datadir}/qsci/

%files -n python2-qscintilla-devel
%{_datadir}/sip/PyQt4/Qsci/
%endif

%if 0%{?py3}
%files -n python3-qscintilla
%{python3_sitearch}/PyQt4/Qsci.*
%{_qt4_datadir}/qsci/

%files -n python3-qscintilla-devel
%{py3_sipdir}/PyQt4/Qsci/
%endif
%endif

%if 0%{?qt5}
%ldconfig_scriptlets qt5

%files qt5 -f qscintilla-qt5.lang
%doc NEWS Python3-qt5/README
%license LICENSE
%{_qt5_libdir}/libqscintilla2_qt5.so.15*
%{_qt5_plugindir}/designer/libqscintillaplugin.so

%files qt5-devel
%doc doc/html-Qt4Qt5 doc/Scintilla example-Qt4Qt5
%{_qt5_headerdir}/Qsci/
%{_qt5_libdir}/libqscintilla2_qt5.so
%{_qt5_archdatadir}/mkspecs/features/qscintilla2.prf
# compat symlink
%{_qt5_libdir}/libqscintilla2-qt5.so

%if 0%{?py2}
%files -n python2-qscintilla-qt5
%{python2_sitearch}/PyQt5/Qsci.*
%{_qt5_datadir}/qsci/
%{python2_sitearch}/QScintilla-%{version}.dist-info/

%files -n python2-qscintilla-qt5-devel
%{_datadir}/sip/PyQt5/Qsci/
%endif

%if 0%{?py3}
%files -n python3-qscintilla-qt5
%{python3_sitearch}/PyQt5/Qsci.*
%{_qt5_datadir}/qsci/
%{python3_sitearch}/QScintilla-%{version}.dist-info/

%files -n python3-qscintilla-qt5-devel
%{py3_sipdir}/PyQt5/Qsci/
%endif
%endif


%changelog
* Thu Oct 29 2020 Yann Collette <ycollette.nospam@free.fr> - 2.11.5-10
- update to 2.11.5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.11.2-9
- drop qt4/python2 support for f32+

* Wed Oct 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.11.2-8
- revive qt4/python2 support on fedora, still needed by hgview (see also #1738953)

* Wed Oct 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.11.2-7
- cleanup/fix conditionals
- drop qt4/python2 support for f32+

* Mon Sep  9 2019 Orion Poplawski <orion@nwra.com> - 2.11.2-6
- Build without python2 and qt4 for EPEL8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.11.2-5
- Rebuilt for Python 3.8

* Mon Aug 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.11.2-4
- re-enable python2, python-qt5 FTBFS fixed (#1737206)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.11.2-2
- cleanup, fix qsci docs and %%check logic
- include python dist-info for qt5 builds
- drop python2 on f31+ for now due to FTBFS

* Thu Jun 27 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.11.2-1
- 2.11.2

* Fri Feb 15 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.11.1-1
- 2.11.1

* Mon Feb 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.11-1
- 2.11

* Thu Oct 04 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.10.8-1
- 2.10.8

* Sun Aug 26 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.10.7-5
- %build: --verbose --sip=/usr/bin/sip-pyqt? wrapper

* Fri Aug 24 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.10.7-4
- drop py3_sip hacks
- use python?-pyqt?-sip-api dep

* Sun Jul 22 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.10.7-3
- fix build (adapt to related sip changes)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.10.7-1
- qscintilla-2.10.7

* Fri Jun 29 2018 Miro Hrončok <mhroncok@redhat.com> - 2.10.5-2
- Rebuilt for Python 3.7
- BR pythonX-devel not to be forgotten next time

* Sat Jun 23 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.10.5-1
- qscintilla-2.10.5

* Wed Apr 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.10.4-1
- qscintilla-2.10.4

* Fri Mar 23 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.10.3-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Mar 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.10.3-1
- qscintilla-2.10.3
- BR: gcc-c++, use %%make_build

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.10.2-2
- rebuild (qt5,PyQt5)

* Sat Nov 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.10.2-1
- qscintilla-2.10.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 05 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.10.1-1
- qscintilla-2.10.1

* Thu Apr 27 2017 Sandro Mani <manisandro@gmail.com> - 2.10-5
- Add python2-qscintilla-qt5

* Thu Mar 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.10-4
- rebuild (python-qt5), -qscintilla: relax pyqt runtime dep

* Wed Mar 01 2017 Sandro Mani <manisandro@gmail.com> - 2.10-3
- Fix incorrect requires for python3-qscintilla-qt5-devel on python-qt5-devel -> python3-qt5-devel

* Mon Feb 20 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.10-2
- -devel: introduce compat symlinks

* Mon Feb 20 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.10-1
- qscintilla-2.10

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 01 2017 Rex Dieter <rdieter@math.unl.edu> - 2.9.4-1
- qscintilla-2.9.4

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.9.3-3
- Rebuild for Python 3.6

* Wed Jul 27 2016 Rex Dieter <rdieter@fedoraproject.org> 2.9.3-2
- rebuild (python-qt5)

* Tue Jul 26 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.9.3-1
- qscintilla-2.9.3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Apr 28 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.9.2-4
- rebuild (python-qt5)

* Wed Apr 20 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.9.2-3
- rebuild (qt)

* Mon Apr 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.9.2-2
- support bootstapping
- rename qscintilla-python => python2-qscintilla
- Provides: python(2|3)-PyQt(4|5)-Qsci

* Mon Apr 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.9.2-1
- qscintilla-2.9.2

* Wed Apr 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.9.1-6
- rebuild (sip), Provides: python2-qscintilla(-devel)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Nov 05 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.1-3
- python3-qscintilla-qt5: use python3-qt5 consistently

* Wed Oct 28 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.1-2
- rebuild (python-qt5)

* Sat Oct 24 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.1-1
- qscintilla-2.9.1

* Tue Sep 08 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9-5
- -python-qt5: tighten python-qt5 dep (#1260876)

* Tue Jun 16 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9-4
- fix libqscintillaplugin.so linkage (#1231721)

* Sun Apr 26 2015 Rex Dieter <rdieter@fedoraproject.org> - 2.9-3
- use %%qmake_qt4 macroo
- Qt5 qscintilla2.prf is installed in bad location (#1215380)

* Thu Apr 23 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9-2
- Provides: bundled(scintilla) = 3.5.4

* Mon Apr 20 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9-1
- 2.9

* Wed Feb 18 2015 Orion Poplawski <orion@cora.nwra.com> - 2.8.4-3
- Rebuild for gcc 5 C++11

* Sun Dec 28 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.4-2
- enable -qt5 support

* Mon Sep 15 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.4-1
- QScintiall-2.8.4

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 03 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.3-1
- QScintiall-2.8.3

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.3-0.3.9b7b5393f228
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun 04 2014 Rex Dieter <rdieter@fedoraproject.org> - 2.8.3-0.2.9b7b5393f228
- QScintilla-gpl-2.8.3-snapshot-9b7b5393f228
- python: explicitly set QMAKEFEATURES (bug #1104559)

* Mon Jun 02 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.3-0.1.f7b1c9821894
- QScintiall-2.8.3-f7b1c9821894 snapshot (2.8.2 FTBFS)

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 2.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Mar 17 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.1-3
- enable python3 bindings (#1065223)

* Mon Mar 17 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.1-2
- designer plugin: Undefined reference to QsciScintilla::QsciScintilla... (#1077146)

* Sun Mar 16 2014 Rex Dieter <rdieter@fedoraproject.org> - 2.8.1-1
- QScintilla-2.8.1
- Provides: python-qscintilla
- experimental qt5/python3 support (not enabled yet)

* Fri Nov 08 2013 Rex Dieter <rdieter@fedoraproject.org> 2.8-1
- QScintilla-2.8

* Wed Oct 16 2013 Rex Dieter <rdieter@fedoraproject.org> 2.7.2-3
- rebuild (PyQt4), refresh incpath patch

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 18 2013 Rex Dieter <rdieter@fedoraproject.org> - 2.7.2-1
- QScintilla-2.7.2
- prune changelog

* Mon Jun 17 2013 Rex Dieter <rdieter@fedoraproject.org> 2.7.1-2
- rebuild (sip)

* Sun Mar 03 2013 Rex Dieter <rdieter@fedoraproject.org> 2.7.1-1
- 2.7.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 17 2012 Rex Dieter <rdieter@fedoraproject.org> 2.7-1
- 2.7

* Mon Oct 01 2012 Rex Dieter <rdieter@fedoraproject.org> 2.6.2-3
- rebuild (sip)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Rex Dieter <rdieter@fedoraproject.org> 2.6.2-1
- 2.6.2

* Sat Feb 11 2012 Rex Dieter <rdieter@fedoraproject.org> 2.6.1-1
- 2.6.1
- pkgconfig-style deps

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 23 2011 Rex Dieter <rdieter@fedoraproject.org> 2.6-2
- rebuild (sip/PyQt4)

* Sat Dec 03 2011 Rex Dieter <rdieter@fedoraproject.org> 2.6-1
- 2.6

* Fri Nov 11 2011 Rex Dieter <rdieter@fedoraproject.org> 2.5.1-2
- rebuild (sip)

* Fri May 06 2011 Rex Dieter <rdieter@fedoraproject.org> 2.5.1-1
- 2.5.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 24 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.4.6-1
- 2.4.6

* Thu Sep 09 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.4.5-1
- 2.4.5

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 14 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.4.4-1
- 2.4.4

* Thu Mar 18 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.4.3-1
- 2.4.3

* Thu Jan 21 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.4.2-1
- 2.4.2

* Fri Jan 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.4.1-1
- 2.4.1
- pyqt4_version 4.7

* Thu Jan 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.4-10
- rebuild (sip)

* Fri Nov 27 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.4-9
- -python: Requires: sip-api(%%_sip_api_major) >= %%_sip_api
- -python-devel: Requires: sip-devel

* Mon Nov 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.4-8
- rebuild (for qt-4.6.0-rc1, f13+)

* Wed Nov 11 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.4-7
- pyqt4_version 4.6.1

* Wed Oct 21 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.4-6
- autocomplete_popup patch

* Fri Oct 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.4-5
- rebuild (PyQt4)

* Tue Aug 11 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.4-4
- -python-devel: make noarch, drop dep on -python

* Sat Aug 08 2009 Rex Dieter <rdieter@fedoraproject.org - 2.4-3
- include designer plugin in main pkg, Obsoletes: qscintilla-designer

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.4-1
- QScintilla-gpl-2.4

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.3.2-2
- Rebuild for Python 2.6

* Mon Nov 17 2008 Rex Dieter <rdieter@fedoraproject.org> - 2.3.2-1
- Qscintilla-gpl-2.3.2
- soname bump 4->5

* Mon Nov 10 2008 Rex Dieter <rdieter@fedoraproject.org> - 2.3.1-1
- Qscintilla-gpl-2.3.1

* Mon Sep 22 2008 Rex Dieter <rdieter@fedoraproject.org> - 2.3-1
- Qscintilla-gpl-2.3
- scintilla_ver is missing (#461777)

* Fri Jul 18 2008 Dennis Gilmore <dennis@ausil.us> - 2.2-3
- rebuild for newer PyQT4
- fix #449423 properly

* Fri Jul 18 2008 Rex Dieter <rdieter@fedoraproject.org> - 2.2-2
- fix build (#449423)

* Mon May 05 2008 Rex Dieter <rdieter@fedoraproject.org> - 2.2-1
- Qscintilla-gpl-2.2
- License: GPLv3 or GPLv2 with exceptions

* Thu Feb 14 2008 Rex Dieter <rdieter@fedoraproject.org> - 2.1-4
- use %%_qt4_* macros (preparing for qt4 possibly moving %%_qt4_datadir)
- -python: fix Requires
- -python-devel: new pkg
- omit Obsoletes: PyQt-qscintilla
  (leave that to PyQt, that can get the versioning right)

* Mon Jan 28 2008 Dennis Gilmore <dennis@ausil.us> - 2.1-3
- fix typo in Obsoletes: on python package

* Mon Jan 28 2008 Dennis Gilmore <dennis@ausil.us> - 2.1-2
- remove dumb require on di from qscintilla-python

* Mon Jan 28 2008 Dennis Gilmore <dennis@ausil.us> - 2.1-1
- update to 2.1 branch
