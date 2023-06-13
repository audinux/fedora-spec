Name:    structure-synth
Version: 1.5.0
Release: 2%{?dist}
Summary: Structure Synth generates 3D structures by specifying a design grammar
License: GPL-2.0-only
URL:     https://sourceforge.net/projects/structuresynth/

Vendor:       Audinux
Distribution: Audinux

# svn checkout https://svn.code.sf.net/p/structuresynth/code/trunk structuresynth
# cd structuresythn
# finf . -nams .svn -exec rm -rf {} \,
# cd ..
# tar cvfz structuresynth.tar.gz structuresynth
# rm -rf structuresynth

Source0: structuresynth.tar.gz
Source1: structure-synth.1
Patch0: structuresynth-nullptr.patch
Patch1: structuresynth-qmake.patch
Patch2: structuresynth-abs_data_path.patch
Patch3: structuresynth-sunflow.patch
Patch4: structuresynth-0001-add-missing-header.patch

BuildRequires: gcc gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtscript-devel
BuildRequires: freeglut-devel
BuildRequires: desktop-file-utils

%description
Structure Synth generates 3D structures by specifying a design grammar.
Even simple systems may generate surprising and complex structures.
Structure Synth offers a graphical environment with multiple tabs, syntax highlighting, and OpenGL preview.

%prep
%autosetup -p1 -n structuresynth

%build

%qmake_qt5 StructureSynth.pro
%make_build

%install

mkdir -p %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}/%{_datadir}/structure-synth/Examples
mkdir -p %{buildroot}/%{_datadir}/structure-synth/Misc
mkdir -p %{buildroot}/%{_datadir}/applications/
mkdir -p %{buildroot}/%{_datadir}/pixmaps/
mkdir -p %{buildroot}/%{_mandir}/man1/

cp -r Examples/* %{buildroot}/%{_datadir}/structure-synth/Examples/
cp -r Misc/* %{buildroot}/%{_datadir}/structure-synth/Misc/
cp StructureSynthBin %{buildroot}/%{_bindir}/structure-synth
cp structure-synth.desktop %{buildroot}/%{_datadir}/applications/
cp images/structuresynth.png %{buildroot}/%{_datadir}/pixmaps/structure-synth.png
cp %{SOURCE1} %{buildroot}/%{_mandir}/man1/

desktop-file-install                         \
  --add-category="Graphics"                  \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/structure-synth.desktop

%files
%doc changelog.txt notes.txt bugs.txt
%license LICENSE.GPL3 LICENSE.LGPL LICENSE.README
%{_bindir}/*
%{_datadir}/*

%changelog
* Fri Sep 25 2020 Yann Collette <ycollette.nospam@free.fr> - 1.5.0-2
- apply debian patches + man page + naming + install

* Fri Sep 25 2020 Yann Collette <ycollette.nospam@free.fr> - 1.5.0-1
- initial-version

