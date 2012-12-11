%define	upstream_name	 Params-Check
%define upstream_version 0.28

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

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


%changelog
* Sat Jan 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.280.0-1mdv2011.0
+ Revision: 630634
- update to new version 0.28

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.260.0-1mdv2010.0
+ Revision: 404281
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.26-4mdv2009.0
+ Revision: 258189
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.26-3mdv2009.0
+ Revision: 246264
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.26-1mdv2008.1
+ Revision: 136330
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Mar 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.26-1mdv2007.0
+ Revision: 133694
- new version

* Mon Jul 10 2006 Emmanuel Andry <eandry@mandriva.org> 0.25-1mdv2007.0
- New release 0.25

* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.24-1mdk
- New release 0.24

* Sat Oct 01 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.23-2mdk
- Buildrequires fix

* Thu Sep 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-1mdk
- first mdk release

