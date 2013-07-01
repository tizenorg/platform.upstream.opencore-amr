Name:       opencore-amr
Summary:    opencore AMRNB dev package
Version:    0.1.2
Release:    4
Group:      libdevel
License:    Apache-2.0
Source0:    %{name}-%{version}.tar.gz
Source1001: 	opencore-amr.manifest


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
cp %{SOURCE1001} .

%build
./autogen.sh
%configure
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
cp LICENSE %{buildroot}/usr/share/license/%{name}
%make_install

%post

%postun


%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_libdir}/libopencore-amrnb.so.0
%{_libdir}/libopencore-amrnb.so.0.0.2
%{_libdir}/libopencore-amrwb.so.0
%{_libdir}/libopencore-amrwb.so.0.0.2
%{_datadir}/license/%{name}

%files devel 
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_includedir}/opencore-amrnb/*.h
%{_includedir}/opencore-amrwb/*.h
%{_libdir}/libopencore-amrnb.so
%{_libdir}/libopencore-amrwb.so
%{_libdir}/pkgconfig/opencore-amrnb.pc
%{_libdir}/pkgconfig/opencore-amrwb.pc
