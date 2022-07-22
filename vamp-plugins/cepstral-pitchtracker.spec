# Tag: Effect, Analyzer
# Type: Plugin, VAMP
# Category: Audio, Effect

Name: cepstral-pitchtracker
Version: 1.0
Release: 2%{?dist}
Summary: A straightforward cepstral pitch- and note-tracker Vamp plugin, probably most suited to tracking singing pitch
License: GLPv2	
URL: https://code.soundsoftware.ac.uk/projects/cepstral-pitchtracker	

Vendor:       Audinux
Distribution: Audinux

Source0: https://code.soundsoftware.ac.uk/attachments/download/626/cepstral-pitchtracker-%{version}.tar.gz

BuildRequires: gcc gcc-c++ make
BuildRequires: vamp-plugin-sdk-devel
BuildRequires: boost-devel

%description
A straightforward cepstral pitch- and note-tracker Vamp plugin,
probably most suited to tracking singing pitch

%package -n vamp-%{name}
Summary: %{name} VAMP plugin

%description -n vamp-%{name}
A straightforward cepstral pitch- and note-tracker Vamp plugin,
probably most suited to tracking singing pitch

%prep
%autosetup -n %{name}-%{version}

sed -i -e "s/CFLAGS := -Wall -g -fPIC/CFLAGS := -fPIC \$(CFLAGS)/g" Makefile.linux64
sed -i -e "s/CXXFLAGS := \$(CFLAGS)/CXXFLAGS := -fPIC \$(CXXFLAGS)/g" Makefile.linux64
sed -i -e "s/-shared -Wl,-Bstatic -lvamp-sdk -Wl,-Bdynamic/-lvamp-sdk/g" Makefile.linux64
sed -i -e "s/all: \$(PLUGIN) \$(TESTS)/all: \$(PLUGIN)/g" Makefile.inc
sed -i -e "/Running/d" Makefile.inc

%build

%set_build_flags
export LDFLAGS="-shared $LDFLAGS"

%make_build -f Makefile.linux64 all

%install

install -m 755 -d %{buildroot}/%{_libdir}/vamp/
install -m 755 cepstral-pitchtracker.so  %{buildroot}/%{_libdir}/vamp/
install -m 644 cepstral-pitchtracker.cat %{buildroot}/%{_libdir}/vamp/
install -m 644 cepstral-pitchtracker.n3  %{buildroot}/%{_libdir}/vamp/

%files -n vamp-%{name}
%doc README
%{_libdir}/vamp/cepstral-pitchtracker.*

%changelog
* Fri Jul 22 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0-2
- update to 1.0-2

* Mon Jan 10 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- Initial spec file

