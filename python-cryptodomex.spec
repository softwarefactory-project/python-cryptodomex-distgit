%global        uname pycryptodomex
%global        pkgname cryptodomex
%global        sum A self-contained Python package of low-level cryptographic primitives.

Name:          python-cryptodomex
Version:       3.4.2
Release:       2%{?dist}
Summary:       %{sum}

URL:           https://pypi.python.org/pypi/cryptodomex
Source:        https://pypi.io/packages/source/p/%{uname}/%{uname}-%{version}.tar.gz
License:       MIT

BuildArch:     x86_64

Buildrequires: python-setuptools
Buildrequires: python2-devel

%description
%{sum}.

%package -n python2-%{pkgname}
Summary:        %{sum}

%description -n python2-%{pkgname}
%{sum}.

%prep
%autosetup -n %{uname}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files -n python2-%{pkgname}
%{python2_sitearch}/*

%changelog
* Thu Mar 2 2017 Nicolas Hicher <nhicher@redhat.com> 4.13.4-2
- normalize spec file

* Mon Feb 28 2017 Nicolas Hicher <nhicher@redhat.com> 4.13.4-1
- initial package
