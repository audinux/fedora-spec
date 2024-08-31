# Status: active
# Tag: Effect, Analyzer
# Type: Plugin, VAMP
# Category: Audio, Effect

Name: pyin
Version: 1.2
Release: 2%{?dist}
Summary: pYIN (Probabilistic YIN) is a modification of the well-loved YIN algorithm for fundamental frequency (F0) estimation in monophonic audio
License: GLPv2
URL: https://code.soundsoftware.ac.uk/projects/pyin
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://code.soundsoftware.ac.uk/attachments/download/2627/pyin-v%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: vamp-plugin-sdk-devel
BuildRequires: boost-devel

%description
pYIN (Probabilistic YIN) is a modification of the well-loved YIN
algorithm for fundamental frequency (F0) estimation in monophonic audio

%package -n vamp-%{name}
Summary: %{name} VAMP plugin

%description -n vamp-%{name}
pYIN (Probabilistic YIN) is a modification of the well-loved YIN
algorithm for fundamental frequency (F0) estimation in monophonic audio

%prep
%autosetup -n %{name}-v%{version}

sed -i -e "s/-Wl,-Bstatic//g" Makefile.linux64

%build

%set_build_flags

%make_build -f Makefile.linux64

%install

install -m 755 -d %{buildroot}/%{_libdir}/vamp/
install -m 755 pyin.so  %{buildroot}/%{_libdir}/vamp/
install -m 644 pyin.cat %{buildroot}/%{_libdir}/vamp/
install -m 644 pyin.n3  %{buildroot}/%{_libdir}/vamp/

%files -n vamp-%{name}
%license COPYING
%doc README
%{_libdir}/vamp/pyin.*

%changelog
* Fri Jul 22 2022 Yann Collette <ycollette.nospam@free.fr> - 1.2-2
- update to 1.2-2

* Wed Jan 12 2022 Yann Collette <ycollette.nospam@free.fr> - 1.2-1
- Initial spec file

