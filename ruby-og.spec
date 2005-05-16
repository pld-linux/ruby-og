%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"])')
%define	ruby_version	%(ruby -r rbconfig -e 'print Config::CONFIG["ruby_version"]')
Summary:	Object-Relational mapping library for Ruby
Summary(pl):	Biblioteka odwzorowañ obiektowo-relacyjnych dla jêzyka Ruby
Name:		ruby-Og
%define tarname og
Version:	0.17.0
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/download.php/4480/%{tarname}-%{version}.tgz
# Source0-md5:	ef2b424148d42fb92021f392df3b73df
uRL:		http://rubyforge.org/projects/nitro/
BuildRequires:	ruby
Requires:	ruby
Requires:	ruby-Glue
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Og "Object Graph" Object-Relational mapping
library for Ruby.

%description -l pl
Ten pakiet zawiera bibliotekê odwzorowañ obiektowo relacyjnych Og
("Object Graph") dla jêzyka Ruby.

%prep
%setup -q -n %{tarname}-%{version}

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
%doc rdoc README CHANGELOG doc/*
%{ruby_rubylibdir}/*
%{ruby_ridir}/Og
%{_examplesdir}/%{name}-%{version}
