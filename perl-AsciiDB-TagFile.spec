%define	pdir	AsciiDB
%define	pnam	TagFile
%include	/usr/lib/rpm/macros.perl
Summary:	AsciiDB-TagFile perl module
Summary(pl):	Modu³ perla AsciiDB-TagFile
Name:		perl-AsciiDB-TagFile
Version:	1.06
Release:	5

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AsciiDB-TagFile allows to manage a simple ASCII database.

%description -l pl
AsciiDB-TagFile pozwala na korzystanie z prostej, tekstowej bazy
danych.

%prep
%setup -q -n AsciiDB-TagFile-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{perl_sitelib}/AsciiDB
%{perl_sitelib}/AsciiDB/*.pm
%{_mandir}/man3/*
