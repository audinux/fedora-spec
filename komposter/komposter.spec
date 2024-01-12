# Tag: Modular, Alsa
# Type: Standalone
# Category: Sequencer, Synthesizer

Name: komposter
Version: 0.1
Release: 1%{?dist}
Summary: Modular virtual analog software synthesizer and sequencer for 4KB and 64KB intros

License: GPL-2.0
URL: https://github.com/electronoora/komposter
Source0: https://github.com/electronoora/komposter/archive/refs/heads/master.zip#/komposter.zip

BuildRequires: gcc gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libglvnd-devel
BuildRequires: openal-soft-devel
BuildRequires: freeglut-devel
BuildRequires: freetype-devel

%description
Modular virtual analog software synthesizer and sequencer for 4KB and 64KB intros

%prep
%autosetup -n %{name}-master

./autogen.sh

%build
%configure
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_datadir}/%{name}/examples/
cp -r examples/* %{buildroot}%{_datadir}/%{name}/examples/

mkdir -p %{buildroot}%{_datadir}/%{name}/doc/
cp -r doc/* %{buildroot}%{_datadir}/%{name}/doc/

mkdir -p %{buildroot}%{_datadir}/%{name}/resources/shaders/
cp -r resources/*.ttf %{buildroot}%{_datadir}/%{name}/resources/
cp -r resources/*.TTF %{buildroot}%{_datadir}/%{name}/resources/
cp -r resources/shaders/* %{buildroot}%{_datadir}/%{name}/resources/shaders/

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
cp -r resources/komposter_icon.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/%{name}/doc/*
%{_datadir}/%{name}/resources/*
%{_datadir}/%{name}/examples/*
%{_datadir}/icons/*

%changelog
* Sun Feb 13 2022 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial version of the spec file
