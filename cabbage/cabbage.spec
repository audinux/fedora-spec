# Tag: Tool
# Type: Plugin, LV2, VST
# Category: Audio, Tool, Programming

Name:    cabbage
Version: 2.9.0
Release: 2%{?dist}
Summary: Framework for developing audio plugins with the Csound programming language.
URL:     https://github.com/rorywalsh/cabbage
License: GPLv3+

Vendor:       Audinux
Distribution: Audinux

# Usage: ./cabbage-sources.sh <TAG>
# ./cabbage-sources.sh v2.9.0

Source0: cabbage.tar.gz
Source1: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip
Source3: cabbage-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: unzip
BuildRequires: csound-devel
BuildRequires: freetype-devel
BuildRequires: libpng-devel
BuildRequires: harfbuzz-devel
BuildRequires: glib2-devel
BuildRequires: alsa-lib-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel
BuildRequires: libcurl-devel
BuildRequires: libsndfile-devel
BuildRequires: desktop-file-utils

Requires: csound-manual

%description
Cabbage. A framework for developing audio plugins and standalone
instruments using the Csound programming language.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n vst-%{name}
Summary:  VST version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst-%{name}
VST version of %{name}

%prep
%autosetup -n %{name}

sed -i -e "s/;Multimedia//g" Installers/Linux/Cabbage.desktop
sed -i -e "s/VST3_SDK/VST2_SDK/g" CMakeLists.txt
#sed -i -e "s/ VST//g" CMakeLists.txt
#sed -i -e "s/ AU//g" CMakeLists.txt

# Install VST SDKs

mkdir SDKs
unzip %{SOURCE1}
mv VST_SDK SDKs/

%build

export HOME=`pwd`
%set_build_flags
export CXXFLAGS="-fPIC $CXXFLAGS"
export CFLAGS="-fPIC $CFLAGS"

PROJECTS="Cabbage CabbagePluginEffect CabbagePluginSynth CabbagePluginMidiEffect" # CLIConverter
for Files in $PROJECTS
do
  %cmake -DPROJECT_NAME=$Files
  %cmake_build
  mv %{__cmake_builddir} build_$Files
done

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/vst/
install -m 755 -d %{buildroot}/%{_libdir}/vst3/

cp build_Cabbage/Cabbage_artefacts/Debug/Cabbage %{buildroot}/%{_bindir}/

cp build_CabbagePluginEffect/CabbagePluginEffect_artefacts/Debug/Standalone/* %{buildroot}/%{_bindir}/
cp build_CabbagePluginEffect/CabbagePluginEffect_artefacts/Debug/VST/* %{buildroot}/%{_libdir}/vst/
cp -rav build_CabbagePluginEffect/CabbagePluginEffect_artefacts/Debug/VST3/* %{buildroot}/%{_libdir}/vst3/

cp build_CabbagePluginEffect/CabbagePluginEffect_artefacts/Debug/Standalone/* %{buildroot}/%{_bindir}/
cp build_CabbagePluginEffect/CabbagePluginEffect_artefacts/Debug/VST/* %{buildroot}/%{_libdir}/vst/
cp -rav build_CabbagePluginEffect/CabbagePluginEffect_artefacts/Debug/VST3/* %{buildroot}/%{_libdir}/vst3/

cp build_CabbagePluginMidiEffect/CabbagePluginMidiEffect_artefacts/Debug/Standalone/* %{buildroot}/%{_bindir}/
cp build_CabbagePluginMidiEffect/CabbagePluginMidiEffect_artefacts/Debug/VST/* %{buildroot}/%{_libdir}/vst/
cp -rav build_CabbagePluginMidiEffect/CabbagePluginMidiEffect_artefacts/Debug/VST3/* %{buildroot}/%{_libdir}/vst3/

# Cabbage install of VST / VST3 files in the binary directory (required)
cp build_CabbagePluginSynth/CabbagePluginSynth_artefacts/Debug/VST/libCabbagePluginSynth.so %{buildroot}/%{_bindir}/CabbagePluginSynth.so
cp build_CabbagePluginEffect/CabbagePluginEffect_artefacts/Debug/VST/libCabbagePluginEffect.so %{buildroot}/%{_bindir}/CabbagePluginEffect.so

#cp build_CLIConverter/CLIConverter_artefacts/Debug/* %{buildroot}/%{_bindir}/

# Install some directories
install -m 755 -d %{buildroot}%{_datadir}/cabbage/docs/
install -m 755 -d %{buildroot}%{_datadir}/cabbage/examples/
install -m 755 -d %{buildroot}%{_datadir}/cabbage/themes/

cp -rav Docs/* %{buildroot}%{_datadir}/cabbage/docs/
cp -rav Examples/* %{buildroot}%{_datadir}/cabbage/examples/
cp -rav Themes/* %{buildroot}%{_datadir}/cabbage/themes/

# Create some desktop files
install -m 755 -d %{buildroot}%{_datadir}/applications/
cp Installers/Linux/Cabbage.desktop %{buildroot}%{_datadir}/applications/

install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/apps/512x512/

cp Images/cabbage.png %{buildroot}/%{_datadir}/icons/hicolor/apps/512x512/
cp Images/CabbageLogo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/cabbage.svg

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/Cabbage.desktop

# Cleanup
rm -rf %{buildroot}/%{_datadir}/cabbage/docs/PythonUtilityScripts/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/Cabbage.desktop

%files
%doc readme.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/icons/hicolor/apps/512x512/*
%{_datadir}/cabbage/
%{_datadir}/cabbage/docs/*
%{_datadir}/cabbage/examples/*
%{_datadir}/cabbage/themes/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Tue Feb 14 2023 Yann Collette <ycollette.nospam@free.fr> - 2.9.0-1
- Initial spec file
