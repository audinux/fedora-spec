# Tag: Editor
# Type: Standalone
# Category: Audio

Name:    opl3bankeditor
Version: 1.5.1
Release: 2%{?dist}
Summary: A small cross-platform editor of the OPL3 FM banks of different formats
URL:     https://github.com/Wohlstand/OPL3BankEditor
License: GPL-3.0-only

Vendor:       Audinux
Distribution: Audinux

# ./opl3bankeditor-source.sh <tag>
# ./opl3bankeditor-source.sh v1.5.1

Source0: OPL3BankEditor.tar.gz
Source1: opl3bankeditor-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
%if 0%{?fedora} >= 38
BuildRequires: qwt-qt5-devel
%else
BuildRequires: qwt-devel
%endif
BuildRequires: qt5-qtserialport-devel
BuildRequires: zlib-devel
BuildRequires: desktop-file-utils

%description
A small cross-platform editor of the OPL3 FM banks of different formats

%prep

%autosetup -n OPL3BankEditor

sed -i -e "/Categories/d" src/resources/opl3_bank_editor.desktop

%build

%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DLIBEXEC_INSTALL_DIR=%{_libexecdir}

%cmake_build

%install

%cmake_install

desktop-file-install --vendor '' \
        --add-category=Midi \
        --add-category=Audio \
        --add-category=AudioVideo \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/opl3_bank_editor.desktop

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/opl3_bank_editor.desktop

%files
%doc README.md changelog.txt
%license LICENSE license.txt
%{_bindir}/opl3_bank_editor
%{_datadir}/mime/*
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/opl3_bank_editor/

%changelog
* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 1.5.1-2
- update to 1.5.2 - fix for fedora 33

* Tue Jun 2 2020 Yann Collette <ycollette.nospam@free.fr> - 1.5.1-1
- update to 1.5.1

* Fri Mar 22 2019 Yann Collette <ycollette.nospam@free.fr> - 1.5.0-1
- initial release of the spec file
