%define	upstream_name	 Params-Check
%define upstream_version 0.28

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	A generic input parsing/checking mechanism
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/K/KA/KANE/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Locale::Maketext::Simple)
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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%{makeinstall_std}

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/Params
%{_mandir}/*/*
