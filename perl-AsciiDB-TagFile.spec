%include	/usr/lib/rpm/macros.perl
%define		pdir	AsciiDB
%define		pnam	TagFile
Summary:	AsciiDB::TagFile perl module
Summary(pl):	Modu³ perla AsciiDB::TagFile
Name:		perl-AsciiDB-TagFile
Version:	1.06
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AsciiDB::TagFile allows to manage a simple ASCII database.

%description -l pl
AsciiDB::TagFile pozwala na korzystanie z prostej, tekstowej bazy
danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_sitelib}/AsciiDB
%{perl_sitelib}/AsciiDB/*.pm
%{_mandir}/man3/*
