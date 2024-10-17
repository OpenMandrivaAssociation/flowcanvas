%define major 5
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	An interactive Gtkmm/Gnomecanvasmm widget
Name:		flowcanvas
Version:	0.7.1
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		https://drobilla.net/software/flowcanvas/
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.bz2
Patch1:		flowcanvas-0.7.1-graphviz23.patch
BuildRequires:	waf
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(libgnomecanvasmm-2.6)
BuildRequires:	pkgconfig(libgvc)

%description
FlowCanvas is an interactive Gtkmm/Gnomecanvasmm widget for "boxes
and lines" style environments (e.g. modular synths or interactive
finite state automata diagrams).

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	An interactive Gtkmm/Gnomecanvasmm widget library
Group:		System/Libraries

%description -n %{libname}
FlowCanvas is an interactive Gtkmm/Gnomecanvasmm widget for "boxes
and lines" style environments (e.g. modular synths or interactive
finite state automata diagrams).

%files -n %{libname}
%doc AUTHORS README ChangeLog
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
This package contains development files for %{name}.

%files -n %{devname}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/

#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%setup_compile_flags
./waf configure \
	--prefix=%{_prefix} \
	--datadir=%{_datadir} \
	--libdir=%{_libdir} \
	--includedir=%{_includedir} \

# execution of waf link in source topdir fails to include autowaf.py:

./autowaf/waf build

%install
./autowaf/waf install --destdir=%{buildroot}

chmod 0755 %{buildroot}%{_libdir}/lib%{name}.so.%{major}*

