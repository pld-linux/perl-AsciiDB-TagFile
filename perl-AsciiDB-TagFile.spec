#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	AsciiDB
%define		pnam	TagFile
Summary:	AsciiDB::TagFile - tie class for a simple ASCII database
Summary(pl.UTF-8):	AsciiDB::TagFile - powiązanie klasy z prostą bazą danych w ASCII
Name:		perl-AsciiDB-TagFile
Version:	1.06
Release:	8
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ba1ef6144e2ca462c46a6b4f83df9e7a
URL:		http://search.cpan.org/dist/AsciiDB-TagFile/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AsciiDB::TagFile allows to manage a simple ASCII database.

%description -l pl.UTF-8
AsciiDB::TagFile pozwala na korzystanie z prostej, tekstowej bazy
danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/AsciiDB
%{perl_vendorlib}/AsciiDB/*.pm
%{_mandir}/man3/*
