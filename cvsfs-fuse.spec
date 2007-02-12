Summary:	Filesystem based on CVS
Summary(pl.UTF-8):	System plików oparty na CVS-ie
Name:		cvsfs-fuse
Version:	0.5
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/cvsfs/%{name}-%{version}.tar.gz
# Source0-md5:	d56d0db0ee02f2f99d48e9fa10a6dba6
URL:		http://cvsfs.sourceforge.net/
BuildRequires:	libfuse-devel
BuildRequires:	libstdc++-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filesystem based on CVS.

%description -l pl.UTF-8
System plików oparty na CVS-ie.

%prep
%setup -q

sed -i -e 's/ -O3//' cvsfsctl/Makefile.in

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install fuse/cvsfs-fuse $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/cvsfsctl
%attr(755,root,root) %{_bindir}/cvsfs-fuse
%{_mandir}/man1/cvsfsctl.1*
%{_mandir}/man8/cvsfs-fuse.8*
