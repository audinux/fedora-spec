# Tag: Tool, AI
# Type: Plugin, LV2, VST3, Standalone
# Category: Audio, Tool

%global commit0 8c71defc996582ddd500dd68098603a20f5a5b8b
Name: ratatouille
Version: 0.0.1
Release: 1%{?dist}
Summary: Ratatouille is a Neural Model loader and mixer
License: BSD-3-Clause
URL: https://github.com/brummer10/Ratatouille.lv2

Vendor:       Audinux
Distribution: Audinux

# ./brummer10-source.sh <project> <tag>
# ./brummer10-source.sh Ratatouille.lv2 8c71defc996582ddd500dd68098603a20f5a5b8b

Source0: Ratatouille.lv2.tar.gz
Source1: brummer10-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: cairo-devel
BuildRequires: libX11-devel

%description
Ratatouille is a Neural Model loader and mixer for Linux/Windows.
It can load two models, which can be *.nam files with the Neural
Amp Modeler module, or *.json or .aidax files with the RTNeural module.

You can also load just a single model file, in that case the "Blend"
control will do nothing. When you've loaded a second model, the "Blend"
control will blend between the two models and mix them to simulate your
specific tone.

Ratatouille.lv2 supports resampling when needed to match the expected
sample rate of the loaded models. Both models may have different
expectations regarding the sample rate.

%package -n lv2-%{name}
Summary: LV2 version of the %{name} plugin.

%description -n lv2-%{name}
LV2 version of the %{name} plugin.

%prep
%autosetup -n Ratatouille.lv2

%build

%set_build_flags

%make_build STRIP=true

%install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/

cp -ra bin/Ratatouille.lv2  %{buildroot}/%{_libdir}/lv2/

%files
%doc README.md
%license LICENSE

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Tue Apr 09 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file