# Conditional build:
%bcond_with	tests	# unit tests (some failing as of 0.22.2)

Summary:	Set of Python 3 modules for machine learning and data mining
Summary(pl.UTF-8):	Zbiór modułów Pythona 3 do uczenia maszynowego i eksporacji danych
Name:		python3-scikit-rf
Version:	1.3.0
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.debian.net/scikit-rf/scikit_rf-%{version}.tar.gz
# Source0-md5:	3a41d221e3bac5497ca2d6e45e0cbe59
URL:		https://scikit-rf.org/
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
%if %{with tests}
BuildRequires:	pydoc3
BuildRequires:	python3-pandas
BuildRequires:	python3-pytest >= 3.3.0
BuildRequires:	python3-pytest-cov
BuildRequires:	python3-scipy
%endif
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package for RF/Microwave engineering. It provides a modern,
object-oriented library for network analysis and calibration which is
both flexible and scalable. See some of the features below and check
out the Documentation for a more in-depth look at scikit-rf.

%prep
%setup -q -n scikit_rf-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTHONPATH=$(pwd) pytest-3 skrf/tests/
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/skrf
%{py3_sitescriptdir}/scikit_rf-*-info
