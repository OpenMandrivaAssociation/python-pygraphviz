%define module	pygraphviz
%define name	python-%{module}
%define version 1.1
%define release	%mkrel 1

Summary:	Python interface to Graphviz
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.gz
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
%setup -q -n %{module}-%{version}

%build
PYTHONDONTWRITEBYTECODE= %__python setup.py build
pushd doc
export PYTHONPATH=`dir -d ../build/lib.linux*`
%make html
popd

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc doc/build/html examples

