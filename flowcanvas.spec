%define major 3
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		flowcanvas
Version:	0.6.0
Release:	%mkrel 1
Summary:	An interactive Gtkmm/Gnomecanvasmm widget
License:	GPLv2+
Group:		System/Libraries
Url:		http://drobilla.net/software/flowcanvas/
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	waf
BuildRequires:	gtkmm2.4-devel
BuildRequires:	libgnomecanvasmm2.6-devel
BuildRequires:	boost-devel
BuildRequires:	graphviz-devel

%description
FlowCanvas is an interactive Gtkmm/Gnomecanvasmm widget for "boxes 
and lines" style environments (e.g. modular synths or interactive 
finite state automata diagrams).

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}

%description -n %{libname}
FlowCanvas is an interactive Gtkmm/Gnomecanvasmm widget for "boxes
and lines" style environments (e.g. modular synths or interactive
finite state automata diagrams).

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/GNOME and GTK+

Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description -n %{develname}
This package contains development files for %{name}.

%prep
%setup -q

%build
%setup_compile_flags
%__waf configure \
	--prefix=%{_prefix} \
	--datadir=%{_datadir} \
	--libdir=%{_libdir} \
	--includedir=%{_includedir}

%__waf build

%install
rm -rf %{buildroot}
%waf_install

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%{_libdir}/lib%{name}.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}
