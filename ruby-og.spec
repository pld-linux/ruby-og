%define	pkgname	og
Summary:	Object-Relational mapping library for Ruby
Summary(pl.UTF-8):	Biblioteka odwzorowań obiektowo-relacyjnych dla języka Ruby
Name:		ruby-%{pkgname}
Version:	0.27.0
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/download.php/8087/%{pkgname}-%{version}.tgz
# Source0-md5:	53949ab14ffa73b2b7cbfa65f091b6a3
Patch0:		%{name}-errordetail.patch
URL:		http://rubyforge.org/projects/nitro/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-glue >= %{version}
Requires:	ruby-facets >= 1.0.0
Obsoletes:	ruby-Og
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Og "Object Graph" Object-Relational mapping
library for Ruby.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę odwzorowań obiektowo relacyjnych Og
("Object Graph") dla języka Ruby.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{_examplesdir}/%{name}-%{version}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc README doc/*
%{ruby_rubylibdir}/*
%{ruby_ridir}/Og
%{_examplesdir}/%{name}-%{version}
