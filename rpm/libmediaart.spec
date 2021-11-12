Name:       libmediaart
Summary:    Library for handling media art
Version:    1.9.5
Release:    1
License:    LGPLv2+
URL:        https://git.gnome.org/browse/libmediaart
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(glib-2.0) >= 2.36.0
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  gobject-introspection-devel >= 1.36
BuildRequires:  vala-devel
BuildRequires:  vala-tools
BuildRequires:  meson

%description
%{summary}.

%package devel
Summary: Development package for libmediaart
Requires: %{name} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%meson -Dimage_library=qt5
%meson_build

%install
%meson_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libmediaart-2.0.so.*
%{_libdir}/girepository-1.0/MediaArt-2.0.typelib
%license COPYING.LESSER

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libmediaart-2.0.pc
%{_libdir}/libmediaart-2.0.so
%{_includedir}/libmediaart-2.0
%{_datadir}/gir-1.0/MediaArt-2.0.gir
%{_datadir}/vala/vapi/libmediaart-2.0.vapi
%{_datadir}/vala/vapi/libmediaart-2.0.deps
