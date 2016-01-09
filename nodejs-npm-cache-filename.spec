%define		pkg	npm-cache-filename
Summary:	Given a cache folder and url, return the appropriate cache folder
Name:		nodejs-%{pkg}
Version:	1.0.1
Release:	1
License:	ISC
Group:		Development/Libraries
#Source0:	http://registry.npmjs.org/nodejs-npm-cache-filename/-/%{pkg}-%{version}.tgz
Source0:	https://github.com/npm/npm-cache-filename/archive/v%{version}/%{pkg}-%{version}.tar.gz
# Source0-md5:	aad1eececeefefb5e9f444ad23d0a1ec
URL:		https://github.com/npm/npm-cache-filename
BuildRequires:	rpmbuild(macros) >= 1.634
BuildRequires:	sed >= 4.0
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Given a cache folder and url, return the appropriate cache folder.

%prep
%setup -qn %{pkg}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr index.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{nodejs_libdir}/%{pkg}
