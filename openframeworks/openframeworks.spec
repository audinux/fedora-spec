Name:    openFrameworks
Version: 0.12.0
Release: 2%{?dist}
Summary: openFrameworks library / code
URL:     https://github.com/openframeworks/openFrameworks
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

# to get the sources:
# ./source_openframeworks.sh 0.12.0

Source0: openFrameworks.tar.gz
Source1: of-make-workspace
Source2: source_openframeworks.sh

BuildRequires: gcc gcc-c++ make
BuildRequires: freeimage-devel
BuildRequires: uriparser-devel
BuildRequires: pugixml-devel
BuildRequires: poco-devel
BuildRequires: openal-soft-devel
BuildRequires: cairo-devel
%if 0%{?fedora} >= 32
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-base-devel
%else
BuildRequires: gstreamer-devel
BuildRequires: gstreamer-plugins-base-devel
%endif
BuildRequires: systemd-devel
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: libsndfile-devel
BuildRequires: libcurl-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: alsa-lib-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: glew-devel
BuildRequires: freeglut-devel
BuildRequires: glfw-devel
BuildRequires: boost-devel
BuildRequires: opencv-devel
BuildRequires: rtaudio-devel
BuildRequires: mpg123-devel
BuildRequires: libXcursor-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libXrandr-devel
BuildRequires: chrpath
#BuildRequires: python2-lxml
#BuildRequires: assimp-devel

%description
openFrameworks is a C++ toolkit for creative coding. If you are new to OF, welcome!

The Project Generator is in /opt/openFrameworks/apps/projectGenerator/projectGeneratorSimple.
To initialize the workspace needed for openFrameworks launch the command: '/opt/openFrameworks/scripts/of-make-workspace'
this command will initialize a workspace folder, with no path given the default folder is: ~/of-workspace.

Remeber to regenerate your local workspace using: '/opt/openFrameworks/scripts/of-make-workspace'
If you already have a local workspace, BACKUP YOUR PROJECTS BEFORE generating a new local workspace.

%prep
%autosetup -n %{name}

%build

export OF_ROOT=`pwd`
export LC_ALL=C

ARCH=$(uname -m)

if [ "$ARCH" = "x86_64" ]; then
    LIBSPATH=linux64
else
    LIBSPATH=linux
fi

%set_build_flags

export CFLAGS=`echo $CFLAGS | sed -e "s|-Werror=format-security||g"`
export CXXFLAGS=`echo $CXXFLAGS | sed -e "s|-Werror=format-security||g"`

cd libs/openFrameworksCompiled/project
%make_build Release

cd ../../..

cd apps/projectGenerator/commandLine
%make_build -j1 Release

cd ../../..
cd libs/openFrameworksCompiled/project
%make_build Release

%install

install -dm755 %{buildroot}/%{_bindir}/
install -Dm755 apps/projectGenerator/commandLine/bin/projectGenerator %{buildroot}/%{_bindir}/projectGenerator

install -dm755 %{buildroot}/opt/openFrameworks
cp -R . %{buildroot}/opt/openFrameworks

install -Dm775 %{SOURCE1} %{buildroot}/opt/openFrameworks/scripts/of-make-workspace

sed -i -e "s/env python/env python2/g" %{buildroot}/opt/openFrameworks/scripts/dev/parsePRs.py

rm -rf %{buildroot}/opt/openFrameworks/.appveyor.yml
rm -rf %{buildroot}/opt/openFrameworks/.gitattributes
rm -rf %{buildroot}/opt/openFrameworks/.gitignore
rm -rf %{buildroot}/opt/openFrameworks/.gitmodules
rm -rf %{buildroot}/opt/openFrameworks/.travis.yml
rm -rf %{buildroot}/opt/openFrameworks/.package*
chrpath --delete %{buildroot}%{_bindir}/projectGenerator
chrpath --delete %{buildroot}/opt/openFrameworks/apps/projectGenerator/commandLine/bin/projectGenerator

%files
%doc README.md
%license LICENSE.md
%{_bindir}/*
/opt/%{name}/*

%changelog
* Thu Aug 31 2023 Yann Collette <ycollette.nospam@free.fr> - 0.12.0-2
- update to 0.12.0-2

* Thu Mar 25 2021 Yann Collette <ycollette.nospam@free.fr> - 0.11.2-2
- update to 0.11.2

* Wed Mar 3 2021 Yann Collette <ycollette.nospam@free.fr> - 0.11.1-2
- update to 0.11.1

* Tue Oct 6 2020 Yann Collette <ycollette.nospam@free.fr> - 0.11.0-2
- fix for fedora 33

* Sat May 23 2020 Yann Collette <ycollette.nospam@free.fr> - 0.11.0-1
- initial specfile
