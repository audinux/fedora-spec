# Status: active
# Tag: Jack, Loop
# Type: Standalone
# Category: Audio, Sequencer

Name: kluppe
Version: 0.6.20
Release: 1%{?dist}
Summary: kluppe is a loop-player and recorder, designed for live use
License: GPL-2.0
URL: https://kluppe.klingt.org/index.html
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://kluppe.klingt.org/downloads/kluppe-%{version}.tar.gz
Patch0: kluppe-0001-fix-makefiles.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: libsndfile-devel
BuildRequires: gtk2-devel
BuildRequires: libxml2-devel
BuildRequires: libusb-compat-0.1-devel
BuildRequires: liblo-devel
BuildRequires: pkgconfig(jack)
BuildRequires: desktop-file-utils

%description
kluppe is a loop-player and recorder, designed for live use.
kluppe is open source.
kluppe does not sound nor look like microsoft excel
kluppe is the austrian word for clip or peg and sounds even crazier if you loop it.

%prep
%autosetup -p1 -n %{name}-%{version}

%build

%set_build_flags

export MYFLAGS=`echo $CFLAGS | sed -e "s|-Werror=format-security||g"`

%make_build

%install

%make_install

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=%{name}
Icon=%{name}
Comment=kluppe is a loop-player and recorder, designed for live use
Terminal=false
Type=Application
Categories=AudioVideo;Audio;
EOF

desktop-file-install                         \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.txt
%license LICENSE.txt
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{_mandir}/man1/*

%changelog
* Mon Oct 07 2024 Yann Collette <ycollette.nospam@free.fr> - 0.6.20-1
- Initial development
