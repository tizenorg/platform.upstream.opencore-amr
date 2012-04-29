#sbs-git:slp/unmodified/opencore-amr opencore-amr 0.1.2 be191ced743e9ac5b45642d5560a29d427a8302c
Name:       opencore-amr
Summary:    opencore AMRNB dev package
Version:    0.1.2
Release:    2
Group:      libdevel
License:    Apache-2.0
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(dlog)
BuildRequires:  pkgconfig(vconf)

BuildRequires:  cmake
BuildRequires:  gettext-devel

%description
opencore AMRNB dev package


%package devel 
Summary:    opencore AMRNB dev package (Developement)
Group:      TO_BE_FILLED 
Requires:   %{name} = %{version}-%{release}

%description devel
opencore AMRNB dev package (Developement)

%prep
%setup -q

%build
./autogen.sh
./configure --prefix=/usr --mandir=%{_prefix}/share/man --infodir=%{_prefix}/share/info CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS"
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post

%postun


%files
%defattr(-,root,root,-)
%{_libdir}/libopencore-amrnb.so.0
%{_libdir}/libopencore-amrnb.so.0.0.2
%{_libdir}/libopencore-amrwb.so.0
%{_libdir}/libopencore-amrwb.so.0.0.2

%files devel 
%defattr(-,root,root,-)
%{_includedir}/opencore-amrnb/*.h
%{_includedir}/opencore-amrwb/*.h
%{_libdir}/libopencore-amrnb.so
%{_libdir}/libopencore-amrwb.so
%{_libdir}/pkgconfig/opencore-amrnb.pc
%{_libdir}/pkgconfig/opencore-amrwb.pc
