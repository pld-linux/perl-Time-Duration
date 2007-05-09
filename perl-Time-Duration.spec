#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Time
%define	pnam	Duration
Summary:	Time::Duration - rounded or exact English expression of durations
Summary(pl.UTF-8):	Time::Duration - przybliżone lub dokładne wyrażanie okresów czasu po angielsku
Name:		perl-Time-Duration
Version:	1.04
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Time/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0c8f3d4702bcf0b0750dd476ed5f17ec
URL:		http://search.cpan.org/dist/Time-Duration/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides functions for expressing durations in rounded or
exact terms.

%description -l pl.UTF-8
Ten moduł udostępnia funkcje do wyrażania okresów czasu przy użyciu
wyrażeń przybliżonych lub dokładnych.

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

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Time/Duration

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%{perl_vendorlib}/Time/*.pm
%{_mandir}/man3/*

%dir %{perl_vendorlib}/Time/Duration
