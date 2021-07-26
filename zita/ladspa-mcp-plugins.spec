# Tag:  Effect
# Type: LADSPA
# Category: Audio

Summary: A set of Moog filters LADSPA plugin
Name:    MCP-plugins
Version: 0.4.0
Release: 1%{?dist}
License: GPL

Vendor:       Audinux
Distribution: Audinux

URL:     http://kokkinizita.linuxaudio.org/linuxaudio/

Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/MCP-plugins-%{version}.tar.bz2

BuildRequires: gcc gcc-c++ make
BuildRequires: ladspa-devel

%description
Sources for MCP-plugins.

%package -n ladspa-mcp-plugins
Summary: A set of Moog filters LADSPA plugin

%description -n ladspa-mcp-plugins
A set of Moog filters LADSPA plugin

%prep
%autosetup

# Force Fedora's optflags
sed -i 's|-O3|%{optflags}|' Makefile
sed -i 's|/usr/lib/ladspa|$(DESTDIR)/usr/%{_lib}/ladspa|g' Makefile

%build

%make_build PREFIX=%{_prefix}

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ladspa
%make_install BINDIR=%{_libdir}/ladspa

%files -n ladspa-mcp-plugins
%doc AUTHORS
%license COPYING
%{_libdir}/ladspa/*

%changelog
* Mon Jul 26 2021 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-1
- initial spec file
