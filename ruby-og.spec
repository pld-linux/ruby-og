%define	tarname	og
Summary:	Object-Relational mapping library for Ruby
Summary(pl):	Biblioteka odwzorowañ obiektowo-relacyjnych dla jêzyka Ruby
Name:		ruby-Og
Version:	0.25.0
Release:	2
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/download.php/7161/%{tarname}-%{version}.tgz
# Source0-md5:	d46c2c06f49c8f83bd84072890f7c273
Patch0:		%{name}-errordetail.patch
URL:		http://rubyforge.org/projects/nitro/
BuildRequires:	rpmbuild(macros) >= 1.263
BuildRequires:	ruby-modules
Requires:	ruby-modules
Requires:	ruby-Glue >= %{version}
Requires:	ruby-facets >= 2005.10.30
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Og "Object Graph" Object-Relational mapping
library for Ruby.

%description -l pl
Ten pakiet zawiera bibliotekê odwzorowañ obiektowo relacyjnych Og
("Object Graph") dla jêzyka Ruby.

%prep
%setup -q -n %{tarname}
%patch0 -p1

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{_examplesdir}/%{name}-%{version}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc README doc/*
%{ruby_rubylibdir}/*
%{ruby_ridir}/Og
%{_examplesdir}/%{name}-%{version}
