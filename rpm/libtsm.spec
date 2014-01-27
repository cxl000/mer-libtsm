Summary: Terminal-emulator State Machine
Name: libtsm
Version: 3
Release: 1
License: LGPL21
Group: Development/Liraries
URL: git://people.freedesktop.org/~dvdhrm/libtsm
Source0: %{name}-%{version}.tar.xz
Patch0:  libtsm-remove-EXTRA.patch
BuildRequires: pkgconfig(xkbcommon)


%description
TSM is a state machine for DEC VT100-VT520 compatible terminal emulators. It tries to support all common standards while keeping compatibility to existing emulators like xterm, gnome-terminal, konsole, ...

%package devel
Summary:   Devel files for libtsm
Group:     Development/Liraries
Requires:  %{name} = %{version}-%{release}

%description devel
Development files for libtsm

%prep
%setup -q
cd libtsm
%patch0 -p1

%build
cd libtsm
mkdir m4
%reconfigure --disable-static
make %{?jobs:-j%jobs} libshl.la
make %{?jobs:-j%jobs}

%install
cd libtsm
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

# >> install post
# << install post


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libtsm.so.3*

%files devel
%defattr(-,root,root,-)
%{_includedir}/libtsm.h
%{_libdir}/libtsm.so
%{_libdir}/pkgconfig/libtsm.pc


