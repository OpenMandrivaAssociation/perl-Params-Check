%define	module	Params-Check
%define	name	perl-%{module}
%define version 0.26
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Summary:	A generic input parsing/checking mechanism
Source0:	http://search.cpan.org/CPAN/authors/id/K/KA/KANE/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildRoot:	%{_tmppath}/%{name}-%{version}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl-Locale-Maketext-Simple
BuildArch:	noarch

%description
Params::Check is a generic input parsing/checking mechanism.

It allows you to validate input via a template. The only requirement is that
the arguments must be named.

Params::Check can do the following things for you:
* Convert all keys to lowercase
* Check if all required arguments have been provided
* Set arguments that have not been provided to the default
* Weed out arguments that are not supported and warn about them to the user
* Validate the arguments given by the user based on strings, regexes, lists or
  even subroutines
* Enforce type integrity if required


%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%{makeinstall_std}

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorlib}/Params
%{_mandir}/*/*


