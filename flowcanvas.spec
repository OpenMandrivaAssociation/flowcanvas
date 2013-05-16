%define major 5

%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:       flowcanvas
Version:    0.7.1
Release:    3

Summary:    An interactive Gtkmm/Gnomecanvasmm widget
License:    GPLv2+
Group:      System/Libraries
Url:        http://drobilla.net/software/flowcanvas/
Source0:    http://download.drobilla.net/%{name}-%{version}.tar.bz2
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  waf
BuildRequires:  gtkmm2.4-devel
BuildRequires:  pkgconfig(libgnomecanvasmm-2.6)
BuildRequires:  boost-devel
BuildRequires:  graphviz-devel

%description
FlowCanvas is an interactive Gtkmm/Gnomecanvasmm widget for "boxes
and lines" style environments (e.g. modular synths or interactive
finite state automata diagrams).

%package -n %{libname}
Summary:    %{summary}
Group:      %{group}

Provides:   %{name} = %{version}-%{release}

%description -n %{libname}
FlowCanvas is an interactive Gtkmm/Gnomecanvasmm widget for "boxes
and lines" style environments (e.g. modular synths or interactive
finite state automata diagrams).

%package -n %{develname}
Summary:    Development files for %{name}
Group:      Development/GNOME and GTK+

Provides:   %{name}-devel = %{version}-%{release}
Requires:   %{libname} = %{version}

%description -n %{develname}
This package contains development files for %{name}.

%prep
%setup -q

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
rm -rf %{buildroot}
./autowaf/waf install --destdir=%{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%{_libdir}/lib%{name}.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}


%changelog
* Sat Dec 24 2011 Frank Kober <emuse@mandriva.org> 0.7.1-3
+ Revision: 745010
- rebuild to link against newer libpng

* Wed May 11 2011 Funda Wang <fwang@mandriva.org> 0.7.1-2
+ Revision: 673597
- rebuild for new graphviz

* Thu Jan 20 2011 Frank Kober <emuse@mandriva.org> 0.7.1-1
+ Revision: 631905
- new version 0.7.1
  o new major.minor 5.1
  o do not obsolete old major pkg
  o workaround waf execution path
- new version 0.7.1
  o new major.minor 5.1
  o do not obsolete old major pkg
  o workaround waf execution path

* Fri Nov 19 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.6.4-4mdv2011.0
+ Revision: 599041
- Don't obsolete old major lib

* Sat Nov 06 2010 Frank Kober <emuse@mandriva.org> 0.6.4-3mdv2011.0
+ Revision: 594242
- Clean spec formatting
- Obsolete old major

* Mon Nov 01 2010 Frank Kober <emuse@mandriva.org> 0.6.4-2mdv2011.0
+ Revision: 591550
- fix major

* Sun Oct 31 2010 Frank Kober <emuse@mandriva.org> 0.6.4-1mdv2011.0
+ Revision: 591197
- new version 0.6.4

* Sun Aug 29 2010 Frank Kober <emuse@mandriva.org> 0.6.0-3mdv2011.0
+ Revision: 574194
- rebuild for gdk-pixbuf

* Tue Jan 19 2010 Jérôme Brenier <incubusss@mandriva.org> 0.6.0-2mdv2010.1
+ Revision: 493740
- add a Provides : flowcanvas for the lib subpackage

* Tue Jan 19 2010 Jérôme Brenier <incubusss@mandriva.org> 0.6.0-1mdv2010.1
+ Revision: 493738
- import flowcanvas


