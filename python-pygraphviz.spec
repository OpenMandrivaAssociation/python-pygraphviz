%define module	pygraphviz
%define name	python-%{module}
%define version 1.0
%define rel	rc5
%define release	%mkrel 0.%{rel}.1

Summary:	Python interface to Graphviz
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}%{rel}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://networkx.lanl.gov/pygraphviz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	graphviz >= 2.0
BuildRequires:	graphviz-devel >= 2.0
BuildRequires:	python-devel
BuildRequires:	python-sphinx

%description
PyGraphviz is a Python interface to the Graphviz graph layout and
visualization package.

With PyGraphviz, you can create, edit, read, write, and draw graphs
using Python to access the Graphviz graph data structure and layout
algorithms.

%prep
%setup -q -n %{module}-%{version}%{rel}

%build
PYTHONDONTWRITEBYTECODE= %__python setup.py build
pushd doc
export PYTHONPATH=`dir -d ../build/lib.linux*`
%make html
popd

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%__rm -rf %{buildroot}%{_datadir}/doc

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/build/html examples
%python_sitearch/pygraphviz
%python_sitearch/*.egg-info
