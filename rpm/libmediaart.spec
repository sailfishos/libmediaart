Name:       libmediaart
Summary:    Library for handling media art
Version:    0.3.0
Release:    1
Group:      System/Libraries
License:    GPLv2
URL:        https://git.gnome.org/browse/libmediaart
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(glib-2.0) >= 2.36.0
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  gobject-introspection-devel >= 1.36
BuildRequires:  vala-devel
BuildRequires:  vala-tools

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
%autogen --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%{_libdir}/*
